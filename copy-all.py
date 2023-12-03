import os
import csv
import cv2
import pandas as pd


with open('annotation.csv', 'r', newline='') as csvfile:
    filereader = csv.reader(csvfile, delimiter=';', quotechar='|')
    filereader.__next__()
    for row in filereader:
        print(row)
        img_class = row[3]
        img_name = (row[2].split('\\'))[-1]
        img = cv2.imread(row[2])
        copy_path = 'new_dataset' #relative or absolute
        if not os.path.exists(copy_path):
            os.mkdir(copy_path)
        cv2.imwrite(fr'{copy_path}\{img_class}_{img_name}', img)
