import csv
import os
from tkinter.ttk import Separator


def save_data(key, value):

    dict_var = {}
    file_path = os.path.join(os.getcwd(), "doc/fig/generalStatistic.dat")

    try:
        with open(file_path, newline="") as file:
            reader = csv.reader(file, delimiter=';')
            for row in reader:
                dict_var[row[0]] = row[1]
    except FileNotFoundError:
        pass

    value = edit_str(value)
    dict_var[key] = value

    with open(file_path, "w") as f:
        for key in dict_var.keys():
            f.write(f"{key};{dict_var[key]}\n")


def edit_str(value) -> str:
    if type(value) == str:
        if len(value) > 25:
            return f'{value[:22]}...'
    return value