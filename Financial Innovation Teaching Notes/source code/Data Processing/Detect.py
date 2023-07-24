import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from tqdm import tqdm


class Detect(object):
    def __init__(self, filename):
        self.data = pd.read_csv(filename)
        self.timeScale = None
    

    def trending(self, series):
        # 以線性回歸的斜率決定趨勢，斜率為正，趨勢為正向，輸出1；反之為趨勢為負向，輸出-1。
        # 斜率為0，輸出0
        y = series.values.reshape(-1,1)
        x = np.array(range(1, series.shape[0] + 1)).reshape(-1,1)
        model = LinearRegression()
        model.fit(x, y)
        slope = model.coef_
        if slope > 0:
            return 1
        elif slope == 0:
            return 0
        else:
            return -1
    

    def eveningStar(self, df):
        # 1. 前7根趨勢為正
        # 2. 第8根上漲
        # 3. 第10根下跌
        # 4. 第8根長度在前50根中PR值大於等於65
        # 5. 第9根長度在前50根中PR值小於等於35
        # 6. 第10根收盤價小於第8根body中央
        # 7. 第8根收盤價小於第9根body中央
        # 8. 第10根開盤價小於第9根body中央
        cond1 = (df['trend7'].iloc[-4] > 0)
        cond2 = (df['direction'].iloc[-3] > 0)
        cond3 = (df['direction'].iloc[-1] < 0)
        cond4 = (df['realbody_per'].iloc[-3] >= 65)
        cond5 = (df['realbody_per'].iloc[-2] <= 35)
        cond6 = (df['close'].iloc[-1] <= (df['open'].iloc[-3] + df['realbody'].iloc[-3] * (1/2)))
        cond7 = (df['close'].iloc[-3] <= (df['open'].iloc[-2] + df['realbody'].iloc[-2] * (1/2)))
        cond8 = (df['open'].iloc[-1] <= (df['open'].iloc[-2] + df['realbody'].iloc[-2] * (1/2)))
        if cond1 and cond2 and cond3 and cond4 and cond5 and cond6 and cond7 and cond8:
            return True
        else:
            return False
    

    def morningStar(self, df):
        # 1. 前7根趨勢為負
        # 2. 第8根下跌
        # 3. 第10根上漲
        # 4. 第8根長度在前50根中PR值大於等於65
        # 5. 第9根長度在前50根中PR值小於等於35
        # 6. 第10根收盤價大於第8根body中央
        # 7. 第8根收盤價大於第9根body中央
        # 8. 第10根開盤價大於第9根body中央
        cond1 = (df['trend7'].iloc[-4] < 0)
        cond2 = (df['direction'].iloc[-3] < 0)
        cond3 = (df['direction'].iloc[-1] > 0)
        cond4 = (df['realbody_per'].iloc[-3] >= 65)
        cond5 = (df['realbody_per'].iloc[-2] <= 35)
        cond6 = (df['close'].iloc[-1] >= (df['open'].iloc[-3] + df['realbody'].iloc[-3] * (1/2)))
        cond7 = (df['close'].iloc[-3] >= (df['open'].iloc[-2] + df['realbody'].iloc[-2] * (1/2)))
        cond8 = (df['open'].iloc[-1] >= (df['open'].iloc[-2] + df['realbody'].iloc[-2] * (1/2)))
        if cond1 and cond2 and cond3 and cond4 and cond5 and cond6 and cond7 and cond8:
            return True
        else:
            return False


    def shootingStar(self, df):
        # 1. 前9根趨勢為正
        # 2. 第9根上漲
        # 3. 第9根長度在前50根中PR值大於等於65
        # 4. 第10根上影線長度大於其body長度的兩倍
        # 5. 第10根開盤或收盤價(較小者)大於等於第9根中央
        # 6. 第10根下影線長度在前50根中PR值小於25
        # 7. 第10根上影線長度在前50根中PR值大於65
        cond1 = (df['trend9'].iloc[-2] > 0)
        cond2 = (df['direction'].iloc[-2] > 0)
        cond3 = (df['realbody_per'].iloc[-2] >= 65)
        cond4 = (df['ushadow_width'].iloc[-1] >= 2 * abs(df['realbody'].iloc[-1]))
        cond5 = (min(df['open'].iloc[-1], df['close'].iloc[-1]) >= (df['open'].iloc[-2] + df['realbody'].iloc[-2] * (1/2)))
        cond6 = (df['lshadow_per'].iloc[-1] <= 25)
        cond7 = (df['ushadow_per'].iloc[-1] >= 65)
        if cond1 and cond2 and cond3 and cond4 and cond5 and cond6 and cond7:
            return True
        else:
            return False
    

    def invertHammer(self, df):
        # 1. 前9根趨勢為負
        # 2. 第9根下跌
        # 3. 第9根長度在前50根中PR值大於等於65
        # 4. 第10根上影線長度大於其body長度的兩倍
        # 5. 第10根開盤或收盤價(較大者)小於等於第9根中央
        # 6. 第10根下影線長度在前50根中PR值小於25
        # 7. 第10根上影線長度在前50根中PR值大於65
        cond1 = (df['trend9'].iloc[-2] < 0)
        cond2 = (df['direction'].iloc[-2] < 0)
        cond3 = (df['realbody_per'].iloc[-2] >= 65)
        cond4 = (df['ushadow_width'].iloc[-1] >= 2 * abs(df['realbody'].iloc[-1]))
        cond5 = (max(df['open'].iloc[-1], df['close'].iloc[-1]) <= (df['open'].iloc[-2] + df['realbody'].iloc[-2] * (1/2)))
        cond6 = (df['lshadow_per'].iloc[-1] <= 25)
        cond7 = (df['ushadow_per'].iloc[-1] >= 65)
        if cond1 and cond2 and cond3 and cond4 and cond5 and cond6 and cond7:
            return True
        else:
            return False


    def bearishHarami(self, df):
        # 1. 前8根趨勢為正
        # 2. 第9根為上漲
        # 3. 第10根下跌
        # 4. 第9根長度在前50根中PR值大於等於65
        # 5. 第10根開盤價小於第9根收盤價
        # 6. 第10根收盤價大於第9根開盤價
        # 7. 第10根長度在前50根中PR值大於等於65
        # 8. 第10根收盤價小於等於第9根中央
        cond1 = (df['trend8'].iloc[-3] > 0)
        cond2 = (df['direction'].iloc[-2] > 0)
        cond3 = (df['direction'].iloc[-1] < 0)
        cond4 = (df['realbody_per'].iloc[-2] >= 65)
        cond5 = (df['open'].iloc[-1] < df['close'].iloc[-2])
        cond6 = (df['close'].iloc[-1] > df['open'].iloc[-2])
        cond7 = (df['realbody_per'].iloc[-1] >= 65)
        cond8 = (df['close'].iloc[-1] <= (df['open'].iloc[-2] + df['realbody'].iloc[-2] * (1/2)))
        if cond1 and cond2 and cond3 and cond4 and cond5 and cond6 and cond7 and cond8:
            return True
        else:
            return False


    def bearishEngulfing(self, df):
        # 1. 前8根趨勢為正
        # 2. 第9根為上漲
        # 3. 第10根下跌
        # 4. 第9根長度在前50根中PR值大於等於65
        # 5. 第10根開盤價大於第9根收盤價
        # 6. 第10根收盤價小於第9根開盤價
        cond1 = (df['trend8'].iloc[-3] > 0)
        cond2 = (df['direction'].iloc[-2] > 0)
        cond3 = (df['direction'].iloc[-1] < 0)
        cond4 = (df['realbody_per'].iloc[-2] >= 65)
        cond5 = (df['open'].iloc[-1] > df['close'].iloc[-2])
        cond6 = (df['close'].iloc[-1] < df['open'].iloc[-2])
        if cond1 and cond2 and cond3 and cond4 and cond5 and cond6:
            return True
        else:
            return False
    

    def bullishHarami(self, df):
        # 1. 前8根趨勢為負
        # 2. 第9根為下跌
        # 3. 第10根上漲
        # 4. 第9根長度在前50根中PR值大於等於65
        # 5. 第10根開盤價大於第9根收盤價
        # 6. 第10根收盤價小於第9根開盤價
        # 7. 第10根長度在前50根中PR值大於等於65
        # 8. 第10根收盤價大於等於第9根中央
        cond1 = (df['trend8'].iloc[-3] < 0)
        cond2 = (df['direction'].iloc[-2] < 0)
        cond3 = (df['direction'].iloc[-1] > 0)
        cond4 = (df['realbody_per'].iloc[-2] >= 65)
        cond5 = (df['open'].iloc[-1] > df['close'].iloc[-2])
        cond6 = (df['close'].iloc[-1] < df['open'].iloc[-2])
        cond7 = (df['realbody_per'].iloc[-1] >= 65)
        cond8 = (df['close'].iloc[-1] >= (df['open'].iloc[-2] + df['realbody'].iloc[-2] * (1/2)))
        if cond1 and cond2 and cond3 and cond4 and cond5 and cond6 and cond7 and cond8:
            return True
        else:
            return False


    def bullishEngulfing(self, df):
        # 1. 前8根趨勢為負
        # 2. 第9根為下跌
        # 3. 第10根上漲
        # 4. 第9根長度在前50根中PR值大於等於65
        # 5. 第10根開盤價小於第9根收盤價
        # 6. 第10根收盤價大於第9根開盤價
        cond1 = (df['trend8'].iloc[-3] < 0)
        cond2 = (df['direction'].iloc[-2] < 0)
        cond3 = (df['direction'].iloc[-1] > 0)
        cond4 = (df['realbody_per'].iloc[-2] >= 65)
        cond5 = (df['open'].iloc[-1] < df['close'].iloc[-2])
        cond6 = (df['close'].iloc[-1] > df['open'].iloc[-2])
        if cond1 and cond2 and cond3 and cond4 and cond5 and cond6:
            return True
        else:
            return False    


    def process(self):
        # 將日期從名目轉成時間尺度
        self.data['date'] = pd.to_datetime(self.data['date'], format="%d.%m.%Y %H:%M:%S.%f")
        # 檢查時間尺度為何
        if 60 <= (self.data['date'].iloc[1] - self.data['date'].iloc[0]).seconds < 1800 :
            self.timeScale = '1m'
        elif 1800 <= (self.data['date'].iloc[1] - self.data['date'].iloc[0]).seconds < 3600:
            self.timeScale = '30m'
        elif 3600 <= (self.data['date'].iloc[1] - self.data['date'].iloc[0]).seconds < 86400:
            self.timeScale = '1H'
        elif 1 <= (self.data['date'].iloc[1] - self.data['date'].iloc[0]).days < 7:
            self.timeScale = '1D'
        elif (self.data['date'].iloc[1] - self.data['date'].iloc[0]).days >= 7:
            self.timeScale = '1W'
        # 新增欲偵測的交易訊號
        self.data['EveningStar'] = 0
        self.data['MorningStar'] = 0
        self.data['ShootingStar'] = 0
        self.data['InvertHammer'] = 0
        self.data['BearishHarami'] = 0
        self.data['BearishEngulfing'] = 0
        self.data['BullishHarami'] = 0
        self.data['BullishEngulfing'] = 0
        self.data['None'] = 0
    

    def trend(self):
        # 以線性回歸的斜率分別計算前7, 8, 9根k棒的趨勢，斜率大於0則趨勢為正，位於趨勢線最尾端的資料的欄位值為1；反之則為-1
        self.data['trend7'] = self.data['close'].rolling(7).apply(self.trending, raw=False)
        self.data['trend8'] = self.data['close'].rolling(8).apply(self.trending, raw=False)
        self.data['trend9'] = self.data['close'].rolling(9).apply(self.trending, raw=False)


    def signal(self):
        # 以10根k棒為單位進行偵測，如符合特定交易訊號，則第10根k棒在該交易訊號的欄位的值為1，反之為0
        # 如均不符合任何交易訊號，則第10根k棒在None的欄位值為1
        for idx in tqdm(self.data.index):
            start_idx, end_idx = (idx - 9), idx
            if start_idx >= 0:
                df = self.data.loc[start_idx:end_idx]
                if self.eveningStar(df):
                    self.data.loc[end_idx, 'EveningStar'] = 1
                elif self.morningStar(df):
                    self.data.loc[end_idx, 'MorningStar'] = 1
                elif self.shootingStar(df):
                    self.data.loc[end_idx, 'ShootingStar'] = 1
                elif self.invertHammer(df):
                    self.data.loc[end_idx, 'InvertHammer'] = 1
                elif self.bearishHarami(df):
                    self.data.loc[end_idx, 'BearishHarami'] = 1
                elif self.bearishEngulfing(df):
                    self.data.loc[end_idx, 'BearishEngulfing'] = 1
                elif self.bullishHarami(df):
                    self.data.loc[end_idx, 'BullishHarami'] = 1
                elif self.bullishEngulfing(df):
                    self.data.loc[end_idx, 'BullishEngulfing'] = 1
                else:
                    self.data.loc[end_idx, 'None'] = 1
        return self.data
    

    def result(self):
        # 印出每個交易訊號下偵測到幾個pattern
        print('Time Scale: %s' % (self.timeScale))
        print('Period: %s - %s' % (self.data['date'].iloc[9], self.data['date'].iloc[-1]))
        print('The Number of Patterns in Each Signal:')
        print('None: {}'.format(self.data.loc[self.data['None'] == 1, 'None'].shape[0]))
        print('EveningStar: {}'.format(self.data.loc[self.data['EveningStar'] == 1, 'EveningStar'].shape[0]))                   
        print('MorningStar: {}'.format(self.data.loc[self.data['MorningStar'] == 1, 'MorningStar'].shape[0]))
        print('ShootingStar: {}'.format(self.data.loc[self.data['ShootingStar'] == 1, 'ShootingStar'].shape[0]))
        print('InvertHammer: {}'.format(self.data.loc[self.data['InvertHammer'] == 1, 'InvertHammer'].shape[0]))
        print('BearishHarami: {}'.format(self.data.loc[self.data['BearishHarami'] == 1, 'BearishHarami'].shape[0]))
        print('BearishEngulfing: {}'.format(self.data.loc[self.data['BearishEngulfing'] == 1, 'BearishEngulfing'].shape[0]))        
        print('BullishHarami: {}'.format(self.data.loc[self.data['BullishHarami'] == 1, 'BullishHarami'].shape[0]))
        print('BullishEngulfing: {}'.format(self.data.loc[self.data['BullishEngulfing'] == 1, 'BullishEngulfing'].shape[0]))


if __name__ == "__main__":
    # 先前處理過的csv檔
    filename =  r'C:\peculab\lecture_ntu\data\eurusd_2010_2017_1T.csv'

    Det = Detect(filename)  

    # 前處理
    Det.process()

    # 計算一個pattern中前7, 8, 9根k棒的趨勢
    Det.trend()

    # 訂定各個交易訊號的規則，並偵測是否有符合的pattern
    df = Det.signal()

    # 印出在每個交易訊號下偵測的結果
    Det.result()

    #　儲存經偵測過的csv檔
    filename_save = r'C:\peculab\lecture_ntu\data\eurusd_2010_2017_1T_rulebase.csv'
    df.to_csv(filename_save, index = False)