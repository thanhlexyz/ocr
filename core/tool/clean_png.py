import os

def clean_png(args):
    cmd = f'rm -rf {args.png_dir}/*.png'
    print(cmd)
    os.system(cmd)
