import os
import csv
import cv2
import pandas as pd

columns = ["Absolute path", "Relative path", "Class"]
data = []

with open('annotation.csv', 'r', newline='') as csvfile:
    filereader = csv.reader(csvfile, delimiter=';', quotechar='|')
    filereader.__next__()
    copy_path = 'new_dataset_task2' # relative or absolute
    if not os.path.exists(copy_path):
        os.mkdir(copy_path)

    for row in filereader:
        print(row)
        img_class = row[3]
        img_name = (row[2].split('\\'))[-1]
        img = cv2.imread(row[2])
        cv2.imwrite(fr'{copy_path}\{img_class}_{img_name}', img)
        data.append([os.path.abspath(fr'{copy_path}\{img_name}'), fr'{copy_path}\{img_name}', img_class])

df = pd.DataFrame(data, columns=columns)
df.to_csv('new_annotation_task2.csv', sep=";")
