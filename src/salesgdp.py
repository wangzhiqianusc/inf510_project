#!/usr/bin/env python
# coding: utf-8

# In[ ]:


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
    year = [2016,2017,2018,2019]

#figsize=(10, 6)
    fig, ax1 = plt.subplots(figsize = (10, 5), facecolor='white')
    ax1.plot(year,sales, color='g', alpha=0.5)
    ax1.set_xlabel('year')
    ax1.set_ylabel('resuaurant sales')

    ax2 = ax1.twinx()
    ax2.plot(year, newlist, '-or')
    ax2.set_ylabel('GDP of United States')
    ax2.set_ylim(18000000,22000000)

