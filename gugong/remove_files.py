import os
import shutil

BASE_DIR = '/Users/weduoo/Desktop/gugong'
DESR_DIR = '/Users/weduoo/Desktop/织绣'

def remove_files():
    """
    移除下载的小文件
    :return:
    """
    dirs_list = os.listdir(BASE_DIR)
    for i, d in enumerate(dirs_list):
        name = os.path.join(BASE_DIR, d, 'origin')
        if os.path.exists(name):
            shutil.rmtree(name)
            print('移除：', i, name)


def move_files():
    dirs_list = os.listdir(BASE_DIR)
    for i, d in enumerate(dirs_list):
        name = os.path.join(BASE_DIR, d, d + '.jpg')
        if os.path.exists(name):
            shutil.move(name, DESR_DIR)
            print('移动：', i, name)


def collection():
    """
    汇总下载的图片
    :return:
    """
    gg = '/Users/weduoo/Desktop/故宫'
    dest_dir = '/Users/weduoo/Desktop/汇总'
    dir_list = os.listdir(gg)
    dul = 0
    for p in dir_list:
        pdir_list = os.listdir(os.path.join(gg, p))
        for name in pdir_list:
            filename = os.path.join(gg, p, name)
            if not os.path.exists(os.path.join(dest_dir, name)):
                shutil.move(filename, dest_dir)
                print('移动 -- > ', filename)
            else:
                os.remove(filename)
                print('重复 -- > ', filename)
                dul += 1
    print('重复文件个数： ', dul)


if __name__ == '__main__':
    # remove_files()
    # move_files()
    collection()

