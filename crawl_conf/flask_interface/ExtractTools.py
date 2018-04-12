import requests
from lxml import etree
from bs4 import BeautifulSoup
from newspaper import Article
import re
import time


class Extract(object):
    def __init__(self):
        self.pattern_encode = re.compile("<meta [^>]*?charset=(.*?)[ |/|>]")
        self.pattern_field_rule = re.compile("【.*?】")
        self.user_agent = {
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Win64; x64; Trident/4.0)',
        }
        self.pattern_time = re.compile('(\D|^)(20\d{2})\D(\d{1,2})\D(\d{1,2})\D{1,4}(\d{1,2})\D(\d{1,2})($|\D)')
        self.special_field = {"url_list", "result_type"}

    def extract(self, url):
        a = Article(url, language='zh')
        a.download()
        a.parse()
        return a.text.split('\n')

    def convert_time_to_timestamp(self, row):
        return_list = False
        if isinstance(row, list):
            row = row[0]
            return_list = True

        if row.find('前') > 0:
            pass
        else:
            tm = self.pattern_time.search(row)
            dt = "%s-%s-%s %s:%s" % (tm.group(2), tm.group(3), tm.group(4), tm.group(5), tm.group(6))
            time_array = time.strptime(dt, '%Y-%m-%d %H:%M')
            result = str(int(time.mktime(time_array)) * 1000)
        if return_list:
            result = [result]
        return result

    def sougou_get_html(self, url):
        if url.find('weixin.sogou') > 0:
            html = ''
            while html.find('txt-box') < 0:
                print(url)
                print('again...')
                html = requests.get(url, headers=self.user_agent).text
            return [html, url]
        else:
            html = requests.get(url, headers=self.user_agent).text
            return [html, url]

    def parse_row_seed(self, base_url, seed):
        url = base_url
        seed = seed
        seed['url'] = url
        res = self.parse_seed(seed)
        if not res:
            return
        if not res[0].get("result_type") == "dynamic_url" or res[0].get("result_type") == "static_url":
            print('ok')
        try:
            if res[0].get("result_type") == "dynamic_url" or res[0].get("result_type") == "static_url":
                for son_url in res[0]["result"]:
                    self.parse_row_seed(son_url, seed["son_modes"][0])
            else:
                for result_item in res:
                    print(result_item["field_name"])
                    print(result_item["result"])
        except:
            print(111)

    def extract_html(self, url, header={}, data={}, method='get'):
        header = dict(self.user_agent, **header)
        if method == 'get':
            row = requests.get(url, headers=header)
        else:
            row = requests.post(url, data=data, headers=header)
        # code = chardet.detect(row.content)
        # html = row.content.decode(code['encoding']) if code.get('encoding') else row.text
        try:
            html = row.content.decode()
        except:
            try:
                html = row.content.decode('gbk')
            except:
                html = row.text
        return [html, row.url]

    def re_replace(self, row, re_rule, code):
        if not (re_rule and code):
            return row
        res = re.compile(re_rule).search(row)
        g = {'res': res}
        temp = eval(code, g)
        return temp

    def parse_item(self, url, html, seed_item, xhtml=None, soup=None):
        field_rules = self.pattern_field_rule.findall(seed_item['field_rule'])
        if not field_rules:
            field_rules.append(seed_item['field_rule'])
        keep_field = {'static_url', 'dynamic_url'}
        if seed_item['field_type'] in keep_field:
            result_type = seed_item['field_type']
        else:
            result_type = 'end'
        # 源转换
        if(seed_item["source_type"]) == "html":
            html = html or self.extract_html(url)[0]
            base_row = html
        elif(seed_item["source_type"]) == "url":
            base_row = self.re_find(seed_item['field_rule'], url)
        # rule解析
        # db.website_config.getCollectionInfos()
        if not field_rules[0] and len(field_rules) == 1:
            result = {
                'field_name': seed_item['field_name'],
                'result': [],
                'result_type': result_type
            }
        elif seed_item['rule_type'] == 'xpath':
            xhtml = xhtml or etree.HTML(base_row)
            for field in field_rules:
                res = xhtml.xpath(field)
                if res and (not isinstance(res[0], str)):
                    res = [item.xpath('string(.)') for item in res]
                if res:
                    result = {'field_name': seed_item['field_name'], 'result': self.re_replace(res, seed_item['replace'][0], seed_item['replace'][1]), 'result_type': result_type}
                    break
        elif seed_item['rule_type'] == 'bs4':
            soup = soup or BeautifulSoup(base_row)
            for field in field_rules:
                res = soup.select(field)
                if res:
                    result = {'field_name': seed_item['field_name'], 'result': self.re_replace(res, seed_item['replace'][0], seed_item['replace'][1]), 'result_type': result_type}
                    break
        elif seed_item['rule_type'] == 're':
            for field in field_rules:
                res = self.re_find(field, base_row)
                result = self.re_replace(res, seed_item['replace'][0], seed_item['replace'][1])
                if res:
                    result = {
                        'field_name': seed_item['field_name'],
                        'result': result,
                        'result_type': result_type}
                    break
        # 特殊字段处理（）
        if seed_item['field_type'] == 'article' and not result['result']:
            result['result'] = self.extract(url)
        if seed_item['field_type'] == "create_time":
            result['result'] = [self.convert_time_to_timestamp(result['result'])]
        return [result, html, xhtml, soup]

    def re_find(self, re_rule, row):
        if not re_rule:
            return row
        temp_result = re.compile(re_rule).search(row)
        return temp_result.group(0) if temp_result else ''

    def parse_seed(self, seed):
        model = seed['mode_data']
        url = seed['url']
        html = None
        xhtml = None
        soup = None
        total_fields = []
        for field in list(model.keys()):
            if field not in self.special_field:
                temp_res, html, xhtml, soup = self.parse_item(url, html, model[field], xhtml, soup)
                total_fields.append(temp_res)
        return total_fields


