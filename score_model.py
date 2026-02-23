from models.db import get_collection
from datetime import datetime
from bson import ObjectId


def _serialize(doc):
    doc['_id'] = str(doc['_id'])
    if isinstance(doc.get('created_at'), datetime):
        doc['created_at'] = doc['created_at'].strftime('%Y-%m-%d %H:%M:%S')
    return doc


def save_score(data: dict) -> str | None:
    """
    Save a completed quiz score.
    Expected fields: player_name, score, total, pct, topics, difficulty, avg_time
    """
    col = get_collection('scores')
    if col is None:
        return None

    doc = {
        'player_name': data.get('player_name', 'Anonymous').strip()[:30],
        'score':       int(data.get('score', 0)),
        'total':       int(data.get('total', 0)),
        'pct':         float(data.get('pct', 0)),
        'topics':      data.get('topics', []),
        'difficulty':  data.get('difficulty', 'mixed'),
        'avg_time':    float(data.get('avg_time', 0)),
        'created_at':  datetime.utcnow(),
    }

    result = col.insert_one(doc)
    return str(result.inserted_id)


def get_recent_scores(limit=20) -> list:
    """Get recent scores, newest first."""
    col = get_collection('scores')
    if col is None:
        return []
    docs = col.find().sort('created_at', -1).limit(limit)
    return [_serialize(d) for d in docs]


def get_leaderboard(limit=10) -> list:
    """Top scores by percentage, then by score."""
    col = get_collection('scores')
    if col is None:
        return []
    docs = col.find().sort([('pct', -1), ('score', -1)]).limit(limit)
    results = []
    for i, doc in enumerate(_serialize(d) for d in docs):
        doc['rank'] = i + 1
        results.append(doc)
    return results


def get_stats() -> dict:
    """Global stats across all quiz attempts."""
    col = get_collection('scores')
    if col is None:
        return {}

    total_games = col.count_documents({})
    if total_games == 0:
        return {'total_games': 0}

    pipeline = [
        {
            '$group': {
                '_id': None,
                'avg_pct':   {'$avg': '$pct'},
                'max_pct':   {'$max': '$pct'},
                'total_games': {'$sum': 1},
            }
        }
    ]
    agg = list(col.aggregate(pipeline))
    result = agg[0] if agg else {}
    result.pop('_id', None)
    result['total_games'] = total_games
    result['avg_pct']  = round(result.get('avg_pct', 0), 1)
    result['max_pct']  = round(result.get('max_pct', 0), 1)
    return result
