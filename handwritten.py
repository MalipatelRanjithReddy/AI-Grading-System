import cv2
import pytesseract

# Configure Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text_from_image(image path):
    """Extract text from handwritten notes (image)."""
    image = cv2.imread("E:\teacher assistant\handwritten.jpg.png")
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    extracted_text = pytesseract.image_to_string(gray_image)
    return extracted_text.strip()
