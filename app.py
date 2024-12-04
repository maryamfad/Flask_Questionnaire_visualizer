from flask import Flask, jsonify, request, send_file
from flask_cors import CORS
import sqlite3
import os
from charts import generate_chart  # Assuming this function generates charts

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

DATABASE = "database.db"

# Ensure database setup
def init_db():
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Responses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Question1 TEXT,
            Question2 TEXT,
            Question3 TEXT,
            Question4 TEXT,
            Question5 TEXT,
            Question6 TEXT,
            Question7 TEXT
        )
    ''')
    connection.commit()
    connection.close()

# Initialize the database on startup
init_db()

# Helper function to connect to the database
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/api/questions', methods=['GET'])
def get_questions():
    """
    Fetch all responses from the database.
    """
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Responses")
    rows = cursor.fetchall()
    connection.close()

    # Convert database rows to JSON-serializable dictionary format
    responses = [
        {
            "id": row["id"],
            "Question1": row["Question1"],
            "Question2": row["Question2"],
            "Question3": row["Question3"],
            "Question4": row["Question4"],
            "Question5": row["Question5"],
            "Question6": row["Question6"],
            "Question7": row["Question7"]
        }
        for row in rows
    ]

    return jsonify(responses)

@app.route('/api/createAResponse', methods=['POST'])
def create_response():
    """
    Insert a new response into the database.
    Expecting JSON data in the format:
    {
        "Question1": [1, 2, 3],
        "Question2": [4, 5],
        ...
    }
    """
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid input, JSON expected"}), 400

        # Extract and prepare question data
        question1 = ','.join(map(str, data.get("Question1", [])))
        question2 = ','.join(map(str, data.get("Question2", [])))
        question3 = ','.join(map(str, data.get("Question3", [])))
        question4 = ','.join(map(str, data.get("Question4", [])))
        question5 = ','.join(map(str, data.get("Question5", [])))
        question6 = ','.join(map(str, data.get("Question6", [])))
        question7 = ','.join(map(str, data.get("Question7", [])))

        # Insert into the database
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute('''
            INSERT INTO Responses (Question1, Question2, Question3, Question4, Question5, Question6, Question7)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (question1, question2, question3, question4, question5, question6, question7))
        connection.commit()
        new_id = cursor.lastrowid  # ID of the newly inserted response
        connection.close()

        return jsonify({"message": "Response created successfully", "id": new_id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/generateChart', methods=['POST'])
def generate_chart_route():
    """
    Generate a chart based on submitted data.
    Expecting JSON data in the format:
    {
        "labels": [...],
        "values": [...]
    }
    """
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid input, JSON expected"}), 400

        # Generate the chart and return the file
        chart_path = generate_chart(data)
        return send_file(chart_path, mimetype='image/png')
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
