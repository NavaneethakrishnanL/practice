import sys
import os
import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
from openpyxl import Workbook
import re

def preprocess_image(img):
    # Enhance image contrast
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(2.0)  # Increase contrast by a factor of 2
    
    # Convert image to grayscale
    img = img.convert('L')
    
    # Apply Gaussian blur to reduce noise
    img = img.filter(ImageFilter.GaussianBlur(radius=1))
    
    return img

def postprocess_text(text):
    # Remove non-alphanumeric characters except spaces
    cleaned_text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return cleaned_text

def extract_text_from_image(image_path):
    # Check if the provided path exists and is a file
    if not os.path.exists(image_path) or not os.path.isfile(image_path):
        print("Error: Invalid image file path.")
        return

    # Open the image file
    img = Image.open(image_path)

    # Pre-process the image
    img = preprocess_image(img)

    # Use OCR to extract text from the image
    extracted_text = pytesseract.image_to_string(img)

    # Post-process the extracted text
    cleaned_text = postprocess_text(extracted_text)

    print("Extracted Text:")
    print(cleaned_text)

    # Create a new Excel workbook
    wb = Workbook()
    ws = wb.active

    # Write the cleaned text to the Excel file
    ws['A1'] = cleaned_text

    # Generate the output Excel file path
    output_excel_path = os.path.splitext(image_path)[0] + '_extracted_text.xlsx'

    # Save the Excel file
    wb.save(output_excel_path)

    print(f"Text extracted from the image has been saved to '{output_excel_path}'.")

if __name__ == "__main__":
    # Check if the image file path is provided as an argument
    if len(sys.argv) != 2:
        print("Usage: python extract_text_from_image.py <image_file_path>")
        sys.exit(1)

    # Extract text from the image
    image_path = sys.argv[1]
    extract_text_from_image(image_path)
