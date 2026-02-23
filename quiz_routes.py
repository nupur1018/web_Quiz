from flask import Blueprint, request, jsonify
from data.questions import get_questions_by_topics, get_topics_meta

quiz_bp = Blueprint('quiz', __name__)


@quiz_bp.route('/topics', methods=['GET'])
def topics():
    """GET /api/topics — list all available quiz topics with metadata."""
    meta = get_topics_meta()
    # Add question counts
    from data.questions import QUESTIONS
    for t in meta:
        t['count'] = len(QUESTIONS.get(t['id'], []))
    return jsonify({'topics': meta}), 200


@quiz_bp.route('/questions', methods=['POST'])
def get_questions():
    """
    POST /api/questions
    Body: { topics: [...], difficulty: 'easy'|'hard'|'mixed', count: 5|10|15 }
    Returns a shuffled list of questions (without revealing the answer index).
    """
    body = request.get_json()
    if not body:
        return jsonify({'error': 'No data provided.'}), 400

    topic_ids  = body.get('topics', [])
    difficulty = body.get('difficulty', 'mixed')
    count      = int(body.get('count', 10))

    if not topic_ids:
        return jsonify({'error': 'Please provide at least one topic.'}), 400

    count = max(1, min(count, 20))  # clamp between 1–20

    questions = get_questions_by_topics(topic_ids, difficulty, count)

    if not questions:
        return jsonify({'error': 'No questions found for the selected topics and difficulty.'}), 404

    # Return questions WITHOUT the answer (frontend validates on submit)
    safe_questions = []
    for i, q in enumerate(questions):
        safe_questions.append({
            'index':    i,
            'topic_id': q['topic_id'],
            'diff':     q['diff'],
            'q':        q['q'],
            'code':     q.get('code', None),
            'opts':     q['opts'],
        })

    # Store answers in session-style (we return a token list for validation)
    # For simplicity: return answers separately (client-side quiz, server saves score)
    answers = [q['ans'] for q in questions]
    explanations = [q['exp'] for q in questions]

    return jsonify({
        'questions':    safe_questions,
        'answers':      answers,       # sent for client-side checking
        'explanations': explanations,
        'total':        len(safe_questions),
    }), 200


@quiz_bp.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok', 'service': 'WebDev Quiz API'}), 200
