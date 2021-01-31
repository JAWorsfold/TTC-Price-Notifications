import requests
import time

from src import TTCRequests, Resources, TTCPriceCheckParser


if __name__ == "__main__":
  
  # load resources
  resources = Resources()

  # build and send price check get requests
  req = TTCRequests(resources.searches, resources.min_profit_margin)

  start_time = time.time()
  req.price_checks()

  req.search_requests()
  req.reset()
  print(resources.searches)

  # build get requests for on-going trades

  # send first batch of requests
  # figure out how many pages there are 

  # first look back for 15 minutes - go though each page until hitting the now timestamp + 15 minutes

  # then store the unix timestamp from the last trade for each item

  # either create notification, ping eso chat, or add results to google sheet

  # after a specified time delay, send the get requests again

  # go through the pages again until hit the recorded item time stamp

  # safe stop? 

  duration = time.time() - start_time
  print(f"Downloaded {len(req.prck_requests)} in {duration} seconds")