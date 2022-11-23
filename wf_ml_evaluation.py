
#Evaluation
import pandas as pd
import numpy as np
import pickle
import warnings
warnings.filterwarnings("ignore")
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,mean_absolute_error
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge
from sklearn.linear_model import ElasticNet


df = pd.read_csv("data_processed/weather_data_processed.csv",index_col='DATE')

del df['Snow']
del df['Snow_depth']
df["target"] = df.shift(-1)["Temp_max"]
df = df.iloc[:-1,:].copy()

X= df[["Precipitation", "Temp_max", "Temp_min"]]
Y= df['target']
x_train, x_test,y_train,y_test = train_test_split(X,Y,test_size =0.2,shuffle=False)

x_train.to_csv('data_processed/x_train.csv')
x_test.to_csv('data_processed/x_test.csv')
y_train.to_csv('data_processed/y_train.csv')
y_test.to_csv('data_processed/y_test.csv')
x_train.to_csv('models/x_train.csv')
x_test.to_csv('models/x_test.csv')
y_train.to_csv('models/y_train.csv')
y_test.to_csv('models/y_test.csv')



#!/usr/bin/python
import wf_ml_training, wf_ml_prediction

#lr= LinearRegression()
#lr.fit(x_train,y_train)
#lrp= lr.predict(x_test)

l_mse= mean_squared_error(wf_ml_prediction.y_test, wf_ml_prediction.lrp)
l_mae= mean_absolute_error(wf_ml_prediction.y_test,wf_ml_prediction.lrp)
l_rmse= np.sqrt(l_mse)



# pickle.dump(lr, open('models/linear_regression.pkl', 'wb'))


#rr= Ridge(alpha=0.01)
#rr.fit(x_train,y_train)
#rrp= rr.predict(x_test)

r_mse= mean_squared_error(wf_ml_prediction.y_test, wf_ml_prediction.rrp)
r_mae= mean_absolute_error(wf_ml_prediction.y_test,wf_ml_prediction.rrp)
r_rmse= np.sqrt(r_mse)


# pickle.dump(rr, open('models/ridge_regression.pkl', 'wb'))



#lasso_r= Lasso(alpha=0.1)
#lasso_r.fit(x_train,y_train)
#larp= lasso_r.predict(x_test)

la_mse= mean_squared_error(wf_ml_prediction.y_test,wf_ml_prediction.larp)
la_mae= mean_absolute_error(wf_ml_prediction.y_test,wf_ml_prediction.larp)
la_rmse= np.sqrt(la_mse)




# pickle.dump(lasso_r, open('models/lasso_regression.pkl', 'wb'))

e_mse= mean_squared_error(wf_ml_prediction.y_test, wf_ml_prediction.erp)
e_mae= mean_absolute_error(wf_ml_prediction.y_test,wf_ml_prediction.erp)
e_rmse= np.sqrt(e_mse)


with open("evaluation/summary.txt", "w") as f:
        f.write("Linear Regression: ")
        
        f.write("MSE: ")
        f.write(str(l_mse))
        f.write(' MAE:')
        f.write(str(l_mae))
        f.write(' RMSE:')
        f.write(str(l_rmse))
        f.write("\n")
        
        f.write("Ridge Regression: ")
        
        f.write("MSE: ")
        f.write(str(r_mse))
        f.write(' MAE:')
        f.write(str(r_mae))
        f.write(' RMSE:')
        f.write(str(r_rmse))
        f.write("\n")

        f.write("LASSO Regression: ")

        f.write("MSE: ")
        f.write(str(la_mse))
        f.write(' MAE:')
        f.write(str(la_mae))
        f.write(' RMSE:')
        f.write(str(la_rmse))
        f.write("\n")

        f.write("Elastic Regression: ")

        f.write("MSE: ")
        f.write(str(e_mse))
        f.write(' MAE:')
        f.write(str(e_mae))
        f.write(' RMSE:')
        f.write(str(e_rmse))
        f.write("\n")       
        


