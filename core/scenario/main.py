import tool

def main(args):
    tool.split_pdf(args)
    text = ''
    for path in tool.list_png(args):
        text += tool.ocr(path)
    print(text)
    # tool.clean_png(args)
