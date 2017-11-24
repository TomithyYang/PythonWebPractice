from bs4 import BeautifulSoup
soup = BeautifulSoup('<p>data</p>', 'html.parser')
soup2 = BeautifulSoup(open("D://demo.html"), "html.parser")