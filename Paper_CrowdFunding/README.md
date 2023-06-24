# Ensemble Machine Learning on Crowdfunding Data for Project Status and Amount Pledged Prediction
### Author: CHENG-HEN, WU
### Advisor: FU-MING, HUANG Ph.D
#  
### Introduction
Many crowdfunding projects could not reach their funding goals. The statistics shows that there is only one-third of projects successfully funded on average. In 2015, only 27.19% of projects met their goals (icopartners.com; Kickstarter in 2017 – Year in review, 2018). To solve the problem, this project aims to evaluate the success status and the final pledge amount of a launched project at the early stage in Kickstar and Indiegogo, both of which are world-famous crowdfunding platforms. Through evaluating the success status of a project at the early stage, backers can foresee whether projects can succeed and avoid wasting their money on a project which probably will fail. On the other hand, fundraisers also can examine a project which may fail and improve its quality as soon as possible. Moreover, only knowing the success status is not enough. If fundraiser can predict the final pledge amount of a project and know how much the predicted pledge amount higher than the funding goal, they will gain more insight. If the predicted pledge amount of a project is much higher than the funding goal, a project is much likely going to be popular with the market, and fundraisers will gain more confident to input more resources into project development. On the other hand, if the predicted pledge amount of a project is below the funding goal but near, fundraisers will still have opportunities to improve their projects and make it succeed.
  
