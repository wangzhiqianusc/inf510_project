#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def grab_data_from_downloaded_raw_files(restaurant_dir,yelp_dir,stategdp_dir,citycoor_dir):
    with open(stategdp_dir) as f:
        for line in f:
            stategdp_raw_data = json.loads(line)
            data = stategdp_raw_data['BEAAPI']['Results']['Data']
            df_stategdp = pd.DataFrame(data)
            
    restaurantDataFrame = pd.read_csv(restaurant_dir) 
    df_yelp = pd.read_csv(yelp_dir) 
    df_citycoor = pd.read_csv(citycoor_dir)
    return df_stategdp,df_yelp,restaurantDataFrame,df_citycoor

