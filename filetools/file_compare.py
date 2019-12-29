import os


def remove_reduant_file(root_path, path1, path2):
    """
    移除不同时存在于两个文件夹中的文件
    :return:
    """
    if path1 is None or path2 is None:
        print("请输入两个文件夹的名字")
        return
    p1 = os.path.join(root_path, path1)
    p2 = os.path.join(root_path, path2)
    files1 = set(os.listdir(p1))
    files2 = set(os.listdir(p2))
    # 取两个结合的交集
    intersection = files1.intersection(files2)
    # 删除 files1 和 files2 中不在交集中的文件
    count1 = 0
    for file_name in files1:
        if file_name not in intersection:
            print(file_name)
            count1 += 1
            os.remove(os.path.join(p1, file_name))
    print(path1, "删除", count1, "个文件")
    print("-----------------------------------------")
    count2 = 0
    for file_name in files2:
        if file_name not in intersection:
            print(file_name)
            count2 += 1
            os.remove(os.path.join(p2, file_name))
    print(path2, "删除", count2, "个文件")


if __name__ == '__main__':
    root_path = "/Users/weduoo/Downloads/road_segmentation_ideal"
    path1 = "training/input"
    path2 = "training/output"
    remove_reduant_file(root_path, path1, path2)
