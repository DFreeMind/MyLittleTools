import requests
import os
from PIL import Image

import time
from requests_html import HTMLSession
from tqdm import tqdm


HEIGHT_MAX = 50
WIDRH_MAX = 250
BASE_DIR = '/Users/weduoo/Desktop/gugong'


def lengthways(origin_dir, dest_dir, h_size, w_size):
    """
    纵向拼接
    :param origin_dir: 小图片
    :param dest_dir: 初步合并的小图片
    :param h_size: 每一小段小图片的数量
    :param w_size
    :return:
    """
    # 图的高度
    hs = []
    for i in range(h_size):
        image_path = os.path.join(origin_dir, '0_' + str(i) + '.jpg')
        image = Image.open(image_path)
        w, h = image.size
        hs.append(h)
    # 总高
    HEIGHT = sum(hs)
    print('图片总高度:', HEIGHT)
    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)
    for i in range(w_size):
        # 获取第一张图的宽度
        w = Image.open(os.path.join(origin_dir, str(i) + '_' + str(0) + '.jpg')).size[0]
        imagefile = []
        for j in range(h_size):
            name = str(i) + '_' + str(j) + '.jpg'
            imagefile.append(Image.open(os.path.join(origin_dir, name)))
        target = Image.new('RGB', (w, HEIGHT))
        y = 0
        for k, image in enumerate(imagefile):
            target.paste(image, (0, y))
            y += hs[k] # 从上往下拼接，左上角的纵坐标递增
        quality_value = 100
        target.save(os.path.join(dest_dir, str(i)+'.jpg'), quality=quality_value)
    return HEIGHT


def crosswise(middle_dir, last_dir, h_size, height, name):
    """
    横向拼接
    :param middle_dir:
    :param last_dir:
    :param h_size
    :param height
    :param name
    :return:
    """
    # 存储中间图的宽度
    ws = []
    # 存储中间图片，用于拼接
    images = []
    for i in range(h_size):
        img = Image.open(os.path.join(middle_dir, str(i)+'.jpg'))
        images.append(img)
        ws.append(img.size[0])
    # 计算总的宽度
    WIDTH = sum(ws)
    print(WIDTH)
    target = Image.new('RGB', (WIDTH, height))
    x = 0
    y = 0
    for k, image in enumerate(images):
        target.paste(image, (x, y))
        x += ws[k] # 从左往右拼接，y 不变，x 值增加
    quality_value = 100
    target.save(os.path.join(last_dir, name + '.jpg'), quality=quality_value)


def download_patches(max_scale, paint_name, path, w_size, h_size):
    """
    下载图片
    :param max_scale
    :param paint_name
    :param path
    :return:
    """
    url = 'http://en.dpm.org.cn/' + path + '_files/' + str(max_scale) + '/'
    base_dir = os.path.join(BASE_DIR, paint_name)
    if not os.path.exists(base_dir):
        os.mkdir(base_dir)

    origin_dir = os.path.join(base_dir, 'origin')
    if not os.path.exists(origin_dir):
        os.mkdir(origin_dir)

    for i in tqdm(range(w_size)):
        for j in range(h_size):
            name = str(i) + '_' + str(j) + '.jpg'
            filename = os.path.join(origin_dir, name)
            if not os.path.exists(filename):
                time.sleep(0.1)
                image = requests.get(url+name, verify=False)
                # print("下载..", filename)
                with open(filename, 'wb') as file:
                    file.write(image.content)


def get_scale(xml_path):
    """
    获取图片的最大缩放比例和图片的横向数量
    :return:
    """
    # 默认为 9
    scale = []
    base_url = 'http://en.dpm.org.cn'
    path = xml_path.split('.')[0]
    # 默认可缩放的比例为 1 - 20
    for i in range(1, 21):
        try_url = base_url + path + '_files/' + str(i) + '/0_0.jpg'
        image = requests.get(try_url)
        if image.ok:
            scale.append(i)
    print(scale)
    # 有些画没有可供查看的大图
    if len(scale) == 0:
        return 0
    return max(scale)



def get_wh_size_(name):
    """
    获取当前绘画的元数据(已下载好)，每一列多少张图，一共多少列
    :return:
    """
    import fnmatch
    path = os.path.join(BASE_DIR, name, 'origin')
    images = os.listdir(path)
    images = fnmatch.filter(images, '*.jpg')
    h_size = len(fnmatch.filter(images, '0_*.jpg'))
    w_size = int(len(images)/h_size)

    return w_size, h_size


