import copy
import csv
import os

class CSVHelper():

    @staticmethod
    def dict_to_csv(file, lst_dict, key, add_date=False, date=None):

        dict_columns = [*lst_dict[0][key]]
        columns = ['date'] + dict_columns if add_date else dict_columns 
        print(columns) 
        try:
            with open(file, 'w', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=columns)
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
    def does_file_exists(path):
        pass
