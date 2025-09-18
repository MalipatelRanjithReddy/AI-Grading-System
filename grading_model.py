import cv2
import pytesseract
import PyPDF2
import google.generativeai as genai

# Configure Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("🚨 GEMINI_API_KEY not found in .env file!")

# Initialize Gemini AI
genai.configure(api_key=API_KEY)

class GradePredictor:
    def extract_text_from_pdf(self, pdf_path):
        """Extract text from a reference PDF."""
        text = ""
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                text += page.extract_text()
        return text.strip()

    def extract_text_from_image(self, image_path):
        """Extract text from handwritten notes (image)."""
        image = cv2.imread(image_path)
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        extracted_text = pytesseract.image_to_string(gray_image)
        return extracted_text.strip()

    def grade_content(self, reference_text, student_text):
        """Grade student content using Gemini AI based on reference material."""
        prompt = (
            f"Compare the following student response to the provided reference text.\n"
            f"Reference Text: {reference_text}\n\n"
            f"Student Response: {student_text}\n\n"
            f"Grade the response out of 10 and provide constructive feedback."
        )

        model = genai.GenerativeModel('gemini-1.5-pro')
        response = model.generate_content(prompt)
        return response.text
