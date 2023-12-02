import os
import cv2
import csv
import numpy as np
import pandas as pd

columns = ["Absolute path", "Relative path", "Class"]
data = [
["askdsalda", "fdgdg", "Item1"],
["askdsalda123123", "fdgdg21312", "Item2"],
["3", "sae3123", "Item3"]
]

df = pd.DataFrame(data, columns=columns)
df.to_csv('annotation.csv')
