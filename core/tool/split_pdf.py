import os

def split_pdf(args):
    pdf_path = os.path.join(args.pdf_dir, f'{args.prefix}.pdf')
    png_path = os.path.join(args.png_dir, f'{args.prefix}')
    cmd = f'pdftoppm -png -f {args.start_page} -l {args.end_page} "{pdf_path}" "{png_path}"'
    print(cmd)
    os.system(cmd)
