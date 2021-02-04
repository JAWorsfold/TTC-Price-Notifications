from datetime import date, datetime
import requests
import sched
import time

from src import TTCRequests, Resources, TTCTradeParser, CSVHelper


def get_unix_timestamp(dt):
    return


def handle_search_requests(sc, wait=60, unix_time=False):
    print("######### INITIATING SEARCHES #########" )
    print(unix_time)
    # my code
    req.search_requests()
    print(req.srch_requests)

    # trades parser must
    # - parse response content
    # - send in unix timestamp and ignore those after the last timestamp (after the last search)
    # - filter our deals from traders not accessible
    # - write to csv the item name (quality, trait), expected profit (unit and total), where the deal is
    # - must keep a set of all tradeIDs already seen and don't add these to csv
    # store the unix timestamp from the last trade for each item

    # req.srch_requests () = new list of searches from parser
    # req.reset_searches() -> DO NOT NEED HOPEFULLY
    unix_time = int(time.time())
    print(unix_time)
    print(f"######### WAITING {wait} SECONDS #########" )
    s.enter(wait, 1, handle_search_requests, (sc, wait,  unix_time))


if __name__ == "__main__":

    print("########## PROGRAM STARTED ############" )

    # get todays date
    dt = date.today()
    dt_start = datetime.combine(dt, datetime.min.time())
    dt_now = datetime.now()
    dtn_timestamp = int(dt_now.timestamp())
    dts_timestamp = int(dt_start.timestamp())
    print(dt_start)
    print(datetime.now())
    print(dts_timestamp)
    print(dtn_timestamp)

    # load resources
    resources = Resources()

    # build and send price check get requests
    req = TTCRequests(resources.searches, resources.min_profit_margin)
    print("######### RUNNING PRICE CHECK #########" )
    req.price_checks()

    # write price check data to csv
    print("######### WRITING PRICE DATA ##########" )
    CSVHelper.dict_to_csv(
      "./data/price_check_data.csv",
      CSVHelper.add_date_column(dt_start, resources.searches),
      sort_order=['date', 'ItemNamePattern'],
      sort_direction=[False, True],
      date_columns=['date'])

    # start schedule job to search periodically for deals
    # s = sched.scheduler(time.time, time.sleep)
    # s.enter(0, 1, handle_search_requests, (s,))
    # s.run()
