# 导入相关包
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from tqdm import tqdm
from pyecharts import Bar
from pyecharts import online
import urllib
from urllib import request
import json
from retrying import retry
import os
import csv
from tqdm import tqdm
import time
import ssl
import requests

# 让 pyecharts 在 jupyter 下载时有图片
online()

# ssl 设置
requests.packages.urllib3.disable_warnings()

#### 获取用户微博数据
"""
下载图片
mid: 微博 id
pics: 待下载的图片
imagepath: 图片保存地址
"""
def download_images(mid,pics,imagepath):
    for index,image_data in enumerate(pics):
        # 大图
        url = image_data["large"]["url"]
        #获得图片后缀
        file_suffix = os.path.splitext(url)[1]
        filename = imagepath  + str(mid) + "_" + str(index) + file_suffix
        if not os.path.exists(filename):
            print("下载..",url,filename)
            time.sleep(1)
            image = requests.get(url,verify=False)
            with open(filename, 'wb') as file:
                file.write(image.content)


"""
获取用户微博，并保存到指定路径的指定文件
"""
def get_mblog(uid, filepath, imagepath, weibo_log):
    if not os.path.exists(imagepath):
        print(imagepath, "文件路径不存在")
        return
    url = "https://m.weibo.cn/api/container/getIndex?type=uid&value=" + uid + "&containerid=107603" + uid + "&page="
    mblog_io = open(filepath, "a")
    mblog_csv = csv.writer(mblog_io)
    mblog_csv.writerow(["mid", "created_at", "text", "source", "reposts_count",
                        "comments_count", "attitudes_count", "is_reposts"])

    with open(weibo_log) as f:
        mids = f.read().splitlines()
    logs = open(weibo_log, "a")
    CARRY_ON = True
    PAGE = 1
    while CARRY_ON:
        print(PAGE)
        try:
            rep = requests.get(url + str(PAGE), verify=False)
            data = rep.json()
            cards = data["data"]["cards"]
            if len(cards) > 0:
                for card in cards:
                    if card["card_type"] == 9 and card["mblog"]["mid"] not in mids:
                        mblog = card["mblog"]
                        mid = mblog["mid"]

                        created_at = mblog["created_at"]
                        text = mblog["text"]
                        source = mblog["source"]
                        reposts_count = mblog["reposts_count"]
                        comments_count = mblog["comments_count"]
                        attitudes_count = mblog["attitudes_count"]
                        if "retweeted_status" in mblog.keys():
                            is_reposts = 1
                        else:
                            is_reposts = 0

                        mblog_csv.writerow((mid, created_at, text, source, reposts_count,
                                            comments_count, attitudes_count, is_reposts))
                        # 获取图片
                        if "pics" in mblog.keys():
                            download_images(mid, mblog["pics"], imagepath)
                        logs.writelines(mid + "\n")
                time.sleep(3)
                PAGE += 1
            else:
                # 已无返回数据
                CARRY_ON = False
        except Exception:
            print("产生错误")
            mblog_io.close()
            logs.close()
            print("重新开始")
            get_mblog(uid, filepath, imagepath, weibo_log)
            raise
    mblog_io.close()
    logs.close()


if __name__ == '__main__':
    # 获取谢娜微博数据 信息
    weibo_data = "/Users/weduoo/Desktop/weibo/xiena.csv"
    image_path = "/Users/weduoo/Desktop/weibo/xiena/"
    weibo_logs = "/Users/weduoo/Desktop/weibo/xiena_complete.txt"
    get_mblog("1192329374", weibo_data, image_path, weibo_logs)