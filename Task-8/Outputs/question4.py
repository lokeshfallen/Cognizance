import pandas as pd
import numpy as np



def Capitalize():

    ser = pd.Series(["amrita", "school", "of", "engineering", "chennai"])
    series = ser.str.capitalize()
    for i in range(0,5):
        print(series[i], end = " ")

Capitalize()

