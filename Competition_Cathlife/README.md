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
<p align="center">
  <img
    src="https://github.com/albert0796/MachineLearning/blob/master/Competition_Cathlife/image/Y%20Field.png"
    width="250px" 
    height="100%"
  >
<p>
  
#### Missing Values
The missing value patterns in the Train and Test datasets were analyzed using a missing value heatmap. The X-axis represents the columns, while the Y-axis represents customer IDs. The data cells with values are represented in blue, while the data cells without values are represented in red. Based on the heatmap analysis, the following observations can be made:
1. There are a total of 73 columns with missing values.
2. Among the 131 features, 17 columns have missing values that account for more than half of the values in those columns.
3. The columns with missing values in the Test dataset are the same as those in the Train dataset.
4. The missing values in the heatmap exhibit parallel distribution in certain columns.
<p align="center">
  <img
src="https://github.com/albert0796/MachineLearning/blob/master/Competition_Cathlife/image/Missing%20Value.png"
    width="600px" 
    height="100%"
  >
<p>

### Data Cleaning & Data Processing
#### Variable Transformation
1. Transforming categorical variables into numerical variables  
- "Low", "Medium", "Medium-High", "High" will be transformed into 1, 2, 3, 4 respectively.
- "Low", "Medium", "High" will be transformed into 1, 2, 3 respectively.
- "N" and "Y" will be transformed into 0 and 1 respectively (including the label).
- "F" and "M" will be transformed into 0 and 1 respectively.
- "A1" will be transformed into 1, "A2" into 2, "B1" into 3, "B2" into 4, "C1" into 5, "C2" into 6, "D" into 7, "E" into 8.
- "A" will be transformed into 1, "B" into 2, "C" into 3, "D" into 4, "E" into 5, "F" into 6, "G" into 7, "H" into 8.
2. Convert continuous numerical variables into categorical ranges or intervals
Take the variable "BMI value" for instance, which will be discretized into whether it falls within the range [0, 0.2) or not, represented by 1 for "yes" and 0 for "no". From the plot, it is evident that when the BMI value is within the range of 0 to 0.2, the number of samples not purchasing critical illness insurance is significantly higher than the number of samples purchasing it. On the other hand, when the BMI value is not within the range of 0 to 0.2, the number of samples not purchasing critical illness insurance is noticeably lower than the number of samples purchasing it. Therefore, it can be inferred that when a customer's BMI value falls within the range of 0 to 0.2, it is highly likely that they will not purchase critical illness insurance. Based on this observation, it is concluded that whether the BMI falls within the [0, 0.2) range is an important feature in explaining Y1 (the purchase of critical illness insurance), and thus the BMI value will be discretized accordingly.
<p align="center">
  <img
src="https://github.com/albert0796/MachineLearning/blob/master/Competition_Cathlife/image/bmi.png"
    width="400px" 
    height="100%"
  >
<p>


#
### 程式碼  
* [所有程式碼txt檔](https://github.com/albert0796/MachineLearning/blob/master/Competition_Cathlife/code/IF_%E7%A8%8B%E5%BC%8F%E7%A2%BC.txt)  
* [Data Cleaning](https://github.com/albert0796/MachineLearning/tree/master/Competition_Cathlife/code/Data%20Cleaning)  
[EDA & Feature Engineering](https://github.com/albert0796/MachineLearning/tree/master/Competition_Cathlife/code/EDA%20%26%20Feature%20Engineering)  
[Further Processing](https://github.com/albert0796/MachineLearning/tree/master/Competition_Cathlife/code/Further%20Processing)  
[Modeling](https://github.com/albert0796/MachineLearning/tree/master/Competition_Cathlife/code/Modeling)  
[Observation](https://github.com/albert0796/MachineLearning/tree/master/Competition_Cathlife/code/Observation)  

