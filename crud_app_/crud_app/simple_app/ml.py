import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
# %matplotlib inline
from statsmodels.tsa.stattools import adfuller
from pandas.plotting import autocorrelation_plot
import statsmodels.api as sm
from statsmodels.graphics.tsaplots import plot_acf,plot_pacf
from pandas.tseries.offsets import DateOffset
from statsmodels.tsa.arima.model import ARIMA


def process(df):
    # df=pd.read_csv('perrin-freres-monthly-champagne-.csv')
    df.columns=["Month","Sales"]
    df.drop(106,axis=0,inplace=True)
    df.drop(105,axis=0,inplace=True)

    # Convert Month into Datetime
    df['Month']=pd.to_datetime(df['Month'])

    df.set_index('Month',inplace=True)

    ### Testing For Stationarity
    test_result=adfuller(df['Sales'])

    #Ho: It is non stationary
    #H1: It is stationary



    commentlist=[]
    def adfuller_test(sales,char):
        result=adfuller(sales)
        commentdict={}
        commentdict['Name']=char
        labels = ['ADF Test Statistic','p-value','#Lags Used','Number of Observations Used']
        for value,label in zip(result,labels):
            commentdict[label]=str(value)
            # print(label+' : '+str(value) )
        if result[1] <= 0.05:
            commentdict['Comment']="strong evidence against the null hypothesis(Ho), reject the null hypothesis. Data has no unit root and is stationary"
            # print("strong evidence against the null hypothesis(Ho), reject the null hypothesis. Data has no unit root and is stationary")
        else:
            commentdict['Comment']="weak evidence against null hypothesis, time series has a unit root, indicating it is non-stationary "
            # print("weak evidence against null hypothesis, time series has a unit root, indicating it is non-stationary ")
        commentlist.append(commentdict)
        
    adfuller_test(df['Sales'],'Sales')
    df['Sales First Difference'] = df['Sales'] - df['Sales'].shift(1)
    df['Sales'].shift(1)

    df['Seasonal First Difference']=df['Sales']-df['Sales'].shift(12)

    ## Again test dickey fuller test
    adfuller_test(df['Seasonal First Difference'].dropna(),"Seasonal First Difference")



    autocorrelation_plot(df['Sales'])

    # fig = plt.figure(figsize=(12,8))
    # ax1 = fig.add_subplot(211)
     # fig = sm.graphics.tsa.plot_acf(df['Seasonal First Difference'].iloc[13:],lags=40,ax=ax1)
    # ax2 = fig.add_subplot(212)
    # fig = sm.graphics.tsa.plot_pacf(df['Seasonal First Difference'].iloc[13:],lags=40,ax=ax2)

    model=ARIMA(df['Sales'],order=(1,1,1))
    model_fit=model.fit()

    df['forecast']=model_fit.predict(start=90,end=103,dynamic=True)

    model=sm.tsa.statespace.SARIMAX(df['Sales'],order=(1, 1, 1),seasonal_order=(1,1,1,12))
    results=model.fit()

    df['forecast']=results.predict(start=90,end=103,dynamic=True)

    future_dates=[df.index[-1]+ DateOffset(months=x)for x in range(0,24)]

    future_datest_df=pd.DataFrame(index=future_dates[1:],columns=df.columns)
    future_df=pd.concat([df,future_datest_df])

    x=future_df['Sales']
    y=future_df['forecast']
    
    

    return commentlist 