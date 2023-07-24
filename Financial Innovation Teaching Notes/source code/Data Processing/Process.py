import pandas as pd
import numpy as np
from scipy import stats
from sklearn.linear_model import LinearRegression


class Process(object):
    def __init__(self, filename, timeScale):
        self.data = pd.read_csv(filename)
        self.timeScale = timeScale


    def preprocessing(self):
        # 將欄位名稱全部轉成小寫
        for i in self.data.columns.values:
            self.data.rename(columns={i : i.lower()}, inplace=True)       
        # 將日期從名目轉成時間尺度，並將其設為索引
        self.data['timestamp'] = pd.to_datetime(self.data['date'], format="%d.%m.%Y %H:%M:%S.%f")
        self.data.set_index('timestamp', inplace=True)

    
    def timeConvert(self):
        # 將資料的時間尺度轉成分鐘資料
        df = pd.DataFrame(self.data['date'])
        df['low'] = self.data['low'].resample(self.timeScale, label='right', closed='right').min()
        df['high'] = self.data['high'].resample(self.timeScale, label='right', closed='right').max()
        df['close'] = self.data['close'].resample(self.timeScale, label='right', closed='right').last()
        df['open'] = self.data['open'].resample(self.timeScale, label='right', closed='right').first()
        self.data = df[1:-1]
        self.data.dropna(inplace=True)
    

    def percentile(self, series):
        t = series.iloc[-1]
        p = stats.percentileofscore(series, t, kind='strict')    
        return p


    def addFeature(self):
        # realbody: k棒長度，close - open
        # direction: k棒漲跌，realbody 的正負號
        # ushadow_width: 上引線長度，恆為正。如果k棒下跌，為high - open；如果k棒上跌，為high - close
        # lshadow_width: 下引線長度，恆為正。如果k棒下跌，為close - low；如果k棒上跌，為open - low
        # ushadow_per: 上引線長度在前50根k棒中的PR值
        # lshadow_per: 下引線長度在前50根k棒中的PR值
        # realbody_per: K棒長度在前50根k棒中的PR值
        self.data['realbody'] = self.data['close'] - self.data['open']
        self.data['direction'] = np.sign(self.data['realbody'])
        self.data['ushadow_width'], self.data['lshadow_width'] = 0, 0
        self.data.loc[self.data['realbody'] <= 0, 'ushadow_width'] = self.data.loc[self.data['realbody'] <= 0, 'high'] - self.data.loc[self.data['realbody'] <= 0, 'open']
        self.data.loc[self.data['realbody'] > 0, 'ushadow_width'] = self.data.loc[self.data['realbody'] > 0, 'high'] - self.data.loc[self.data['realbody'] > 0, 'close']
        self.data.loc[self.data['realbody'] <= 0, 'lshadow_width'] = self.data.loc[self.data['realbody'] <= 0, 'close'] - self.data.loc[self.data['realbody'] <= 0, 'low']
        self.data.loc[self.data['realbody'] > 0, 'lshadow_width'] = self.data.loc[self.data['realbody'] > 0, 'open'] - self.data.loc[self.data['realbody'] > 0, 'low']
        self.data['ushadow_per'] = self.data['ushadow_width'].rolling(50).apply(self.percentile, raw=False)
        self.data['lshadow_per'] = self.data['lshadow_width'].rolling(50).apply(self.percentile, raw=False)
        self.data['realbody_per'] = abs(self.data['realbody']).rolling(50).apply(self.percentile, raw=False)        
        self.data.dropna(inplace = True)
        return self.data


if __name__ == "__main__":
    filename = 'C:/peculab/lecture_ntu/data/eurusd_2010_2017.csv'
    timeScale = '1T'

    Pro = Process(filename, timeScale)

    # 欄位大小寫、將日期名目尺度轉成時間尺度
    Pro.preprocessing()

    # 將資料的時間尺度轉成分鐘資料
    Pro.timeConvert()

    # 增加特徵欄位
    df = Pro.addFeature()

    # 儲存做完前處理的csv檔
    filename_save = 'C:/peculab/lecture_ntu/data/eurusd_2010_2017_1T.csv'
    df.to_csv(filename_save, index = False)