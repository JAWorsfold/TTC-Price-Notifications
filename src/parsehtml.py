import sys
import os
from html.parser import HTMLParser


class TTCPriceCheckParser(HTMLParser):

  _active_tag = False
  _tag_count = 0
  _data = []

  def reset_check(self):
    self._tag_count = 0
    self._data = []

  def handle_starttag(self, tag, attrs):
    if self._tag_count == 5:
      return
    if tag == "span":
      for attr in attrs:
        if "gold" in attr[1]:
          self._active_tag = True

  def handle_endtag(self, tag):
    if self._tag_count == 5:
      return
    if self._active_tag and tag == "span":
      self._active_tag = False
      self._tag_count += 1

  def handle_data(self, data):
    if self._tag_count == 5:
      return
    if self._active_tag:
      self._data.append(
          data.replace("\\r", "").replace("\\n", "").strip())

  def get_prices(self):
    data = self._data
    return {
        "min": float(data[0].replace(',', '')),
        "avg": float(data[1].replace(',', '')),
        "max": float(data[2].replace(',', '')),
        "low-sug": float(data[3].replace(',', '')),
        "high-sug": float(data[4].replace(',', ''))
    }
