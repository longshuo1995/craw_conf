from flask import Flask, request
import json
# import Configs_local as Configs
import Configs

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/insert', methods=['POST'])
def insert_seed():
    data = request.values.get('data')
    data = json.loads(data)
    print(data)
    data['seed'] = json.dumps(data['seed'])
    Configs.MongoConfig.col_special_web_config.insert_one(data)


@app.route('/parse', methods=['POST'])
def resolve_seed():
    data = request.values.get('data')
    data = json.loads(data)
    res = Configs.ToolObjMange.extract_tool.parse_seed(data)
    return json.dumps(res)


# @app.route('/insert', methods=['POST'])
# def insert_cfg():
#     seed = request.values.get('data')
#     seed = json.loads(seed)
#     seed['seed'] = json.dumps(seed['seed'])
#     conn = Configs_local.MongoConfig.get_table(Configs.MongoConfig.db_web_config, Configs.MongoConfig.tb_url_seed)
#     conn.insert_one(seed)
#     return ""


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=Configs.Config.port)
