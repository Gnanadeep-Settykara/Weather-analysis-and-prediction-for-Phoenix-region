#!/usr/bin/env python
#TRAINING
import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge
from sklearn.linear_model import ElasticNet


x_train = pd.read_csv("data_processed/x_train.csv",index_col='DATE')
x_test = pd.read_csv("data_processed/x_test.csv",index_col='DATE')
y_train = pd.read_csv("data_processed/y_train.csv",index_col='DATE')
y_test = pd.read_csv("data_processed/y_test.csv",index_col='DATE')

lr= LinearRegression()
lr.fit(x_train,y_train)

pickle.dump(lr, open('models/linear_regression.pkl', 'wb'))


rr= Ridge(alpha=0.05)
rr.fit(x_train,y_train)

pickle.dump(rr, open('models/ridge_regression.pkl', 'wb'))



lasso_r= Lasso(alpha=0.05)
lasso_r.fit(x_train,y_train)

pickle.dump(lasso_r, open('models/lasso_regression.pkl', 'wb'))


model_enet = ElasticNet(alpha=0.05)
model_enet.fit(x_train,y_train)

pickle.dump(model_enet, open('models/enet_regression.pkl', 'wb'))


