from flask import Flask
import socket
import pymysql

app = Flask(__name__)

def get_connection():
    return pymysql.connect(
        host='db01',
        user='db_user',
        password='Passw0rd',
        database='employee_db',
        cursorclass=pymysql.cursors.DictCursor
    )

@app.route("/")
def main():
    hostname = socket.gethostname()
    return f"Welcome! Response from {hostname}"

@app.route("/how are you")
def hello():
    hostname = socket.gethostname()
    return f"I am good, how about you? (served by {hostname})"

@app.route("/employees")
def employees():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM employees")
        rows = cursor.fetchall()
        conn.close()

        hostname = socket.gethostname()
        return {
            "served_by": hostname,
            "data": rows
        }

    except Exception as e:
        return {"error": str(e)}, 500