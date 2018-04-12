import re
from Eval import Eval
res = re.compile('.*').search('http://www.baidu.com')
code = "[res.group(0)+'&pn=%s' % i for i in range(10)]"
ev = Eval()
result = ev.reserve_eval(res, code)
print(result)

