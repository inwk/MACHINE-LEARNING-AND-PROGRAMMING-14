import argparse
import os
import numpy as np
from tqdm import tqdm
import glob

from mypath_test import Path
from dataloaders_test import make_data_loader
from modeling.sync_batchnorm.replicate import patch_replication_callback
from modeling.deeplab import *
from utils.loss import SegmentationLosses
from utils.calculate_weights import calculate_weigths_labels
from utils.metrics import Evaluator
import warnings
from dataloaders_test.utils import decode_segmap
from PIL import Image
torch.backends.cudnn.enabled = False
warnings.filterwarnings("ignore", category=DeprecationWarning) 

class Trainer(object):
    def __init__(self, args):
        self.args = args

        if args.batch_size is None:
            args.batch_size = 1000

        # Define Dataloader
        kwargs = {'num_workers': args.workers, 'pin_memory': True}
        if self.args.mode == 'acc':
            self.test_loader, self.nclass = make_data_loader(args, **kwargs)
        else:
            self.nclass = self.args.numClass
        # Define network
        model = DeepLab(num_classes=self.nclass,
                        backbone=args.backbone,
                        output_stride=args.out_stride,
                        sync_bn=args.sync_bn,
                        freeze_bn=args.freeze_bn)
        self.model = model
        
        # Define Evaluator
        self.evaluator = Evaluator(self.nclass)

        # Using cuda
        if args.cuda:
            self.model = torch.nn.DataParallel(self.model, device_ids=self.args.gpu_ids)
            patch_replication_callback(self.model)
            self.model = self.model.cuda()

        # Resuming checkpoint
        self.best_pred = 0.0
        if args.checkpoint is not None:
            if not os.path.isfile(args.checkpoint):
                raise RuntimeError("=> no checkpoint found at '{}'" .format(args.checkpoint))
            checkpoint = torch.load(args.checkpoint)
            if args.cuda:
                self.model.load_state_dict(checkpoint['state_dict'])
            else:
                self.model.load_state_dict(checkpoint['state_dict'])
            self.best_pred = checkpoint['best_pred']

    def test(self):
        self.model.eval()
        self.evaluator.reset()
        tbar = tqdm(self.test_loader, desc='\r')
        test_loss = 0.0
        for i, sample in enumerate(tbar):
            image, target = sample['image'], sample['label']
            if self.args.cuda:
                image, target = image.cuda(), target.cuda()
            with torch.no_grad():
                output = self.model(image)
            pred = output.data.cpu().numpy()
            target = target.cpu().numpy()
            pred = np.argmax(pred, axis=1)
            num = 0
            cPath = os.getcwd()
            for each_pred in pred:
                rgb_img = decode_segmap(each_pred, self.args.dataset)
                rgb_img = Image.fromarray((rgb_img * 255).astype(np.uint8))
                rgb_img.save(cPath+'/'+self.args.outpath+str(num)+'.jpg')
                num += 1
            self.evaluator.add_batch(target, pred)

        # Fast test during the training
        Acc = self.evaluator.Pixel_Accuracy()
        Acc_class = self.evaluator.Pixel_Accuracy_Class()
        mIoU = self.evaluator.Mean_Intersection_over_Union()
        FWIoU = self.evaluator.Frequency_Weighted_Intersection_over_Union()
        DSC = self.evaluator.Dice_Similarity_Coefficient()

        print('Class1 mIOU: %.3f, Class1 DSC: %.3f' %(mIoU[1], DSC[1]))
        print('Class2 mIOU: %.3f, Class2 DSC: %.3f' %(mIoU[2], DSC[2]))
        

def main():
    parser = argparse.ArgumentParser(description="PyTorch DeeplabV3Plus Training")
    parser.add_argument('--backbone', type=str, default='resnet',
                        choices=['resnet', 'xception', 'drn', 'mobilenet'],
                        help='backbone name (default: resnet)')
    parser.add_argument('--outpath', type=str, default='dataVisualization/',
                        help='directory to save image fiels')
    parser.add_argument('--out-stride', type=int, default=16,
                        help='network output stride (default: 8)')
    parser.add_argument('--dataset', type=str, default='pascal',
                        choices=['pascal', 'coco', 'cityscapes', 'ctimages'],
                        help='dataset name (default: pascal)')
    parser.add_argument('--use-sbd', action='store_true', default=True,
                        help='whether to use SBD dataset (default: True)')
    parser.add_argument('--workers', type=int, default=4,
                        metavar='N', help='dataloader threads')
    parser.add_argument('--base-size', type=int, default=256,
                        help='base image size')
    parser.add_argument('--crop-size', type=int, default=256,
                        help='crop image size')
    parser.add_argument('--sync-bn', type=bool, default=None,
                        help='whether to use sync bn (default: auto)')
    parser.add_argument('--freeze-bn', type=bool, default=False,
                        help='whether to freeze bn parameters (default: False)')
    parser.add_argument('--loss-type', type=str, default='ce',
                        choices=['ce', 'focal'],
                        help='loss func type (default: ce)')
    parser.add_argument('--batch-size', type=int, default=None,
                        metavar='N', help='input batch size for \
                                training (default: auto)')
    
    # cuda, seed and logging
    parser.add_argument('--no-cuda', action='store_true', default=
                        False, help='disables CUDA training')
    parser.add_argument('--gpu-ids', type=str, default='0',
                        help='use which gpu to train, must be a \
                        comma-separated list of integers only (default=0)')
    parser.add_argument('--seed', type=int, default=1, metavar='S',
                        help='random seed (default: 1)')
    # checking point
    parser.add_argument('--checkpoint', type=str, default=None,
                        help='put the path to resuming file if needed')

    # evaluation option
    parser.add_argument('--eval-interval', type=int, default=1,
                        help='evaluuation interval (default: 1)')
    parser.add_argument('--no-val', action='store_true', default=False,
                        help='skip validation during training')

    args = parser.parse_args()
    args.cuda = not args.no_cuda and torch.cuda.is_available()
    if args.cuda:
        try:
            args.gpu_ids = [int(s) for s in args.gpu_ids.split(',')]
        except ValueError:
            raise ValueError('Argument --gpu_ids must be a comma-separated list of integers only')
            
    if args.sync_bn is None:
        if args.cuda and len(args.gpu_ids) > 1:
            args.sync_bn = True
        else:
            args.sync_bn = False


    torch.manual_seed(args.seed)
    trainer = Trainer(args)
    trainer.test()

if __name__ == "__main__":
   main()
