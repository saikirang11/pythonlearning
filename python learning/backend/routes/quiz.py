from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import db, Quiz, Lesson

quiz_bp = Blueprint('quiz', __name__)

@quiz_bp.route('/quiz/<int:lesson_id>', methods=['GET'])
@jwt_required()
def get_quiz(lesson_id):
    quizzes = Quiz.query.filter_by(lesson_id=lesson_id).all()
    return jsonify([
        {
            'id': q.id,
            'question': q.question,
            'options': q.options
        } for q in quizzes
    ]), 200

@quiz_bp.route('/quiz/submit', methods=['POST'])
@jwt_required()
def submit_quiz():
    data = request.get_json()
    lesson_id = data.get('lesson_id')
    answers = data.get('answers')  # {quiz_id: answer}
    quizzes = Quiz.query.filter_by(lesson_id=lesson_id).all()
    feedback = []
    correct_count = 0
    for q in quizzes:
        user_answer = answers.get(str(q.id))
        is_correct = user_answer == q.answer
        feedback.append({
            'quiz_id': q.id,
            'correct': is_correct,
            'explanation': q.explanation if not is_correct else ''
        })
        if is_correct:
            correct_count += 1
    return jsonify({'score': correct_count, 'feedback': feedback}), 200 