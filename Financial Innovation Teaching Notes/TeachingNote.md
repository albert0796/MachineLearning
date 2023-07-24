# Financial Vision
**Handout's Authors:** Cheng-Han Wu, Jun-Hao Chen

---

## Course Information
**Course Name:** Financial Innovations  
**Course Code:** Fin 7033  
**Course Instructor:** Yun-Cheng Tsai  
**Lecturer:** Jun-Hao Chen , Cheng-Han Wu  
**Lecture Date:** Nov. 27 & Dec. 4, 2020

---


## Course Instructor & Lecturer
**Instructor: Yun-Cheng Tsai**
- CoFounder / PecuLab
- Assistant Professor / School of Big Data Management, Soochow University
- Adjunct Assistant Professor / Department of Finance, National Taiwan University

**Lecturer: Jun-Hao Chen**
- Researcher / PecuLab
- Phd student / Department of Information Engineering, National Taiwan University

**Lecturer: Cheng-Han Wu**
- Researcher / PecuLab
- B.S. degree /  Economics, Soochow University

---

## Syllabus
### A.	Prerequisites
#### i.	Deep learning basics
-	Regression model
-	Logistic regression model
-	Multilayer perceptron (MLP)

[(李宏毅 (Hung-yi Lee))](http://speech.ee.ntu.edu.tw/~tlkagk/index.html)

#### ii.	Python 3
-	numpy (process high-dimentional arrays) + pandas (process csv files)
-	Keras 2.x (cpu-only is okay)
-	matplotlib (visualization)

[(莫煩PYTHON)](https://mofanpy.com/)  
[(政治大學蔡炎龍磨課師課程)](http://moocs.nccu.edu.tw/course/123/intro)

### B.	Course
#### i.	Overview
-	Background Knowledge to Candlestick
-	Research Purpose 
-	Research Method
-	Limitation & Extended Research
#### ii.	Introduction of rule-based candlestick patterns
-	Basic 8 candlestick patterns
-	Tricks of rules
-	HW1: collect at least two customized rule-based patterns with indices
#### iii.	Introduction of two deep learning classification models
-	RNN / LSTM
-	CNN (Lenet-5)
-	HW2: use both kinds of model to classify MNIST dataset with at least 90%
#### iv.	Candlestick pattern classification model
-	RNN / LSTM
-	Encoding (GASF) + CNN (Lenet-5)
-	Visualize results (confusion matrix & misclassified patterns)
-	HW3: use both kinds of model to classify customized candlestick pattern (at least 3 classes)
#### v.	Introduction of explainable artificial intelligence (XAI)
-	Concept of LIME
-	How to implement XAI on candlestick classification model (CNN)
-	(optional) More ways to explain: adversarial attack
-	HW4: explain your own model by any XAI methods
#### vi.	Introduction of generation model
-	Basic autoencoder model
-	Variational Autoencoder (VAE) & Adversarial Autoencoder (AAE)
-	(optional) VAE / AAE conditions on labels
-	(optional) More ways to generate data: adversarial samples
-	HW5: make a generator to generate your customized patterns

#### Introduction to Peculab

#### Reference

---

## I.	Overview
### A.	Background Knowledge to Candlestick
-	A candlestick is a type of price chart used in technical analysis that displays the high, low, open, and closing prices of a security for a specific period. In technical analysis, Candlesticks reflect the impact of investor sentiment on security price, and its pattern is a movement in prices shown graphically on a candlestick chart that some believe can predict a particular market movement.  
[(Candlestick Definition)](https://www.investopedia.com/terms/c/candlestick.asp)  
[(The 5 Most Powerful Candlestick Patterns)](https://www.investopedia.com/articles/active-trading/092315/5-most-powerful-candlestick-patterns.asp) 
-	If the opening price is above the closing price then a filled (normally red or black) candlestick is drawn; If the closing price is above the opening price, then normally a green or a hollow candlestick (white with black outline) is shown. In addition, the filled or hollow portion of the candle is known as the body or real body, and can be long, normal, or short depending on its proportion to the lines above or below it. Moreover, the lines above and below, known as shadows, tails, or wicks represent the high and low price ranges within a specified time period. However, not all candlesticks have shadows.  

![](https://i.imgur.com/kpzFUvR.png)

-	Take a candlestick pattern, “Evening Star”, for example, which is a top reversal signal. It is formed after an obvious uptrend, and a long white body occurs at the end of an uptrend usually when the confidence has finally built up. The following day gaps up, yet the trading range remains small for the day, which is the star of the formation. The third day is a black candle day and represents the fact that the bears have now seized control. 
[(THE MAJOR CANDLESTICKS SIGNALS “12 Signals to Master any Market”)](https://www.academia.edu/39149023/THE_MAJOR_CANDLESTICKS_SIGNALS_12_Signals_to_Master_any_Market_Master_these_Major_Candlestick_Signals_if_you_want_to)

![](https://i.imgur.com/kP5ti2k.png)

### B.	Research Aim 
**To successfully identify candlestick pattern of a financial target as a reliable trading signal through an image classification model.**
-	Differing from the general candlestick trading strategy that identifies a candlestick pattern by human’s eyes, the method used in the “Financial Vision” catches a candlestick pattern by means of the deep learning classification model.
-	In financial trading, techniques like pattern recognition could advance the efficiency of strategic decisions and reduce some human errors in identifying a candlestick pattern.
-	Compared to the model which designed to work on time series problem, the training process of the CNN model tends to be more similar to how human learns to study financial data.

### C.	Research Objective
* **Data Labeling:** Label the candlestick pattern according to people’s domain knowledge or the predefined rule which relies on discipline in a textbook.
* **Model Training:** Fit a deep learning classification model to the rule-based candlestick pattern and its labels.
* **Model Prediction:** With the streaming data collected in real-time, the model will be able to detect the incoming candlestick pattern and provide a real-time trading signal for a trader.
* **Error Modification:** To those incoming candlestick patterns which are misclassified by the model, they will be labeled and input into the model for training so as to enhance the model’s performance.

### D.	Limitation & Extended Research
**i.	The number of rule-based patterns used for model training are limited.**
-	In practice, the number of the pattern labeled by a trader are not enough. Besides, the number also get limited when the condition of the predefined rule becomes strict.
-	The size of dataset is crucial to model training in machine learning, especially to a model with lots of parameters. In order to get a good performance, it is necessary to show a machine learning model a proportional number of examples.  
[(A strategy to apply machine learning to small datasets in materials science)](https://www.nature.com/articles/s41524-018-0081-z)
-	To get more data, the method of data augmentation can be applied, which functions to generate more candlestick patterns for model training and improve the robustness of a model. In addition, difference between a pattern generated synthetically by the method in the “Financial Vision” and a pattern labeled by a trader is hard to recognized by humans.  
[(Data Augmentation | How to use Deep Learning when you have Limited Data — Part 2)](https://nanonets.com/blog/data-augmentation-how-to-use-deep-learning-when-you-have-limited-data-part-2/)  
[(A survey on Image Data Augmentation for Deep Learning)](https://journalofbigdata.springeropen.com/articles/10.1186/s40537-019-0197-0)

**ii.	The mechanism by which the candlestick model works lacks of transparency. It is necessary to examine what the training model focuses on and its judgement bases on and whether it conforms to a trader’s domain knowledge or not.**
-	Deep Neural Networks (DNNs) comprises hundreds of layers and millions of parameters, which makes it be considered as complex black-box models. As the black-box model is increasingly being employed to make important predictions in critical contexts, the demand for transparency is increasing from the various stakeholders in AI. It is because that it is dangerous to apply the black-box model to make decisions that are not justifiable and legitimate, and, on the other hand, an expert requires far more information from the model than a simple binary prediction. 
-	Through the Explainable AI (XAI), which focuses on exposing complex AI models to humans in a systematic and interpretable manner, interpretability of the deep learning model will get improved so as to correct deficiencies of the system:
    1. Interpretability helps ensure impartiality in decision-making, and consequently, correct from bias in the training dataset.
    2.	Interpretability facilitates the provision of robustness by highlighting potential adversarial perturbations that could change the prediction.
    3.	Interpretability can act as an insurance, guaranteeing that a truthful causality exists in the model reasoning.
[(Explainable Artificial Intelligence (XAI): Concepts, Taxonomies, Opportunities and Challenges toward Responsible AI)](https://arxiv.org/abs/1910.10045)  
[(“Why Should I Trust You?” Explaining the Predictions of Any Classifier)](https://arxiv.org/abs/1602.04938)

---

## II.	Introduction of Rule-Based Candlestick Patterns
“Rule-Based Candlestick Patterns” is the step of data labeling. Data labeling is an important part of data preprocessing for machine learning, particularly for supervised learning, in which both input and output data are labeled for classification to provide a learning basis for future data processing and enable a learning model to correctly identify an unlabeled new input. Noticeably, instead of a method that a trader directly labels a candlestick pattern with his/her own domain knowledge, the following case labels a candlestick pattern through predefined rules. According to the predefined rule, it will detect a pattern which can form a specific trading signal through an algorithm.
### A.	Basic 8 Candlestick Patterns
[(THE MAJOR CANDLESTICKS SIGNALS “12 Signals to Master any Market”)](https://www.academia.edu/39149023/THE_MAJOR_CANDLESTICKS_SIGNALS_12_Signals_to_Master_any_Market_Master_these_Major_Candlestick_Signals_if_you_want_to)

**i.	Bullish Engulfing**

![](https://i.imgur.com/mrXvDqL.png)

-	The Bullish Engulfing pattern is a reversal signal, which thought to be the beginning of a bullish trend in the security. It also represents a complete change in investor sentiment. After a downtrend has been in effect, the price opens lower than where it closed the previous day. Before the end of the day, the emotional psychology of the trend has been altered, and the buyers have taken over and moved the price above where it opened the day before. 
-	Criteria:
    1.	The body of the second day completely engulfs the body of the first day.
    2.	Prices have been in a definable down trend.
    3.	The body of the second candle is opposite color of the first candle, the first candle being the color of the previous trend.
    4.	The greater the open gaps down from the previous close, the greater the probability of a strong reversal.

**ii.	Bullish Harami**

![](https://i.imgur.com/hWQGNCH.png)

-	The Bullish Harami pattern indicates that a bearish trend in an asset or market may be reversing. After a strong down-trend has been in effect and after a selling day, the bulls open the price a higher than the previous close. The short's get concerned and start covering. The price finishes higher for the day. This is enough support to have the short sellers take notice that the trend has been violated. A strong day the next day would convince everybody that the trend was reversing.
-	Criteria:
    1.	The body of the first candle is black, the body of the second candle is white.
    2.	The downtrend has been evident for a good period. A long black candle occurs at the end of the trend.
    3.	The second day opens higher than the close of the previous day and closes lower than the open of the prior day.
    4.	The longer the black candle and the white candle, the more forceful the reversal.
    5.	The higher the white candle closes up on the black candle, the more convincing that a reversal has occurred despite the size of the white candle.

#### iii.	Bearish Engulfing

![](https://i.imgur.com/a5FzmQu.png)

-	The information conveyed in this signal creates an extremely high probability that the buying is over and reveals an opportunity for establishing a good short position. After an uptrend has been in effect, the price opens higher than where it closed the previous day. Before the end of the day, the sellers have taken over and moved the price below where it opened the day before. The emotional psychology of the trend has now been reversed.
-	 Criteria:
     1. The body of the second day completely engulfs the body of the first day.
     2.	Prices have been in a definable down trend, even if it has been short term.
     3.	The body of the second candle is opposite color of the first candle, the first candle being the color of the previous trend.
     4.	The greater the open gaps up from the previous close, the greater the probability of a strong reversal.
 
#### iv.	Bearish Harami

![](https://i.imgur.com/Jr7zPDB.png)

-	The Bearish Harami pattern suggests prices may soon reverse to the downside. After a strong uptrend has been in effect and after a long white candle day, the bears open the price lower than the previous close. The longs get concerned and start profit taking. The price finishes lower for the day. The bulls are now concerned as the price closes lower. It is becoming evident that the trend has been violated. A weak day after that would convince everybody that the trend was reversing.
-	Criteria:
    1.	The body of the first candle is white; the body of the second candle is black.
    2.	The uptrend has been apparent. A long white candle occurs at the end of the trend.
    3.	The second day opens lower than the close of the previous day and closes higher than the open of the prior day.
    4.	The longer the white candle and the black candle, the more forceful the reversal.
    5.	The lower the black candle closes down on the white candle, the more convincing that a reversal has occurred, despite the size of the black candle.

#### v.	Shooting Star

![](https://i.imgur.com/lL70XKJ.png)

-	A shooting star is a bearish candlestick. After a strong up-trend has been in effect, the atmosphere is bullish. But before the end of the day, the bears step in and take the price back down to the lower end of the trading range, creating a small body for the day. Specifically, the long upper shadow represents that sellers had started stepping in. Even though the bulls may have been able to keep the price positive by the end of the day, the evidence of the selling was apparent.
-	Criteria:
    1.	A strong up-trend has been in effect.
    2.	The upper shadow should be at least two times the length of the body.
    3.	The color of the body is not important although a black body should have slightly more bearish implications.
    4.	There should be no lower shadow or a very small lower shadow.
    5.	The longer the upper shadow, the higher the potential of a reversal occurring.
    6.	A gap up from the previous day's close sets up for a stronger reversal move provided.

#### vi.	Inverted Hammer

![](https://i.imgur.com/3okcfO6.png)

-	The inverted hammer pattern is usually taken to be a trend-reversal signal. After a downtrend has been in effect, the atmosphere is bearish. But the next day, the Bulls step in and take the price back up without major resistance from the Bears. If the price maintains strong after the Inverted Hammer day the signal is confirmed.
-	Criteria:
    1.	A downtrend has been in effect.
    2.	The upper shadow should be at least two times the length of the body.
    3.	The color of the body is not important, although a white body should have slightly more bullish implications.
    4.	There should be no lower shadow, or a very small lower shadow.
    5.	The longer the upper shadow, the higher the potential of a reversal occurring.
    6.	A gap down from the previous day's close sets up for a stronger reversal move.

#### vii.	Morning Star

![](https://i.imgur.com/B9jtt7a.png)

-	The Morning Star is a bottom reversal signal. A strong downtrend has been in effect. The sellers start getting panicky. There is a large selloff day. The next day as the selling continues, bulls are stepping in at the low prices. The second day does not have a large trading range. The third day the bears start to lose conviction as the bull increase their buying. When the price starts moving back into the trading range of the first day, the sellers diminish and the buyers seize control. 
-	Criteria:
    1.	The downtrend has been apparent.
    2.	The body of the first candle is black, continuing the current trend. The second candle is an indecision formation.
    3.	The third day shows evidence that the bulls have stepped in. That candle should close at least halfway up the black candle.
    4.	The longer the black candle and the white candle, the more forceful the reversal.
    5.	A gap between the first day and the second day adds to the probability that a reversal is occurring.

#### viii.	Evening Star

![](https://i.imgur.com/j9JOB37.png)

-	The Evening Star pattern is a top reversal signal. A strong uptrend has been in effect. The buyers can't imagine anything going wrong, they are piling in. However, it has now reached the prices where sellers start taking profits or think the price is fairly valued. The next day all the buying is being met with the selling, causing for a small trading range. The bulls get concerned and the bears start taking over. The third day is a large sell off day.
-	Criteria:
    1.	The uptrend has been apparent.
    2.	The body of the first candle is white, continuing the current trend. The second candle is an indecision formation.
    3.	The third day shows evidence that the bears have stepped in. That candle should close at least halfway down the white candle.
    4.	The longer the white candle and the black candle, the more forceful the reversal.
    5.	A gap between the first day and the second day adds to the probability that a reversal is occurring.

### B.	Tricks of Rules
* The raw data is time series data in csv format. Take figure 1 for example, which is 1-minute pricing data for EUR / USD, and the period ranges from 2010 to 2012.

**fig.1**

![](https://i.imgur.com/Fk5WIdS.png)


* First, before defining rules, it is necessary to set a period in every single candlestick pattern we are going to detect. In figure 2, we set a period of a single candlestick pattern in 10 bars, which means that every time a candlestick pattern is detected by 10 candlestick bars. There are N candlestick patterns among the time series data, which we are going to detect.

**Fig 2.**

![](https://i.imgur.com/E49bOao.png)

* Second, we define rules about the trading signal, and detect the candlestick pattern according to the rules. If a candlestick pattern conforms to the rule of a trading signal, it will be labeled as that trading signal. In figure 3, a rule used to detect one of trading signals, Evening Star, is defined by the algorithm.
The following criterion is the rule used to detect a Evening Star candlestick pattern (each pattern in 10 bars):
    1.	The trending formed by top 7 candlesticks is positive.
    2.	The direction of 8th candlestick should be positive.
    3.	The direction of 10th candlestick should be negative.
    4.	The absolute value of the length of 8th candlestick should be over 65 percentiles among last 50 candlesticks.
    5.	The absolute value of the length of 9th candlestick should be below 35 percentiles among last 50 candlesticks.
    6.	The close price of the 10th candlestick should be below the median of the 8th candlestick’s real body.
    7.	The close price of the 8th candlestick should be below the median of the 9th candlestick’s real body.
    8.	The open price of the 10th candlestick should be below the median of the 9th candlestick’s real body.
    
**Fig 3.**
```
def eveningStar(df):
    cond1 = (df['trend'].iloc[-4] > 0)
    cond2 = (df['direction'].iloc[-3] > 0)
    cond3 = (df['direction'].iloc[-1] < 0)
    cond4 = (df['realbody_per'].iloc[-3] >= 65)
    cond4 = (df['realbody_per'].iloc[-2] <= 35)
    cond5 = (df['close'].iloc[-1] <= (df['open'].iloc[-3] + df['body'].iloc[-3] * (1/2)))
    cond6 = df['close'].iloc[-3] <= (df['open'].iloc[-2] + df['body'].iloc[-2] * (1/2)))
    cond7 = df['open'].iloc[-1] <= (df['open'].iloc[-2] + df['body'].iloc[-2] * (1/2)))
    
    if cond1 and cond2 and cond3 and cond4 and cond5 and cond6 and cond7:
        return 1
    else:
        return 0


data['EveningStar'] = None

for idx in data.index:
    start_idx, end_idx = (idx - 9), idx
    if start_idx >= 0:
        df = data.loc[start_idx:end_idx]
        label = eveningStar(df)
        data['EveningStar'].loc[end_idx] = label
```

* Third, the figure 4 presents the number of labeled candlestick patterns in each trading signal.

**Fig 4.**

![](https://i.imgur.com/gsD7igx.png)
<br>
### C.	HW1: collect at least two customized rule-based patterns with indices
#### **i.	Data Processing:**
The raw data is time series prices data for EUR/USD and its period ranges from 2010 to 2012.

1.	Convert the data’s time scale into 1 minute.
    - “pandas resample” is recommended.

2.	Add new columns: “upper_shadow”, “lower_shadow”, “realbody”, “upper_per”, “lower_per” and “realbody_per”
    -	“upper_per”, “lower_per” and “realbody_per” mean the absolute value of the upper shadow, lower shadow and real body of one candlestick’s percentiles among last 50 or 100 candlesticks respectively.
    -	“scipy percentileofscore” and “pandas rolling” are recommended.

#### **ii.	Data Labeling:**
Set a period of a single candlestick pattern in 10 bars, which means that every time a candlestick pattern is detected by 10 candlestick bars.

1.	Add new columns: “trend7”, “trend8” and “trend9”.
    -	“trend7”, “trend8” and “trend9” mean the direction of the trend formed by 7, 8 and 9 candlesticks respectively.
    -	Take “trend7” in figure 5 for example. If the direction of a trend formed by 7 continuation candlesticks is positive, whose index range from 7 to 13, the value of the “trend7” column in index 13 will be 1. On the other hand, If the direction is negative, the value will be -1.
    -	There are many methods to determine the direction of a trend, like regression or the difference between the close price of first and last candlesticks… Choose a method you like and explain it clearly.
    -	“pandas rolling” or loop is recommended.

**Fig 5.**

![](https://i.imgur.com/6sgeImF.png)

2.	Add new columns: at least two customized rule-based trading signals.
    -	Take a trading signal in figure 6, Evening Star, for example. If a pattern formed by 10 continuation candlesticks, whose index ranges from 10 to 19, conforms to the rule of Evening Star, the value of the “Evening Star” column in index 19 will be 1. If not, the value will be zero.
    -	For details about the trick of rule, see (II-B).
    -	“pandas rolling” or loop is recommended. 

**Fig 6.**

![](https://i.imgur.com/IbSqI3t.png)

3.	Present the number of labeled candlestick patterns in each trading signal.

![](https://i.imgur.com/SR51EZr.png)

4.	Visualize at least one labeled candlestick patterns in each trading signal.
    -	“mpl_finance.candlestick_ohlc” is recommended.
    
![](https://i.imgur.com/zFQE8A3.png)

5.	Other Requirement:
- Use if __name__ == '__main__' in your code in the “py” file.

![](https://i.imgur.com/dJaTwjG.png)

- Please submit 5 file (required) and other files (option) you need to use:
    1.	Process_ID_name.py: HW1 (i) / Construct a class.
    2.	Detect_ID_name.py: HW1 (ii) / Construct a class.
    3.	Main_ID_name.py: Call the module in [Process.py](https://github.com/albert0796/MachineLearning/blob/master/Financial%20Innovation%20Teaching%20Notes/source%20code/Data%20Processing/Process.py) and [Detect.py](https://github.com/albert0796/MachineLearning/blob/master/Financial%20Innovation%20Teaching%20Notes/source%20code/Data%20Processing/Detect.py) and meet the requirement in HW1.
    4.	Demo_HW1_ID_name.ipynb & .html: Present the result in markdown’s format. The file should include the following things:
        -	the module in [Process.py](https://github.com/albert0796/MachineLearning/blob/master/Financial%20Innovation%20Teaching%20Notes/source%20code/Data%20Processing/Process.py), [Detect.py](https://github.com/albert0796/MachineLearning/blob/master/Financial%20Innovation%20Teaching%20Notes/source%20code/Data%20Processing/Detect.py), [Main.py](https://github.com/albert0796/MachineLearning/blob/master/Financial%20Innovation%20Teaching%20Notes/source%20code/Data%20Processing/Main.py) and other files you need to use. Please add annotations in your code.
        -	The step following the requirement in HW1.
        -	explain clearly on each step, especially your customized rule-based trading signals.
        -	Show the resource you take for reference when doing the task.
-	For details of homework requirement, please see the reference template [Demo.ipynb](https://github.com/albert0796/MachineLearning/blob/master/Financial%20Innovation%20Teaching%20Notes/source%20code/Data%20Processing/Demo.ipynb).

7.	Extended Thinking
    -	Why do we detect the pattern according to the defined rule through the algorithm and also use learning model to classify the pattern?

6.	Complement:
    -	[THE MAJOR CANDLESTICKS SIGNALS “12 Signals to Master any Market”](https://www.academia.edu/39149023/THE_MAJOR_CANDLESTICKS_SIGNALS_12_Signals_to_Master_any_Market_Master_these_Major_Candlestick_Signals_if_you_want_to)
    -	Coding Style:
        1.	[Google Python 風格指南 (一)](https://medium.com/han-shih/google-python-%E9%A2%A8%E6%A0%BC%E6%8C%87%E5%8D%97-%E4%B8%80-4dda701f606b)
        2.	[Google Python 風格指南 (二)](https://medium.com/han-shih/google-python-%E9%A2%A8%E6%A0%BC%E6%8C%87%E5%8D%97-%E4%BA%8C-a7ee27d85cf9)
        3.	https://github.com/google/styleguide/blob/gh-pages/pyguide.md

---
        
## III. Candlestick pattern classification model

For details of the encoding method and pattern classification model, please see:  
- [Encoding candlesticks as images for patterns classification using convolutional neural networks](https://arxiv.org/abs/1901.05237).
- [Github](https://github.com/pecu/FinancialVision)
### A. HW2: use both kinds of model to classify MNIST dataset with at least 90%
Please submit a condensed file in zip in which there are 4 files (required) and other files (option) you need to use:

1. mnist_model_ID_name.py: Construct a class / Annotations
2. candlestick_model_ID_name.py: Construct a class / Annotations
3. Demo_HW2_ID_name.ipynb & .html: 
    - Markdown’s format and other modules you use
    - The step following the requirement in HW2
    - Explain clearly on each step.
    - Reference.
-	For details of homework requirement, please see the reference template [Demo.ipynb](https://github.com/albert0796/MachineLearning/blob/master/Financial%20Innovation%20Teaching%20Notes/source%20code/Modeling/Demo.ipynb).

---

## IV. Introduction of explainable artificial intelligence (XAI)

For details of explainable artificial intelligence (XAI), please see:  
-  [Explainable Deep Convolutional Candlestick Learner](https://arxiv.org/abs/2001.02767)
-  [Github](https://github.com/pecu/FinancialVision/tree/master/Explainable%20Deep%20Convolutional%20Candlestick%20Learner)

---

## V. Introduction of generation model
For details of explainable artificial intelligence (XAI), please see:  
- [Data Augmentation For Deep Candlestick Learner](https://arxiv.org/abs/2005.06731)
- [Github](https://github.com/pecu/FinancialVision/tree/master/Data%20Augmentation%20For%20Deep%20Candlestick%20Learner)

---

# Introduction to Peculab
### List of The Research Topics in Financial Vision
- [Encoding candlesticks as images for patterns classification using convolutional neural networks](https://github.com/pecu/FinancialVision/tree/master/Encoding%20candlesticks%20as%20images%20for%20patterns%20classification%20using%20convolutional%20neural%20networks) [[Arxiv]](https://arxiv.org/abs/1901.05237)
    - Chen, J., Tsai, Y. Encoding candlesticks as images for pattern classification using convolutional neural networks. Financ Innov 6, 26 (2020). https://doi.org/10.1186/s40854-020-00187-0
- [Explainable Deep Convolutional Candlestick Learner](https://github.com/pecu/FinancialVision/tree/master/Explainable%20Deep%20Convolutional%20Candlestick%20Learner) [[Arxiv]](https://arxiv.org/abs/2001.02767)
    - Accepted by [The 32nd International Conference on Software Engineering & Knowledge Engineering (SEKE 2020)](http://ksiresearch.org/seke/seke20.html), KSIR Virtual Conference Cener, Pittsburgh, USA, July 9--July 19, 2020.
- [Data Augmentation For Deep Candlestick Learner](https://github.com/pecu/FinancialVision/tree/master/Data%20Augmentation%20For%20Deep%20Candlestick%20Learner) [[Arxiv]](https://arxiv.org/abs/2005.06731)
- [Adversarial Robustness of Deep Convolutional Candlestick Learner](https://github.com/pecu/FinancialVision/tree/master/Adversarial%20Robustness%20of%20Deep%20Convolutional%20Candlestick%20Learner) [[Arxiv]](https://arxiv.org/abs/2006.03686)
- [Deep Reinforcement Learning for Foreign Exchange Trading](https://github.com/pecu/FinancialVision/blob/master) [[IEA/AIE 2020]](https://link.springer.com/chapter/10.1007/978-3-030-55789-8_34?fbclid=IwAR3kRZw9-PhK80ooSV7fRNih_XaHhBwdmmV3Fw7hJzV-ScMDhLoAmo8bIwU)
### Github
- [Financial Vision](https://github.com/pecu/FinancialVision?fbclid=IwAR3FgZGCDtdD1HhP36UtnKgegBfuLpZy8B_9wcFlVzizu01nxWKDTyEsl68)
### Other Introduction
- [The News Coverage for 2020 COSCOP from The Storm Media](https://www.facebook.com/watch/live/?v=2713173259001733&ref=watch_permalink)
- [Introduciton Vedio for Peculab](https://www.youtube.com/watch?v=97eegbLcQ24&feature=youtu.be&fbclid=IwAR2kFKKtYsNEZReWD7VIof8NWdweHF5olRAB3ZrZogD4kebteqEEYYjSkDk)
- [Peculab Website](http://www.peculab.org/?fbclid=IwAR2gJBAcZjyq5f0d2-_rUmQVunybW0Pzv66C4moTExmO0g3QkcbqxMZrUGA)

---

# Reference
1.	李宏毅 (Hung-yi Lee). Retrieved from 李宏毅 (Hung-yi Lee): 
http://speech.ee.ntu.edu.tw/~tlkagk/index.html
2.	莫煩PYTHON. Retrieved from 莫煩PYTHON: 
https://mofanpy.com/
3.	政治大學蔡炎龍磨課師課程. Retrieved from 政治大學蔡炎龍磨課師課程:
http://moocs.nccu.edu.tw/course/123/intro
4.	Alejandro Barredo Arrietaa, Natalia D´ıaz-Rodr´ıguezb, Javier Del Sera,c,d, Adrien Bennetotb,e,f, Siham Tabikg, Alberto Barbadoh, Salvador Garciag, Sergio Gil-Lopeza, Daniel Molinag, Richard Benjaminsh, Raja Chatilaf,  Francisco Herrerag. (2019.12.26). Explainable Artificial Intelligence (XAI): Concepts, Taxonomies, Opportunities and Challenges toward Responsible AI.
5.	Chen, J., Tsai, Y. Encoding candlesticks as images for pattern classification using convolutional neural networks. Financ Innov 6, 26 (2020).
6.	Chen, Jun-Hao and Chen, Samuel Yen-Chi and Tsai, Yun-Cheng and Shur, Chih-Shiang. Explainable Deep Convolutional Candlestick Learner. (2020).
7.	Chia-Ying Tsao, Jun-Hao Chen, Samuel Yen-Chi Chen, Yun-Cheng Tsai. Data Augmentation for Deep Candlestick Learner. (2020)
8.	Github; Google Python Style Guide. Retrieved from Github:
https://github.com/google/styleguide/blob/gh-pages/pyguide.md
6.	Investopedia; Candlestick Definition. (2020). Retrieved from Investopedia: https://www.investopedia.com/terms/c/candlestick.asp
7.	Investopedia; The 5 Most Powerful Candlestick Patterns. (2020). Retrieved from Investopedia: 
https://www.investopedia.com/articles/active-trading/092315/5-most-powerful-candlestick-patterns.asp
8.	Marco Tulio Ribeiro, Sameer Singh, Carlos Guestrin. (2016.8.9). ”Why Should I Trust You?” Explaining the Predictions of Any Classifier. 
9.	Medium; Google Python 風格指南 (一). (2019). Retrieved from Medium:
https://medium.com/han-shih/google-python-%E9%A2%A8%E6%A0%BC%E6%8C%87%E5%8D%97-%E4%B8%80-4dda701f606b
10.	Medium; Google Python 風格指南 (二). (2019). Retrieved from Medium:
https://medium.com/han-shih/google-python-%E9%A2%A8%E6%A0%BC%E6%8C%87%E5%8D%97-%E4%BA%8C-a7ee27d85cf9
11.	Nanonets; Data Augmentation | How to use Deep Learning when you have Limited Data — Part 2. (2018). Retrieved from Nanonets: 
https://nanonets.com/blog/data-augmentation-how-to-use-deep-learning-when-you-have-limited-data-part-2/
12.	Shorten, C., Khoshgoftaar, T.M. (2019). A survey on Image Data Augmentation for Deep Learning.
13.	Stephen W. Bigalow. THE MAJOR CANDLESTICKS SIGNALS “12 Signals to Master any Market”. The Candlestick Forum LLC.
14.	Whatis.com; data labeling. Retrieved from Whatis.com:
https://whatis.techtarget.com/definition/data-labeling
15.	Wikipedia; Candlestick pattern. (2020). Retrieved from Wikipedia: https://en.wikipedia.org/wiki/Candlestick_pattern
16.	Zhang, Y., Ling, C. (2018). A strategy to apply machine learning to small datasets in materials science. 
