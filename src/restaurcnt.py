#!/usr/bin/env python
# coding: utf-8

# In[ ]:
import pandas as pd

def restaurcnt(df_yelp,df_citycoor):
    for restaurant in ["McDonald's",'Starbucks','Subway','Taco Bell','Chick-fil-A','Burger King',"Wendy's","Dunkin'","Domino's Pizza",'Panera Bread','Pizza Hut','Chipotle Mexican Grill','Sonic Drive-In','KFC',"Applebee's Grill + Bar",'Olive Garden Italian Restaurant',"Arby's",'Little Caesars','Buffalo Wild Wings','Dairy Queen']:
        restaurcnt = df_yelp[df_yelp['name']==restaurant].groupby('city').size().reset_index()
        restaurcnt.rename(index = str, columns={0:"count"}, inplace = True)
        #find cities in citycoor dataframe and add the latitude and longitude to restaurcnt
        restaurcnt = pd.merge(restaurcnt,df_citycoor, left_on='city',right_on = 'City',how ='left')
    return restaurcnt

