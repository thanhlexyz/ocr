import argparse
import torch
import os

torch.set_printoptions(4, sci_mode=False)

def create_folders(args):
    ls = [args.pdf_dir, args.txt_dir, args.png_dir]
    for folder in ls:
        os.makedirs(folder, exist_ok=True)

def get_args():
    # create args parser
    parser = argparse.ArgumentParser()
    parser.add_argument('--scenario', type=str, default='main')
    parser.add_argument('--mode', type=str, default='test')
    # prepare
    parser.add_argument('--prefix', type=str, default='n3_vocab')
    parser.add_argument('--start_page', type=int, default=9)
    parser.add_argument('--end_page', type=int, default=9)
    # data directory
    parser.add_argument('--pdf_dir', type=str, default='../data/pdf')
    parser.add_argument('--png_dir', type=str, default='../data/png')
    parser.add_argument('--txt_dir', type=str, default='../data/txt')
    # metric
    parser.add_argument('--metric', type=str, default='value')
    parser.add_argument('--n_smooth', type=int, default=1)
    # device
    if torch.cuda.is_available():
        parser.add_argument('--device', type=str, default='cuda:0')
    else:
        parser.add_argument('--device', type=str, default='cpu')
    # other flags
    parser.add_argument('--verbose', action='store_true')
    parser.add_argument('--seed', type=int, default=0)
    # parse args
    args = parser.parse_args()
    # create folders
    create_folders(args)
    return args
