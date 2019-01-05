# 信息获取说明
## 用户微博获取
微博 url：https://m.weibo.cn/api/container/getIndex?type=uid&value=1192329374&containerid=1076031192329374
微博 url(含页数)：https://m.weibo.cn/api/container/getIndex?type=uid&value=1192329374&containerid=1076031192329374&page=2

**参数：**
- type：类型， 用户id，[uid]
- value：类型的值，用户id， [1192329374]
- containerid：容器类型，107603 + 用户 id
- page: 页数，每页返回 10 条微博

**返回数据**

这里值获取微博信息不获取其他信息，因此在 `cards` 数组里只获取 `card_type` 类型为 `9` 的 cards。接着就是获取 mblog 里面的微博信息，需要后去如下的信息：
- id/idstr/mid: 当前微博的 id
- created_at: 在什么时间创建（不太有意义）
- text: 实际的微博，表情会与文本一起存在
- raw_text: 原微博，在是**转发**的微博时会有此属性
- source: 微博从什么平台发布
- reposts_count: 转发数量
- comments_count: 评论数量
- attitudes_count: 点赞数量

获取微博配的图片，图片在 `pics` 属性中，若是纯文字则没有图片。在最层的 `url` 中存储的是小图片，在 `large` 中存贮的是大图。

获取微博配的视频，视频在 `page_info` 中，之后在找到 `media_info` 里面的 `stream_url` 就是视频的地址。

若属性里还有 `retweeted_status` 就说明此条微博时评论引用微博。暂时不处理这种微博，只记录。
```json
{
    "ok": 1, 
    "data": {
        "cards": [
            {
                "card_type": 9, 
                "itemid": "1076031192329374_-_4237116843937317", 
                "scheme": "https://m.weibo.cn/status/GfzzSgwh7?mblogid=GfzzSgwh7&luicode=10000011&lfid=1076031192329374", 
                "mblog": {
                    "created_at": "2小时前", 
                    "id": "4237116843937317", 
                    "idstr": "4237116843937317", 
                    "mid": "4237116843937317", 
                    "can_edit": false, 
                    "text": "今天好孩子发布会，好像瘦点儿了<span class=\"url-icon\"><img src=\"//h5.sinaimg.cn/m/emoticon/icon/default/d_touxiao-3458a765a2.png\" style=\"width:1em;height:1em;\" alt=\"[偷笑]\"></span> 看着我拉着婴儿车旋转舞动会不会很嗨🤗 ​​​", 
                    "textLength": 75, 
                    "source": "", 
                    "favorited": false, 
                    "thumbnail_pic": "http://wx4.sinaimg.cn/thumbnail/4711809ely1fr2z4cfy47j21l6280e81.jpg", 
                    "bmiddle_pic": "http://wx4.sinaimg.cn/bmiddle/4711809ely1fr2z4cfy47j21l6280e81.jpg", 
                    "original_pic": "http://wx4.sinaimg.cn/large/4711809ely1fr2z4cfy47j21l6280e81.jpg", 
                    "is_paid": false, 
                    "mblog_vip_type": 0, 
                    "user": {}, 
                    "picStatus": "0:1,1:1,2:1,3:1,4:1,5:1", 
                    "reposts_count": 3343, 
                    "comments_count": 4917, 
                    "attitudes_count": 82175, 
                    "pending_approval_count": 0, 
                    "isLongText": false, 
                    "visible": {}, 
                    "more_info_type": 0, 
                    "content_auth": 0, 
                    "edit_config": {}, 
                    "mblogtype": 0, 
                    "weibo_position": 1, 
                    "bid": "GfzzSgwh7", 
                    "pics": [
                        {
                            "pid": "4711809ely1fr2z4cfy47j21l6280e81", 
                            "url": "https://wx4.sinaimg.cn/orj360/4711809ely1fr2z4cfy47j21l6280e81.jpg", 
                            "size": "orj360", 
                            "geo": {}, 
                            "large": {"url":""}
                        }
                    ]
                }, 
                "show_type": 0
            }
        ], 
        "showAppTips": 0, 
        "scheme": "sinaweibo://cardlist?containerid=1076031192329374&extparam=&luicode=10000011&lfid=1076031192329374&featurecode="
    }
}
```
## 获取微博的评论
获取评论方式 url：https://m.weibo.cn/api/comments/show?id=4236304998304332&page=1

参数：
- id: 当前微博 id，可以从微博请求连接中获取到
- page: 当前第几页

**返回数据**

这里要获取用户的评论和用户基本信息，所有的返回数据在 `data/data` 数组中需要获取如下信息：
- `source`: 发布的设备，
- `text`: 评论信息
- `like_counts`: 点赞数量
- `user` 字段中需要获取如下信息：
    - `id`: 用户的id，用于统计参与的用户
    - `profile_url`: 用户的首页信息地址
    - `screen_name`: 昵称

```json
{
    "ok": 1, 
    "msg": "数据获取成功", 
    "data": {
        "data": [
            {
                "id": 4237164545724845, 
                "created_at": "2分钟前", 
                "source": "前后2000万 OPPO R11s", 
                "user": {
                    "id": 6510497406, 
                    "screen_name": "风继续吹-201511", 
                    "profile_image_url": "https://tvax4.sinaimg.cn/crop.0.0.132.132.180/0076BnMGly8fpjoi3pd5bj303o03omx0.jpg", 
                    "verified": false, 
                    "verified_type": -1, 
                    "mbtype": 0, 
                    "profile_url": "https://m.weibo.cn/u/6510497406?uid=6510497406&luicode=10000011&lfid=1076031192329374", // 个人主页地址
                    "remark": "", 
                    "following": false, //我是否关注
                    "follow_me": false // 是否关注我
                }, 
                "text": "挺美的 辣妈 很美", // 评论
                "like_counts": 0,  // 点赞数量
                "liked": false // 我是否点赞
            }
        ], 
        "total_number": 5283, 
        "max": 529
    }
}
```

