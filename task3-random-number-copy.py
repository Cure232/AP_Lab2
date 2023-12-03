import os
import csv
import random

import cv2
import pandas as pd

columns = ["Absolute path", "Relative path", "Class"]
data = []
img_names = set()

with open('annotation.csv', 'r', newline='') as csvfile:
    filereader = csv.reader(csvfile, delimiter=';', quotechar='|')
    filereader.__next__()
    copy_path = 'new_dataset_task3' # relative or absolute
    if not os.path.exists(copy_path):
        os.mkdir(copy_path)

    for row in filereader:
        print(row)
        img_class = row[3]

        img_name = str(random.randint(0, 10000))+'.jpg'
        while img_name in img_names:
            img_name = str(random.randint(0, 10000))+'.jpg'
        img_names.add(img_name)

        img = cv2.imread(row[2])
        data.append([os.path.abspath(fr'{copy_path}\{img_name}'), fr'{copy_path}\{img_name}', img_class])
        cv2.imwrite(fr'{copy_path}\{img_name}', img)


df = pd.DataFrame(data, columns=columns)
df.to_csv('new_annotation_task3.csv', sep=";")
