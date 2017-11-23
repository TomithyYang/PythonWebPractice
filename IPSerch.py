import requests
url = "http://m.ip138.com/ip.asp?ip="
url1 = "http://m.ip138.com/ip.asp"
try:
    ua = {"ip": '202.204.80.112'}
    r = requests.get(url +'202.204.80.112') #方法1
    r1 = requests.get(url1, params=ua) #方法2
    r.raise_for_status
    r1.raise_for_status
    r1.encoding = r1.apparent_encoding
    r.encoding = r.apparent_encoding

    print(r.text[-500:])

    print(r1.text[-500:])
except:
    print("爬取失败") 

       