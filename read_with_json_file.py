import json


def read_data(path):
    with open(path) as f:
        data = json.load(f)
    return data
