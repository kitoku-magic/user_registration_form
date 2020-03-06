from src.controller import *

class controller:
    def __init__(self):
        self.__request = request
        self.__response_data = {}
        self.__template_file_name = ''
    def get_request(self):
        return self.__request
    def set_request_data(self, request_data):
        self.__request_data = request_data
    def get_request_data(self):
        return self.__request_data
    def add_response_data(self, name, value):
        self.__response_data[name] = value
    def set_template_file_name(self, template_file_name):
        self.__template_file_name = template_file_name
    def run(self):
        r = None
        try:
            self.execute()

            template = setting.app.jinja_environment.get_template(self.__template_file_name + '.html')
            http_response = template.render({'res': self.__response_data})

            r = make_response(http_response)
            #r.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
            #r.headers['Pragma'] = 'no-cache'
            #r.headers['Expires'] = '0'
        except custom_exception as e:
            setting.app.logger.exception('{}'.format(e))
            if 2 <= len(e.args):
                show_error_message = e.args[1]
            else:
                show_error_message = '予期しないエラーが発生しました。\nブラウザの戻るボタンで前ページにお戻り下さい。'
            self.add_response_data('title', 'エラー')
            self.add_response_data('show_error_message', show_error_message)
            template = setting.app.jinja_environment.get_template('error.html')
            http_response = template.render({'res': self.__response_data})
            r = make_response(http_response)
        except Exception as e:
            setting.app.logger.exception('{}'.format(e))
            show_error_message = '予期しないエラーが発生しました。\nブラウザの戻るボタンで前ページにお戻り下さい。'
            self.add_response_data('title', 'エラー')
            self.add_response_data('show_error_message', show_error_message)
            template = setting.app.jinja_environment.get_template('error.html')
            http_response = template.render({'res': self.__response_data})
            r = make_response(http_response)
        finally:
            return r
    def create_csrf_token(self):
        csrf_token = secrets.token_hex(64)
        session['csrf_token'] = csrf_token
        self.add_response_data('csrf_token', csrf_token)
    def check_csrf_token(self):
        post_csrf_token = self.get_request().form.get('csrf_token', type=str)
        session_csrf_token = session.get('csrf_token')
        session.pop('csrf_token', None)
        if post_csrf_token is not None and session_csrf_token is not None:
            if post_csrf_token == session_csrf_token:
                return True
            else:
                raise custom_exception('トークンが一致しません', '不正なリクエストです。')
        else:
            raise custom_exception('トークンが設定されていません', '不正なリクエストです。')
