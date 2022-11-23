#### SER594: Machine Learning Evaluation
#### (title) Weather analysis and prediction for Phoenix Region 
#### (author) Gnanadeep Settykara
#### (date) 11/21/2022

## Evaluation Metrics
### Metric 1
**Name:** Mean Absolute Error (MAE)

**Choice Justification:** The mean absolute error adds the errors in absolute value, in order to prevent the negative differences from canceling out the positive differences and averaging them out. The changes in MAE, in contrast to RMSE, are linear. I think it helps for my problem as it is regression, because I can find the difference between predicted temperature and actual temperature of a particular day using this metric.

Interpretation:** The MAE for the models I used is around 3.5 (in Fahrenheit), which is relatively less deviating from actual value.

### Metric 2
**Name:** Root Mean Square Error (RMSE)

**Choice Justification:** For the RMSE, the difference between the forecast and the actual value is the error, which is squared. It then sums them up and finds the square root of that mean. Double transformations have two effects: they increase the importance of larger errors and prevent positive and negative errors from canceling one other out since they all become positive. I think it helps for my problem as it is regression, because I can find the difference between predicted temperature and actual temperature of a particular day using this metric.

Interpretation:** The RMSE for the models I used is around 4.7 (in Fahrenheit), which is relatively less difference.

### Metric 3
**Name:** Mean Square Error (MSE)

**Choice Justification:**MSE is determined by taking the observed value, and subtracting the predicted value, then square the result for all values. The total of all of these squared values should then be divided by the total number of observations. I think it helps for my problem as it is regression, because I can find the difference between predicted temperature and actual temperature of a particular day using this metric.

Interpretation:** The MSE for the models I used is around 22.1 (in Fahrenheit), which is less difference in terms of celsius.


#Base Model: Linear Regression

## Alternative Models
### Alternative 1 Ridge Model
**Construction:** Ridge regression is an advancement of linear regression in which the loss function is changed to reduce the model's complexity. A penalty parameter that is equal to the square of the coefficients' magnitude is added to the model to make this adjustment. Alpha is the parameter we must choose for the loss function. A high alpha value can cause under-fitting whereas a low alpha value might cause over-fitting. I used alpha value 0.05 for this model.

**Evaluation:** Ridge Regression:(alpha=0.05)
MSE: 22.122111485549443 
MAE:3.5081621797287688 
RMSE:4.703414874912635

## Alternative Models
### Alternative 2 LASSO Model
**Construction:** LASSO modifies the loss function to reduce model complexity by restricting the sum of the absolute values of the model coefficients. I used the alpha value of 0.05 for this model.

**Evaluation:** LASSO Regression:(alpha=0.05)
MSE: 22.180968067445317 
MAE:3.5165656563677916 
RMSE:4.709667511347836


## Alternative Models
### Alternative 3 ElasticNet Model
**Construction:** ElasticNet combines the characteristics of both the Ridge and Lasso regression methods. The ElasticNet class is used in scikit-learn to build an ElasticNet regression model. I used alpha value 0.05 in this model as well. 

**Evaluation:** Elastic Regression:(alpha=0.05)
MSE: 22.180260738646943 
MAE:3.516331725186546 
RMSE:4.709592417465331


## Best Model

**Model:** Linear Regression is the best model among all the models, because it is giving the least error values (MSE, MAE, RMSE), and among the alternative models to linear Regression, Ridge is the best performing model by looking at the values of the metrics. Ridge model metrics are almost similar to those of linear regression model, varying slightly. 