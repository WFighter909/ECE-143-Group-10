import numpy as np
import pandas as pd
from global_variables import *


def clean_data(fname):
    missing_values = ["n/a", "na", "--", None,'None']
    origin_data = pd.read_csv(fname, na_values=missing_values)
    cleaned_data = origin_data[new_key_list]
    #print(cleaned_data.iloc[0])
    cleaned_data.fillna(method="ffill", inplace=True)
    cleaned_data.to_csv('{}_cleaned.csv'.format(fname[:-4]),index=False)


if __name__ == '__main__':
    # clean_data('data/KSEA.csv')
    for city in list(city_code_refer.values()):
        clean_data('data/{}.csv'.format(city))
