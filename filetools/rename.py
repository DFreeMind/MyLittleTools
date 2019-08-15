import os


def rename(path, origin_mark, target_mark):
    """

    :param path:
    :param origin_mark:
    :param target_mark:
    :return:
    """
    if os.path.isdir(path):
        files = os.listdir(path)
        for filename in files:
            orgin_filename = os.path.join(path, filename)
            # 替换需要替换的字符
            new_filename = filename.replace(origin_mark, target_mark)
            target_filename = os.path.join(path, new_filename)
            os.rename(orgin_filename, target_filename)
    else:
        # 获取文件名
        filename = os.path.basename(path)
        new_filename = filename.replace(origin_mark, target_mark)
        os.rename(path, new_filename)


if __name__ == '__main__':
    path = input("输入文件/文件夹路径:")
    origin_mark = input("输入需要替换的字符:")
    target_mark = input("输入替换为的字符:")
    print(path, origin_mark, target_mark)
    rename(path, origin_mark, target_mark)
