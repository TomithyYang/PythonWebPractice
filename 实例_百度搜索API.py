import requests
url1 = "http://www.baidu.com/s"
url2 = "http://www.so.com/s"
keywords = "python"
kv1 = {"wd":keywords}
kv2 = {"q":keywords}
try:
    a = input("使用百度？yes/no")
    if (a == "yes"):
        url = url1
        kv = kv1
    else:
        url = url2
        kv = kv2

    r = requests.get(url, params=kv)
    r.raise_for_status
    r.encoding = r.apparent_encoding
    print(len(r.text))
except:
    print("爬取失败")
