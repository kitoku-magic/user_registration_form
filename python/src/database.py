from abc import ABCMeta
from flask_sqlalchemy import SQLAlchemy, model
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base

class DeclarativeABCMeta(DeclarativeMeta, ABCMeta):
    """
    SQLAlchemyの基底クラスを抽象クラス化する為の定義
    """
    pass

db = SQLAlchemy(model_class=declarative_base(cls=model.Model, metaclass=DeclarativeABCMeta))
