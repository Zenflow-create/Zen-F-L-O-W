from flask import Flask, render_template  # <-- updated import

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # <-- updated return line
import requests
from flask import jsonify

@app.route('/api/quote')
def get_quote():
    try:
        res = requests.get('https://api.quotable.io/random')
        res.raise_for_status()
        return jsonify(res.json())
    except Exception as e:
        return jsonify({"error": "Failed to fetch quote"}), 500

@app.route('/tasks')
def tasks():
    return render_template('tasks.html')
@app.route('/timer')
def timer():
    return render_template('timer.html')
@app.route('/goals')
def goals():
    return render_template('goals.html')
@app.route('/quotes')
def quotes():
    return render_template('quotes.html')


@app.route('/api/mood', methods=['POST'])
def set_mood():
    from flask import request
    data = request.get_json()
    mood = data.get('mood')
    # Here you could save mood to database
    return jsonify({"status": "success", "mood": mood})

@app.route('/api/achievement', methods=['POST'])  
def log_achievement():
    from flask import request
    data = request.get_json()
    achievement = data.get('achievement')
    # Here you could save achievement to database
    return jsonify({"status": "success", "achievement": achievement})




if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

