import requests
import os


def download_manhua(save_path, zhan, pages):
    """
    下载巨人漫画
    :param save_path: 存储路径
    :param zhan: 章节
    :param pages: 页数
    :return:
    """
    base_url = "http://img.17dm.com/juren/manhua/" + zhan + "/"
    for page in range(1, int(pages) + 1):
        image_name = zhan + "_" + str(page) + ".jpg"
        filename = save_path + "/" + image_name
        if not os.path.exists(filename):
            image = requests.get(base_url + str(page) + ".jpg")
            with open(filename, 'wb') as f:
                f.write(image.content)
                print(image_name)
        else:
            print("已下载：", filename)


if __name__ == '__main__':
    zhan = input("输入章节：")
    pages = input("输入章节数：")
    save_path = "D:\Downloads\juren" #input("输入保存路径：")
    download_manhua(save_path, zhan, pages)
