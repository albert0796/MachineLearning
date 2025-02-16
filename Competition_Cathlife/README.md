# Cathlife Critical Illness Insurance Purchasing Data Analysis
### Author: Wu Cheng-Han, Chou Po-Chia, Lin Jin-Tong
### Advisor: Dr. Huang Fu-Ming
### Orgnizer: [Cathay Insurance](https://tbrain.trendmicro.com.tw/Competitions/Details/7)
### Honor: [Ranked top 3% out of 300 nationwide](https://tbrain.trendmicro.com.tw/Competitions/Details/7)
#
### [Full Analysis Document](https://github.com/albert0796/MachineLearning/blob/master/Competition_Cathlife/report/Cathlife%20Critical%20Illness%20Insurance%20Purchasing%20Data%20Analysis.pdf)
For far more details, especially the parts of Exploratory Data Analysis, Data Cleaning and Modeling, please refer to the full analysis document.
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
3. Making a new featrue from the original features  
For example, "TOTAL AMT - Total Annual Coverage" is calculated by summing up the relevant columns related to the annual coverage amount (a total of 15 columns). 

#### Missing Value Imputation
1. Domain-specific Imputation  
The missing values exhibit parallel distribution in the columns "APC_1ST_AGE" (Age of the first policyholder), "REBUY_TIMES_CNT" (Number of repeat purchases), "RFM_M_LEVEL" (Number of previous policies owned), "RFM_R" (Time interval since the last policyholder's identity was insured), and "LEVEL" (Relationship level) (refer to Table 2). It can be indicated that these samples have never served as policyholders. However, the meaning of these missing values does not belong to any specific category in these five columns. Therefore, these missing values will be replaced with a new category: 0.
<p align="center">
  <img
src="https://github.com/albert0796/MachineLearning/blob/master/Competition_Cathlife/image/Domain-specific%20Imputation.png"
    width="400px" 
    height="100%"
  >
<p>

2. Regression Imputation 1  
Use the columns in the dataset that do not have missing values as the independent variables and the column to be imputed as the dependent variable. Use the feature_importances_ function in the ExtraTreesRegressor model to calculate the importance scores of each independent variable for the dependent variable. Sort the variables in descending order and select the top 10 important variables as the explanatory variables. Divide these 10 variables into 10 groups: the first important variable, the first + second important variables, the first + second + third important variables, and so on. Use these 10 feature combinations as the explanatory variables and the column to be imputed as the dependent variable. Perform calculations using the ExtraTreesRegressor model, and for each feature combination, measure the accuracy using a specific metric. If the column to be imputed is a categorical variable, use the F1 score as the accuracy metric. If it is a numerical variable, use MSE and RMSE as the accuracy metrics. Finally, select the feature combination with the best accuracy metric and use the ExtraTreesRegressor model to predict and impute the missing values in the column to be imputed. If the F1 score is below 0.7 for each feature combination or if the MSE and RMSE are not ideal, discard this method.

3. Regression Imputation 2  
This method is a more cautious approach to reinforce the first approach. If the accuracy metric results from the first approach are not satisfactory, for the sake of rigor, the second approach will be considered for imputing missing values. First, the columns without missing values are used as independent variables, and the column to be imputed is set as the dependent variable. The ExtraTreesClassifier model is employed with 10 different seeds, and the model is run 10 times. Each time, the feature_importances_ function is used to calculate the importance scores of each independent variable. The top 10 important variables (independent variables) are listed for each run. The frequency of occurrence of all the independent variables (columns without missing values) in the top 10 important variables across the 10 runs is then calculated. Finally, the variables (independent variables) with the highest frequencies are selected, and the ExtraTreesClassifier model is used to predict and impute the missing values in the column to be imputed.

4. Filling with Mode and Mean  
Fill the missing values of the target column by using either the mode or the mean of that column.

### Model Construction
#### Further Processing
- One-Hot Encoding
#### Model Selection
Due to the time constraints and hardware limitations during the competition, we focus on enhancing and testing only the two most promising models. We ran the cleaned data through six different models: XGBoost, AdaBoost, Random Forest, DecisionTree, Logistic Regression, and MLP. The goal was to select the two models with the highest AUC for further enhancement and testing. These models were run with default parameters without any tuning. From Table 5, it can be seen that XGBoost and AdaBoost achieved the top two AUC scores. However, since the top three models are all tree-based models with similar underlying principles, we aimed to choose one tree-based model and one non-tree-based model to diversify the subsequent testing and increase the potential for score improvement. Additionally, the Logistic Regression model ranked fourth, and its AUC score was not significantly lower. Furthermore, this model has room for optimization, such as addressing the impact of imbalanced data by using techniques like SMOTE sampling. Additionally, tree-based models inherently have a tendency to select important features during computation, while Logistic Regression does not. This can be improved by selecting features based on their importance using techniques like Feature Importance. Therefore, in the end, we chose the XGBoost model with the highest AUC and the non-tree-based Logistic Regression model for further enhancement and testing.
#### Modeling
- Training & validating data spliting  
The Train dataset was split into 67% training data (Training Data) and 33% validation data (Validation Data).  
- Hyper-parameter tuning
  - XGBoost
    - Default Parameters: The model was trained without any preprocessing, and the model parameters were set to their default values.
    - Parameter Tuning: The model's parameters were adjusted to optimize its performance.
    - Parameter Tuning and Feature Selection: In addition to adjusting the parameters, important features were selected to train the model.
    - Enhanced Data Processing: New data processing techniques were applied to improve the model's performance.
    - Enhanced Data Processing with Parameter Tuning: Both new data processing techniques and parameter tuning were applied to further improve the model's performance.
  - Logistic Regression
    - Default Parameters: The model was trained without any preprocessing, and the model parameters were set to their default values. The predictions were directly uploaded.
    - One-Hot Encoding and Parameter Tuning: The categorical variables were encoded using one-hot encoding, and the model's parameters were adjusted for better performance.
    - One-Hot Encoding, Parameter Tuning, and Feature Selection: In addition to one-hot encoding and parameter tuning, important features were selected to train the model.
    - One-Hot Encoding, Parameter Tuning, and SMOTE Sampling: In addition to one-hot encoding and parameter tuning, the dataset was balanced using the SMOTE sampling technique.
    - Enhanced Data Processing: New data processing techniques were applied to improve the model's performance.

#
### Result & Discussion
According to the final statistics, the XGBoost model performed best on the validation dataset when using the new data cleaning method and tuning the parameters. However, the actual uploaded scores showed that the XGBoost model performed best when no preprocessing was applied. Nevertheless, the platform will ultimately use a new dataset to test the models and determine the scores for the Private Leaderboard. Therefore, it is still uncertain which model will ultimately prevail. Additionally, Logistic Regression performed worse than any configuration of XGBoost, regardless of the method applied for preprocessing.
<p align="center">
  <img
src="https://github.com/albert0796/MachineLearning/blob/master/Competition_Cathlife/image/result.png"
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

