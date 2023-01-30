from api import *

def main():
	x = API()
	print(x.aggregate_apis(1, mean_config))
	print("\n")

	print(x.aggregate_apis(1, median_config))
	print("\n")

	print(x.aggregate_apis(2, mean_config))
	print("\n")

	print(x.aggregate_apis(2, median_config))
	print("\n")

if __name__ == "__main__":
    main()
