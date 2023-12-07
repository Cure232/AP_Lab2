import csv


class HorseIterator:
    data_position = 0

    def __init__(self, limit):
        self.limit = limit
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.limit:
            for i in range(self.data_position, len(data)):
                if data[i][2] == "bay horse":
                    self.counter += 1
                    self.data_position = i + 1
                    return data[i][0]
        else:
            raise StopIteration


class ZebraIterator:
    data_position = 0

    def __init__(self, limit):
        self.limit = limit
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.limit:
            for i in range(self.data_position, len(data)):
                if data[i][2] == "zebra":
                    self.counter += 1
                    self.data_position = i + 1
                    return data[i][0]
        else:
            raise StopIteration


def scan_annotation(annotation_path: str) -> list[list[str]]:
    with open(annotation_path, 'r', newline='') as csvfile:
        filereader = csv.reader(csvfile, delimiter=';', quotechar='|')
        result = []
        for row in filereader:
            row.pop(0)
            result.append(row)
        return result 


if __name__ == '__main__':
    data = scan_annotation('annotation.csv')
    s_iter1 = HorseIterator(3)
    s_iter2 = ZebraIterator(5)
    s_iter2.__next__
    for val in s_iter1:
        print(val)

    for val in s_iter2:
        print(val)
