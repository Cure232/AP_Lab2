import csv


data = []


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
                if data[i][3] == "Bay horse":
                    self.counter += 1
                    self.data_position = i + 1
                    return data[i][1]
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
                if data[i][3] == "Zebra":
                    self.counter += 1
                    self.data_position = i + 1
                    return data[i][1]
        else:
            raise StopIteration


with open('new_annotation_task2.csv', 'r', newline='') as csvfile:
    filereader = csv.reader(csvfile, delimiter=';', quotechar='|')
    filereader.__next__()
    for row in filereader:
        data.append(row)

s_iter1 = HorseIterator(3)
s_iter2 = ZebraIterator(5)

for val in s_iter1:
    print(val)

for val in s_iter2:
    print(val)
