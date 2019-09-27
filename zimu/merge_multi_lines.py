# coding:utf-8
import re
import sys


def merge_lines(filename):
    """
    将多行字幕合并成一行
    :param filename: 文件地址
    :return:
    """

    with open(filename, 'r', encoding="utf8") as f:
        a = f.read()
        # try:
        #     a = a.decode('utf8')
        # except:
        #     pass

        aa = a.split('\n\n')
        f.close()
        k = []

        for a in aa:
            if len(a.split('\n')) < 2:
                for m in a.split('\n'):
                    k.append(m.replace('- ', '-'))
                continue
            time = "\n".join(a.split('\n')[:2])
            chi = [x for x in a.split('\n')[2:] if x != x.encode('unicode-escape')]
            eng = [x for x in a.split('\n')[2:] if x == x.encode('unicode-escape')]

            k.append(time)
            if len(chi) > 0: k.append(" ".join(chi).replace('- ', '-'))
            if len(eng) > 0: k.append(" ".join(eng).replace('- ', '-'))
            k.append('')

        with open(filename + "_fixed.srt", "w", encoding='utf8') as ff:
            for m in k:
                ff.write(m + '\n')


if __name__ == '__main__':
    filename = input("输入文件地址：")
    merge_lines(filename)
