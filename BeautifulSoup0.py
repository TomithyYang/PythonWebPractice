from bs4 import BeautifulSoup #引入BeautifulSoup库
soup = BeautifulSoup('<p>data</p>', 'html.parser') #将网页信息转变为BeautifulSoup变量
#soup2 = BeautifulSoup(open("D://demo.html"), "html.parser")

soupExample = BeautifulSoup("<p>中文</p>", "html.parser")
print (soupExample.p.string)
print (soupExample.prettify())