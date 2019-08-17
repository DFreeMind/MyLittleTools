import os
import time
import requests
import socks
import socket
from requests_html import HTMLSession
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# 站点地址
SITE = "https://kissmanga.com/Manga/"

# 代理设置
SOCKS5_PROXY_HOST = '127.0.0.1'
SOCKS5_PROXY_PORT = 1086  # socks 代理本地端口

default_socket = socket.socket
socks.set_default_proxy(socks.SOCKS5, SOCKS5_PROXY_HOST, SOCKS5_PROXY_PORT)
socket.socket = socks.socksocket

headers={"User-Agent": "Mozilla/5.001 (windows; U; NT4.0; en-US; rv:1.0) Gecko/25250101"}

def parse_series(mangaName):
    """
    解析漫画列表
    @:param mangaName 漫画地址
    :return:
    """
    url = SITE + mangaName
    print(url)
    sess = HTMLSession()
    h = sess.get("http://jkw552403.github.io/2015/09/06/curl-requests-urlib2/")
    print(h.html.find("src"))



if __name__ == '__main__':
    parse_series("Naruto")