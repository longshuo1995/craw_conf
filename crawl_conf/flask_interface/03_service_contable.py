'''
1. 通过title， code 提取实时链接  以便用户能获取实时的原文链接（可以通过代理/多任务优化速度）
2. 为解决转载问题， 修复配置可视化配置器。
'''
import Configs
import time
import gevent


class IntervalSpider:
    def __init__(self):
        self.start_time_seconds = time.time()
        self.url_set = {"dynamic_url", "static_url"}

    def parse_urls(self, seed, url_list):
        for url in url_list:
            self.parse_item_helper(seed['model'], [url])

    def parse_item_helper(self, seed, url_list=None):
        if seed['result_type'] == "static_url" and url_list:
            return self.parse_urls(seed, url_list)
        elif seed['result_type'] in self.url_set:
            url_list = Configs.ToolObjMange.extract_tool.parse_seed(seed)
            print(url_list)

    def parse_item(self, item):
        seed = item.get('seed')
        db_name = item['db_name']
        source_spider = item['source_spider']
        result_type = item['result_type']
        urls = item['url_list'][0]
        self.parse_item_helper(seed, db_name, source_spider, result_type, )

    def get_differ_seconds(self):
        differ_seconds = int(self.start_time_seconds % (24 * 60 * 60))
        return differ_seconds

    def accord_time(self, interval):
        return self.get_differ_seconds() % interval < 10


if __name__ == '__main__':
    interval = IntervalSpider()
    res = interval.accord_time(60)
    print(res)
