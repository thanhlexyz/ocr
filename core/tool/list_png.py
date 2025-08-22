import os

def list_png(args):
    for name in os.listdir(args.png_dir):
        if args.prefix in name:
            path = os.path.join(args.png_dir, name)
            yield path
