import numpy as np
import pandas as pd


def treat_missing(data, missing_column, fill_with_num, fill_with_cat):

    for column in missing_column:

        if data[column].is_numeric():
            value = fill_with
            data.column.fillna(value, axis = 1, inplace = True)
        elif data[column].is_categorical:
            value = fill_with



        

    

