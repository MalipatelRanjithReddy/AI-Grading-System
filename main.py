from grading_model import GradePredictor

def main():
    predictor = GradePredictor()

    # File paths
    reference_pdf = r"E:\teacher assistant\reference.pdf"
    handwritten_image = r"E:\teacher assistant\handwritten.jpg.png"

    try:
        reference_text = predictor.extract_text_from_pdf(reference_pdf)
        student_text = predictor.extract_text_from_image(handwritten_image)
        
        if reference_text and student_text:
            print("Reference PDF Extracted Successfully!")
            print("Handwritten Notes Extracted Successfully!\n")
            
            # Grading
            result = predictor.grade_content(reference_text, student_text)
            print("Grading Result:\n", result)
        else:
            print("Error: Could not extract content from PDF or image.")
    except FileNotFoundError as e:
        print(f"File Not Found: {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")

if __name__ == "__main__":
    main()
