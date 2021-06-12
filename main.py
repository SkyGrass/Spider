import sys
import json
import urllib.request as HttpUtils
from bs4 import BeautifulSoup
import py
import json

urls = []


def preurl(provinces):
    for province in provinces:
        path = py.getFirsLetter(province)
        urls.append({
            'name':
            province,
            'path':
            path,
            'url':
            'http://www.sciencehr.net/uploads/ptgdxxmd/{0}.html'.format(path)
        })
    print(len(urls))
    return len(urls) > 0


def main(provinces):
    if (preurl(provinces)):
        list = []
        for item in urls: 
            url = item['url']
            province=item['name']
            html = HttpUtils.urlopen(url).read()
            soup = BeautifulSoup(html, "lxml", from_encoding="gb18030")
            trs = soup.select('.wenzi > table > tr')

            for index, row in enumerate(trs):
                if (index > 1):
                    list.append({
                        'province':
                        province,
                        'code':
                        row.find_all("td")[2].get_text(),
                        'name':
                        row.find_all("td")[1].get_text(),
                        'level':
                        row.find_all("td")[5].get_text(),
                        'city':
                        row.find_all("td")[4].get_text(),
                        'isclosed':
                        False,
                        "remark":
                        "".join(row.find_all("td")[6].get_text().split())
                    })
        writeTxt(list)


def writeTxt(list):
    with open("data.json", "w", encoding='utf-8') as f:
        f.write(json.dumps(list, ensure_ascii=False))


if __name__ == '__main__':
    p = [
        "北京", "上海", "天津", "重庆", "河北", "山西", "内蒙古", "安徽", "山东", "江苏", "福建",
        "江西", "浙江", "广东", "广西", "海南", "辽宁", "吉林", "黑龙江", "河南", "湖南", "湖北",
        "陕西", "宁夏", "甘肃", "青海", "新疆", "四川", "贵州", "云南", "西藏"
    ]
    main(p)
