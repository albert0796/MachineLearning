# PatternHunter – A Deep Learning-Based Candlestick Pattern Recognition System

### Introduction
The candlestick pattern recognition is one of the post popular investment techniques among professional traders. The essence of this techniques is that it doesn’t have a very objective or rigid rule. Instead, each trader depends on their unique trading intuitiveness and knowledge to visually recognize the profitable candlestick pattern. Therefore, to take advantage of this technique to a great extent and support the trader, we build an AI-based system that can absorb professional traders’ domain knowledge through its complicated neural network and excel in visual recognition with the convolutional structure. Moreover, since the system can automatically execute the procedure and have the customized user interface, the user of traders can avoid the human error and make investment more efficiently. 

#
### System Procedure
<p align="left">
  <img src="https://github.com/albert0796/MachineLearning/blob/master/Pattern%20Hunter/image/test%20(2).png" height="100%" width="800px">
<p>
  
The system covers front-end stage and back-end stage:</br>
- Back-end stage
1. Integrate APIs provided by the security firms or some specific sources to collect financial targets’ historical data.
2. Encode each one-dimensional time-series data with open, high, low, and close (OHLC) prices into a two-dimensional GAF matrix.
3. Train the Convolutional Neural Network (CNN) model with the historical data and make it able to recognize the candlestick pattern.
4. Periodically send the real-time data by integrating APIs and input it to the trained model and make the prediction.
5. The predicting result of historical data and real-time data will be wrapped in the API for the front-end stage.
6. The system will periodically and automatically update the training dataset with the cumulative real-time data for the model and re-train it to improve its performance.

- Front-end stage
1.	Build a website, named “PatternHunter”, with the customized user interface.
2.	The interface demonstrates the historical and the real-time candlestick movement with the different time scale.
3.	When the user selects one part of the candlestick movement with different window sizes, the system will show the position of profitable candlestick patterns recognized by the AI model among that region. 
4.	The system will also demonstrate the real-time profitable candlestick pattern for the user to deal with their investment.

#
### Methodology
#### Historical Data
Depending on the user’s needs, the system can cover as many types of financial targets as possible. The GitHub project use S&P 500 and EUR USD as example. The data is time-series data with features of open, high, low, and close prices and volume.
#### Labeling
As the introduction mentioned, the system aims to absorb different professional traders’ knowledge and trading intuitiveness. Therefore, we will let human traders label the profitable candlestick patterns they expect. And the GitHub project will temporarily use the rule to label the data until the human trader complete their labeling tasks. The rule we use refers to THE MAJOR CANDLESTICKS SIGNALS “12 Signals to Master any Market” by Stephen W. Bigalow. The profitable patterns include Morning Star, Evening Star, Bearish Harami, Bullish Harami, Shooting star, Inverted Hammer, Bearish Engulfing and Bullish Engulfing.
<p align="left">
  <img src="https://github.com/albert0796/MachineLearning/blob/master/Pattern%20Hunter/image/rule-based%20pattern.png" height="100%" width="300px">
<p>

### Gramian Angular Field (GAF) Encoding
Since candlestick pattern recognition depends on visual recognition, we apply CNN model that is excellent in picking up on patterns in the image. Besides, given that the financial time-series data is a one-dimensional array and cannot fit the two-dimensional convolution of the CNN, the data should be converted into a consistent matrix form. Therefore, we apply the GAF encoding method to encode time series data into the suitable type. And Noticeably, according to the [literature review](https://arxiv.org/abs/1901.05237), the GAF-CNN model has more than 90% accuracy in candlestick pattern recognition. For the detail of GAF encoding, please refers to [this paper](https://arxiv.org/abs/1901.05237).
<p align="left">
  <img src="https://github.com/albert0796/MachineLearning/blob/master/Pattern%20Hunter/image/gaf.png" height="100%" width="300px">
<p>





