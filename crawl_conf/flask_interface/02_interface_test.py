import requests
import json
data = {
    "url": "http://www.baidu.com",
    "seed": {
        "article": {
            "field_name": "article",
            "field_rule": "//a/href",
            "rule_type": "xpath",
            "field_type": "article"
        },
        "create_time":
            {
                "field_name": "create_time",
                "field_rule": "//span",
                "rule_type": "xpath",
                "field_type": "create_time"
            }
    }
}

data = {'data': json.dumps(data)}
res = requests.post("http://127.0.0.1:10086/parse", data=data).text
print(json.loads(res))
