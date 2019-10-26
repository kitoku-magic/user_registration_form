import os
import sys

from flask import Flask
from jinja2 import FileSystemLoader
import uwsgi
from uwsgidecorators import filemon

base_path = '/opt/app/user_registration_form/python'

# クラスのインポート
sys.path.append(base_path + '/src/')

from controller.user_registration.user_registration_first_input_controller import user_registration_first_input_controller
from controller.user_registration.user_registration_first_complete_controller import user_registration_first_complete_controller

# ファイルの変更を検知したら、uwsgiを再起動する
#target_directories = [
#    base_path + '/src',
#    base_path + '/src/controller',
#    base_path + '/src/controller/user_registration',
#    base_path + '/template',
#    base_path + '/template/user_registration',
#    base_path + '/webroot',
#    base_path + '/webroot/static',
#    base_path + '/webroot/static/css',
#    base_path + '/webroot/static/script',
#]
#for target_directory in target_directories:
#    filemon(target_directory)(uwsgi.reload)

app = Flask(__name__)
# 設定ファイルから情報読み込み
app.config.from_pyfile(base_path + '/src/config/config.py')

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
