import pandas as pd
import sqlite3

# Load the combined CSV file
data = pd.read_csv("combined_data.csv")

# Connect to SQLite database (or create one if it doesn't exist)
conn = sqlite3.connect("responses.db")
cursor = conn.cursor()

# Create the table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Responses (
        PersonID INT PRIMARY KEY,
        Question1 TEXT,
        Question2 INT,
        Question3 TEXT,
        Question4 INT,
        Question5 TEXT,
        Question6 INT,
        Question7 TEXT
    )
''')

# Insert the data into the table
data.to_sql('Responses', conn, if_exists='append', index=False)

conn.commit()
conn.close()
