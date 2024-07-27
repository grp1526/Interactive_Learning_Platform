from flask import Flask, render_template, request, redirect, url_for

app = Flask(_name_)

# Sample data
courses = [
    {"id": 1, "title": "Python Basics", "description": "Learn the basics of Python."},
    {"id": 2, "title": "Web Development", "description": "Learn how to build websites."}
]

quizzes = [
    {"course_id": 1, "questions": [
        {"question": "What is Python?", "options": ["A fruit", "A programming language", "A snake"], "answer": "A programming language"},
        {"question": "Who created Python?", "options": ["Guido van Rossum", "Elon Musk", "Bill Gates"], "answer": "Guido van Rossum"}
    ]}
]

progress = {1: {"completed_lessons": 2, "total_lessons": 5}, 2: {"completed_lessons": 1, "total_lessons": 5}}

@app.route('/')
def index():
    return render_template('index.html', courses=courses)

@app.route('/course/<int:course_id>')
def course(course_id):
    course = next((course for course in courses if course["id"] == course_id), None)
    return render_template('course.html', course=course, progress=progress.get(course_id))

@app.route('/quiz/<int:course_id>')
def quiz(course_id):
    quiz = next((quiz for quiz in quizzes if quiz["course_id"] == course_id), None)
    return render_template('quiz.html', quiz=quiz)

if _name_ == '_main_':
    app.run(debug=True)