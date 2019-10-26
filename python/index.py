import os
import sys

from flask import Flask
from jinja2 import FileSystemLoader

base_path = '/opt/app/user_registration_form/python'

# クラスのインポート
sys.path.append(base_path + '/src/')

from controller.user_registration.user_registration_first_input_controller import user_registration_first_input_controller
from controller.user_registration.user_registration_first_complete_controller import user_registration_first_complete_controller

config_type = {
    'testing':  'config.testing',
    'development':  'config.development',
    'production': 'config.production',
    'default': 'config.development'
}

app = Flask(__name__, instance_relative_config=True)
# 設定ファイルから情報読み込み
app.config.from_object(config_type.get(os.getenv('FLASK_APP_ENV', 'default')))
app.config.from_pyfile('sensitive_data.py', silent=False)

# jinja2のtemplateディレクトリの場所を変更する
# 省略した場合はこのファイルと同階層の "templates" になる
app.jinja_loader = FileSystemLoader(
    os.path.join(base_path, 'template')
)

# 各リクエストに応じた処理を実行
@app.route('/', methods=['GET'])
def index():
    obj = user_registration_first_input_controller()
    return obj.run()
@app.route('/user_registration/first_complete', methods=['POST'])
def user_registration_first_complete():
    obj = user_registration_first_complete_controller()
    return obj.run()

if __name__ == '__main__':
    app.run()
