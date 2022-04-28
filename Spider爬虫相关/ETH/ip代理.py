#coding=utf-8
import requests
import json
from random import choice


# 通过请求星速代理服务器获取代理IP
def get_proxy_ip(server_url):
    server_resp = requests.get(server_url)
    proxy_resp = json.loads(server_resp.text)

    if proxy_resp["code"] == 200:
        ip_list = proxy_resp["result"]
        if len(ip_list) <= 0:
            return None

        # 随机返回一个代理IP信息
        return choice(ip_list)


# 解析txt格式的请求行
def parse_ip(server_url):
    one_proxy_ip_line = get_proxy_ip(server_url)

    if one_proxy_ip_line is None:
        return None, None

    line_list = one_proxy_ip_line.split(",")
    ip_port = line_list[0].split(":")
    ip = ip_port[0]
    port = ip_port[1]
    return ip, port


if __name__ == '__main__':
    xingsudailiUrl = ""

    # 获取代理服务器
    proxyHost, proxyPort = parse_ip(xingsudailiUrl)

    if proxyHost is None or proxyPort is None:
        raise Exception("无法从星速代理服务器获取代理IP，请稍后重试！")


    # 请求地址
    targetUrl = "https://www.baidu.com"

    proxyMeta = "http://%(host)s:%(port)s" % {
        "host": proxyHost,
        "port": proxyPort,
    }

    # pip install -U requests[socks]  socks5
    # proxyMeta = "socks5://%(host)s:%(port)s" % {
    #     "host" : proxyHost,
    #     "port" : proxyPort,
    # }

    proxies = {
        "http": proxyMeta,
        "https": proxyMeta
    }

    resp = requests.get(targetUrl, proxies=proxies)
    print(resp.status_code)
    print(resp.text)



