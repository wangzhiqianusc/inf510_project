#!/usr/bin/env python
# coding: utf-8

# In[ ]:
import pandas as pd
import matplotlib.pyplot as plt

def countandgdp(df_citycoor,df_stategdp,restaurcnt):
#df_stategdp
#city and their states
    citylist = ['Denver','Dallas','Atlanta','Boston','Minneapolis','Philadelphia','San Francisco','Portland','San Diego','Charlotte','Cincinnati','Cleveland','Columbus','Detroit','Indianapolis','Kansas City','Miami','Orlando','Phoenix','Pittsburgh','Riverside','Sacramento','San Antonio','St. Louis','Tampa']+['New York City', 'Los Angeles', 'Chicago', 'Houston']
    citystate = df_citycoor[df_citycoor['City'].isin(citylist)]
#print(citystate)
#gdp 2018 in these states
#print(df_stategdp)
    #df_stategdp.to_csv('stategdp.csv')
    selectedstategdp = df_stategdp[df_stategdp['GeoName'].isin(citystate['State'])]
    gdp2018 = selectedstategdp.loc[selectedstategdp["TimePeriod"] == '2018']
#city restaurant number
    df_vis3 = pd.merge(citystate,gdp2018, left_on='State',right_on = 'GeoName')
#print(restaurcnt)
    dfvis3 = pd.merge(df_vis3,restaurcnt, left_on='City',right_on = 'city')
#print(dfvis3)
    dfvis3['DataValue'] = dfvis3['DataValue'].map(lambda x:(float(x[:-10]+x[-9:-6]+x[-5:])))

    dfvis3.set_index('City_x').plot.scatter(x='count', y='DataValue')