## 获取微博点赞数据 
点赞信息获取 url：https://m.weibo.cn/api/attitudes/show?id=4237116843937317&page=1

**参数：**
- `id`: 词条微博的 id
- `page`: 第几页，每页展示 50 条

**返回数据**

需要获取的数据在 `data/data` 字段中，需获取如下信息
- `source`: 操作设备名称
- `user`:用户信息
    - `id`: 用户 id
    - `profile_url`: 个人主页地址
    - `screen_name`: 昵称
```json
{
    "ok": 1, 
    "msg": "数据获取成功", 
    "data": {
        "total_number": 104951, 
        "max": 2100, 
        "data": [
            {
                "id": 4237168459296182, 
                "created_at": "刚刚", 
                "source": "柔光自拍vivo X7", 
                "user": {
                    "id": 5803297786, 
                    "screen_name": "Shirley-的主场", 
                    "profile_image_url": "https://tva1.sinaimg.cn/crop.0.0.438.438.180/006kK2Rcjw8ezfaiyje3qj30c60c6mxn.jpg", 
                    "verified": false, 
                    "verified_type": -1, 
                    "mbtype": 0, 
                    "profile_url": "https://m.weibo.cn/u/5803297786?uid=5803297786&luicode=10000011&lfid=1076031192329374", 
                    "remark": "", 
                    "following": false, 
                    "follow_me": false
                }
            }
        ]
    }
}
```

## 获取微博转发数据
微博转发信息获取 url：https://m.weibo.cn/api/statuses/repostTimeline?id=4237116843937317&page=1

**参数：**
- `id`: 此条微博的id
- `page`: 第几页，每页显示 10 条

**返回数据：**

返回的数据均在 `data/data` 字段下，此处要获取如下信息：
- `text`: 转发时的评论，如果内容为 "转发微博" 则表示值转发不评论
- `user`:用户信息
    - `id`: 用户 id
    - `profile_url`: 个人主页地址
    - `screen_name`: 昵称

```json
{
    "ok": 1, 
    "msg": "数据获取成功", 
    "data": {
        "data": [
            {
                "id": 4237170380036347, 
                "raw_text": "转发微博", 
                "text": "转发微博", 
                "created_at": "刚刚", 
                "user": {
                    "id": 3675989462, 
                    "screen_name": "海斗su", 
                    "profile_image_url": "https://tvax4.sinaimg.cn/crop.0.0.664.664.180/db1b25d6ly8fisne8026pj20ig0iggmq.jpg", 
                    "verified": false, 
                    "verified_type": -1, 
                    "mbtype": 2, 
                    "profile_url": "https://m.weibo.cn/u/3675989462?uid=3675989462&luicode=10000011&lfid=1076031192329374", 
                    "remark": "", 
                    "following": false, 
                    "follow_me": false
                }, 
                "like_counts": 0, 
                "liked": false
            }
        ], 
        "total_number": 3565, 
        "hot_total_number": 5, 
        "max": 357
    }
}
```
## 获取微博中评论、转发、点赞的用户的信息
获取用户信息：（super-帅比）https://m.weibo.cn/api/container/getIndex?uid=6013003248&luicode=10000011&lfid=1076036013003248&featurecode=20000320&containerid=1005056013003248

containerid 为：100505 + 用户 id

用户基础信息获取：[https://m.weibo.cn/api/container/getIndex?containerid=2302836013003248_-
_INFO&title=%25E5%259F%25BA%25E6%259C%25AC%25E8%25B5%2584%25E6%2596%2599&
luicode=10000011&lfid=2302836013003248&featurecode=20000320]

** 参数: ** 
- containerid 为：230283 + 用户 id
- lfid 为：230283 + 用户 id

**返回数据：**

所有的数据均在 `data/cards` 中，需要从每个 card 中获取到 `card_group`, 从中在获取到 `昵称``性别``所在地``简介``注册时间` 信息。
```json
{
    "ok": 1, 
    "data": {
        "cardlistInfo": {}, 
        "cards": [
            {
                "card_type": 11, 
                "show_type": 2, 
                "card_group": [
                    {
                        "card_type": 41, 
                        "item_name": "昵称", 
                        "item_content": "Dejlige_"
                    }, 
                    {
                        "card_type": 41, 
                        "item_name": "性别", 
                        "item_content": "女"
                    }, 
                    {
                        "card_type": 41, 
                        "item_name": "所在地", 
                        "item_content": "山西 运城"
                    }, 
                    {
                        "card_type": 41, 
                        "item_name": "简介", 
                        "item_content": "底线 蔡徐坤 ❤️"
                    }
                ]
            }, 
            {
                "card_type": 11, 
                "show_type": 2, 
                "is_asyn": 0, 
                "card_group": [ 
                    {
                        "card_type": 41, 
                        "item_name": "注册时间", 
                        "item_content": "2016-01-28"
                    }
                ]
            }
        ], 
        "showAppTips": 0, 
        "scheme": "sinaweibo://cardlist?containerid=2302835841808579_-
        _INFO&extparam=&luicode=10000011&lfid=2302835841808579&featurecode="
    }
}
```