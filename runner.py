from api import *

def setup_args():
	parser = argparse.ArgumentParser()

	parser.add_argument("--member_id", type=str, help="The member_id we want to access.", required=True)
	args = parser.parse_args()

	return args

def main():
	coalesce = CoalesceAPI()
	args = setup_args()

	print("mean_config")
	print("coalesced result: {}".format(coalesce.aggregate_apis(args.member_id, mean_config)))
	print("\n")

	print("median_config")
	print("coalesced result: {}".format(coalesce.aggregate_apis(args.member_id, median_config)))
	print("\n")

	print("min_config")
	print("coalesced result: {}".format(coalesce.aggregate_apis(args.member_id, min_config)))
	print("\n")

	print("max_config")
	print("coalesced result: {}".format(coalesce.aggregate_apis(args.member_id, max_config)))
	print("\n")

if __name__ == "__main__":
    main()
