# Ecommerce-Churn-Prediction
**Author:** [@harshpx](https://github.com/harshpx)

## Overview
This Project is based on 2 Machine Learning Classification models:
* Customer churn predictor
* Customer satisfaction analyzer

for an E-commerce SAAS Company.


***Technologies used:*** Python, Scikit-Learn, Streamlit.

#### To see this app working live: 
Hop onto: [https://ecommerce-churn-prediction.streamlit.app/](https://ecommerce-churn-prediction.streamlit.app/)


#### To run this project on your local system: 
To deploy this project locally, first make sure you have all dependencies installed. *see ```requirements.txt```*

And Run: ```streamlit app.py``` or ```python3 -m streamlit app.py``` in the terminal of file directory.


## Brief Project Description
This Machine Learning model uses customer data of an E-Commerce SAAS Company. 
It uses ```XGBClassifier``` model for customer churn prediction and customer satisfaction analysis.

### Model's Description

1. **Churn Detection**
This is a binary classification model and uses XGBClassifier
Classification accuracy Achieved: 98%

2. **Satisfaction Analysis**
This is a multiclass classification model, that predicts satisfaction score of a customer based on given data.
Satisfaction score lies in the range of 1-5 (higher the better).
Classification accuracy achieved: 70%

The overall project UI is created and deployed using Streamlit API.

## Challenges
Most challenging aspect of the this project was data collection.
It is extremely essential for a good model to start with a good dataset, as training with incorrect data might lead to an improper model, and that can be fatal when finances are at stake. Therefore data integrity is extremely necessary for these projects.

## Practical application and Scope
Using previous customer data in order to better understand customer's needs is very essential for the growth of a profit-oriented company.
Hence with the help of Machine learning and Data Science approaches, we can you technology to scale our business and increase our profits.

This project is also a step in that direction.

The analysis of customer churn, helps the company to take constructive decisions for better sereve their customers.
