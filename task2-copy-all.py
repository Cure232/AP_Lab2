import os
import csv

import cv2
import pandas as pd


def save_as_csv(to_save: list[list[str]], columns: list[str], relpath: str) -> None:
    df = pd.DataFrame(to_save, columns=columns)
    df.to_csv(relpath, sep=";")
    print(f'Successfully saved in {relpath}')


def scan_annotation(annotation_path: str) -> list[list[str]]:
    with open(annotation_path, 'r', newline='') as csvfile:
        filereader = csv.reader(csvfile, delimiter=';', quotechar='|')
        result = []
        for row in filereader:
            row.pop(0)
            result.append(row)
        return result


def copy_dataset(dataset: list[list[str]], copy_path: str) -> None:
    # relative or absolute
    if not os.path.exists(copy_path):
        os.mkdir(copy_path)

    for row in dataset:
        img_class = row[-1]
        img_name = (row[1].split('\\'))[-1]
        new_img_name = f'{img_class}_{img_name}'
        img = cv2.imread(row[1])
        cv2.imwrite(fr'{copy_path}\{new_img_name}', img)
        print(row)
        print("Saved successfully")


if __name__ == "__main__":
    data = scan_annotation('annotation.csv')
    columns = data.pop(0)

    copy_dataset(data, 'new_dataset_task2')
    save_as_csv(data, columns, 'new_annotation_task2.csv')
