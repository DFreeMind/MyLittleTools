"""
请求每一集的弹幕
danmu_csv: 保存到 csv 文件的文件流
vid: 视频 id
episode_cn: 当前集的中文名
"""


def get_youku_danmu(danmu_csv, vid, episode_cn):
    MAT = 1
    FLAG = True
    while FLAG:
        print(episode_cn, "----", MAT)
        url = "http://service.danmu.youku.com/list?mat=" + str(
            MAT) + "&mcount=1&ct=1001&iid=" + vid + "&aid=329435&cid=97&lid=0&ouid=0"
        data = requests.get(url).json()
        if len(data["result"]) > 0:
            # 解析数据
            parse_youku_danmu(danmu_csv, data["result"], episode_cn)
            MAT += 1
            time.sleep(1)
        else:
            FLAG = False


"""
弹幕数据解析
"""

def parse_youku_danmu(danmu_csv, danmus, episode_cn):
    for danmu in danmus:
        uid = danmu["uid"]
        ipaddr = danmu["ipaddr"]
        episode_id = danmu["iid"]
        createtime = danmu["createtime"]
        content = danmu["content"]
        danmu_csv.writerow((uid, ipaddr, episode_id, episode_cn, createtime, content))


def youku_danmu(filepath, episodes):
    danmu = open(filepath, "a")
    danmu_csv = csv.writer(danmu)
    danmu_csv.writerow(["uid", "ipaddr", "episode_id", "episode_cn", "createtime", "content"])

    for i, episode in (enumerate(episodes)):
        get_youku_danmu(danmu_csv, episode[0], episode[1])

    danmu.close()

######################### 评论
"""
请求每一集的评论
danmu_csv: 保存到 csv 文件的文件流
vid: 视频 id
episode_cn: 当前集的中文名
"""
def get_youku_comments(comment_csv, vid, episode_cn):
    PAGE = 1
    FLAG = True
    while FLAG:
        print(episode_cn, "----", PAGE)
        url = "http://p.comments.youku.com/ycp/comment/pc/commentList?app=100-DDwODVkv&objectId=" + vid + "&objectType=1&listType=0&currentPage=" + str(
            PAGE) + "&pageSize=30&sign=c8c7a7ab7056176b3b28ebdd27769a21&time=1525962252"
        data = requests.get(url).json()
        if len(data["data"]["comment"]) > 0:
            # 解析数据
            parse_youku_comments(comment_csv, data["data"]["comment"], vid, episode_cn)
            PAGE += 1
            time.sleep(1)
        else:
            FLAG = False


"""
评论数据解析
"""
def parse_youku_comments(comment_csv, comments, vid, episode_cn):
    for comment in comments:
        userId = comment["user"]["userId"]
        userName = comment["user"]["userName"]
        createTime = comment["createTime"]
        upCount = comment["upCount"]
        downCount = comment["downCount"]
        content = comment["content"].replace("\n", "")
        comment_csv.writerow((userId, userName, vid, episode_cn, createTime, upCount, downCount, content))


def youku_comments(filepath, episodes):
    comment = open(filepath, "a")
    comment_csv = csv.writer(comment)
    comment_csv.writerow(
        ["userId", "userName", "episode_id", "episode_cn", "createTime", "upCount", "downCount", "content"])

    for i, episode in (enumerate(episodes)):
        get_youku_comments(comment_csv, episode[0], episode[1])

    comment.close()


if __name__ == '__main__':

    bjnztj = [("880078209", "第 01 集"), ("880078104", "第 02 集"), ("880078056", "第 03 集"), ("880109272", "第 04 集"),
              ("880112230", "第 05 集"),
              ("880112798", "第 06 集"), ("880143160", "第 07 集"), ("880144723", "第 08 集"), ("880145085", "第 09 集"),
              ("880179270", "第 10 集"),
              ("880179884", "第 11 集"), ("884389334", "第 12 集"), ("884389588", "第 13 集"), ("888106992", "第 14 集"),
              ("888106801", "第 15 集"),
              ("888107530", "第 16 集"), ("888151519", "第 17 集"), ("888152909", "第 18 集"), ("888153384", "第 19 集"),
              ("888176615", "第 20 集")]
    # 弹幕
    bjnztj_file = "/Users/weduoo/Desktop/youku/bjnztj_danmu.csv"
    youku_danmu(bjnztj_file, bjnztj)

    # 评论
    bjnztj_cmments_file = "/Users/weduoo/Desktop/youku/bjnztj_comments.csv"
    youku_comments(bjnztj_cmments_file, bjnztj)