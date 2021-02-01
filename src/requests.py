import concurrent.futures
import requests
import threading

from src import TTCPriceCheckParser

thread_local = threading.local()


class TTCRequests():

  _url = "https://eu.tamrieltradecentre.com/"
  _prck_suffix = "pc/Trade/SearchResult?SearchType=PriceCheck"
  _srch_suffix = "api/pc/Trade/Search?SearchType=Sell"
  _guild_fees = 0.07
  _first_search = True
  prck_requests = []
  srch_requests = []

  def __init__(self, searches, prof_marg):
    self.searches = searches
    self.prof_marg = prof_marg
    self._build_urls(self.prck_requests, self._prck_suffix)
    self._build_urls(self.srch_requests, self._srch_suffix)

  def reset_searches(self):
    for search in self.srch_requests:
      search["resp"] = None

  def price_checks(self):
    self.make_all_requests(self.prck_requests)
    for req in self.prck_requests:
      parser = TTCPriceCheckParser()
      parser.reset_check()
      parser.feed(str(req["resp"].content))
      req["search"].update(parser.get_prices())
    self._update_search_urls()
    print(self.prck_requests)

  def search_requests(self):
    self.make_all_requests(self.srch_requests)
    print(self.srch_requests)

  def _calc_buy_price(self, sell_price):
    fees = sell_price * self._guild_fees
    prof_marg_amt = sell_price * self.prof_marg
    return (round(sell_price - fees - prof_marg_amt, 2),
            round(sell_price - fees, 2))

  def _build_urls(self, urls, suffix):
    for i in self.searches:
      url = f"{self._url}{suffix}"
      for k, v in i.items():
        url += f"&{k}={v}"
      urls.append({"search": i, "url": url, "resp": None})

  def _update_search_urls(self):
    for req in self.srch_requests:
      param_name = "PriceMax"
      price_max, price_aft_fees = self._calc_buy_price(req["search"]["avg"])
      max_price_param = {param_name: price_max,
                         "price_after_fees": price_aft_fees}
      req['search'].update(max_price_param)
      req['url'] += f"&{param_name}={str(price_max)}&SortBy=LastSeen&Order=desc"

  def get_session(self):
    if not hasattr(thread_local, "session"):
      thread_local.session = requests.Session()
    return thread_local.session

  def make_request(self, req):
    session = self.get_session()
    with session.get(req["url"]) as response:
      req["resp"] = response

  def make_all_requests(self, req):
    with concurrent.futures.ThreadPoolExecutor(
        max_workers=(len(req) // 2 + len(req) % 2)
    ) as executor:
      executor.map(self.make_request, req)
