import requests
import argparse

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

		return response.json()

	def aggregate_apis(self, member_id, configuration=None):
		result1 = self.call_api("http://127.0.0.1:5000/api1", member_id)
		result2 = self.call_api("http://127.0.0.1:5000/api2", member_id)
		result3 = self.call_api("http://127.0.0.1:5000/api3", member_id)
		list_of_results = [result1, result2, result3]

		aggregate_deductible = configuration(list_of_results, "deductible")
		aggregate_stop_loss = configuration(list_of_results, "stop_loss")
		aggregate_oop_max = configuration(list_of_results, "oop_max")

		return {
			"deductible": aggregate_deductible,
			"stop_loss": aggregate_stop_loss,
			"oop_max": aggregate_oop_max
		}

def mean_config(list_of_results, key):
	total = 0
	for i in list_of_results:
		total += i[key]
	return int(total/len(list_of_results))

def median_config(list_of_results, key):
	all_values = []
	mid = int(len(list_of_results)/2)
	for i in list_of_results:
		all_values.append(i[key])
	sorted_all_values = sorted(all_values)

	return sorted_all_values[mid]


# x = API()
# print(x.aggregate_apis(1, mean_config))
# print("\n")

# print(x.aggregate_apis(1, median_config))
# print("\n")

# print(x.aggregate_apis(2, mean_config))
# print("\n")

# print(x.aggregate_apis(2, median_config))
# print("\n")


# print(x.aggregate_apis())
# print("\n")

