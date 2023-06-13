from db import get_db
import string
import random

'''
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

S = 10  # number of characters in the string.  
# call random.choices() string module to find the string in Uppercase + numeric data.  
ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))    
print("The randomly generated string is : " + str(ran)) # print the random data  
'''
############### sensor

#sensor = sensor_controller.get_sensor(company_api_key,location_id,sensor_id) #retorna un sensor o error
def get_sensor(company_api_key,location_id,sensor_id):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT location_id, sensor_id, sensor_name, sensor_category, sensor_meta, sensor_api_key FROM sensor WHERE sensor_id = ? AND location_id = ?"
    cursor.execute(statement, [sensor_id,location_id])
    return cursor.fetchone()


#sensors = sensor_controller.get_sensors(company_api_key) #retorna todos los sensor o error
def get_sensors(company_api_key):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT location_id, sensor_id, sensor_name, sensor_category, sensor_meta, sensor_api_key FROM sensor WHERE location_id = (SELECT sensor.location_id FROM company, location, sensor WHERE company.company_api_key = ? AND location.company_api_key = company.company_api_key AND sensor.location_id = location.location_id GROUP BY sensor.location_id)"
    cursor.execute(statement, [company_api_key])
    return cursor.fetchall()


#sensor = sensor_controller.insert_sensor(admin,password,company_api_key,location_id,sensor_name,sensor_category,sensor_meta)
def insert_sensor(admin,password,company_api_key,location_id,sensor_name,sensor_category,sensor_meta):
    db = get_db()
    cursor = db.cursor()
    statement_uno = "SELECT name FROM admin WHERE name = ? AND password = ?"
    cursor.execute(statement_uno, [admin, password])

    comprobar = cursor.fetchone() #Existe admin y contraseña es correcta

    if comprobar is None:
        return False
    else:
        S = 10  # numero de caracteres en el string  
        ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))
        sensor_api_key =  str(ran)
        cursor_dos = db.cursor() # otro cursor
        statement_dos = "INSERT INTO sensor(location_id, sensor_name, sensor_category, sensor_meta, sensor_api_key) VALUES (?, ?, ?, ?, ?, ?)"
        cursor_dos.execute(statement_dos, [location_id, sensor_name, sensor_category, sensor_meta, sensor_api_key])
        db.commit()
        return True

#sensor = sensor_controller.update_sensor(admin,password,company_api_key,location_id,sensor_id,sensor_name,sensor_category,sensor_meta)
def update_sensor(admin,password,company_api_key,location_id,sensor_id,sensor_name,sensor_category,sensor_meta):
    db = get_db()
    cursor = db.cursor()
    statement_uno = "SELECT name FROM admin WHERE name = ? AND password = ?"
    cursor.execute(statement_uno, [admin, password])

    comprobar = cursor.fetchone() #Existe admin y contraseña es correcta

    if comprobar is None:
        return False
    else:
        cursor_dos = db.cursor() # otro cursor
        statement_dos = "UPDATE sensor SET location_id = ?, sensor_id = ?, sensor_name = ?, sensor_category = ?, sensor_meta = ? WHERE location_id = ? AND company_api_key = ?"
        cursor_dos.execute(statement_dos, [location_id, sensor_id, sensor_name, sensor_category, sensor_meta, location_id, company_api_key])
        db.commit()
        return True


#sensor = sensor_controller.delete_sensor(admin,password,sensor_id,company_api_key) 
def delete_sensor(admin,password,sensor_id,company_api_key):
    db = get_db()
    cursor = db.cursor()
    statement_uno = "SELECT name FROM admin WHERE name = ? AND password = ?"
    cursor.execute(statement_uno, [admin, password])

    comprobar = cursor.fetchone() #Existe admin y contraseña es correcta

    if comprobar is None:
        return False
    else:
        cursor_dos = db.cursor() # otro cursor
        statement_dos =  "DELETE FROM sensor WHERE sensor_id = ? AND location_id = (SELECT sensor.location_id FROM company, location, sensor WHERE company.company_api_key = ? AND location.company_api_key = company.company_api_key AND sensor.location_id = location.location_id GROUP BY sensor.location_id)"
        cursor_dos.execute(statement_dos, [location_id, company_api_key])
        db.commit()
        return True


#########   sensor_data

#sensor = sensor_controller.get_sensor_data(sensor_api_key,desde,hasta) #retorna sensor_data o error
def get_sensor_data(sensor_api_key,desde,hasta):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT sensor_api_key, tiempo, variable_uno, variable_dos FROM sensor_data WHERE sensor_api_key = ? AND tiempo BETWEEN ? AND ?"
    cursor.execute(statement, [sensor_api_key,desde,hasta])
    return cursor.fetchall()


#sensor = sensor_controller.insert_sensor_data(sensor_api_key,tiempo,variable_uno,variable_dos)
def insert_sensor_data(sensor_api_key,tiempo,variable_uno,variable_dos):
    db = get_db()
    cursor = db.cursor()

    statement = "INSERT INTO sensor_data(sensor_api_key, tiempo, variable_uno, variable_dos) VALUES (?, ?, ?, ?)"
    cursor.execute(statement, [sensor_api_key,tiempo,variable_uno,variable_dos])
    db.commit()
    return True






