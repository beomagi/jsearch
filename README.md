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
  ![sample_search_1](https://github.com/beomagi/jsearch/assets/12766711/ade41d9c-aa67-4593-867a-1f38956c3f2e)

  This output can be fed back into JQ:
  ![image](https://github.com/beomagi/jsearch/assets/12766711/2e66f328-d9cf-42fc-bee1-e19b9e1b3e84)


e.g.
 Using reddit data via curl https://www.reddit.com/r/linux.json > reddit_r_linux.json
 ![sample_search_2](https://github.com/beomagi/jsearch/assets/12766711/741bbfbd-36f2-4c9a-8eec-b1e3f383bc9c)
