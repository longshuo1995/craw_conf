from pymysql import connect


class SearchTools(object):
    mysql_host = '192.168.1.193'
    port = 3306
    user = "root"
    password = "Zkfr_duba@0623."
    database = "zkdp"
    conn = connect(host=mysql_host, port=port, user=user, password=password, database=database, charset='utf8')
    query_key_sql = 'select DISTINCT(key_word) from keyword'

    @staticmethod
    def get_key():
        cursor = SearchTools.conn.cursor()
        cursor.execute(SearchTools.query_key_sql)
        res = cursor.fetchall()
        final_result = [' '.join(i).strip() for i in res]
        final_result = [i for i in final_result if i]
        return final_result

