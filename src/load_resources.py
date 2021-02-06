# have to load the resources
# the traders/ acessible list
# which things to actually search for

import json

class Resources():

  _traders_fp = ".\\resources\\traders.json"
  _searches_fp = ".\\resources\\searches.json"
  traders = {}
  searches = {}
  traits = {}
  recaptcha = ""
  min_profit_margin = 0.1

  def __init__(self):
    # load traders from filepath
    traders = self._load_file_as_json(self._traders_fp)

    # remove any inaccessible traders
    inaccessible = traders["inaccessible"]
    self.traders = {
        key: value for (key, value) in traders["traders"].items()
        if value["region"] not in inaccessible
    }

    # load searches
    searches = self._load_file_as_json(self._searches_fp)
    self.searches = searches["searches"]
    if searches["min_profit_margin"]:
      self.min_profit_margin = searches["min_profit_margin"]
    self.traits = searches["traits"]
    self.recaptcha = searches["recaptcha"]

  def _load_file_as_json(self, fp):
    with open(fp) as f:
      return json.load(f)
