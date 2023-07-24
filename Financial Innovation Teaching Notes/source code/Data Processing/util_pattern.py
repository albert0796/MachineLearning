import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import mpl_finance as mpf


def pattern(df, signal, timeScale, path = None):         
    # 設定xy軸座標值、圖片標題大小       
    fontsize = 15
    plt.rcParams['xtick.labelsize'] = fontsize  
    plt.rcParams['ytick.labelsize'] = fontsize 
    plt.rcParams['axes.titlesize'] = fontsize           

    # 設定圖片的大小
    fig = plt.figure(figsize=(18, 12))
    ax = plt.subplot2grid((1, 1), (0, 0))          

    # 設定圖片背景為網格
    plt.grid()

    # 將x座標軸數值設為日期
    ax.set_xticks(range(10))
    ax.set_xticklabels(df['date'])      

    # 將x坐標軸數值旋轉45度
    locs, labels = plt.xticks() 
    plt.setp(labels , rotation = 45)

    # 繪出前幾根K棒的趨勢線
    global end_idx
    if signal == ('EveningStar' or 'MorningStar'):
        end_idx = 7
    elif signal == ('ShootingStar' or 'InvertHammer'):
        end_idx = 9
    elif signal == ('BearishHarami' or 'BearishEngulfing' or 'BullishHarami' or 'BullishEngulfing'):
        end_idx = 8 
    y = df['close'].iloc[0:end_idx].values.reshape(-1, 1)
    x = np.array(range(1, end_idx + 1)).reshape(-1, 1)
    model = LinearRegression()
    model.fit(x, y)
    y_pred = model.predict(x)        
    ax.plot(y_pred, label='Trend')          

    # 繪出k棒 
    arr = np.c_[range(df.shape[0]), df[['open', 'high', 'low', 'close']].values]
    mpf.candlestick_ohlc(ax, arr, width=0.4, alpha=1, colordown='#53c156', colorup='#ff1717')    

    # 設定圖例位置與大小
    ax.legend(loc = 'best', prop = {'size': fontsize})

    # 設定圖片標題名字
    title_name = signal + '_' + timeScale
    ax.set_title(title_name)

    # 上調整個圖片的位置
    fig.subplots_adjust(bottom = 0.35)

    # # 儲存圖片
    # name = path + '/' + signal + '_' + timeScale + '.png'
    # plt.savefig(name)     
    
    # 印出圖片
    plt.show()

    # 不要印出圖片
    # plt.close('all')  