To predict the success status and the final pledge amount of a launched project, I apply a machine learning method, Stacking, to make prediction. It is an Ensemble Learning technique typically by using a meta-level-classifier (Sikora, Riyaz and Al-laymoun, O'la Hmoud, 2014). It can be used to overcome three types of problems which are suffered from base learning algorithms: the statistical problem; the computational problem; and the representational problem (Thomas G. Dietterich, 2000). Experimental evidence in Freund and Schapire (1996) and other studies summarized in Dietterich (1997) have shown that ensemble methods are often much more accurate than any base learning algorithms (M.A. Arbib, Ed., 2002).
#  
### Dataset
The records respectively from Kickstarter and Indeigogo occupy 55.89% and 44.11% of the whole dataset. The number of successful projects is accounting for 36.02% of total projects while the number of failed projects is around 63.98% of total projects. The average amount of pledge is 11900 US dollars, the average amount of goal is 31500 US dollars. There are six columns for each project in the dataset, which are status, category, location, backers, goal_usd and pledge_usd. TABLE I and TABLE II describe detailed data information.

TABLE I. DATA TYPE AND DESCRIPTION OF EACH COLUMN
<p align="left">
  <img src="https://github.com/albert0796/MachineLearning/blob/master/Paper_CrowdFunding/data/DATA%20TYPE%20AND%20DESCRIPTION%20OF%20EACH%20COLUMN.png">
<p>

TABLE II. DESCRIPTIVE STATISTICS OF DATA COLUMNS
<p align="left">
  <img src="https://github.com/albert0796/MachineLearning/blob/master/Paper_CrowdFunding/data/TABLE%20II.%20DESCRIPTIVE%20STATISTICS%20OF%20DATA%20COLUMNS.png">
<p>

#
### Exploratory Data Analysis (EDA)
#### Number of Successful and Failed Projects by Category   
The number of failed projects is larger than the number of successful ones in most categories. Only in categories of Comics and Theaters does the number of successful projects exceed the numbers of failed projects. On the other hand, the total number of successful projects accounts for 36.02% of total projects. There are fourteen categories in which a percentage of successful projects are higher than this number. They are Comics, Theater, Audio, Tabletop_games, Music, Games, Film & Video, Gaming, Art, Design, Camera_gear, Dance, Politics and Home.
<p align="left">
  <img src="https://github.com/albert0796/MachineLearning/blob/master/Paper_CrowdFunding/data/Number%20of%20Successful%20and%20Failed%20Projects%20by%20Category.png">
<p>

#### Average Pledge & Number of Projects by Category
Among all the categories, a category of Energy_green_tech has the highest average amount of pledge. Under the top 10 categories which have ten of the most number of projects, a category of technology has the highest average amount of pledge. A project which has the most amount of pledge, 20338986 US dollars, is located in a category of Design.
<p align="left">
  <img src="https://github.com/albert0796/MachineLearning/blob/master/Paper_CrowdFunding/data/Average%20Pledge%20%26%20Number%20of%20Projects%20by%20Category.png">
<p>

#### Average Pledge & Average Backers by Category
There is a large gap between the line of the average amount of pledge and the average number of backers under a category of transportation. It suggests that the average amount of pledge by a backer under a category of transportation is much higher than under the other categories.
<p align="left">
  <img src="https://github.com/albert0796/MachineLearning/blob/master/Paper_CrowdFunding/data/Average%20Pledge%20%26%20Average%20Backers%20by%20Category.png">
<p>

#### Pearson correlation in backers, pledge_usd and goal_usd
The result shows that there is high correlation between pledge_usd and backers, and the rest of features reflect low correlation in between.
<p align="left">
  <img src="https://github.com/albert0796/MachineLearning/blob/master/Paper_CrowdFunding/data/Pearson%20correlation%20in%20backers%2C%20pledge_usd%20and%20goal_usd.png">
<p>
In further discussion, under a category of education, which is a main category with 17025 projects, the amount of pledge is only moderately correlated with the number of backers while the amount of pledge is highly correlated with the amount of goal in successful projects. Nonetheless, there is only high correlation between the amount of pledge and the amount of goal, and the rest of features reflect low correlation in between.

Successful Projects under the Category of Education</div>
<p align="left">
  <img src="https://github.com/albert0796/MachineLearning/blob/master/Paper_CrowdFunding/data/Pearson%20Correlation%20in%20Features%20in%20Successful%20Projects%20under%20the%20Category%20of%20Education.png">
<p>

Failed Projects under the Category of Education
<p align="left">
  <img src="https://github.com/albert0796/MachineLearning/blob/master/Paper_CrowdFunding/data/Pearson%20Correlation%20in%20Features%20in%20Failed%20Projects%20under%20the%20Category.png">
<p>

#
### Methodology
The target variables are the success status and the final pledge amount of a launched project, and the predictor variables include four features that are project category, project currency, number of backers and amount of goal. 
#### 1. Train Test Spliting
Split the original dataset into two datasets used for training and testing the model. The training dataset accounts for 70% of the original datasets and the other 30% ones are used for testing. 
#### 2. Model Construction
I build the Stacking, which consists of 7 different base models, without hyper-tuning, and a meta-model that combines the predictions of the base models. The base models include the Decision Tree, Random Forest, AdaBoost, Logistic Regression, SVM, Neural Network and XGBoost, and the meta-model applies the Lasso Regression. Each base model will make the prediction from the training data, and those output will be used as the new training set for the meta model and make the final prediction. After the training of the Stacking model, the testing dataset will be used to test the performance of the Stacking model. Furthermore, I also respectively train those 7 based models with hyper-tuning and compare the performance of those 7 models and the Stacking models. 
<p align="left">
  <img src="https://github.com/albert0796/MachineLearning/blob/master/Paper_CrowdFunding/data/stacking.png">
<p>
  
### Evaluation
I independently train the 7 based models with hyper-tuning and compare the performance of those 7 models and the Stacking models.
#### Success Status
| Model | AUC |
| :----:| :----: |
| Ensemble | 0.9803 |
| XGBoost | 0.9701 |
| AdaBoost | 0.9603 |
| Decision Tree | 0.9601 |
| Random Forest | 0.9505 |
| SVM | 0.9499 |
| Logistic Regression | 0.9498 |
| Neural Networking | 0.948 |
#### Final Pledge Amount of a Launched Project
| Model | $R^{2}$ |
| :----: | :----: |
| XGBoost | 0.7875 |
| Ensemble | 0.7852 |
| Random Forest | 0.7535 |
| Decision Tree | 0.6378 |
| AdaBoost | 0.6105 |
| Neural Networking |0.6032 |
| SVM | 0.5412 |
| Logistic Regression | 0.5093 |


