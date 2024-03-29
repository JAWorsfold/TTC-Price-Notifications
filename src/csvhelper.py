import copy
import csv
import os
import pandas as pd
from pathlib import Path


class CSVHelper():

  @staticmethod
  def dict_to_csv(file, lst_dict, sort_order=None, 
                  sort_direction=None, date_columns=False):
    df = pd.DataFrame.from_dict(lst_dict)
    df = df.replace(r'^\s*$', 0, regex=True)
    if not os.path.exists(file):
      dr = '/'.join(file.split('/')[:-1])
      Path(dr).mkdir(parents=True, exist_ok=True)
    else:
      df = CSVHelper.remove_duplicates(file, df, date_columns=date_columns)
      if df is None: return
    if sort_order:
      df.sort_values(by=sort_order, ascending=sort_direction, inplace=True)
    df.to_csv(file, index=False, mode='w', header=True)

  @staticmethod
  def add_date_column(date, lst_dict):
    new_list = []
    for d in lst_dict:
        date_dict = {'date': date}
        date_dict.update(d)
        new_list.append(date_dict)
    return new_list

  @staticmethod
  def remove_duplicates(file, df, date_columns=False):
    df_read = pd.read_csv(file, parse_dates=date_columns)
    return pd.concat([df_read, df]).drop_duplicates(ignore_index=True)
