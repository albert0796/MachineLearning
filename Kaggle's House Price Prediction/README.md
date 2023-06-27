# Kaggle's House Prices Prediction
### Reference: [Kaggle's House Prices - Advanced Regression Techniques](https://www.kaggle.com/c/house-prices-advanced-regression-techniques)  
#
### Introduction
The goal of the project is to predict the final sale prices of houses. The dataset contains various features of residential homes, such as the number of bedrooms, the size of the lot, the neighborhood, and many others. The project covers much feature engineering, involving handling missing values, transforming variables, creating interaction terms. Additionally, it applies Stacking, ensemble learning, and hype-tunes multiple machine learning model to predict and make comparison. 
#
### Dataset
There are 79 explanatory variables describing the aspect of residential homes and the final price as a response variable. The dataset includs the number of 1460 samples.
#
### Data Cleaning
#### Type Convertion
1. Transform ordinal categorical features by assigning numerical values in the order of their magnitudes. For example, for the feature "ExterQual" representing the quality of exterior materials, the categories are Excellent, Good, Average/Typical, Fair, and Poor. Since these categories have an inherent order, they are assigned values of 5, 4, 3, 2, and 1, respectively.
2. Some features may contain missing values, but these missing values do not imply an actual missing value. Instead, they represent a specific category that indicates the absence of that feature. For instance, in the feature "BsmtQual" indicating the height of the basement, missing values indicate "No basement" and are considered as a separate category. These missing values will be assigned a new category label 'NA'.
3. For ordinal categorical features that have both ordinal categories and the 'NA' category, a distinct numerical value of 999 is assigned to represent 'NA'. Additionally, a new binary feature is created to indicate the presence or absence of that particular feature. If the feature is present, the binary value is 0; otherwise, it is 1.
4. Convert numerical features with categorical interpretations into categorical features.
#### Missing Value Imputation
After the type convertion, there are only one feature having 259 missing values, and I apply regression imputation to solve the problem.
<p align="center">
  <img
src="https://github.com/albert0796/MachineLearning/blob/master/Kaggle's%20House%20Price%20Prediction/image/missing%20value.png"
    width="700px" 
    height="100%"
  >
<p>

- Regression Imputation  
The approach involves using the ExtraTreesRegressor model and its feature importances functionality to calculate the importance scores of each explanatory variable (columns without missing values) with respect to the target variable (column to be filled). The feature importances are ranked in descending order, and the top 10 important columns are selected as explanatory variables.  
These 10 selected columns are then divided into 10 groups of feature combinations: the first important column, the first and second important columns, the first, second, and third important columns, and so on. Each group of feature combinations is used as the explanatory variables, and the target column with missing values is used as the target variable. The ExtraTreesRegressor model is applied to predict and fill the missing values, and a corresponding accuracy metric is calculated for each group of features.  
If the target column is categorical, the F1 score is used as the accuracy metric, while if the target column is numerical, the mean squared error (MSE) and root mean squared error (RMSE) are used as the accuracy metrics. Finally, the feature combination with the best accuracy metric is selected, and the ExtraTreesRegressor model is used to predict and fill the missing values in the target column.
#
### Further Processing
#### Feature Engineering
Create New Features From Existing Features. For example, I create a new feature named "TotalHouse" that is the sum of the total square feet of basement area, First Floor square feet and second floor square feet. Also, I create another new feature named "Functional_TotalHouse" that is the product of TotalHouse and home functionality. 
<p align="center">
  <img
src="https://github.com/albert0796/MachineLearning/blob/master/Kaggle's%20House%20Price%20Prediction/image/feature%20engineering.PNG"
    width="600px" 
    height="100%"
  >
<p>

#### One-hot Encoding
#### Feature Selection
Remove the features with an importance score equal to 0 using ExtraTreesClassifier.
#### Collinear Identification
Remove features that exhibit high multicollinearity and have feature importance far below the threshold set by SelectFromModel.
#
### Hypertune
I use K-fold, a cross validation method, to hyper-tune the model. The K is set to be 5 and $R^{2}$ is used as an evalution index. 
The hypertune models include Decision Tree, Random Forest, AdaBoost, Lasso Regression, Neural Network, XGBoost, SVM and LightGBM. For the detalis of the hyper-parameter in each model, please refer to [Kaggle 房價預測_Hypertune.ipynb](https://github.com/albert0796/MachineLearning/blob/master/ClassHangout/kaggle/code/Kaggle%20%E6%88%BF%E5%83%B9%E9%A0%90%E6%B8%AC_Hypertune.ipynb)
- [K-fold](https://scikit-learn.org/stable/modules/cross_validation.html)  
  The method of cross-validation involves taking K-1 portions of the data as the training set and the remaining portion as the validation set. A validation error is calculated based on this split. Then, another portion of data that has not been used as the validation set is selected, and the previously used validation set is added back to the training set. This process is repeated until each portion of data has been used as the validation set. This results in K iterations, and K validation errors are calculated. Finally, the K validation errors are averaged to obtain a mean score, which serves as the evaluation metric for assessing the model's performance.
#
### Modeling & Performance
#### Stacking
All the tuned models, including XGBoost, LightGBM, AdaBoost, Random Forest, MLP, SVM, and Lasso Regression, are used for stacking. The ensemble model excludes Decision Tree due to its lower performance compared to the other models. The Final Model selected for stacking is Lasso Regression.
<p align="center">
  <img
src="https://github.com/albert0796/MachineLearning/blob/master/Kaggle's%20House%20Price%20Prediction/image/stacking.png"
    width="600px" 
    height="100%"
  >
<p>

- Performance  
Its $R^{2}$ score achieve 0.9033
<p align="center">
  <img
src="https://github.com/albert0796/MachineLearning/blob/master/Kaggle's%20House%20Price%20Prediction/image/stacking%20performance.png"
    width="600px" 
    height="100%"
  >
<p>

#
### Comparison of Model Performance
| Model | $R^{2}$ |
| :----: | :----: |
| Stacking | 0.9033 |
| LightGBM | 0.9007 |
| XGBoost | 0.9003 |
| Random Forest | 0.8822 |
| Neural Network | 0.8703 |
| AdaBoost | 0.8605 |
| Lasso | 0.8547 |
| SVM | 0.8445 |





