# -*- coding: utf-8 -*-
import urllib
import urllib.request
import urllib.parse
import http.cookiejar
import re
import requests


class SimulationLogin:

    def __init__(self):
        self.loginUrl = 'http://localhost:8088/Admin/Login.aspx'
        self.cookies = http.cookiejar.CookieJar()
        self.postdata = urllib.parse.urlencode({
            'id_username': 'admin',
            'id_password': 'admin',
            'txtCode': '1234'
        }).encode(encoding='utf-8')
        self.opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(self.cookies))

    def getPage(self):
        request = urllib.request.Request(
            url=self.loginUrl,
            data=self.postdata)
        result = self.opener.open(request)
        # 打印登录内容
        print(result.read().decode('utf-8'))


if __name__ == '__main__':
    sim = SimulationLogin()
    sim.getPage()

