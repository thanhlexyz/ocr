from PIL import Image
import pytesseract

def ocr(path):
    print(f'[+] ocr {path=}')
    image = Image.open(path)
    text = pytesseract.image_to_string(image, lang='jpn')
    return text
