📘 AI-Powered Student Assignment Evaluation System

An AI-driven web application that allows teachers to manage, evaluate, and provide feedback on handwritten student assignments. The system uses OCR (Optical Character Recognition) and Google Gemini AI to extract handwritten notes and compare them against teacher-provided reference PDFs, automatically generating grades and feedback.

🚀 Features

👨‍🏫 Teacher Portal: Signup/Login, manage student submissions, view grades & feedback

🧑‍🎓 Student Portal: Submit handwritten notes, view grades & teacher feedback

📄 PDF & Handwritten Note Processing: Extracts text from both PDFs and images

🤖 AI-Powered Grading: Uses Gemini Pro API for intelligent grading & evaluation

🔒 Authentication: Secure login system for teachers & students

💾 Database Integration: Stores users, assignments, grades, and feedback

🛠️ Tech Stack

Frontend: HTML, CSS, JavaScript (React optional)

Backend: Python (Flask)

Database: SQLite (can extend to PostgreSQL/MySQL)

AI/ML: Google Gemini API, Tesseract OCR, OpenCV, PyPDF2

📂 Project Structure
/project-root
 ├── /backend
 │   ├── app.py            # Main Flask app
 │   ├── models.py         # Database models
 │   ├── routes.py         # API routes
 │   ├── requirements.txt  # Dependencies
 │
 ├── /frontend
 │   ├── /src
 │   │   ├── components    # React/JSX components
 │   │   ├── App.js
 │   │   ├── index.js
 │
 ├── /database
 │   ├── database.db
 │
 ├── /static
 │   ├── styles.css
 │
 └── /templates
     ├── teacher_dashboard.html
     ├── student_dashboard.html
     ├── index.html

⚙️ Installation & Setup
1️⃣ Clone the repository
git clone[ https://github.com/your-username/ai-assignment-grader.git](https://github.com/MalipatelRanjithReddy/AI-Grading-System.git)

2️⃣ Create virtual environment & install dependencies
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt

3️⃣ Setup Gemini API Key

Create a .env file in the backend folder:

GEMINI_API_KEY=your_api_key_here

4️⃣ Run the backend server
cd backend
python app.py

5️⃣ Run the frontend (optional React setup)
cd frontend
npm install
npm start

🧪 Sample Data

Reference PDF: Explains "The Water Cycle" stages

Student Notes (Image): Handwritten explanation of the water cycle

The system extracts both, compares, and generates grade + feedback

📊 Future Enhancements

Multi-language handwritten text recognition

Advanced plagiarism detection

Export grades & feedback as PDF reports

Mobile app version

🤝 Contributing

Contributions are welcome! Feel free to fork, create issues, and submit PRs.

📜 License

MIT License
