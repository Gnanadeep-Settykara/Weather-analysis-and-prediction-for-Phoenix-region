#### SER594: Experimentation
#### (title) Weather analysis and prediction for Phoenix Region 
#### (author) Gnanadeep Settykara
#### (date) 11/21/2022


## Explainable Records
### Record 1
**Raw Data:** 
DATE		Precipitation   snow	snow_depth	Temp_max	Temp_min  Weather
21-08-1933	  0.01	     0	   0		 102		 77	    Sweltering


Prediction Explanation:** For this record, the predicted value obtained through Linear regression is 101.4961215 F, which is pretty close to the actual temperature of the day 102 F, this output seems valid because, on a day with maximum temperature of 102F, and minimum temperature of 77F, it seems pretty legit that the day's temperature will be somewhere between those values and also the date falls in the month of june, which is summer and it sees the most hot and sweltering days in Phoenix, Arizona region. 


### Record 2
**Raw Data:** 
DATE		Precipitation   snow	snow_depth	Temp_max	Temp_min  Weather
03-03-1983	 1.98		    0	     	  0		60		 52	    Cool


Prediction Explanation:** For this record, the predicted value obtained through Linear regression is 59.00156678 F, which is pretty close to the actual temperature of the day 58 F, this output seems valid because, on a day with maximum temperature of 60F, and minimum temperature of 52F, it seems pretty legit because, with precipitation of 1.98 inch, and temperatures between 60 and 52F, the day seems cool. Also, the date falls in the month of march, which remains cool in the Phoenix, Arizona region.

## Interesting Features
### Feature A
**Feature:** Precipitation

**Justification:** 'Precipitation' feature is the rainfall occured on a day. It affects the temperature/weather of the day in a way that if the precipitation increases, the temperature of the day decreases and vice-versa. This seems pretty straight forward as rainfall usually cools the weather.

### Feature B
**Feature:** Temp_max

**Justification:** 'Temp_max' feature is the maximum temperature recorded on a day. Weather generally depends on the maximum and minimum temperatures of the day. IF the max temperature of the day is high, then the probability that the weather/ overall temperature of the day is hot/high.

## Experiments 
### Varying A
**Prediction Trend Seen:** If 'precipitation'/ A is increased, then the predicted temperature decreased. Example: I took precipitation value '2' for the #record 2 (Temp_max=60, Temp_min=52) as mentioned above, the output became 58.9721 F from 59.0015 F. Similarly, if the 'precipiation' value decreases, then the predicted temperature increases. Ex: If 'A'=1.5 for record 2 as mentioned above, the predicted temperature became 59.7065 F	

### Varying B
**Prediction Trend Seen:** If 'Temp_max'/ B is increased, then the predicted temperature increased. Example: I took Temp_max value '65' for the #record 2 (precipitation=1.98, Temp_min=52) as mentioned above, the output became 63.5751 F from 59.0015 F. Similarly, if the 'Temp_max' value decreases, then the predicted temperature decreases. Ex: If 'B'=55 for record 2 as mentioned above, the predicted temperature became 54.4280 F

### Varying A and B together
**Prediction Trend Seen:** If both A and B features are increased, then the predicted value increased. Example: I took 'A'=2, 'B'=65 keeping Temp_min=52 (as from #record 2 above), the output became 63.54575 F. Similarly, if both A and B are decreased, the output decreased. Ex: If 'A'=1.5, 'B'=55, keeping Temp_min=52, the output became 55.1329 F from 59.0015 F.


### Varying A and B inversely
**Prediction Trend Seen:** If A and B are varied inversly, then the output is depending on B feature.i.e., if 'A' is increased and 'B' is decreased, the predicted value decreased and vice-versa. Example: If 'A'=2, 'B'=55 keeping Temp_min=52 ( values are varied as from #record 2, Here 'A' increased, 'B' decreased) the output became 54.3986 F from 59.0015 F

