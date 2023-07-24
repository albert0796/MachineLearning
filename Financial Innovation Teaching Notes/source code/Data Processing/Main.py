import os
import pandas as pd
from tqdm import tqdm
from random import sample 

from Process import Process
from Detect import Detect
from util.util_pattern import pattern


class Main(object):
    def __init__(self, filename_raw, filename_pro, filename_rule, pattern_path, timeScale):
        self.data_pro_df = None
        self.data_rule_df = None
        self.filename_raw = filename_raw
        self.filename_pro = filename_pro
        self.filename_rule = filename_rule
        self.pattern_path = pattern_path
        self.timeScale = timeScale
    

    def save(self, data, filename, file_format):
        # 儲存csv和pickle檔
        if file_format == 'csv':
            data.to_csv(filename, index = False)
        elif file_format == 'pickle':
            with open(filename, 'wb+') as f:
                pickle.dump(data, f)


    def load(self, filename, file_format):
        # 載入csv和pickle檔
        if file_format == 'csv':
            data = pd.read_csv(filename)
            return data
        elif file_format == 'pickle':
            with open(filename, 'rb') as f:
                data = pickle.load(f)
            return data


    def process(self):
        # 呼叫process.py檔，做資料前處理
        Pro = Process(self.filename_raw, self.timeScale)
        Pro.preprocessing()
        Pro.timeConvert()
        self.data_pro_df = Pro.addFeature()
        self.save(self.data_pro_df, self.filename_pro, 'csv')
    

    def detect(self):
        # 呼叫Detect.py檔，做rule-base偵測
        Det = Detect(self.filename_pro)
        Det.process()
        Det.trend()
        self.data_rule_df = Det.signal()
        Det.result()
        self.save(self.data_rule_df, self.filename_rule, 'csv')
    

    def graph(self, signal, num_pattern = 1):
        # 繪出符合交易訊號的pattern
        data_df = self.load(self.filename_rule, 'csv')
        idx_signal_ls = list(data_df.loc[data_df[signal] == 1].index)
        idx_signal_sample_ls = sample(idx_signal_ls, num_pattern)
        for idx in tqdm(idx_signal_sample_ls):
            idx_start, idx_end = (idx - 9), idx
            df = data_df.loc[idx_start:idx_end]
            path = self.pattern_path + '/' + str(signal)
            pattern(df, signal, self.timeScale, path)


if __name__ == "__main__":
    filename_raw = 'C:/peculab/lecture_ntu/data/eurusd_2010_2017.csv'
    filename_pro = 'C:/peculab/lecture_ntu/data/eurusd_2010_2017_1T.csv'
    filename_rule = 'C:/peculab/lecture_ntu/data/eurusd_2010_2017_1T_rulebase.csv'
    pattern_path = 'C:/peculab/lecture_ntu/pattern'
    timeScale = '1min'
    signal_ls = ['EveningStar', 'MorningStar', 'ShootingStar', 
                 'InvertHammer', 'BearishHarami', 'BearishEngulfing',
                 'BullishHarami', 'BullishEngulfing']

    M =  Main(filename_raw, filename_pro, filename_rule, pattern_path, timeScale)

    # 資料前處理
    M.process()

    # rule-base偵測
    M.detect()
    
    # 繪出在各個交易訊號中1個pattern
    signal_ls = ['EveningStar']
    for signal in signal_ls:
        path = 'C:/peculab/lecture_ntu/pattern/' + str(signal) 
        os.mkdir(path)
        M.graph(signal)
    


    




    
    
