import requests
import bs4
from bs4 import BeautifulSoup


def getHTMLTest(url):
    try:
        r = requests.get(url, timeout=30)

        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def fillUnivList(uList, html):
    soup = BeautifulSoup(html, "html.parser")

    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            uList.append([tds[0].string.strip(), tds[1].text, tds[4].string.strip()])


def printUnivList(uList, num):
    """ 打印前 num 名的大学 """
    # {1:{3}^10} 中的 {3} 代表取第三个参数
    tplt = "{0:^10}      {1:{3}^8}         {2:^10}"
    print(tplt.format("排名", "学校名称", "总分", chr(12288)))  # chr(12288) 代表中文空格
    for i in range(num):
        u = uList[i]
        print(tplt.format(u[0], u[1], u[2], chr(12288)))


if __name__ == '__main__':
    uinfo = []
    url = 'http://www.shanghairanking.cn/rankings/bcur/2020'

    html = getHTMLTest(url)
    fillUnivList(uinfo, html)

    printUnivList(uinfo, 50)
