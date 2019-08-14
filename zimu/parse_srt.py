import os
import io
import sys
import re
import time
import string
import requests
from bs4 import BeautifulSoup

stop_words = ["is", "to", "am", "are", "was", "were", "on", "in", "of", "for", "who", "where", "how",
              "oh", "the", "them", "she", "her"]


def list_file(directory):
    """
    列出将要解析的文件
    :param directory:
    :return:
    """
    files = os.listdir(directory)
    # 解析文件
    with open("./record/done_files.txt", "r", encoding="utf8") as f:
        files_done = f.read()

    for file in files:
        # 解析为解析过得字幕
        if file not in files_done:
            parse_file(file)


def parse_file(file):
    print("=====================>" + file)
    filename = "./srt/" + file
    f = open(filename, "r", encoding='ISO-8859-1')

    # 空行、行数标号正则表达式
    rgx_none_and_num = re.compile(r'\d{1,2}\n')

    # 时间正则表达式
    rgx_time = re.compile(r'\d\d:\d\d:\d\d,\d\d\d --> \d\d:\d\d:\d\d,\d\d\d\n')

    # 读取每一行字幕
    lines = f.readlines()

    # 只处理单词
    for line in lines:
        if rgx_none_and_num.search(line) or rgx_time.search(line):
            continue
        elif line.strip():
            # 去除每一行的标点, 并去除开始和结尾空格
            line_no_pun = re.sub(r'[^\w\s]', '', line).strip()
            # line_no_pun = line.translate(string.punctuation).strip()
            words = line_no_pun.lower().split()
            # 处理单词列表
            print(words)
            parse_wrods(words)

    f.close()
    # 保存已经解析过的字幕文件
    with open("./record/done_files.txt", "a", encoding="utf8") as f:
        f.write(file)
        f.write("\n")


def parse_wrods(words):
    """
    处理一行单词
    :param words:
    :return:
    """
    parse_done = []
    # 已完成查询的单词
    with open("./record/done_words.txt", "r") as f:
        words_done = f.read()

    # 已添加的无解释的单词
    with open("./record/no_explain.txt", "r") as f:
        no_explains = f.read()

    with open("./record/done_words.txt", "a") as f:
        for word in words:
            # 解析没有解析过得单词
            if word not in words_done and word not in parse_done:
                time.sleep(3)
                phonetics_list, explains_list = get_word(word)
                if len(explains_list) > 0 and len(phonetics_list) > 0:
                    append_word_explain(word, phonetics_list, explains_list)
                else:
                    # 记录没有查询到解释的词
                    with open("./record/no_explain.txt", "a") as ff:
                        if word not in no_explains:
                            ff.write(word)
                            ff.write("\n")
                f.write(word)
                f.write("\n")
                parse_done.append(word)


def append_word_explain(word, phonetics, explains):
    """
    向文件中添加单词解释
    :param word: 要解释的单词
    :param phonetics: 发音（英、美）
    :param explains: 单词中文解释
    :return:
    """
    ps = "\t".join(phonetics)
    with open("./record/words.txt", "a", encoding="utf-8") as f:
        f.write(word + ": " + ps)
        f.write("\n")
        for explain in explains:
            f.write("\t" + explain + "\n")
        f.write("\n")


def get_word(word):
    """
    获取具体单词的解释
    :param word: 单词
    :return: 发音列表、解释列表
    """
    print("------------->" + word)
    url = "http://dict.youdao.com/w/" + word +"/#keyfrom=dict2.top"
    r = requests.get(url)  # 向有道词典请求资源
    html = r.text
    soup = BeautifulSoup(html, 'html.parser')  # 结构化文本soup
    div = soup.find(name='div', attrs={'class': 'trans-container'})  # 获取中文释义所在的标签
    if not div:
        return [], []

    # 获取发音列表
    phonetics = soup.find_all(name="span", attrs={'class': 'pronounce'})
    phonetics_list = [li.get_text(strip=True) for li in phonetics]
    print(phonetics_list)

    # 获取解释列表
    lis = div.find_all("li")
    explains_list = [li.get_text(strip=True) for li in lis]
    print(explains_list)

    return phonetics_list, explains_list


if __name__ == '__main__':
    d = "./srt"
    list_file(d)
    # parse_file("./srt/Naruto 001 English.srt")