#!/usr/bin/env python
# coding: utf-8

# In[ ]:
import pandas as pd
import matplotlib.pyplot as plt

def salesgdp(df_restaurant,df_stategdp):
#df_restaurant
#restaurant sales through different years and GDP through different years
# $ to integer
    newlist = []
    for sales in df_restaurant['sales'].values.tolist():
        if len(sales) < 9: 
            if sales[-1] == '*':
                newlist.append(int(sales[1:-5]+sales[-4:-1]))
            else:
                newlist.append(int(sales[1:-4]+sales[-3:]))
        else:
            if sales[-1] == '*':
                newlist.append(float(sales[1:-9]+sales[-8:-5]+'.'+sales[-4:-1]))
            else:
                newlist.append(float(sales[1:-8]+sales[-7:-4]+'.'+sales[-3:]))
    df_restaurant['sales'] = newlist
    #print(df_restaurant)

#calculate sales in each year
    df_sales = df_restaurant['sales'].groupby(df_restaurant['year']).sum()
    sales = df_sales.tolist()
#print(df_sales)

#gdp
#print(df_stategdp)
    us_gdp = df_stategdp.loc[df_stategdp["GeoName"] == "United States*"].head()['DataValue']
    gdp = us_gdp.tolist()
    print(gdp)
    newlist = []
    for num in gdp:
        newlist.append(float(num[:-10]+num[-9:-6]+num[-5:]))
    newlist.append(21500000)
    print(newlist)
    year = ["2016",'2017','2018','2019']

    fig, ax1 = plt.subplots(figsize = (10, 5), facecolor='white')
    plt.title("Sales of fast food industry and GDP of United States: 2016-2019")
    ax1.plot(year,sales, '-or', color='g',label = 'restaurant sales')
    ax1.set_xlabel('year')
    ax1.set_ylabel('resuaurant sales')
    ax1.set_xticks([2016,2019,1])
    
    plt.legend()

    ax2 = ax1.twinx()
    ax2.plot(year, newlist, '-or', alpha=0.5,label = 'GDP of United States')
    ax2.set_ylabel('GDP of United States')
    ax2.set_ylim(18000000,22000000)
    
    plt.legend()
