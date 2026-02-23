from flask import Blueprint, request, jsonify
from models.score_model import save_score, get_recent_scores, get_stats

score_bp = Blueprint('scores', __name__)


@score_bp.route('/scores', methods=['POST'])
def submit_score():
    """
    POST /api/scores
    Body: { player_name, score, total, pct, topics, difficulty, avg_time }
    """
    body = request.get_json()
    if not body:
        return jsonify({'error': 'No data provided.'}), 400

    required = ['player_name', 'score', 'total', 'pct']
    for field in required:
        if field not in body:
            return jsonify({'error': f'Missing field: {field}'}), 400

    doc_id = save_score(body)
    if doc_id is None:
        # DB unavailable — still return success to not break the quiz
        return jsonify({'message': 'Score noted (DB unavailable).', 'id': None}), 200

    return jsonify({'message': 'Score saved!', 'id': doc_id}), 201


@score_bp.route('/scores', methods=['GET'])
def recent_scores():
    """GET /api/scores — get recent quiz scores."""
    limit  = request.args.get('limit', 20, type=int)
    scores = get_recent_scores(limit=limit)
    return jsonify({'scores': scores, 'count': len(scores)}), 200


@score_bp.route('/stats', methods=['GET'])
def stats():
    """GET /api/stats — global quiz statistics."""
    data = get_stats()
    return jsonify(data), 200
