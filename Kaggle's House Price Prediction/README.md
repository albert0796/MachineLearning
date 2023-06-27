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
