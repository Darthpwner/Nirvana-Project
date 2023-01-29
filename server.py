from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Welcome to this test server!"


db_users = {
    "John" : "Miami",
    "David" : "Miami",
    "Jane" : "London",
    "Gabriella" : "Paris",
    "Tanaka" : "Tokyo"
}

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
    else:
        return "DUMMY API1"

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
    else:
        return "DUMMY API2"

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
    else:
        return "DUMMY API3"
