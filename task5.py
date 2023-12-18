from task2 import scan_annotation

data = []

class HorseIterator:
    data_position = 0

    def __init__(self, limit):
        """Initializes HorseIterator that can iterate through data variable from this script.

        Args:
            limit (int): Max number of iterations.
        """
        self.limit = limit
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        """Returns path to next item, increments the counter.

        Raises:
            StopIteration: Standard iterator signal.

        Returns:
            str: Absolute path to next Horse image.
        """
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
        """Initializes HorseIterator that can iterate through data variable from this script.

        Args:
            limit (int): Max number of iterations.
        """
        self.limit = limit
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        """Returns path to next item, increments the counter.

        Raises:
            StopIteration: Standard iterator signal.

        Returns:
            str: Absolute path to next Zebra image.
        """
        if self.counter < self.limit:
            for i in range(self.data_position, len(data)):
                if data[i][2] == "zebra":
                    self.counter += 1
                    self.data_position = i + 1
                    return data[i][0]
        else:
            raise StopIteration


if __name__ == '__main__':
    data = scan_annotation('annotation.csv')
    s_iter1 = HorseIterator(3)
    s_iter2 = ZebraIterator(5)
    print(s_iter2.__next__())
    for val in s_iter1:
        print(val)

    for val in s_iter2:
        print(val)
