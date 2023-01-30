from api import *

def main():
	coalesce = CoalesceAPI()

	print(coalesce.aggregate_apis(1, mean_config))
	print("mean_config\n")
	print(coalesce.aggregate_apis(1, median_config))
	print("median_config\n")
	print(coalesce.aggregate_apis(1, min_config))
	print("min_config\n")
	print(coalesce.aggregate_apis(1, max_config))
	print("max_config\n")

	print(coalesce.aggregate_apis(2, mean_config))
	print("mean_config\n")
	print(coalesce.aggregate_apis(2, median_config))
	print("median_config\n")
	print(coalesce.aggregate_apis(2, min_config))
	print("min_config\n")
	print(coalesce.aggregate_apis(2, max_config))
	print("max_config\n")

if __name__ == "__main__":
    main()
