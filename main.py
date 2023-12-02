import os
import cv2
import csv
import numpy as np
import pandas as pd

columns = ["Absolute path", "Relative path", "Class"]
data = []
rel_path1 = r'dataset\bay horse'
rel_path2 = r'dataset\zebra'

name_list1 = os.listdir(rel_path1)
name_list2 = os.listdir(rel_path2)

for name in name_list1:
    data.append([os.path.abspath(rel_path1 + '\\' + name), f'{rel_path2}\\{name}', "Bay horse"])
for name in name_list2:
    data.append([os.path.abspath(rel_path2 + '\\' + name), f'{rel_path2}\\{name}', "Zebra"])


df = pd.DataFrame(data, columns=columns)
df.to_csv('annotation.csv', sep=";")
