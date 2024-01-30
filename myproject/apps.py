from django.apps import AppConfig


class MyprojectConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myproject'

from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/data')
def get_data():
    # Implement code to fetch and downsample data here
    # For simplicity, I'll provide dummy data
    data = [
        {"timestamp": "2022-01-01", "profit_percentage": 10},
        # ... more data ...
    ]
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
