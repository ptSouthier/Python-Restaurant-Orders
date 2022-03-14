import csv


def analyze_log(path_to_file):
    with open(path_to_file) as file:
        path_reader = csv.reader(file)
        result_data = [result_row for result_row in path_reader]
        print(result_data)
