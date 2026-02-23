from flask import Flask, render_template
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
CORS(app)

# Register blueprints
from routes.quiz_routes      import quiz_bp
from routes.score_routes     import score_bp
from routes.leaderboard_routes import lb_bp

app.register_blueprint(quiz_bp,   url_prefix='/api')
app.register_blueprint(score_bp,  url_prefix='/api')
app.register_blueprint(lb_bp,     url_prefix='/api')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/leaderboard')
def leaderboard():
    return render_template('leaderboard.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
