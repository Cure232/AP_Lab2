import os
import csv
import random

import cv2
import pandas as pd


def scan_annotation(annotation_path: str) -> list[list[str]]:
    with open(annotation_path, 'r', newline='') as csvfile:
        filereader = csv.reader(csvfile, delimiter=';', quotechar='|')
        result = []
        for row in filereader:
            row.pop(0)
            result.append(row)
        return result


def save_as_csv(to_save: list[list[str]], columns: list[str], relpath: str) -> None:
    df = pd.DataFrame(to_save, columns=columns)
    df.to_csv(relpath, sep=";")
    print(f'Successfully saved in {relpath}')


def randomized_dataset_copy(dataset: list[list[str]], copy_path: str) -> None:
    # relative or absolute
    if not os.path.exists(copy_path):
        os.mkdir(copy_path)

    img_names = set()
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


if __name__ == "__main__":
    data = scan_annotation('annotation.csv')
    columns = data.pop(0)
    
    randomized_dataset_copy(data, 'new_dataset_task3')
    save_as_csv(data, columns, 'new_annotation_task3.csv')
