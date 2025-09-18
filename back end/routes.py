from flask import Blueprint, request, jsonify
from models import db, User, Assignment
import os
from dotenv import load_dotenv
import requests

api_blueprint = Blueprint("api", __name__)
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_ENDPOINT = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"

# ----------------- USER ROUTES -----------------
@api_blueprint.route("/signup", methods=["POST"])
def signup():
    data = request.json
    new_user = User(email=data["email"], password=data["password"], role=data["role"])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully!"})

@api_blueprint.route("/login", methods=["POST"])
def login():
    data = request.json
    user = User.query.filter_by(email=data["email"], password=data["password"]).first()
    if user:
        return jsonify({"message": "Login successful", "role": user.role, "id": user.id})
    return jsonify({"message": "Invalid credentials"}), 401

# ----------------- ASSIGNMENTS -----------------
@api_blueprint.route("/upload", methods=["POST"])
def upload_assignment():
    data = request.json
    new_assignment = Assignment(
        student_id=data["student_id"],
        submission_file=data["submission_file"]
    )
    db.session.add(new_assignment)
    db.session.commit()
    return jsonify({"message": "Assignment uploaded successfully!"})

@api_blueprint.route("/submissions", methods=["GET"])
def get_submissions():
    assignments = Assignment.query.all()
    result = [
        {
            "id": a.id,
            "student_id": a.student_id,
            "submission_file": a.submission_file,
            "grade": a.grade,
            "feedback": a.feedback,
        }
        for a in assignments
    ]
    return jsonify(result)

# ----------------- GRADING -----------------
@api_blueprint.route("/grade", methods=["POST"])
def grade_assignment():
    data = request.json
    reference_text = data["reference"]
    student_text = data["student"]

    headers = {"Content-Type": "application/json"}
    params = {"key": GEMINI_API_KEY}
    body = {
        "contents": [
            {
                "parts": [
                    {"text": f"Compare student response to reference.\nReference: {reference_text}\n\nStudent: {student_text}\n\nGrade (out of 10) and Feedback:"}
                ]
            }
        ]
    }

    response = requests.post(GEMINI_ENDPOINT, headers=headers, params=params, json=body)
    result = response.json()

    # Extract AI grading response
    grading_result = result["candidates"][0]["content"]["parts"][0]["text"]

    return jsonify({"grading_result": grading_result})
