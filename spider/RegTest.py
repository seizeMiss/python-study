import requests
import re
from fake_useragent import UserAgent


class Spider(object):

    def __init__(self, start_page, end_page):
        self.start_page = start_page
        self.end_page = end_page
        self.file_name = "duanzi.txt"

    def loadPage(self, url):

        ua = UserAgent(verify_ssl=False)
        header = {'User-Agent': ua.random}
        response = requests.get(url=url, headers=header)
        html = response.content

        print(html)

        return html.decode('gb18030')

    def screenPage(self, html):

        pattern = re.compile(r'<div class="f18 mb20">(.*?)</div>', re.S)
        item_list = pattern.findall(html)

        return item_list

    def writePage(self, list):

        with open(self.file_name, 'a', encoding='utf-8') as f:
            for content in list:
                content = content.replace("…", "…").replace("“", "“").replace("”", "”")
                content = content.replace("　", "").replace("	", "").replace(":", "：")
                content = content.replace("<p>", "").replace("</p>", "").replace("<br />", "").replace(" ", "")
                content = content.replace("u3000", "")

                content = content.strip()

                f.write(content)

                f.write('*', 30)

    def run(self):
        for page in range(self.start_page, self.end_page + 1):
            url = "http://www.neihan8.com/article/list_5_{}.html".format(str(page))
            print("正在下载第{}页".format(str(page)))

            html = self.loadPage(url)
            item_list = self.screenPage(html)
            self.writePage(item_list)


if __name__ == '__main__':
    start_page = int(input("请输入您需要爬取的起始页："))

    end_page = int(input("请输入您需要爬取的终止页："))
    mySpider = Spider(start_page, end_page)

    mySpider.run()
