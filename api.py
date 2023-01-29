import requests

class API:
	def __init__(self, member_id):
		self.member_id = member_id

	def call_api(self, base_url):
		url = "{}?member_id={}".format(base_url, self.member_id)
		print("url: {}".format(url))

		# Call API and get response
		response = requests.get(base_url)
		print(response.status_code)
		print(response.json())
		print("\n")



x = API(1)
x.call_api("http://127.0.0.1:5000/api1")
x.call_api("http://127.0.0.1:5000/api2")
x.call_api("http://127.0.0.1:5000/api3")
