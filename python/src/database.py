from abc import ABCMeta
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from flask_sqlalchemy import SQLAlchemy, model

class DeclarativeABCMeta(DeclarativeMeta, ABCMeta):
    pass

db = SQLAlchemy(model_class=declarative_base(cls=model.Model, metaclass=DeclarativeABCMeta))
