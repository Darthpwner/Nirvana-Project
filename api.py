import requests

class API:
	def __init__(self):
		pass

	def call_api(self, base_url, member_id):
		url = "{}?member_id={}".format(base_url, member_id)
		print("url: {}".format(url))

		# Call API and get response
		response = requests.get(base_url)
		print(response.status_code)
		print(response.json())
		print("\n")

	def aggregate_apis(self, member_id):
		x.call_api("http://127.0.0.1:5000/api1", member_id)
		x.call_api("http://127.0.0.1:5000/api2", member_id)
		x.call_api("http://127.0.0.1:5000/api3", member_id)



x = API()
# x.call_api("http://127.0.0.1:5000/api1", 1)
# x.call_api("http://127.0.0.1:5000/api2", 1)
# x.call_api("http://127.0.0.1:5000/api3", 1)

# x.call_api("http://127.0.0.1:5000/api1", 2)

x.aggregate_apis(1)
