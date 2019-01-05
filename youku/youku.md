# 评论
评论 URL：
http://p.comments.youku.com/ycp/comment/pc/commentList?app=100-DDwODVkv&objectId=884389334&objectType=1&listType=0&currentPage=6&pageSize=30&sign=2056692c183efe4254a20c2e431946a3&time=1525611949

- objectId：视频 ID
- currentPage：评论当前页面
- pageSize：页面评论数量

**返回的数据**
```json
{
    "code": 0, 
    "data": {
        "sourceCommentSize": 629, 
        "totalSize": 837, 
        "totalPage": 21, 
        "pageSize": 30, 
        "comment": [
            {
                "atUsers": { }, 
                "flags": { }, 
                "upCount": 8, 
                "parentCommentId": 0, 
                "userId": 1155192313, 
                "content": "感觉最后会跟卢家凯在一起", 
                "downCount": 0, 
                "replyCount": 0, 
                "createTime": 1524649229889, 
                "userIsLiked": 0, 
                "parentComment": { }, 
                "id": 3409500200, 
                "user": {
                    "vipInfo": {}, 
                    "userLevel": 17, 
                    "avatarMiddle": "https://wwc.alicdn.com/avatar/getAvatar.do?userId=859825765&width=160&height=160&type=sns", 
                    "avatarLarge": "https://wwc.alicdn.com/avatar/getAvatar.do?userId=859825765&width=160&height=160&type=sns", 
                    "userName": "n小允", 
                    "userId": 1155192313, 
                    "userCode": "UNDYyMDc2OTI1Mg==", 
                    "avatarSmall": "https://wwc.alicdn.com/avatar/getAvatar.do?userId=859825765&width=160&height=160&type=sns"
                }
            }
        ], 
        "currentPage": 6, 
        "hot": [ ]
    }
}
```


# 弹幕
弹幕查询地址：http://service.danmu.youku.com/list?mat=30&mcount=1&ct=1001&iid=884389334&aid=329435&cid=97&lid=0&ouid=0

参数：
- mat：第几次请求弹幕（mat 需要根据实际的弹幕量进行调整）
- iid：视频 ID

返回数据格式：
```json
{
    "count": 16, 
    "filtered": 1, 
    "result": [
        {
            "aid": 329435, 
            "content": "单身的话还是会去北京", 
            "createtime": 1524581256000, 
            "ct": 3002, 
            "id": 707049746, 
            "iid": 884389334, 
            "ipaddr": 1740701100, 
            "level": 1, 
            "lid": 0, 
            "mat": 30, 
            "ouid": 685162531, 
            "playat": 1800214, 
            "propertis": "{\"pos\":3,\"size\":1,\"effect\":0,\"color\":15060379,\"color2\":12098412}", 
            "status": 99, 
            "type": 1, 
            "uid": 685162531, 
            "ver": 1
        }
    ]
}
```

