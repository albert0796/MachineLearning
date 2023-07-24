import numpy as np
import pandas as pd
import pickle
import random
from sklearn.model_selection import train_test_split

from utils import util_gasf


def df_to_arr(df, target_ls, num_signal, num_other):
    num_total = (num_signal * (len(target_ls) - 1)) + num_other
    ohlc_arr = np.zeros((num_total, 10, 4))
    n = 0
    for i in target_ls:
        target_df = df.loc[df[i] == 1]
        if i == 'None':
            index_ls = random.sample(list(target_df.index), num_other)
        else:
            index_ls = random.sample(list(target_df.index), num_signal)
        for idx in index_ls:
            start, end = idx -9, idx
            target_arr = df.loc[start:end, ['open', 'high', 'low', 'close']].values
            ohlc_arr[n, :, :] = target_arr
            n += 1
    return ohlc_arr


def gasf(arr):
    gasf_arr = util_gasf.get_gasf(arr)
    return gasf_arr


def labeling(target_ls, num_signal, num_other):
    num_total = (num_signal * (len(target_ls) - 1)) + num_other
    label = np.zeros((num_total, 1))
    label_arr = np.zeros((num_total, len(target_ls)))
    n = 0
    for item in enumerate(target_ls):
        l = item[0]
        if item[1] == 'None':           
            label[n:num_other, :] = l
            label_arr[n:num_other, l] = 1
            n += num_other
        else:
            label[n:(n + num_signal), :] = l
            label_arr[n:(n + num_signal), l] = 1
            n += num_signal
    return label, label_arr        


def split(gasf_arr, ohlc_arr, label, label_arr):
    gasf_arr_train, gasf_arr_testnval, label_train, label_testnval = train_test_split(gasf_arr, label, test_size=0.33, random_state=42, shuffle = True)
    gasf_arr_val, gasf_arr_test, label_val, label_test = train_test_split(gasf_arr_testnval, label_testnval, test_size=0.33, random_state=42, shuffle = True)
    label_arr_train, label_arr_testnval, label_train, label_testnval = train_test_split(label_arr, label, test_size=0.33, random_state=42, shuffle = True)
    label_arr_val, label_arr_test, label_val, label_test = train_test_split(label_arr_testnval, label_testnval, test_size=0.33, random_state=42, shuffle = True)
    ohlc_arr_train, ohlc_arr_testnval, label_train, label_testnval = train_test_split(ohlc_arr, label, test_size=0.33, random_state=42, shuffle = True)
    ohlc_arr_val, ohlc_arr_test, label_val, label_test = train_test_split(ohlc_arr_testnval, label_testnval, test_size=0.33, random_state=42, shuffle = True)
    
    dict_data={}
    dict_data['train_gaf'] = gasf_arr_train
    dict_data['val_gaf'] = gasf_arr_val
    dict_data['test_gaf'] = gasf_arr_test
    dict_data['train_data'] = ohlc_arr_train
    dict_data['val_data'] = ohlc_arr_val
    dict_data['test_data'] = ohlc_arr_test
    dict_data['train_label_arr'] = label_arr_train
    dict_data['val_label_arr'] = label_arr_val
    dict_data['test_label_arr'] = label_arr_test
    dict_data['train_label'] = label_train
    dict_data['val_label'] = label_val
    dict_data['test_label'] = label_test
    return dict_data


if __name__ == "__main__":
    filename = r'.\data\eurusd_2010_2017_1T_rulebase.csv'
    target_ls = ['None', 'EveningStar', 'MorningStar', 'BearishEngulfing','BullishEngulfing', 
                 'ShootingStar', 'InvertHammer', 'BearishHarami', 'BullishHarami']
    # total numbers of classes: 8 (7 + 1)  
    # numbers in each signals: 2000 / numbers in the other class: 4000
    num_signal = 988
    num_other = 988 * 2
    
    df = pd.read_csv(filename)
    ohlc_arr = df_to_arr(df, target_dict, num_signal, num_other)
    gasf_arr = gasf(ohlc_arr)
    label, label_arr = labeling(target_dict, num_signal, num_other)
    data_dict = split(gasf_arr, ohlc_arr, label, label_arr)

    with open(r'.\data\label8_eurusd_10bar_1500_500_val200_gaf_culr.pkl', 'wb') as f:
        pickle.dump(data_dict, f)






















