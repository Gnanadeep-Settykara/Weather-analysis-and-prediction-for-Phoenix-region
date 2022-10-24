#### SER594: Exploratory Data Munging and Visualization
#### Title: Weather Prediction
#### Author: Gnanadeep Settykara
#### Date: 10/22/2022

## Basic Questions
**Dataset Author(s):** GHCN (Global Historical Climatology Network)-Daily, National Centers for Environmental Information (NCEI) 

Link- https://www.ncei.noaa.gov/access/services/data/v1/?dataset=daily-summaries&dataTypes=WT03,WT04,WV03,WT05,WSFM,WT06,WT07,WT08,WV07,WT09,WDF1,WDF2,WDF5,WT10,PGTM,WT11,WT13,FRGT,WSF2,FMTM,ACMH,WSF5,SNOW,ACMC,TOBS,WSF1,WSFG,WT01,WESD,WSFI,WT02,GAHT,PRCP,SNWD,TMAX,WDFG,WT14,ACSH,WT16,ACSC,WT18,AWND,WT21,WV20,WDFI,PSUN,TAVG,TMIN,WDFM,TSUN&stations=USW00023183&startDate=1933-06-01&endDate=2022-10-16&boundingBox=90,-180,-90,180&units=standard&includeStationName=true

**Dataset Construction Date:** 2012 ( Note: The dataset was initially constructed in 2012, with historical data starting from June 1933, and it is being updated since then.)

**Dataset Record Count:** 30753

**Dataset Field Meanings:** Actually there are 53 fields in the dataset, out of which only "5" fields are the core elements. (This is described in the GHCN- Daily documentation, refer the document added in the data_original folder.)
PRCP = Precipitation (mm or inches), it is the amount of rainfall detected on a given day near Phoenix Airport, Arizona
SNOW = Snowfall (mm or inches), it is the amount of snowfall recorded on a given day near Phoenix Airport, Arizona
SNWD = Snow depth (mm or inches), it is the thickness of snowfall on the ground in mm or inches on a given day near Phoenix Airport, Arizona
TMAX = Maximum temperature (Fahrenheit or Celsius), it is the maximum temperature recorded on a given day near Phoenix Airport, Arizona
TMIN = Minimum temperature (Fahrenheit or Celsius), it is the minimum temperature recorded on a given day near Phoenix Airport, Arizona

**Dataset File Hash(es):** For original Dataset MD5 checksum- 6ff2eb05e732ccfaea05e6a748f50e8c

## Interpretable Records
### Record 1
**Raw Data:** (Row) 18954 (Date) 26-06-1990 (Precipitation)	0 (Snow) 0 (Temp_max) 122 (Temp_min) 91 (Weather) Sweltering


Interpretation:** Over the period from 1933 to 2022, we can observe that maximum temperature is recorded on this given date which is 122 F. It can be observed that the date falls in the month of june, which might be the peak time of the summer. Also, a week before and after this date recorded similar high temperatures. 

### Record 2
**Raw Data:** (Row) 30467 (Date) 02-01-2022 (Precipitation)	0 (Snow) 0 (Temp_max) 59 (Temp_min) 36 (Weather) Cool


**Interpretation:** During this date, the minimum temperature recorded is 36 F. The given date falls in the month of january, which is during the winter and it can be observed that similar temperatures were recorded in the nearby days.

## Data Sources
### Transformation 1
**Description:** In the dataset, there are 53 fields initially, but only five of them were core elements (described in the documentation attached in the data_original folder). So, I only considered those 5 fields and removed all other columns.

**Soundness Justification:** All other fields are either not recorded properly or not useful. ( As per the official documentation from GHCN)

### Transformation 2
**Description:** In the dataset, after retaining only the important fields. I removed all the NaN/null values present in the data. I also dropped the Snow_depth column as all the values in it are zeroes.

**Soundness Justification:** By using the fillna(0), I filled the missing data present in the precipitation and snow columns. For, the temp_max and temp_min columns, I used the ffill method to fill the missing values.

### Transformation 3
**Description:** I included a new categorical variable "weather" into to the dataset, by using the temp_max and temp_min columns.

**Soundness Justification:** By using the bins and labels, I created labels for the data and added them to the weather columnn.

## Visualization
### Visual 1
**Analysis:** This is the scatterplot between snow and precipitation. It shows almost no correlation between the variables.

### Visual 2
**Analysis:** This is the scatterplot between max temperature and precipitation. It shows negative correlation between the variables.
### Visual 3
**Analysis:** This is the scatterplot between snow and max temperature. It shows negative correlation between the variables.
### Visual 4
**Analysis:** This is the scatterplot between min temperature and precipitation. It shows negative correlation between the variables.
### Visual 5
**Analysis:** This is the scatterplot between snow and min temperature. It shows negative correlation between the variables.
### Visual 6
**Analysis:** This is the scatterplot between max and min temperatures. It shows high correlation between the two columns.
### Visual 7
**Analysis:** This is the histogram between the frequency and weather. It shows how many hot,sweltering, warm and cool days occured over the given period of time from 1933 to 2022.

