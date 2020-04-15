import logging
import os
from flask import Flask
from flask_mail import Mail
from jinja2 import Environment, FileSystemLoader
from logging.handlers import RotatingFileHandler

from src.controller.user_registration.user_registration_first_input_controller import user_registration_first_input_controller
from src.controller.user_registration.user_registration_first_complete_controller import user_registration_first_complete_controller
from src.controller.user_registration.user_registration_input_controller import user_registration_input_controller
from src.controller.user_registration.user_registration_confirm_controller import user_registration_confirm_controller
from src.controller.user_registration.user_registration_complete_controller import user_registration_complete_controller
from src.custom_filter import nl2br
from src.database import init_db

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

# ログの設定
handler = RotatingFileHandler(
    base_path + '/log/app.log',
    maxBytes=app.config['LOG_MAX_BYTES'],
    backupCount=app.config['LOG_BACKUP_COUNT']
)
handler.setFormatter(logging.Formatter("[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s"))
handler.setLevel(app.config['LOG_LEVEL'])

# ロガーを設定
app.logger.addHandler(handler)

# jinja2のtemplateディレクトリの場所を変更する
# 省略した場合はこのファイルと同階層の "templates" になる
jinja_environment = Environment(
    loader=FileSystemLoader(os.path.join(base_path, 'template')),
    autoescape=True,
)
jinja_environment.filters['nl2br'] = nl2br
app.jinja_environment = jinja_environment

# メール
mail = Mail()
mail.init_app(app)

# DB
app = init_db(app)

# 各リクエストに応じた処理を実行
@app.route('/', methods=['GET'])
def index():
    obj = user_registration_first_input_controller()
    return obj.run()
@app.route('/user_registration/first_complete', methods=['POST'])
def user_registration_first_complete():
    obj = user_registration_first_complete_controller()
    return obj.run()
@app.route('/user_registration/input', methods=['GET'])
def user_registration_input():
    obj = user_registration_input_controller()
    return obj.run()
@app.route('/user_registration/confirm', methods=['POST'])
def user_registration_confirm():
    obj = user_registration_confirm_controller()
    return obj.run()
@app.route('/user_registration/complete', methods=['POST'])
def user_registration_complete():
    obj = user_registration_complete_controller()
    return obj.run()
