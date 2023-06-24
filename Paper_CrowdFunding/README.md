# Ensemble Machine Learning on Crowdfunding Data for Project Status and Amount Pledged Prediction
### Author: CHENG-HEN, WU
### Advisor: FU-MING, HUANG Ph.D
#  
### Abstract  
Many crowdfunding projects could not reach their funding goals. The statistics shows that there is only one-third of projects successfully funded on average. In 2015, only 27.19% of projects met their goals (icopartners.com; Kickstarter in 2017 – Year in review, 2018). To solve the problem, this project aims to evaluate the success status and the final pledge amount of a launched project at the early stage in Kickstar and Indiegogo, both of which are world-famous crowdfunding platforms. Through evaluating the success status of a project at the early stage, backers can foresee whether projects can succeed and avoid wasting their money on a project which probably will fail. On the other hand, fundraisers also can examine a project which may fail and improve its quality as soon as possible. Moreover, only knowing the success status is not enough. If fundraiser can predict the final pledge amount of a project and know how much the predicted pledge amount higher than the funding goal, they will gain more insight. If the predicted pledge amount of a project is much higher than the funding goal, a project is much likely going to be popular with the market, and fundraisers will gain more confident to input more resources into project development. On the other hand, if the predicted pledge amount of a project is below the funding goal but near, fundraisers will still have opportunities to improve their projects and make it succeed.
  
To predict the success status and the final pledge amount of a launched project, I apply a machine learning method, Stacking, to make prediction. It is an Ensemble Learning technique typically by voting, averaging or using a meta-level-classifier (Sikora, Riyaz and Al-laymoun, O'la Hmoud, 2014). It can be used to overcome three types of problems which are suffered from base learning algorithms: the statistical problem; the computational problem; and the representational problem (Thomas G. Dietterich, 2000). Experimental evidence in Freund and Schapire (1996) and other studies summarized in Dietterich (1997) have shown that ensemble methods are often much more accurate than any base learning algorithms (M.A. Arbib, Ed., 2002).
#  
### Dataset
The records respectively from Kickstarter and Indeigogo occupy 55.89% and 44.11% of the whole dataset. The number of successful projects is accounting for 36.02% of total projects while the number of failed projects is around 63.98% of total projects. The average amount of pledge is 11900 US dollars, the average amount of goal is 31500 US dollars. There are six columns for each project in the dataset, which are status, category, location, backers, goal_usd and pledge_usd. TABLE I and TABLE II describe detailed data information.
TABLE I. DATA TYPE AND DESCRIPTION OF EACH COLUMN
<p align="left">
  <img src="https://github.com/albert0796/MachineLearning/blob/master/Paper_CrowdFunding/data/DATA%20TYPE%20AND%20DESCRIPTION%20OF%20EACH%20COLUMN.png)https://github.com/albert0796/MachineLearning/blob/master/Paper_CrowdFunding/data/DATA%20TYPE%20AND%20DESCRIPTION%20OF%20EACH%20COLUMN.png" width = "200" height = "100">
<p>


