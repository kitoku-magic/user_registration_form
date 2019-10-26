import secrets

from flask import render_template, request, make_response, session

class controller:
    __request = {}
    __post_data = {}
    __response_data = {}
    __template_file_name = ''
    def __init__(self):
        self.__request = request
        # リクエストされたデータを、扱いやすくする為に辞書型に変換する
        if self.__request.method == 'POST':
            fields = [k for k in self.__request.form]
            values = [self.__request.form[k] for k in self.__request.form]
            self.__post_data = dict(zip(fields, values))
    def get_request(self):
        return self.__request
    def get_post_data(self):
        return self.__post_data
    def set_response_data(self, name, value):
        self.__response_data[name] = value
    def set_template_file_name(self, template_file_name):
        self.__template_file_name = template_file_name
    def run(self):
        r = None
        try:
            self.execute()

            http_response = render_template(self.__template_file_name + '.html', res=self.__response_data)

            r = make_response(http_response)
            #r.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
            #r.headers['Pragma'] = 'no-cache'
            #r.headers['Expires'] = '0'
        except Exception as e:
            self.set_response_data('title', 'エラー')
            http_response = render_template('error.html', res=self.__response_data)
            r = make_response(http_response)
        finally:
            return r
    def create_csrf_token(self):
        csrf_token = secrets.token_hex(64)
        session['csrf_token'] = csrf_token
        self.set_response_data('csrf_token', csrf_token)
    def check_csrf_token(self):
        post_csrf_token = self.get_request().form.get('csrf_token', type=str)
        session_csrf_token = session.get('csrf_token')
        if post_csrf_token is not None and session_csrf_token is not None:
            if post_csrf_token == session_csrf_token:
                return True
            else:
                raise Exception('トークンが一致しません')
        else:
            raise Exception('トークンが設定されていません')
