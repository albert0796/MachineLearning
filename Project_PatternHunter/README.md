# Pattern Hunter
### 作者: 吳政翰
### 指導者: 蔡芸琤 助理教授、陳俊豪 博士生
#  
### [詳見完整報告](https://github.com/albert0796/MachineLearning/blob/master/Project_PatternHunter/Report/%E5%A0%B1%E5%91%8A%E8%AA%AA%E6%98%8E%E6%9B%B8.pdf)
### 研究說明  
期望開發出一套交易訊號偵測與推薦系統給予投資人使用，該系統串流了某個時間尺度的標的資產，可為分鐘、小時、日或周資料，並使用深度學習影像辨識的方式，按該時間尺度的頻率偵測標的資產在形態學上交易訊號，如在某區段偵測出符合形態學上交易訊號，系統則會將該訊號提供給投資人作為買賣判斷的依據。該研究的發想在於 形態學交易大多需要仰賴人為主觀的判斷，尚未有一套技術指標能夠精準地量化， 光靠人為的判斷難免會失真而且費時費力，因此如果能透過深度學習的方法來辨識形態學的影像，投資人不但能增加投資判斷的精準度，也能更有效率地進行形態學交易。 
### 系統流程  
![image](https://github.com/albert0796/MachineLearning/blob/master/Project_PatternHunter/Report/flow_chart.png)  
本系統分成前端與後端兩項開發。測試的標的資產為 S&P 500，時間尺度為日資料。前端的部分，首先透過 financialmodelingprep 所提供的 API 載入標的資產的開盤、最高、最低、收盤價資料 (ohlc)；接著將 ohlc 做 GAF 轉換，將一維的時間序列資料轉換為二維的圖像資料；接著透過 CNN 模形進行訓練；隨後再透過 financialmodelingprep 的 API 串流即時資料，模形將會依串流的即時資料進行形態學交易訊號預測。後端的部分主要進行網站開發以及使用者介面優化。本篇研究只包含後端開發的部分。  
#  
### 程式碼  
* [所有流程markdown檔](https://github.com/albert0796/MachineLearning/blob/master/Project_PatternHunter/Code/Pattern%20Hunter%20%E5%90%B3%E6%94%BF%E7%BF%B0.ipynb)
* [Main檔](https://github.com/albert0796/MachineLearning/blob/master/Project_PatternHunter/Code/Main.py)  
[歷史資料Api](https://github.com/albert0796/MachineLearning/blob/master/Project_PatternHunter/Code/Api_history.py)  
[交易訊號偵測](https://github.com/albert0796/MachineLearning/blob/master/Project_PatternHunter/Code/Signal2.py)  
[GAF轉換](https://github.com/albert0796/MachineLearning/blob/master/Project_PatternHunter/Code/util_gasf.py)  
[CNN建模](https://github.com/albert0796/MachineLearning/blob/master/Project_PatternHunter/Code/util_gasf.py)  
[即時資料Api](https://github.com/albert0796/MachineLearning/blob/master/Project_PatternHunter/Code/Api_realtime.py)  
