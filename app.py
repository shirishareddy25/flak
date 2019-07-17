#from logging.handlers import RotatingFileHandler
from flask import request
from flask import Flask
from influxdb import InfluxDBClient
'''import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s : %(message)s')

file_handler = RotatingFileHandler("app.log", maxBytes=2000, backupCount=10)

file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

logger.info('user has logged in')
'''
app = Flask(__name__)
client: InfluxDBClient = InfluxDBClient(host='localhost', port=8086, database='indb')


@app.route('/sensors_data', methods=['POST'])
def sensors_data():
    try:
        _json = request.json

        _table = _json['table']
        _temp = _json['temp']
        _humidity = _json['humidity']
        _fire_comb = _json['fire_comb']
        _gas_id = _json['gas_id']
        _id = _json['id']

        json_body = [
            {
                "measurement": _table,
                "tags": {

                    "temperature": _temp,
                    "humidity": _humidity,
                    "fire_comb": _fire_comb,
                    "gas_id": _gas_id
                },
                "fields":
                    {
                        "id": _id,
                    }


            }
        ]
        client.write_points(json_body)

        resp = 'inserted!!!!!!'
        #logger.info('user has inserted into sensors_data')

        return resp

    except Exception as e:
        print(e)

@app.route('/range_dep', methods=['POST'])
def range_dep():
    try:
        _json = request.json

        _table = _json['table']
        _ir_range = _json['ir_range']
        _light_dep = _json['light_dep']
        _id = _json['id']

        json_body = [
            {
                "measurement": _table,
                "tags": {

                    "ir_range": _ir_range,
                    "light_dependency": _light_dep,

                },
                "fields":
                    {
                        "id": _id,
                    }


            }
        ]
        client.write_points(json_body)

        resp = 'inserted!!!!!!'
        #logger.info('user has inserted into range_dep')
        return resp

    except Exception as e:
        print(e)
'''
@app.route('/select/<id>', methods=['GET'])
def select(id):
    try:
        client['']
        results = client.query("select * from table where id="+id)
        #points = results.get_points(tags={'id': '_id'})
        return results

    except Exception as e:
        print(e)

@app.route("/user/<id>/<table_name>", methods=["GET"])
def user_detail(id,table_name):
    user = client.query.get(id)
    return user
    '''
if __name__ == "__main__":
    app.run()
