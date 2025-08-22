import pytesseract
from PIL import Image
import os

def extract_text_from_image(image_path):
    # Load the image using Pillow
    image = Image.open(image_path)

    # Use Tesseract to do OCR on the image
    custom_config = r'--oem 3 --psm 6 -l jpn'  # Set Tesseract config for Japanese
    text = pytesseract.image_to_string(image, config=custom_config)

    return text

def main():
    # Path to the PNG file
    image_path = 'path_to_your_image.png'  # Change this to your PNG file path

    if not os.path.exists(image_path):
        print(f"The image file {image_path} does not exist.")
        return

    # Extract text
    extracted_text = extract_text_from_image(image_path)

    # Print the extracted text
    print("Extracted Text:")
    print(extracted_text)

if __name__ == '__main__':
    main()
