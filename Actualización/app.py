
#from flask import Flask, jsonify, request
import os

from flask import (Flask, redirect, render_template, request, jsonify,
                   send_from_directory, url_for)
import sensor_controller
import location_controller
from db import create_tables
from db import llena_tabla


app = Flask(__name__)

##################################       LOCATION    ######################################

#### Para obtener una o todas las locaciones de una compañia
@app.route('/api/v1/location', methods=["GET"])
def get_location():
    company_api_key = request.args.get('company_api_key')
    location_id = request.args.get('location_id')

    if (company_api_key != None) and (location_id != None):
        location = location_controller.get_location(company_api_key,location_id) #retorna una location o error
        return jsonify(location)
    elif (company_api_key != None):
        locations = location_controller.get_locations(company_api_key) #retorna todas las location o error
        return jsonify(locations)
    else:
        return "Error", 400 #No se envia company api key

#### Para agregar una locacion (nueva)
@app.route("/api/v1/location", methods=["POST"])
def insert_location():
    admin = request.args.get('admin')
    password = request.args.get('password')
    company_api_key = request.args.get('company_api_key')
    location_name = request.args.get('location_name')
    location_country = request.args.get('location_country')
    location_city = request.args.get('location_city')
    location_meta = request.args.get('location_meta')

    if (company_api_key != None) and (admin != None) and (password != None):
        location = location_controller.insert_location(admin,password,company_api_key,location_name,location_country,location_city,location_meta)
        return "Success", 201
    else: 
        return "Error", 400

#### Para actualizar una locacion existente
@app.route("/api/v1/location", methods=["PUT"])
def update_location():
    admin = request.args.get('admin')
    password = request.args.get('password')
    location_id = request.args.get('location_id')
    company_api_key = request.args.get('company_api_key')
    location_name = request.args.get('location_name')
    location_country = request.args.get('location_country')
    location_city = request.args.get('location_city')
    location_meta = request.args.get('location_meta')

    if (company_api_key != None) and (admin != None) and (password != None):    
        location = location_controller.update_location(admin,password,location_id,company_api_key,location_name,location_country,location_city,location_meta)
        return "Success", 201
    else: 
        return "Error", 400

#### Para eliminar una locacion existente
@app.route("/api/v1/location", methods=["DELETE"])
def delete_location():
    admin = request.args.get('admin')
    password = request.args.get('password')
    location_id = request.args.get('location_id')
    company_api_key = request.args.get('company_api_key')

    if (company_api_key != None) and (admin != None) and (password != None):    
        location = location_controller.delete_location(admin,password,location_id,company_api_key)
        return "Success", 201
    else: 
        return "Error", 400

##########################################   SENSOR        #################################################################################

#### Para obtener uno o todos los sensores de una locacion
@app.route('/api/v1/sensor', methods=["GET"])
def get_sensor():
    company_api_key = request.args.get('company_api_key')
    location_id = request.args.get('location_id')
    sensor_id = request.args.get('sensor_id')

    if (company_api_key != None) and (location_id != None) and (sensor_id != None):        
        sensor = sensor_controller.get_sensor(company_api_key,location_id,sensor_id) #retorna un sensor o error
        return jsonify(sensor)
    elif (company_api_key != None):
        sensors = sensor_controller.get_sensors(company_api_key) #retorna todos los sensor o error
        return jsonify(sensors)
    else:
        return "Error", 400 #No se envia company api key

### Para agregar un sensor (nuevo)
@app.route("/api/v1/sensor", methods=["POST"])
def insert_sensor():
    admin = request.args.get('admin')
    password = request.args.get('password')
    location_id = request.args.get('location_id')
    company_api_key = request.args.get('company_api_key')
    sensor_name = request.args.get('sensor_name')
    sensor_category = request.args.get('sensor_category')
    sensor_meta = request.args.get('sensor_meta')

    if (company_api_key != None) and (admin != None) and (password != None):       
        sensor = sensor_controller.insert_sensor(admin,password,company_api_key,location_id,sensor_name,sensor_category,sensor_meta)
        return "Success", 201
    else: 
        return "Error", 400

#### Para actualizar un sensor existente
@app.route("/api/v1/sensor", methods=["PUT"])
def update_sensor():
    admin = request.args.get('admin')
    password = request.args.get('password')
    location_id = request.args.get('location_id')
    sensor_id = request.args.get('sensor_id')
    company_api_key = request.args.get('company_api_key')
    sensor_name = request.args.get('sensor_name')
    sensor_category = request.args.get('sensor_category')
    sensor_meta = request.args.get('sensor_meta')
    print("algo app")

    if (company_api_key != None) and (admin != None) and (password != None):        
        sensor = sensor_controller.update_sensor(admin,password,company_api_key,location_id,sensor_id,sensor_name,sensor_category,sensor_meta)
        return "Success", 201
    else: 
        return "Error", 400

#### Para eliminar un sensor existente
@app.route("/api/v1/sensor", methods=["DELETE"])
def delete_sensor():
    admin = request.args.get('admin')
    password = request.args.get('password')
    sensor_id = request.args.get('sensor_id')
    company_api_key = request.args.get('company_api_key')

    if (company_api_key != None) and (admin != None) and (password != None):        
        sensor = sensor_controller.delete_sensor(admin,password,sensor_id,company_api_key)
        return "Success", 201
    else: 
        return "Error", 400


###################################      SENSOR_DATA      ##########################################################################################

#### Para recuperar data de un sensor especifico
@app.route('/api/v1/sensor_data', methods=["GET"])
def get_data_sensor():
    sensor_api_key = request.args.get('sensor_api_key')
    desde = request.args.get('desde')
    hasta = request.args.get('hasta')

    if (sensor_api_key != None) and (desde != None) and (hasta != None):      
        sensor = sensor_controller.get_sensor_data(sensor_api_key,desde,hasta) #retorna sensor_data o error
        return jsonify(sensor)
    else:
        return "Error", 400

#### Para agregar datos de un sensor especifico
@app.route("/api/v1/sensor_data", methods=["POST"])
def insert_sensor_data():
    request_data = request.get_json()
    sensor_api_key = None
    tiempo = None
    variable_uno = None
    variable_dos = None

    if request_data:
        if ('sensor_api_key' in request_data) and ('tiempo' in request_data) and ('variable_uno' in request_data) and ('variable_dos' in request_data):
            sensor_api_key = request_data['sensor_api_key']
            tiempo = request_data['tiempo']
            variable_uno = request_data['variable_uno']
            variable_dos = request_data['variable_dos']
            sensor = sensor_controller.insert_sensor_data(sensor_api_key,tiempo,variable_uno,variable_dos)
            return "Success", 201
        else: 
            return "Error", 400

##############################################################################################
#################################### INICIA ####################################################
if __name__ == "__main__":
    create_tables()
    llena_tabla()
    """
    Here you can change debug and port
    Remember that, in order to make this API functional, you must set debug in False
    """
    app.run()
    ##app.run(host='0.0.0.0', port=8000, debug=False)
