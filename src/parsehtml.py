import sys
import os
from html.parser import HTMLParser


class TTCPriceCheckParser(HTMLParser):

  _active_tag = False
  _tag_count = 0
  _attr_str = "gold"
  _price_data = []

  def reset_check(self):
    self._tag_count = 0
    self._price_data = []

  def handle_starttag(self, tag, attrs):
    if self._tag_count == 6:
      return
    if tag == "span":
      for attr in attrs:
        if self._attr_str in attr[1]:
          self._active_tag = True
          self._tag_count += 1

  def handle_endtag(self, tag):
    if self._tag_count == 6:
      return
    if tag == "span" and self._active_tag:
      self._active_tag = False

  def handle_data(self, data):
    if self._tag_count == 6:
      return
    if self._active_tag:
      self._price_data.append(data.strip())

  def get_prices(self):
    prices = self._price_data
    return {
        "min": prices[0],
        "avg": prices[1],
        "max": prices[2],
        "low-sug": prices[3],
        "high-sug": prices[4]
    }
