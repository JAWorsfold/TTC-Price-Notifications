# have to load the resources
# the traders/ acessible list
# which things to actually search for

import json

traders_file = open("..\\resources\\traders.json")

traders = json.load(traders_file)

inaccessible = traders["inaccessible"]

traders = {key: value for (key, value) in traders["traders"].items()
           if value["region"] not in inaccessible}

traderId = 56
if str(traderId) in traders:
  print(traders[str(traderId)])
else:
  print('undefined')
