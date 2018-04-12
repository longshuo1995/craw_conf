import re

p = re.compile('【(.*?)】')
res = p.findall('xxx')
print(res)
