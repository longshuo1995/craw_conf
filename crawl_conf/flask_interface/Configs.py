from ExtractTools import Extract
import SearchTools
from pymongo import MongoClient


class Config(object):
    host = "192.168.1.178"
    port = 10085


class ToolClassManage(object):
    SearchTools = SearchTools.SearchTools


class ToolObjMange(object):
    extract_tool = Extract()

'''
db.createUser({user:"zhfr_mongodb_root",pwd:"zkfr_DUBA@0406mgdb#com",roles:["userAdminAnyDatabase", db: "admin"]})
'''


class MongoConfig(object):
    db_web_config = "website_config"
    tb_url_seed = "url_seed"
    port = 38228
    mongo_username = "zhfr_mongodb_root"
    mongo_password = 'zkfr_DUBA@0406mgdb#com'
    # conn = MongoClient(host=Config.host, port=port, username=mongo_username, password=mongo_password)
    conn = MongoClient(host=Config.host)
    db_config = conn.website_config
    col_special_web_config = db_config.special_web_config

    @staticmethod
    def get_table(db_name, table_name):
        return eval("MongoConfig.conn.%s.%s" % (db_name, table_name))


if __name__ == '__main__':
    MongoConfig.col_special_web_config.insert_one({
        "name": 'zs',
        "age": 11
    })
