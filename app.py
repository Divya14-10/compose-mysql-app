from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

@app.route("/")
def home():
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50))")
        cursor.execute("INSERT INTO users (name) VALUES ('Divya')")
        conn.commit()

        cursor.execute("SELECT * FROM users")
        data = cursor.fetchall()

        cursor.close()
        conn.close()

        return f"✅ Connected to MySQL! Data: {data}"
    except Exception as e:
        return f"❌ Error connecting to MySQL: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

