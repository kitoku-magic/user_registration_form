from python_library.src.custom_sqlalchemy.database import engine
from python_library.src.custom_sqlalchemy.database import session
from src.application import app

@app.after_request
def after_request(response):
    session.remove()
    # session.remove()だけだと、次のリクエストで同じコネクションを使い回していた
    engine.dispose()
    return response

# 各リクエストに応じた処理を実行
@app.route('/', methods=['GET'])
def index():
    from src.controller.user_registration.user_registration_first_input_controller import user_registration_first_input_controller
    obj = user_registration_first_input_controller()
    return obj.run()
@app.route('/user_registration/first_complete', methods=['POST'])
def user_registration_first_complete():
    from src.controller.user_registration.user_registration_first_complete_controller import user_registration_first_complete_controller
    obj = user_registration_first_complete_controller()
    return obj.run()
@app.route('/user_registration/input', methods=['GET'])
def user_registration_input():
    from src.controller.user_registration.user_registration_input_controller import user_registration_input_controller
    obj = user_registration_input_controller()
    return obj.run()
@app.route('/user_registration/confirm', methods=['POST'])
def user_registration_confirm():
    from src.controller.user_registration.user_registration_confirm_controller import user_registration_confirm_controller
    obj = user_registration_confirm_controller()
    return obj.run()
@app.route('/user_registration/complete', methods=['POST'])
def user_registration_complete():
    from src.controller.user_registration.user_registration_complete_controller import user_registration_complete_controller
    obj = user_registration_complete_controller()
    return obj.run()
