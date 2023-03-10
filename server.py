from flask import Flask, request
import random

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Welcome to this test server! There are three possible apis to call: [api1, api2, api3]. Please add the api endpoint and pass in a member_id param i.e. http://127.0.0.1:5000/api1?member_id=1"

@app.route('/api1', methods=['GET'])
def api1():
    args = request.args
    member_id = args.get('member_id')

    if member_id == '1':
    	return {
	    	"deductible": 1000,
	        "stop_loss": 10000,
	        "oop_max": 5000
	    }
    elif member_id.isnumeric():
        return {
            "deductible": random.randint(0, 100000),
            "stop_loss": random.randint(0, 100000),
            "oop_max": random.randint(0, 100000)
        }
    else:
        return "Please enter member_id for api1" 

@app.route('/api2', methods=['GET'])
def api2():
    args = request.args
    member_id = args.get('member_id')

    if member_id == '1':
    	return {
            "deductible": 1200,
            "stop_loss": 13000,
            "oop_max": 6000
        }
    elif member_id.isnumeric():
        return {
            "deductible": random.randint(0, 100000),
            "stop_loss": random.randint(0, 100000),
            "oop_max": random.randint(0, 100000)
        }
    else:
        return "Please enter member_id for api2"

@app.route('/api3', methods=['GET'])
def api3():
    args = request.args
    member_id = args.get('member_id')

    if member_id == '1':
    	return {
            "deductible": 1000,
            "stop_loss": 10000,
            "oop_max": 6000
        }
    elif member_id.isnumeric():
        return {
            "deductible": random.randint(0, 100000),
            "stop_loss": random.randint(0, 100000),
            "oop_max": random.randint(0, 100000)
        }
    else:
        return "Please enter member_id for api3"
