# 正则表达式的基本方法
import re
# 搜索和匹配
match1 = re.search(r'[1-9]\d{5}', 'BIT 100081')
match2 = re.match(r'[1-9]\d{5}', '100081 BIT')  # 从开始位置进行匹配
if match1:
    print(match1.group(0))
if match2:
    print(match2.group(0))
# 查找全部并返回列表
ls = re.findall(r'[1-9]\d{5}', 'BIT100081 TSU100084')
print(ls)
# 分割
sp1 = re.split(r'[1-9]\d{5}', 'BIT100081 TSU100084')
sp2 = re.split(r'[1-9]\d{5}', 'BIT100081 TSU100084', maxsplit = 1)
print(sp1)
print(sp2)
# 迭代
for m in re.finditer(r'[1-9]\d{5}', 'BIT100081 TSU100084'):
    if m:
        print(m.group(0))
# 替换
sub1 = re.sub(r'[1-9]\d{5}', ':zipcode', 'BIT100081 TSU100084')
print(sub1)
# match对象的属性和方法
m = re.search(r'[1-9]\d{5}', 'BIT100081 TSU100084')
print(m.string)
print(m.re)
print(m.pos)
print(m.endpos)
print(m.group(0))  # match对象只包括一次匹配对象的结果
print(m.start())
print(m.end())
print(m.span())