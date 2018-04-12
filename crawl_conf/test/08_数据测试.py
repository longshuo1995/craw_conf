import requests
url = 'http://127.0.0.1:8000/check'
data = {
    'data': '{"base_url":"http://www.ifeng.com/","url":"http://www.ifeng.com/","temp_parent":{"url_list":["http://www.ifeng.com/"],"result_type":"static_url","model":{}}}'
}

html = requests.post(url, data).text
with open('file.html', 'w') as f:
    f.write(html)

