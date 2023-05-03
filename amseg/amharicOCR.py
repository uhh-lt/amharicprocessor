import os
from glob import glob
from io import BytesIO

import pytesseract
from pdf2image import convert_from_bytes


class AmharicOCR:
    """
    A class for performing Optical Character Recognition (OCR) on Amharic PDFs.
    """

    def __init__(self, file_path: str, save_files_path: str):
        """
        Constructor for the AmharicOCR class.

        Args:
            file_path (str): The path to the directory containing the input PDF files.
            save_files_path (str): The path to the directory where the extracted text files will be saved.
        """
        self.file_paths = file_path
        self.save_files_path = save_files_path

    def run(self):
        """
        Runs the OCR extraction on all Amharic PDF files in the input directory.

        Returns:
            None
        """
        paths = self.get_all_amharic_pdfs_path()

        for path in paths:
            filename = os.path.splitext(os.path.basename(path))[0]
            extracted_text = self.extract_text_from_pdf(path, filename)

        print("OCR extraction completed successfully.")

    def get_all_amharic_pdfs_path(self) -> list:
        """
        Retrieves a list of all Amharic PDF file paths in the input directory.

        Returns:
            list: A list of file paths to Amharic PDF files.
        """
        pdf_file_paths = glob(os.path.join(self.file_paths, "*.pdf"))
        print(f"Found {len(pdf_file_paths)} PDF files.")

        return pdf_file_paths

    def extract_text_from_pdf(self, path, filename):
        """
        Extracts the text from the input PDF file using Tesseract OCR.

        Args:
            path (str): The file path to the input PDF file.
            filename (str): The name of the file to be used when saving the extracted text file.

        Returns:
            str: The extracted text from the PDF file.
        """

        # Read the PDF file into a buffer
        try:
            with open(path, 'rb') as file:
                pdf_buffer = BytesIO(file.read())
        except FileNotFoundError as e:
            print(f"Error: {e}")
            return None

        # Convert PDF to images
        pages = convert_from_bytes(pdf_buffer.getvalue(), 500)

        # Initialize an empty string to store extracted text
        extracted_text = ''

        # Loop through each page and extract text
        for page in pages:
            # Convert the image to grayscale
            gray_image = page.convert('L')

            # Use Tesseract OCR to extract text from the grayscale image
            text = pytesseract.image_to_string(gray_image, lang='amh')

            # Append the extracted text to the string
            extracted_text += text

         # Save the extracted text to a file
        with open(os.path.join(self.save_files_path, f"{filename}.txt"), 'w') as f:
            f.write(extracted_text)

        return extracted_text
