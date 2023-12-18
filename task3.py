import os
import random

import cv2
import pandas as pd

from task2 import scan_annotation
from main import save_as_csv


def randomized_dataset_copy(dataset: list[list[str]], copy_path: str) -> list[list[str]]:
    """Copies given dataset into given folder while giving images unique random names.

    Args:
        dataset (list[list[str]]): Data as a table (matrix) of strings without columns.
        copy_path (str): Folder where you copy the dataset.

    Returns:
        list[list[str]]: New dataset with new content.
    """
    # relative or absolute
    if not os.path.exists(copy_path):
        os.mkdir(copy_path)

    img_names = set()
    result = []

    for row in dataset:
        img_class = row[-1]
        img_name = str(random.randint(0, 10000)) + '.jpg'
        while img_name in img_names:
            img_name = str(random.randint(0, 10000)) + '.jpg'
        img_names.add(img_name)

        img = cv2.imread(row[1])
        cv2.imwrite(fr'{copy_path}\{img_name}', img)
        print(row)
        print("Saved successfully")
        result.append([os.path.abspath(fr'{copy_path}\{img_name}'), fr'{copy_path}\{img_name}', img_class])
    return result


if __name__ == "__main__":
    data = scan_annotation('annotation.csv')
    columns = data.pop(0)
    
    new_data = randomized_dataset_copy(data, 'new_dataset_task3')
    save_as_csv(new_data, columns, 'new_annotation_task3.csv')
