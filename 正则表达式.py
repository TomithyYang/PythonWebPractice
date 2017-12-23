import re

# 函数式用法

# 匹配邮编

# search只会搜索第一个
search = re.search(r'[1-9]\d{5}', 'BIT100081 TSU100084')
print (search.group(0))

# match从每一段开头开始搜索
match = re.match(r'[1-9]\d{5}', '100081BIT TSU100084')
print (match.group(0))

list = re.findall(r'[1-9]\d{5}', '100081BIT TSU100084')
print (list) # 返回的是数组

# split
for i in range(4):
    list = re.split(r'[1-9]\d{5}', '100081BIT TSU100084' , maxsplit=i)
    print (list) # maxsplit控制分割个数

# finditer 返回迭代控制器
for m in re.finditer(r'[1-9]\d{5}', '100081BIT TSU100084'):
    if m:
        print (m.group(0))

# 类用法

pat = re.compile(r'[1-9]\d{5}')
print (pat.search('100081BIT TSU100084'))