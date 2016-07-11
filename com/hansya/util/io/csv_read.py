import csv


class CSVReader(object):
    def __init__(self):
        pass

    @staticmethod
    def read(file_path):
        csv_file = csv.reader(open(file_path, "r+"))
        for row in csv_file:
            yield row
