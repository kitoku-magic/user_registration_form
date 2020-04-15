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

db = SQLAlchemy(model_class=declarative_base(cls=model.Model, metaclass=DeclarativeABCMeta))

def init_db(app):
    db.init_app(app)
    app.app_context().push()

    # 静的プリペアドステートメントを使う為に、cursorをカスタマイズする為
    db.engine.dialect.execution_ctx_cls = custom_sql_execution_context

    # 何度も実行する為、事前にコンパイル
    sql_parameter_replace_pattern = re.compile('%\(.+?\)s')

    @event.listens_for(db.engine, 'before_cursor_execute', retval=True)
    def change_prepared_statement(conn, cursor, statement, parameters, context, executemany):
        statement = sql_parameter_replace_pattern.sub('%s', statement)
        parameters = tuple(parameters.values())
        return statement, parameters

    return app
