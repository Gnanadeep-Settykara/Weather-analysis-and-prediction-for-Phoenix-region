#Prediction
#!/usr/bin/env python
import pickle
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge
from sklearn.linear_model import ElasticNet

linear_reg= pickle.load(open("models/linear_regression.pkl","rb"))
ridge_reg= pickle.load(open("models/ridge_regression.pkl","rb"))
lasso_reg= pickle.load(open("models/lasso_regression.pkl","rb"))
elastic_reg= pickle.load(open("models/enet_regression.pkl","rb"))
x_test = pd.read_csv("models/x_test.csv",index_col='DATE')
y_test = pd.read_csv("models/y_test.csv",index_col='DATE')


lrp= linear_reg.predict(x_test)
rrp= ridge_reg.predict(x_test)
larp= lasso_reg.predict(x_test)
erp= elastic_reg.predict(x_test)
#print("(Linear Regression) Prediction on test set:",lrp)
#print("(Ridge Regression) Prediction on test set:",rrp)
#print("(Lasso Regression) Prediction on test set:",larp)
#print("(ElasticNet Regression) Prediction on test set:",erp)


a= float(input("enter precipitation value:"))
b= int(input("enter max temp value:"))
c= int(input("enter min temp value:"))
inp= [[a,b,c]]
x= linear_reg.predict(inp)
y= ridge_reg.predict(inp)
z= lasso_reg.predict(inp)
w= elastic_reg.predict(inp)
print("(Linear Regression) Predicted Temperature:",x[0][0],"F")
print("(Ridge Regression) Predicted Temperature:",y[0][0],"F")
print("(LASSO Regression) Predicted Temperature:",z[0],"F")
print("(ElasticNet Regression) Predicted Temperature:",w[0],"F")


'''

x= linear_reg.predict(np.array[inp])
y= ridge_reg.predict(np.array[inp])
z= lasso_reg.predict(np.array[inp])    
print("(Linear Regression) Prediction on test set:",x)
print("(Ridge Regression) Prediction on test set:",y)
print("(Lasso Regression) Prediction on test set:",z)
'''
