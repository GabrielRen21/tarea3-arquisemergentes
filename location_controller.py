from db import get_db
import string
import random


#location = location_controller.get_location(company_api_key,location_id) #retorna una location o error
def get_location(company_api_key,location_id):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT location_id, company_api_key, location_name, location_country, location_city, location_meta FROM location WHERE location_id = ? AND company_api_key = ?"
    cursor.execute(statement, [location_id,company_api_key])
    return cursor.fetchone()


#locations = location_controller.get_locations(company_api_key) #retorna todas las location o error
def get_locations(company_api_key):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT location_id, company_api_key, location_name, location_country, location_city, location_meta FROM location WHERE company_api_key = ?"
    cursor.execute(statement, [company_api_key])
    return cursor.fetchall()


#location = location_controller.insert_location(admin,password,company_api_key,location_name,location_country,location_city,location_meta)
def insert_location(admin,password,company_api_key,location_name,location_country,location_city,location_meta):
    db = get_db()
    cursor = db.cursor()
    statement_uno = "SELECT name FROM admin WHERE name = ? AND password = ?"
    cursor.execute(statement_uno, [admin, password])

    comprobar = cursor.fetchone() #Existe admin y contraseña es correcta
    
    if comprobar != None:
        return False
    else:
        #cursor_dos = db.cursor() # otro cursor
        statement_dos = "INSERT INTO location(company_api_key, location_name, location_country, location_city, location_meta) VALUES (?, ?, ?, ?, ?)"
        cursor.execute(statement_dos, [company_api_key, location_name, location_country, location_city, location_meta])
        db.commit()
        return True

#location = location_controller.update_location(admin,password,location_id,company_api_key,location_name,location_country,location_city,location_meta)
def update_location(admin,password,location_id,company_api_key,location_name,location_country,location_city,location_meta):
    db = get_db()
    cursor = db.cursor()
    statement_uno = "SELECT name FROM admin WHERE name = ? AND password = ?"
    cursor.execute(statement_uno, [admin, password])

    comprobar = cursor.fetchone() #Existe admin y contraseña es correcta

    if comprobar is None:
        return False
    else:
        cursor_dos = db.cursor() # otro cursor
        statement_dos = "UPDATE location SET location_name = ?, location_country = ?, location_city = ?, location_meta = ? WHERE location_id = ? AND company_api_key = ?"
        cursor_dos.execute(statement_dos, [location_name, location_country, location_city, location_meta, location_id, company_api_key])
        db.commit()
        return True


#location = location_controller.delete_location(admin,password,location_id,company_api_key)
def delete_location(admin,password,location_id,company_api_key):
    db = get_db()
    cursor = db.cursor()
    statement_uno = "SELECT name FROM admin WHERE name = ? AND password = ?"
    cursor.execute(statement_uno, [admin, password])

    comprobar = cursor.fetchone() #Existe admin y contraseña es correcta 

    if comprobar is None:
        return False
    else:
        cursor_dos = db.cursor() # otro cursor
        statement_dos =  "DELETE FROM location WHERE  location_id = ? AND company_api_key = ?"
        cursor_dos.execute(statement_dos, [location_id, company_api_key])
        db.commit()
        return True




