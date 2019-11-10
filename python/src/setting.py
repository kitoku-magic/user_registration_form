import os

from flask import Flask
from flask_mail import Mail
from jinja2 import FileSystemLoader

from src.database import db
from src.controller.user_registration.user_registration_first_input_controller import user_registration_first_input_controller
from src.controller.user_registration.user_registration_first_complete_controller import user_registration_first_complete_controller

base_path = '/opt/app/user_registration_form/python'

config_type = {
    'testing':  'src.config.testing',
    'development':  'src.config.development',
    'production': 'src.config.production',
    'default': 'src.config.development'
}

sensitive_config_type = {
    'testing':  'src.instance.testing',
    'development':  'src.instance.development',
    'production': 'src.instance.production',
    'default': 'src.instance.development'
}

app = Flask(__name__)
# 設定ファイルから情報読み込み
app.config.from_object(config_type.get(os.getenv('FLASK_APP_ENV', 'default')))
app.config.from_object(sensitive_config_type.get(os.getenv('FLASK_APP_ENV', 'default')))

# jinja2のtemplateディレクトリの場所を変更する
# 省略した場合はこのファイルと同階層の "templates" になる
app.jinja_loader = FileSystemLoader(
    os.path.join(base_path, 'template')
)

mail = Mail()

db.init_app(app)
mail.init_app(app)

# 各リクエストに応じた処理を実行
@app.route('/', methods=['GET'])
def index():
    obj = user_registration_first_input_controller()
    return obj.run()
@app.route('/user_registration/first_complete', methods=['POST'])
def user_registration_first_complete():
    obj = user_registration_first_complete_controller()
    return obj.run()
