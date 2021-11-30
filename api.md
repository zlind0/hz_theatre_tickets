# 杭州大剧院查询、购票API

## 查询“爱乐乐季”演出

示例：

```
curl -H 'Host: c-api-prod.nase.tech' -H 'sid: bc7a7ca0-51e4-11ec-9a69-6dc3de3cb7f3' -H 'content-type: application/json; charset=utf-8' -H 'User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 15_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.15(0x18000f2e) NetType/WIFI Language/zh_CN' -H 'Referer: https://servicewechat.com/wxbf5f2e9c0e7d7938/161/page-frame.html' --compressed 'https://c-api-prod.nase.tech/hzdjy/api/v0/post/list?sorts=%7B%22order_index%22%3A%22desc%22%2C%22metaShowStartAt%22%3A%22asc%22%7D&skip=0&limit=10&checkSaleSchedule=true&metas=%5B%22location%22%2C%22startTime%22%2C%22coverImage%22%2C%22attribute%22%2C%22activityId%22%2C%22minmax%22%2C%22rangePicker%22%2C%22discountApplyType%22%2C%22MZId%22%2C%22locationAdress%22%5D&filter=%7B%22categories%22%3A%5B%22%E7%88%B1%E4%B9%90%E4%B9%90%E5%AD%A3%22%5D%2C%22cateIsAlias%22%3A%22true%22%2C%22status%22%3A%5B%22publish%22%5D%2C%22excludedCates%22%3A%5B%22%E6%8B%9B%E5%95%86%E9%93%B6%E8%A1%8C%22%2C%22%E4%BD%BF%E7%94%A8%E6%82%A6%E4%BA%AE%E5%8D%A1%22%2C%22%E4%BD%BF%E7%94%A8%E4%BA%BA%E6%89%8D%E5%8D%A1%22%2C%22%E4%B8%93%E6%8B%8D%E9%93%BE%E6%8E%A5%22%2C%22%E4%BD%BF%E7%94%A8%E6%82%A6%E5%84%BF%E5%8D%A1%22%2C%22%E4%BD%BF%E7%94%A8%E6%AC%A1%E5%8D%A1%22%5D%2C%22location%22%3A%22%E6%9D%AD%E5%B7%9E%E5%A4%A7%E5%89%A7%E9%99%A2%22%7D&metaFilter=%5B%5D'
```

附：解码结果

```
https://c-api-prod.nase.tech/hzdjy/api/v0/post/list?sorts={"order_index":"desc","metaShowStartAt":"asc"}&skip=0&limit=10&checkSaleSchedule=true&metas=["location","startTime","coverImage","attribute","activityId","minmax","rangePicker","discountApplyType","MZId","locationAdress"]&filter={"categories":["爱乐乐季"],"cateIsAlias":"true","status":["publish"],"excludedCates":["招商银行","使用悦亮卡","使用人才卡","专拍链接","使用悦儿卡","使用次卡"],"location":"杭州大剧院"}&metaFilter=[]
```

## 查询某场演出的余票

首先查到卖票ID

```
curl -H 'Host: c-api-prod.nase.tech' -H 'sid: bc7a7ca0-51e4-11ec-9a69-6dc3de3cb7f3' -H 'content-type: application/json; charset=utf-8' -H 'Authorization: SESS d88bb0fe777df26f1db162fc60edd5bf130bf899b87df66c946439b30fd04527' -H 'User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 15_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.15(0x18000f2e) NetType/WIFI Language/zh_CN' -H 'Referer: https://servicewechat.com/wxbf5f2e9c0e7d7938/161/page-frame.html' --compressed 'https://c-api-prod.nase.tech/hzdjy/api/v0/schedule/list?postId=11427&isMzOrder=false&status=%5B%22normal%22%5D&checkSaleSchedule=true&skip=0&limit=100&sorts=%7B%22startAt%22%3A%22asc%22%7D'
```

查到id字段填到下面的url里去。
```
curl -H 'Host: c-api-prod.nase.tech' -H 'sid: bc7a7ca0-51e4-11ec-9a69-6dc3de3cb7f3' -H 'content-type: application/json; charset=utf-8' -H 'Authorization: SESS d88bb0fe777df26f1db162fc60edd5bf130bf899b87df66c946439b30fd04527' -H 'User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 15_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.15(0x18000f2e) NetType/WIFI Language/zh_CN' -H 'Referer: https://servicewechat.com/wxbf5f2e9c0e7d7938/161/page-frame.html' --compressed 'https://c-api-prod.nase.tech/hzdjy/api/v0/schedule/2419?isMzOrder=false'
```

## 购票



```
curl -H 'Host: c-api-prod.nase.tech' -H 'sid: bc7a7ca0-51e4-11ec-9a69-6dc3de3cb7f3' -H 'content-type: application/json; charset=utf-8' -H 'Authorization: SESS d88bb0fe777df26f1db162fc60edd5bf130bf899b87df66c946439b30fd04527' -H 'User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 15_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.15(0x18000f2e) NetType/WIFI Language/zh_CN' -H 'Referer: https://servicewechat.com/wxbf5f2e9c0e7d7938/161/page-frame.html' --compressed 'https://c-api-prod.nase.tech/hzdjy/api/v0/order/ticket/calc?priceId=6852&count=1&isMzOrder=false&skipPolicyCheck=false'
```

