import re
from abc import ABCMeta
from flask_sqlalchemy import SQLAlchemy, model
from sqlalchemy import event
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from src.custom_sql_execution_context import custom_sql_execution_context

class DeclarativeABCMeta(DeclarativeMeta, ABCMeta):
    """
    SQLAlchemyの基底クラスを抽象クラス化する為の定義
    """
    pass

db = SQLAlchemy(
    model_class=declarative_base(cls=model.Model, metaclass=DeclarativeABCMeta)
)

def init_db(app):
    db.init_app(app)
    app.app_context().push()

    # 静的プリペアドステートメントを使う為に、cursorをカスタマイズする為
    db.engine.dialect.execution_ctx_cls = custom_sql_execution_context

    # セッションの設定
    session_options = app.config['SQLALCHEMY_SESSION_OPTIONS']
    session_options['bind'] = db.engine
    db.session.configure(**session_options)

    # 何度も実行する為、事前にコンパイル
    sql_parameter_replace_pattern = re.compile('%\(.+?\)s')

    @event.listens_for(db.engine, 'before_cursor_execute', retval=True)
    def change_prepared_statement(conn, cursor, statement, parameters, context, executemany):
        """
        SQL実行前に静的プリペアドステートメントを実行出来る様にSQLとパラメータを書き換える
        """
        statement = sql_parameter_replace_pattern.sub('%s', statement)
        parameters = tuple(parameters.values())
        return statement, parameters

    return app
