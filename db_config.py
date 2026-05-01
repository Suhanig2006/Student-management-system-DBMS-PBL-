# type: ignore
import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="suhanig18",
        database="student_management_system"
    )
