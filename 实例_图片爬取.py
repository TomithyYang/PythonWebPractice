import requests
ua = {"User-Agent":"Mozilla/5.0"}
import os
url = "http://pic70.nipic.com/file/20150626/610812_114205201599_2.jpg"
root = "D://PythonWeb//"
path = root + url.split('/')[-1]

try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url, headers = ua)
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print("文件保存成功")
    else:
        print("文件已存在")        
except:
    print ("爬取失败")

