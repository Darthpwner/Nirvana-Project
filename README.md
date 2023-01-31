# Nirvana-Project

**Usage**
1. Kick off the server by running `flask --app server run`
2. To validate the endpoint by hand, go to `http://127.0.0.1:5000` in any web browser. 
3. Run `python runner.py --member_id <MEMBER_ID>` with a positive integer to test. '1' is hardcoded to have the values set in the example, and any other member_id is randomly generated from the range (0, 100000).
4. I've defined 4 types of configurations: mean, median, min, and max. To define a new configuration, please add the new configuration to `api.py` as a non-member function and pass it in as the second argument in the `coalesce.aggregate_apis` call. Example: `coalesce.aggregate_apis(args.member_id, mean_config)`