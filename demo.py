#给bs4调用demo使用
import requests
r = requests.get("http://python123.io/ws/demo.html")
demo = r.text
