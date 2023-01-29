from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Welcome to this test server!"

@app.route("/api1")
def api1():
	return "{deductible: 1000, stop_loss: 10000, oop_max: 5000}"

@app.route("/api2")
def api2():
	return "{deductible: 1200, stop_loss: 13000, oop_max: 6000}"

@app.route("/api3")
def api3():
	return "{deductible: 1000, stop_loss: 10000, oop_max: 6000}"