def get_wh_size(max_scale, path, dir_name):
    """
    获取当前绘画的元数据（通过网络获取），每一列多少张图，一共多少列
    :return:
    """
    url = 'http://en.dpm.org.cn/' + path + '_files/' + str(max_scale) + '/'
    base_dir = os.path.join(BASE_DIR, dir_name)
    if not os.path.exists(base_dir):
        os.mkdir(base_dir)

    origin_dir = os.path.join(base_dir, 'origin')
    if not os.path.exists(origin_dir):
        os.mkdir(origin_dir)

    h_size = 0
    while True:
        name = '0_' + str(h_size) + '.jpg'
        filename = os.path.join(origin_dir, name)
        if not os.path.exists(filename):
            time.sleep(0.1)
            image = requests.get(url + name, verify=False)
            if not image.ok:
                break
            # print("下载..", filename)
            h_size += 1
            with open(filename, 'wb') as file:
                file.write(image.content)
        else:
            h_size += 1
    w_size = 0
    while True:
        name = str(w_size) + '_0.jpg'
        filename = os.path.join(origin_dir, name)
        if not os.path.exists(filename):
            time.sleep(0.1)
            image = requests.get(url + name, verify=False)
            if not image.ok:
                break
            # print("下载..", filename)
            w_size += 1
            with open(filename, 'wb') as file:
                file.write(image.content)
        else:
            w_size += 1

    return w_size, h_size


def get_paint(paints_href):
    """
    获取大图的实际地址，通常以 xml 结尾
    :param paints_href 页面地址
    :return:
    """
    base_url = 'http://www.dpm.org.cn'
    for name, href in paints_href:
        filename = os.path.join(BASE_DIR, name, name + '.jpg')
        if os.path.exists(filename):
            print('此图已存在：', filename)
            continue
        session = HTMLSession()
        resp = session.get(base_url + str(href))
        # 找到含有 xml 的连接地址
        img = resp.html.find('div#hl_content', first=True).find('img', first=True)
        url = img.attrs['custom_tilegenerator']
        if url == '':
            print('--没有解析出大图地址--：', name)
            continue
        xml_path = url.split('=')[1]
        max_scale = get_scale(xml_path)
        if max_scale == 0:
            print('--暂时无大图--：', name)
            continue
        path = xml_path.split('.')[0]

        start = time.time()

        # 分析当前图片的信息, 返回宽高个数
        print('开始解析宽高数据：', name)
        w_size, h_size = get_wh_size(max_scale, path, name)
        print('图片宽高数据：', w_size, h_size)

        # 下载小图片，返回宽高数量的最大值
        print('开始下载：', name)
        download_patches(max_scale, name, path, w_size, h_size)

        # 纵向合并小图片
        origin_dir = os.path.join(BASE_DIR, name, 'origin')
        dest_dir = os.path.join(BASE_DIR, name, 'middle')
        height = lengthways(origin_dir, dest_dir, h_size, w_size)

        # 纵向合并完成最终拼接
        print('开始纵向拼接' + name)
        last_path = os.path.join(BASE_DIR, name)
        print('纵向拼接' + name + '完成')
        print('开始横向拼接' + name + '完成')
        crosswise(dest_dir, last_path, w_size, height, name)
        print('横向拼接' + name + '完成')
        print(name, ' 用时:', time.time() - start)



def get_paints_list(start_page=23):
    """
    获取故宫网站上图片的链接
    绘画：91， 一共 108 页
    法书：92， 一共 41 页
    织绣：96， 一共 38 页
    src = 'http://www.dpm.org.cn/searchs/paints/category_id/91/p/1.html'
    :return:
    """
    session = HTMLSession()
    for i in range(start_page, 38):
        resp = session.get('http://www.dpm.org.cn/searchs/paints/category_id/96/p/' + str(i) + '.html')
        print(resp.html)
        # 获取绘画所在的 tr 信息
        trs = resp.html.find('div.table1', first=True).find('table tr')[1:]

        # 获取绘画的详细页面链接和绘画的名称
        paints_href = []
        for tr in trs:
            a = tr.find('a', first=True)
            name = a.text
            href = a.attrs['href']
            print(name, href)
            paints_href.append((name, href))

        get_paint(paints_href)


if __name__ == '__main__':
    # import sys
    # args = sys.argv
    # try:
    #     if len(args) > 1:
    #         get_paints_list(start_page=int(args[1]))
    #     else:
    #         get_paints_list(start_page=29)
    # except:
    #     if len(args) > 1:
    #         get_paints_list(start_page=int(args[1]))
    #     else:
    #         get_paints_list(start_page=29)
    href = '/collection/paint/228354.html'
    get_paint([('王希孟千里江山图卷', href)])
