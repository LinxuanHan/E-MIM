import argparse

parser = argparse.ArgumentParser(description='Hyper-parameters management')

# Hardware options
parser.add_argument('--n_threads', type=int, default=2,help='number of threads for data loading')
parser.add_argument('--cpu', action='store_true',help='use cpu only')
parser.add_argument('--gpu_id', type=list,default=[0], help='use cpu only')
parser.add_argument('--seed', type=int, default=2021, help='random seed')

# Preprocess parameters
parser.add_argument('--n_labels', type=int, default=4,help='number of classes') # 分割肝脏则置为2（二类分割），分割肝脏和肿瘤则置为3（三类分割）
parser.add_argument('--upper', type=int, default=200, help='')
parser.add_argument('--lower', type=int, default=-200, help='')
parser.add_argument('--norm_factor', type=float, default=500.0, help='')
parser.add_argument('--expand_slice', type=int, default=10, help='')
parser.add_argument('--min_slices', type=int, default=64, help='')
parser.add_argument('--xy_down_scale', type=float, default=1, help='')
parser.add_argument('--slice_down_scale', type=float, default=1.0, help='')
parser.add_argument('--valid_rate', type=float, default=0.2, help='')

# data in/out and dataset
parser.add_argument('--dataset_path',default = r'C:\Users\HLX\Desktop\dataset',help='fixed trainset root path')
parser.add_argument('--test_data_path',default = r'C:\Users\HLX\Desktop\dataset',help='Testset path')
# parser.add_argument('--test_data_path',default = r'F:\HLX\BrainTS\split_test_3D_256',help='Testset path')
parser.add_argument('--save',default='GEN',help='save path of trained model')
parser.add_argument('--batch_size', type=list, default=1,help='batch size of trainset')

# train
parser.add_argument('--epochs', type=int, default=1000, metavar='N',help='number of epochs to train (default: 200)')
parser.add_argument('--lr', type=float, default=0.001, metavar='LR',help='learning rate (default: 0.0001)')
parser.add_argument('--early-stop', default=2000, type=int, help='early stopping (default: 30)')
parser.add_argument('--crop_size', type=int, default=64)
parser.add_argument('--val_crop_max_size', type=int, default=32)
parser.add_argument('--continue_train', type=bool, default=False, help='continue train')

# test
parser.add_argument('--test_cut_size', type=int, default=64, help='size of sliding window')
parser.add_argument('--test_cut_stride', type=int, default=64, help='stride of sliding window')
parser.add_argument('--postprocess', type=bool, default=True, help='post process')

args = parser.parse_args()

