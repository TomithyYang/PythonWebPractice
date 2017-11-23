# -*- coding:utf-8 -*- #
import requests
url = "https://article.jd.com/?id=448246"


try:
    kv = {"User-Agent": "Mozilla/5.0"} #提供用户使用浏览器名称
    r = requests.get(url, headers = kv) #将使用的浏览器名称添加，使爬虫成功
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print (r.text)
except:
    print (u"爬取失败")