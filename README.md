# Nirvana-Project

**Usage**
1. Kick off the server by running `flask --app server run`
2. To validate the endpoint by hand, go to `http://127.0.0.1:5000` in any web browser. 
3. Run `python runner.py --member_id <MEMBER_ID>` with a positive integer to test. '1' is hardcoded to have the values set in the example, and any other member_id is randomly generated from the range (0, 100000).
Example: `python runner.py --member_id 1`
4. I've defined 4 types of configurations: mean, median, min, and max. To define a new configuration, please add the new configuration to `api.py` as a non-member function and pass it in as the second argument in the `coalesce.aggregate_apis` call. 
Example: `coalesce.aggregate_apis(args.member_id, mean_config)`

**Future Design Considerations**
* Make `aggregate_apis` function more flexible and allow it to take more than 3 API calls. Right now, I hardcoded it to the three APIs mentioned in the project spec, but if we need more API calls, this should be flexible.
* More documentation would be helpful.