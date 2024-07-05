Usage:
```
./jsearch.py -f <json_file> -s <search_string> [-i] [-h] [-k]
./jsearch.py -j <json_text> -s <search_string> [-i] [-h] [-k]
-i ignore case
-h highlight search string
-k keys only
```

e.g.
 Against github data:
  collected data using - curl https://api.github.com/events > github_events_20240705.json
  ![image](https://github.com/beomagi/jsearch/assets/12766711/199ec1ef-328b-41cc-9010-259ba79ab80b)


  This output can be fed back into JQ:
  ![image](https://github.com/beomagi/jsearch/assets/12766711/2e66f328-d9cf-42fc-bee1-e19b9e1b3e84)


e.g.
 Using reddit data via curl https://www.reddit.com/r/linux.json > reddit_r_linux.json
 ![image](https://github.com/beomagi/jsearch/assets/12766711/ccfd903a-5e50-44b7-a89d-a70bd47c2b39)

