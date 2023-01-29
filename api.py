import requests

class API:
	def __init__(self):
		pass

	def call_api(self, base_url, member_id):
		url = "{}?member_id={}".format(base_url, member_id)
		print("url: {}".format(url))

		# Call API and get response
		response = requests.get(url)
		print(response.status_code)
		print(response.json())
		print("\n")

		return response.json()

	def aggregate_apis(self, member_id):
		result1 = self.call_api("http://127.0.0.1:5000/api1", member_id)
		result2 = self.call_api("http://127.0.0.1:5000/api2", member_id)
		result3 = self.call_api("http://127.0.0.1:5000/api3", member_id)

		# TODO: Make this configurable
		aggregate_deductible = int((result1["deductible"] + result2["deductible"] + result3["deductible"])/3)
		aggregate_stop_loss = int((result1["stop_loss"] + result2["stop_loss"] + result3["stop_loss"])/3)
		aggregate_oop_max = int((result1["oop_max"] + result2["oop_max"] + result3["oop_max"])/3)

		return {
			"deductible": aggregate_deductible,
			"stop_loss": aggregate_stop_loss,
			"oop_max": aggregate_oop_max
		}


x = API()
print(x.aggregate_apis(1))
print(x.aggregate_apis(2))
print(x.aggregate_apis())

