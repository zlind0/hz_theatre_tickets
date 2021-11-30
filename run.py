#!/usr/bin/env python
# coding: utf-8

# In[86]:


import requests, json
import datetime


# In[64]:


def get_season_shows():
    params = (
        ('sorts', '{"order_index":"desc","metaShowStartAt":"asc"}'),
        ('skip', '0'),
        ('limit', '10'),
        ('checkSaleSchedule', 'true'),
        ('metas', '["location","startTime","coverImage","attribute","activityId","minmax","rangePicker","discountApplyType","MZId","locationAdress"]'),
        ('filter', '{"categories":["\u7231\u4E50\u4E50\u5B63"],"cateIsAlias":"true","status":["publish"],"excludedCates":["\u62DB\u5546\u94F6\u884C","\u4F7F\u7528\u60A6\u4EAE\u5361","\u4F7F\u7528\u4EBA\u624D\u5361","\u4E13\u62CD\u94FE\u63A5","\u4F7F\u7528\u60A6\u513F\u5361","\u4F7F\u7528\u6B21\u5361"],"location":"\u676D\u5DDE\u5927\u5267\u9662"}'),
        ('metaFilter', '[]'),
    )

    response = requests.get('https://c-api-prod.nase.tech/hzdjy/api/v0/post/list', params=params)
    return json.loads(response.text)

def get_ticket_id(show_id):
    headers = {
        'Host': 'c-api-prod.nase.tech',
        'sid': 'bc7a7ca0-51e4-11ec-9a69-6dc3de3cb7f3',
        'content-type': 'application/json; charset=utf-8',
        'Authorization': 'SESS d88bb0fe777df26f1db162fc60edd5bf130bf899b87df66c946439b30fd04527',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.15(0x18000f2e) NetType/WIFI Language/zh_CN',
        'Referer': 'https://servicewechat.com/wxbf5f2e9c0e7d7938/161/page-frame.html',
    }

    params = (
        ('postId', show_id),
        ('isMzOrder', 'false'),
        ('status', '["normal"]'),
        ('checkSaleSchedule', 'true'),
        ('skip', '0'),
        ('limit', '100'),
        ('sorts', '{"startAt":"asc"}'),
    )

    response = requests.get('https://c-api-prod.nase.tech/hzdjy/api/v0/schedule/list', headers=headers, params=params)
    tktid=json.loads(response.text)
    return [m['id'] for m in tktid['data']]
    
def get_avail_tickets(ticket_id):
    headers = {
        'Host': 'c-api-prod.nase.tech',
        'sid': 'bc7a7ca0-51e4-11ec-9a69-6dc3de3cb7f3',
        'content-type': 'application/json; charset=utf-8',
        'Authorization': 'SESS d88bb0fe777df26f1db162fc60edd5bf130bf899b87df66c946439b30fd04527',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.15(0x18000f2e) NetType/WIFI Language/zh_CN',
        'Referer': 'https://servicewechat.com/wxbf5f2e9c0e7d7938/161/page-frame.html',
    }

    params = (
        ('isMzOrder', 'false'),
    )

    response = requests.get(f'https://c-api-prod.nase.tech/hzdjy/api/v0/schedule/{ticket_id}', headers=headers, params=params)
    return json.loads(response.text)


# In[77]:


season_shows=get_season_shows()


# In[84]:


show_data=[]
for show in season_shows['data']:
    _data={}
    _data['id']=show['id']
    _data['title']=show['title']
    _data['time']={i['key']:i['value'] for i in show['metas']}['startTime']
    _data['ticket_id']=get_ticket_id(_data['id'])
    _data['ticket']=[]
    for tid in _data['ticket_id']:
        tkt=get_avail_tickets(tid)
        for p in tkt['data']['price']:
            sign='[X]'
            if p['stock']>0: sign='[!]'
            if p['stock']>20: sign='[√]'
            res=f"{sign}{p['price']}元:余{p['stock']}/售{p['sold']}/总{p['count']}"
            _data['ticket'].append(res)
    show_data.append(_data)


# In[89]:


print("数据获取时间",datetime.datetime.now())
for s in show_data:
    print('-----------------------')
    print(s['title'])
    print('时间：',s['time'])
    print('\n'.join(s['ticket']))


# In[ ]:





# In[ ]:




