
url = "http://weixin.sogou.com/weixin?type=2&ie=utf8&query=火灾 消防&page=0"
from ExtractTools import Extract
from lxml import etree
import requests
e = Extract()

user_agent = {
    'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding' : 'gzip, deflate',
    'Accept-Language' : 'zh-CN,zh;q=0.9,en;q=0.8',
    'Cache-Control' : 'max-age=0',
    'Cookie' : 'SUV=0021271775499BC15A620FCBBB7C9680; CXID=9A85F25519154E9EDACC7236C6AD475D; SUID=4AC1943D4B238B0A5A6AD744000C6ABB; ad=v$xQSkllll2zzHN9lllllVIhTkGlllll5BFxvkllll9llllllv7ll5@@@@@@@@@@; IPLOC=CN1100; ld=qkllllllll2zKQ8flllllVIdb5olllll5FJ7Zkllll9llllljylll5@@@@@@@@@@; LSTMV=242%2C74; LCLKINT=3402; ABTEST=0|1518169342|v1; JSESSIONID=aaaawNDzxMBae6qA-QQfw; weixinIndexVisited=1; SNUID=208ED3DFE2E784233936C591E26DDC5E; sct=3',
    'Host' : 'weixin.sogou.com',
    'Proxy-Connection' : 'keep-alive',
    'Upgrade-Insecure-Requests' : '1',
    'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36',
}

res = requests.get(url, headers=user_agent)
html = res.text
with open("test.html", 'w', encoding="utf-8") as f:
    f.write(html)
xhtml = etree.HTML(html)
result = xhtml.xpath("//h3//a/@href")
print(result)

