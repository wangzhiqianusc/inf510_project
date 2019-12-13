#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def yelpdataorganize2(city):
    newlist = []
    df = pd.DataFrame(columns = ['address','city','name','rating','review_count'])
    #print(city[0])
    try:
        #print(city[0])
        newdict = city[0]['businesses']
    except KeyError:
        newdict = city[1]['businesses']
    for dic in city:
        if 'businesses' in dic.keys():
            for restaurant in dic['businesses']:
                df = df.append(pd.DataFrame({'address': restaurant['location']['address1'],'city':restaurant['location']['city'],'name':restaurant['name'],'rating':restaurant['rating'],'review_count':restaurant['review_count']},index=[0]))
    return df

