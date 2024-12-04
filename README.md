# Flask API with SQLite Database

This project is a simple Flask-based REST API that handles user responses and generates charts. The responses are stored in a SQLite database. The app provides endpoints to retrieve questions and create new responses.

## Prerequisites

Before running the application, make sure you have the following installed on your system:

- Python 3.x
- `pip` (Python package installer)

## Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/maryamfad/Flask_Questionnaire_visualizer
   cd backend
   ```
2. **Create a Virtual Environment (Optional but Recommended)**:
   ```bash
   python3 -m venv venv
   ```
3. **Activate the Virtual Environment**:

* On Windows:
  ```bash
  venv\Scripts\activate

* On macOS/Linux:
  ```bash
  source venv/bin/activate

4. **Install Dependencies**:

```bash
pip install -r requirements.txt
```

5. **Run the Flask App**:
```bash
python app.py
```
6. **Access the Application**:
Once the server is running, you can access the application at http://127.0.0.1:5000/.
The following endpoints are available:

* GET /api/questions – Retrieves the available questions.
* POST /api/createAResponse – Submits a new response. You can send a JSON payload with the answers to the questions.
