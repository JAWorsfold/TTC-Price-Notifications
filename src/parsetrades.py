from datetime import datetime

class TTCTradeParser:
  # trades parser must
  # - parse response content
  # - send in unix timestamp and ignore those after the last timestamp (after the last search)
  # - filter our deals from traders not accessible
  # - write to csv the item name (quality, trait), expected profit (unit and total), where the deal is
  # - must keep a set of all tradeIDs already seen and don't add these to csv
  # store the unix timestamp from the last trade for each item

  def __init__(self, resources):
    self._traderIDs = resources.traders
    self._traits = resources.traits
    self.reset()

  def reset(self):
    self.trades = []

  def _get_page_searches(self, page_count):
    new_searches = []
    for n in range(1, page_count):
      new_url = search['url'] + '&page=' + str(n+1)
      new_searches.append(
        {"search": search['search'], "url": new_url, 
        "resp": None, "page": n + 1})
    return new_searches

  def parse_trades(self, lst_searchs):
    # create a new list dict with just what to write to the new file
    # deep copy search or only take what is needed from the search dict
    for search in lst_searchs:
      response = search['resp'].json()
      current_page = response['TradeListPageModel']['TotalPageCount']
      if current_page > 0:
        trade_details = response['TradeListPageModel']['TradeDetails']
        # posted, item info, amount, total profit, buy_unit, buy_total, sell_unit, sell_total, sell_after_fees
        for trade_item in trade_details:
          self.trades.append(
            {
              print(datetime.utcfromtimestamp(trade_item['DiscoverUnixTime']))
            }
          )


      # if search['page'] == 1:
      #   # first search
      #   page_count = response['TradeListPageModel']['TotalPageCount']
      #   if page_count > 1:
      #     new_searches = self._get_page_searches(page_count)
    #     # create new requests
    #   if search['page']
    #   if page_count == 1:
    #     # self.add_trades(search['search'], response)
    #     # more requests sent
    #     pass
    #   elif page_count > 1:
    #     # https://eu.tamrieltradecentre.com/api/pc/Trade/Search?SearchType=Sell&ItemID=211&ItemNameP
    #     # attern=Dreugh+Wax&ItemCategory1ID=&ItemTraitID=&ItemQualityID=&IsChampionPoint=false&Level
    #     # Min=&LevelMax=&MasterWritVoucherMin=&MasterWritVoucherMax=&AmountMin=&AmountMax=&PriceMin=&PriceMax=&page=2
    #     pass
    #   print(search['resp'].json()['TradeListPageModel']['TotalPageCount'])
    #   # posted, item info, amount, total profit, buy_unit, buy_total, sell_unit, sell_total, sell_after_fees
    #   # {'TradeListPageModel': {'TradeDetails': [], 'CurrentPage': 0, 'TotalPageCount': 0, 'TotalMatchCount': 0}, 'IsSuccess': True, 'Code': 0}
    # pass
