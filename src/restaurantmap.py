#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def restaurantmap(df_yelp,df_citycoor):
    latitude = 39.0902
    longitude = -95.7129
    yelp_map = folium.Map(location=[latitude, longitude], zoom_start=4)

    for restaurant in ["McDonald's",'Starbucks','Subway','Taco Bell','Chick-fil-A','Burger King',"Wendy's","Dunkin'","Domino's Pizza",'Panera Bread','Pizza Hut','Chipotle Mexican Grill','Sonic Drive-In','KFC',"Applebee's Grill + Bar",'Olive Garden Italian Restaurant',"Arby's",'Little Caesars','Buffalo Wild Wings','Dairy Queen']:
        restaurcnt = df_yelp[df_yelp['name']==restaurant].groupby('city').size().reset_index()
        restaurcnt.rename(index = str, columns={0:"count"}, inplace = True)
        colordict = {0: 'lightblue', 1: 'lightgreen', 2: 'orange', 3: 'red'}
        feature_group = FeatureGroup(name=restaurant,show = False)
        #find cities in citycoor dataframe and add the latitude and longitude to restaurcnt
        restaurcnt = pd.merge(restaurcnt,df_citycoor, left_on='city',right_on = 'City',how ='left')
        for lat, lon, count, city in zip(restaurcnt['latitude'], restaurcnt['longitude'], restaurcnt['count'], restaurcnt['city']):
            folium.CircleMarker(
                [lat, lon],
                radius=.4*count,
                popup = ('City: ' + str(city).capitalize() + '<br>'
                         'Count of restaurant: ' + str(count) + '<br>'
                        ),
                color='b',
                key_on = count,
                threshold_scale=[0,1,2,3],
                #fill_color=colordict[],
                fill=True,
                fill_opacity=0.7
                ).add_to(feature_group)
        feature_group.add_to(yelp_map)

    folium.LayerControl(collapsed=False).add_to(yelp_map)       
    return yelp_map

