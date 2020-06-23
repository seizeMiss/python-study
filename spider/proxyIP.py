# -*- coding: utf-8 -*-
import bs4
import urllib.request
import urllib3
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import re
from retrying import retry
import requests


def getHtml(url):
    ua = UserAgent(verify_ssl=False)
    header = {'User-Agent': ua.random}
    http = urllib3.PoolManager()
    response = http.request("GET", url, headers=header)
    html = response.data
    return html


@retry(stop_max_attempt_number=3)
def getHtmlForRequests(url):
    ua = UserAgent(verify_ssl=False)
    headers = {'User-Agent': ua.random}
    proxies = {
        "https": "https://117.114.149.66:55443"
    }
    response = requests.get(url, headers=headers, proxies=proxies, timeout=5)
    html = response.text
    # print(html)
    return html


def is_invalid_ip4(ip):
    ip = str(ip).strip()
    if ip.find(".") == -1:
        return False
    its = [v for v in ip.split('.')]

    if len(its) != 4:
        return False

    for v in its:
        if not v.isdigit():
            return False
        if v < 0 & v > 255:
            return False

    return True


def is_invalid_ip4_for_reg(ip):
    ip = str(ip).strip()
    if ip.find(".") == -1:
        return False

    reg = r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    res = re.match(reg, ip, re.S)
    if res is None:
        return False

    return True


def main():
    ipList = []
    for i in range(1, 5):
        s = '.html'
        url = 'http://www.66ip.cn/areaindex_1/'
        cur_url = url + str(i) + s
        html_doc = getHtmlForRequests(cur_url)

        sp = BeautifulSoup(html_doc, "html.parser", from_encoding='utf-8')

        table = sp.select("#footer div table")
        sp = BeautifulSoup(str(table[0]), "html.parser")
        trs = sp.findAll('tr')
        for tr in trs:
            for a in tr.children:
                ip_val = a.string.strip()
                port = a.next_sibling.string.strip()
                if is_invalid_ip4_for_reg(ip_val):
                    ipList.append(ip_val + ":" + port)
                    print(ip_val + ":" + port)
                break
        print('-' * 32)


if __name__ == '__main__':
    ip = '123.0.0.1'
    print(is_invalid_ip4_for_reg(ip))

    main()
