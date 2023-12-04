import csv

data = []
counters = dict()
counters['BAY HORSE'] = 0
counters['ZEBRA'] = 0


def get_next_item_path(item_class):
    item_class = item_class.upper()
    counter = 0
    for item in data:
        if item[3].upper() == item_class:
            if counter == counters[item_class]:
                counters[item_class] += 1
                return item[1]
            else:
                counter += 1


with open('annotation.csv', 'r', newline='') as csvfile:
    filereader = csv.reader(csvfile, delimiter=';', quotechar='|')
    filereader.__next__()
    for row in filereader:
        data.append(row)

print(get_next_item_path("ZEBRA"))
print(get_next_item_path("ZEBRA"))
print(get_next_item_path("Bay horse"))
