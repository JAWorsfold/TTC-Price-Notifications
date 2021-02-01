import requests
import sched
import time

from src import TTCRequests, Resources, TTCTradeParser

global wait_time
wait_time = 60


def handle_search_requests(sc, unix_time=False):
  print("Starting search")
  print(unix_time)
  # my code
  req.search_requests()

  # trades parser must
  # - parse response content
  # - send in unix timestamp and ignore those after the last timestamp (after the last search)
  # - filter our deals from traders not accessible
  # - write to csv the item name (quality, trait), expected profit (unit and total), where the deal is
  
  # store the unix timestamp from the last trade for each item

  # req.reset_searches()
  unix_time = int(time.time())
  print(unix_time)
  print("Starting wait")
  s.enter(1, 1, handle_search_requests, (sc, unix_time))


if __name__ == "__main__":

  print("Program starting")
  # load resources
  resources = Resources()

  # build and send price check get requests
  req = TTCRequests(resources.searches, resources.min_profit_margin)
  req.price_checks()
  # TODO - write to csv - date+time + search data
  # TODO - write to csv helper class

  # start schedule job to search periodically for deals
  message = "First"
  s = sched.scheduler(time.time, time.sleep)
  s.enter(0, 1, handle_search_requests, (s,))
  s.run()
