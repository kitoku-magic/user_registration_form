from src.controller import *

class controller:
    def __init__(self):
        self.__request = request
        self.__response_data = {}
        self.__template_file_name = ''
    def get_request(self):
        return self.__request
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
            r.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
            r.headers['Pragma'] = 'no-cache'
            r.headers['Expires'] = '0'
        except custom_exception as e:
            setting.app.logger.exception('{}'.format(e))
            if 2 <= len(e.args):
                show_error_message = e.args[1]
            else:
                show_error_message = setting.app.config['SHOW_UNEXPECTED_ERROR']
            r = self.make_error_response(show_error_message)
        except Exception as e:
            setting.app.logger.exception('{}'.format(e))
            show_error_message = setting.app.config['SHOW_UNEXPECTED_ERROR']
            r = self.make_error_response(show_error_message)
        except:
            setting.app.logger.exception(traceback.format_exc())
            show_error_message = setting.app.config['SHOW_UNEXPECTED_ERROR']
            r = self.make_error_response(show_error_message)
        finally:
            return r
    def make_error_response(self, show_error_message):
        self.add_response_data('title', 'エラー')
        self.add_response_data('show_error_message', show_error_message)
        template = setting.app.jinja_environment.get_template('error.html')
        http_response = template.render({'res': self.__response_data})
        return make_response(http_response)
    def create_csrf_token(self):
        csrf_token = util.get_token(setting.app.config['SECRET_TOKEN_BYTE_LENGTH'])
        session['csrf_token'] = csrf_token
        self.add_response_data('csrf_token', csrf_token)
    def check_csrf_token(self):
        post_csrf_token = self.get_request().form.get('csrf_token', type=str)
        session_csrf_token = session.get('csrf_token')
        session.pop('csrf_token', None)
        if post_csrf_token is not None and session_csrf_token is not None:
            if True == secrets.compare_digest(post_csrf_token, session_csrf_token):
                return True
            else:
                raise custom_exception(setting.app.config['TOKEN_NOT_EQUAL_ERROR'])
        else:
            raise custom_exception(setting.app.config['TOKEN_NOT_SETTING_ERROR'])
    def set_template_common_data(self, title, template_file_name):
        self.add_response_data('title', title)
        self.set_template_file_name(template_file_name)
