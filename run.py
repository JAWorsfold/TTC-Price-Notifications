# Program start
# -- connect to Google drive
# -- load existing IDs
# -- run get requests for average prices
# -- store average price, suggested min, suggested max for that day (Google tab)
# -- load items from prop file (name, minimum price if avg or suggested too low, profit margin)
# -- calculate the max price for search - avg - 7% fees - minimum profit margin
# -- run get requests for items specific and max price in search
# -- first run - look at past 12 hours
# -- second run look at past 5 minutes (repeat)
# -- map reduce
#   -- remove any ids already searched
#   -- keep requesting pages until unix time matches the unix time from the last run
# -- map reduce output : dict with id of sale, item name, buy price, quantity, location (region, town, trader), sell price, profit.
# -- Store this information live in google sheets.
# New tab for each day it runs.

# Concurrent requests for each item? Maybe try using async?
# Concurrent writes to Google sheet?

# https://eu.tamrieltradecentre.com/pc/Trade/SearchResult?SearchType=PriceCheck&&ItemNamePattern=Dreugh+Wax

import requests
import time

from src import TTCPriceCheckParser


def download_site(url, session):
  with session.get(url) as response:
    print(f"{url}")
    print(f"Response:\n{response.content}")


def download_all_sites(sites):
  with requests.Session() as session:
    for url in sites:
      download_site(url, session)


if __name__ == "__main__":
  # make price check concurrent -> list of price check request urls
  sites = [
      "https://eu.tamrieltradecentre.com/pc/Trade/SearchResult?SearchType=PriceCheck&&ItemNamePattern=Dreugh+Wax"
  ]
  start_time = time.time()

  parser = TTCPriceCheckParser()
  url = "https://eu.tamrieltradecentre.com/pc/Trade/SearchResult?SearchType=PriceCheck&&ItemNamePattern=Dreugh+Wax"
  with requests.Session() as session:
    req_start_time = time.time()
    with session.get(url) as response:
      req_end_time = time.time()
      parser.feed(str(response.text))
  duration = time.time() - start_time
  print(parser.get_prices())
  print("program duration: ", duration)
  print("request duration: ", req_end_time - req_start_time)
