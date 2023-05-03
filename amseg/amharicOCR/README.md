# AmharicOCR

The AmharicOCR class is a Python class that performs Optical Character Recognition (OCR) on Amharic PDF files using Tesseract OCR. The class extracts text from each page of the input PDF file, converts it to grayscale, and uses Tesseract OCR to extract the text from the grayscale image.
# Requirements

To use the AmharicOCR class, you need to have the following Python packages installed:

    pytesseract
    pdf2image

You also need to have Tesseract OCR installed on your machine. You can download Tesseract OCR from the following link: https://github.com/tesseract-ocr/tesseract
# Usage

To use the AmharicOCR class, create an instance of the class and pass the path to the directory containing the input PDF files and the path to the directory where the extracted text files will be saved:

```

from amseg.amharicOCR import AmharicOCR

ocr = AmharicOCR(file_path="path/to/pdf/files", save_files_path="path/to/save/files")
ocr.run()
```

The run() method will extract the text from all Amharic PDF files in the input directory and save the extracted text files to the output directory.

