import copy
import csv
import os


class CSVHelper():

  @staticmethod
  def dict_to_csv(file, lst_dict, key, add_date=False, date=None, append=True):
    dict_columns = [*lst_dict[0][key]]
    columns = ['date'] + dict_columns if add_date else dict_columns
    open_to = 'a' if append else 'w'
    try:
      with open(file, open_to, newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=columns)
        if not append:
          writer.writeheader()
        for data in lst_dict:
          if add_date:
            date_dict = {'date': date}
            date_dict.update(data[key])
          row = date_dict if add_date else data[key]
          writer.writerow(row)
    except IOError:
      print("I/O error")

  @staticmethod
  def does_file_exist():
    # check if file already exists
    pass

  @staticmethod
  def does_data_data_exist():
    # check is the date is already recorded
    pass
