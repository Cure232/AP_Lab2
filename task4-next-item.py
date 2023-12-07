import csv


counters = dict()
counters['BAY HORSE'] = 0
counters['ZEBRA'] = 0


def get_next_item_path(item_class: str) -> str:
    item_class = item_class.upper()
    counter = 0
    for item in data:
        if item[3].upper() == item_class:
            if counter == counters[item_class]:
                counters[item_class] += 1
                return item[1]
            else:
                counter += 1


def scan_annotation(annotation_path: str) -> list[list[str]]:
    with open(annotation_path, 'r', newline='') as csvfile:
        filereader = csv.reader(csvfile, delimiter=';', quotechar='|')
        result = []
        for row in filereader:
            row.pop(0)
            result.append(row)
        return result 



if __name__ == "__main__":
    data = scan_annotation('annotation.csv')
    print(get_next_item_path("ZEBRA"))
    print(get_next_item_path("ZEBRA"))
    print(get_next_item_path("Bay horse"))
    print(get_next_item_path("ZEBRA"))
    print(get_next_item_path("Bay horse"))
    print(get_next_item_path("Bay horse"))
