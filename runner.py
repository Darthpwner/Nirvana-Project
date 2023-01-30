from api import *

def setup_args():
	parser = argparse.ArgumentParser()

	parser.add_argument("--member_id", type=str, help="The member_id we want to access.", required=True)
	args = parser.parse_args()

	return args

def main():
	coalesce = CoalesceAPI()

	args = setup_args()

	print(coalesce.aggregate_apis(args.member_id, mean_config))
	print("mean_config\n")
	print(coalesce.aggregate_apis(args.member_id, median_config))
	print("median_config\n")
	print(coalesce.aggregate_apis(args.member_id, min_config))
	print("min_config\n")
	print(coalesce.aggregate_apis(args.member_id, max_config))
	print("max_config\n")

if __name__ == "__main__":
    main()
