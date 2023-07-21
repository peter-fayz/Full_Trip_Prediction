# Full_Trip_Prediction

![Project Logo](https://github.com/peter-fayz/Full_Trip_Prediction/assets/138496693/54182e40-fbcd-4561-afc3-4fa860251431)

## Introduction

Full_Trip_Prediction is a machine learning project that aims to predict the percentage of orders that will be restocked using data exported from Shopify. The project utilizes historical orders data to train a predictive model that can provide insights into inventory management and restocking decisions. This will save extra shipping costs and save a lot of time to return products to stock and prioritize the required orders

## Dataset

The dataset used in this project consists of historical order information exported from the Shopify platform. It includes features such as order date, product details, quantities sold, and whether an item was restocked after being sold out. The data will be pre-processed to extract relevant features and create the target variable for prediction.

## Installation

To run this project, you need Python 3 and the following dependencies:

- pandas
- scikit-learn
- plotly
- Dash
- numpy

You can install the required dependencies using the following command:

```bash
pip install pandas scikit-learn plotly Dash numpy
```

## Model

The machine learning model used in this project is a classification model to predict the percentage of orders that will be restocked. We will explore and experiment with different classification algorithms, such as Logistic Regression, Random Forest classification, and Gradient Boosting classification, to determine the best performing model.

### Feature Engineering

To improve the model's performance, we will conduct feature engineering on the dataset. This may include creating new features from existing ones, scaling or normalizing numerical features, and encoding categorical variables appropriately.

### Model Training

The dataset will be split into training and testing sets to train and evaluate the model's performance. We will use the training data to fit the chosen classification algorithm and adjust hyperparameters to achieve the best results. Cross-validation will be used to assess the model's robustness and reduce overfitting.

### Model Evaluation

The model's performance will be evaluated using various classification metrics, accuracy score, confusion matrix and classification report. We will also visualize the predicted values compared to the actual restock percentages to gain insights into the model's accuracy.

### Model Deployment

Once the best-performing model is identified, we will deploy it in a production environment, allowing users to make restock predictions based on their historical order data. The deployment may involve creating a web application or API to facilitate predictions on-demand.

We aim to strike a balance between model complexity and interpretability to ensure the predictive model provides meaningful insights and valuable predictions for inventory management decisions.
