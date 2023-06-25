# Cathlife Critical Illness Insurance Purchasing Data Analysis
### Author: Wu Cheng-Han, Chou Po-Chia, Lin Jin-Tong
### Advisor: Dr. Huang Fu-Ming
### Orgnizer: [Cathay Insurance](https://tbrain.trendmicro.com.tw/Competitions/Details/7)
### Honor: [Ranked 34th among 244 teams on the private leaderboard](https://tbrain.trendmicro.com.tw/Competitions/Details/7)。
#
### [Full Analysis Document](https://github.com/albert0796/MachineLearning/blob/master/Competition_Cathlife/report/Cathlife%20Critical%20Illness%20Insurance%20Purchasing%20Data%20Analysis.pdf)
#  
### Introduction  
The project aim to utilize customers' historical data to predict whether existing customers will purchase critical illness insurance policies within a specific timeframe, thus creating a predictive purchasing model. This model will help identify customers with higher insurance needs and provide sales professionals with a method to target potential customers with such needs, aiming to reduce overall costs and maximize profits.
#
### EDA, Exploratory Data Analysis
#### Dataset Description
The official dataset provided includes two types: Train and Test. Training dataset contains the number of 100000 data points and the number of 131 feature columns. Testing dataset contains the number of 150000 data points and the number of 130 feature columns.
#### Y field (dependent variable)
The Y1 field means whether customers will purchase the insurance. Its value has only two categories: Y, N. The Y-value represents customers who have purchased the insurance, totaling 2000 data points, while the N-value represents customers who have not purchased the insurance, totaling 98,000 data points. Noticeably, according to the difference between the data number of those two categories, it suggests that the dataset is quite inbalance.
<p align="left">
  <img
    src="https://github.com/albert0796/MachineLearning/blob/master/Competition_Cathlife/image/Y%20Field.png"
    width="250px" 
    height="100%"
  >
<p>
  
### Missing Values
The missing value patterns in the Train and Test datasets were analyzed using a missing value heatmap. The X-axis represents the columns, while the Y-axis represents customer IDs. The data cells with values are represented in blue, while the data cells without values are represented in red. Based on the heatmap analysis, the following observations can be made:
1. There are a total of 73 columns with missing values.
2. Among the 131 features, 17 columns have missing values that account for more than half of the values in those columns.
3. The columns with missing values in the Test dataset are the same as those in the Train dataset.
4. The missing values in the heatmap exhibit parallel distribution in certain columns.


### 程式碼  
* [所有程式碼txt檔](https://github.com/albert0796/MachineLearning/blob/master/Competition_Cathlife/code/IF_%E7%A8%8B%E5%BC%8F%E7%A2%BC.txt)  
* [Data Cleaning](https://github.com/albert0796/MachineLearning/tree/master/Competition_Cathlife/code/Data%20Cleaning)  
[EDA & Feature Engineering](https://github.com/albert0796/MachineLearning/tree/master/Competition_Cathlife/code/EDA%20%26%20Feature%20Engineering)  
[Further Processing](https://github.com/albert0796/MachineLearning/tree/master/Competition_Cathlife/code/Further%20Processing)  
[Modeling](https://github.com/albert0796/MachineLearning/tree/master/Competition_Cathlife/code/Modeling)  
[Observation](https://github.com/albert0796/MachineLearning/tree/master/Competition_Cathlife/code/Observation)  

