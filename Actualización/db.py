import sqlite3
import string
import random
DATABASE_NAME = "games.db"


def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn


def create_tables():
    tables = [
        """CREATE TABLE IF NOT EXISTS admin(
            name TEXT NOT NULL PRIMARY KEY,
			password TEXT NOT NULL
        )""",
        """CREATE TABLE IF NOT EXISTS company(
            company_id INTEGER PRIMARY KEY AUTOINCREMENT, 
            company_name TEXT NOT NULL,
			company_api_key TEXT NOT NULL,
            company_admin TEXT NOT NULL
        )""",
        """CREATE TABLE IF NOT EXISTS location(
            location_id INTEGER PRIMARY KEY AUTOINCREMENT,
            company_api_key TEXT NOT NULL,
            location_name TEXT NOT NULL,
			location_country TEXT NOT NULL,
			location_city TEXT NOT NULL,
            location_meta TEXT NOT NULL
        )""",
        """CREATE TABLE IF NOT EXISTS sensor(
            sensor_id INTEGER PRIMARY KEY AUTOINCREMENT,
            location_id INTEGER,
			sensor_name TEXT NOT NULL,
			sensor_category TEXT NOT NULL,
            sensor_meta TEXT NOT NULL,
			sensor_api_key TEXT NOT NULL
        )""",
        """CREATE TABLE IF NOT EXISTS sensor_datas(
            data_id INTEGER PRIMARY KEY AUTOINCREMENT,
            sensor_api_key TEXT NOT NULL,
			tiempo INTEGER NOT NULL,
			variable_uno REAL NOT NULL,
            variable_dos REAL NOT NULL
        )"""
    ]
    
    db = get_db()
    cursor = db.cursor()
    for table in tables:
        cursor.execute(table)

def llena_tabla():
    db = get_db()
    cursor_dos = db.cursor()
    uno = "admin"
    statement_dos = "INSERT OR REPLACE INTO admin(name, password) VALUES (?, ?)"
    cursor_dos.execute(statement_dos,[uno,uno])
    cursor_tres = db.cursor()
    #C = 10  # numero de caracteres en el string  
    #ranC = ''.join(random.choices(string.ascii_uppercase + string.digits, k = C))
    #company_api_key =  str(ranC)
    #print("company_api_key",company_api_key)
    company_name = "company1"
    company_api_key = "12345ABCDE"
    company_admin = uno
    statement_tres = "INSERT OR REPLACE INTO company(company_name, company_api_key,company_admin) VALUES (?, ?, ?)"
    cursor_tres.execute(statement_tres,[company_name,company_api_key,company_admin])
    db.commit()
