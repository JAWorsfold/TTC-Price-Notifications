class TTCTradeParser:
  # trades parser must
  # - parse response content
  # - send in unix timestamp and ignore those after the last timestamp (after the last search)
  # - filter our deals from traders not accessible
  # - write to csv the item name (quality, trait), expected profit (unit and total), where the deal is
  # - must keep a set of all tradeIDs already seen and don't add these to csv
  # store the unix timestamp from the last trade for each item
  pass

  def count_page_numbers(self):
    # count how many pages there are for each request
    # populate a new list of searches (search, url, response) for each new page
    # return the list and run again if not empty
    pass

  def get_trades(self):
    # create a new list dict with just what to write to the new file
    # deep copy search or only take what is needed from the search dict
    pass