import numpy as np
import pandas as pd


def treat_missing(data, missing_column, fill_with_num = None, fill_with_cat = None):

    for column in missing_column:

        if data[column].is_numeric():
            value = fill_with_num
            data.column.fillna(value, axis = 1, inplace = True)
        elif data[column].is_categorical:
            value = fill_with_cat
            data.column.fillna(value, axis = 1, inplace = True)
        else:
            break


def 





        

    

