from flask import Blueprint, jsonify, request
from models.score_model import get_leaderboard

lb_bp = Blueprint('leaderboard', __name__)


@lb_bp.route('/leaderboard', methods=['GET'])
def leaderboard():
    """GET /api/leaderboard — top 10 scores."""
    limit = request.args.get('limit', 10, type=int)
    data  = get_leaderboard(limit=limit)
    return jsonify({'leaderboard': data, 'count': len(data)}), 200
