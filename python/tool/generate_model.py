# モデルクラスを自動生成するプログラム

import os
import sys
import shutil

current_directory = os.path.dirname(__file__)

sys.path.append(os.path.join(current_directory, '../src'))

from instance import config

from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.inspection import inspect

Base = automap_base()

engine = create_engine(config.SQLALCHEMY_DATABASE_URI)
shutil.rmtree(current_directory + '/../src/instance/__pycache__')
Base.prepare(engine, reflect=True)

# 1ファイル、1テーブルの関係
for table in Base.classes:
    inspect_table = inspect(table)
    local_table_name = inspect_table.persist_selectable.name
    # 自動生成するファイル名とクラス名は、オリジナルから変えておく
    local_class_name = local_table_name + '_base'
    base_path = current_directory + '/../src/model/generate/'
    base_path += local_class_name + '.py'
    body = ''
    f = open(base_path, mode='w')
    body += 'from src.model import *\n'
    body += '\n'
    body += 'class ' + local_class_name + '('
    length_body = ''
    property_body = ''
    created_at_body = ''
    updated_at_body = ''
    columns = inspect_table.persist_selectable.columns._all_columns
    for column in columns:
        column_attr_list = []
        # データ型の設定
        data_type = column.type.__class__.__name__ + '('
        data_type_attr_list = []
        if hasattr(column.type, 'unsigned') and column.type.unsigned is not None:
            data_type_attr_list.append('unsigned = ' + str(column.type.unsigned))
        if hasattr(column.type, 'length') and column.type.length is not None:
            # 桁数の数値は、定数にする
            data_type_attr_list.append(column.name + '_length')
            length_body += '    ' + column.name + '_length = ' + str(column.type.length) + '\n'
        data_type += ', '.join(data_type_attr_list) + ')'
        column_attr_list.append(data_type)
        # 外部キーの設定
        if hasattr(column, 'foreign_keys') and len(column.foreign_keys) > 0:
            for foreign_key in column.foreign_keys:
                column_attr_list.append("model.get_db_instance(model).ForeignKey('" + foreign_key._colspec + "')")
        # NULLの設定
        if hasattr(column, 'nullable') and column.nullable is not None:
            column_attr_list.append('nullable = ' + str(column.nullable))
        # DEFAULTの設定（クラスの中の値に入っている）
        if hasattr(column, 'server_default') and \
           column.server_default is not None and \
           hasattr(column.server_default, 'arg') and \
           column.server_default.arg.__class__.__name__ == 'TextClause':
            column_attr_list.append('server_default = ' + str(column.server_default.arg.text))
        # AUTO_INCREMENTの設定
        if hasattr(column, 'autoincrement') and column.autoincrement is True:
            column_attr_list.append('autoincrement = ' + str(column.autoincrement))
        # PRIMARY KEYの設定
        if hasattr(column, 'primary_key') and column.primary_key is True:
            column_attr_list.append('primary_key = ' + str(column.primary_key))
        # UNIQUE KEYの設定
        if hasattr(column, 'unique') and column.unique is True:
            column_attr_list.append('unique = ' + str(column.unique))
        # INDEXの設定
        if hasattr(column, 'index') and column.index is True:
            column_attr_list.append('index = ' + str(column.index))
        # コメントの設定
        if hasattr(column, 'comment') and column.comment is not None:
            column_attr_list.append("comment = '" + str(column.comment) + "'")
        # created_atとupdated_atが両方存在する場合は、専用のmixinを使うので、ここではまだ設定しない
        if column.name == 'created_at':
            created_at_body += '    ' + column.name + ' = model.get_db_instance(model).Column(' + ', '.join(column_attr_list) + ')\n'
        elif column.name == 'updated_at':
            updated_at_body += '    ' + column.name + ' = model.get_db_instance(model).Column(' + ', '.join(column_attr_list) + ')\n'
        else:
            property_body += '    ' + column.name + ' = model.get_db_instance(model).Column(' + ', '.join(column_attr_list) + ')\n'
    # created_atとupdated_atが両方存在するか調べる
    if created_at_body != '':
        if updated_at_body != '':
            body += 'timestamp_mixin, '
        else:
            property_body += created_at_body
    elif updated_at_body != '':
        property_body += updated_at_body
    body += 'model):\n'
    body += "    __tablename__ = '" + local_table_name + "'\n"
    body += length_body
    body += property_body
    # リレーションの設定
    relation_body = ''
    many_variables_suffix = '_collection'
    for prop in inspect_table.relationships:
        foreign_table_name = prop.mapper.persist_selectable.name
        foreign_class_name = foreign_table_name + '_base'
        # TODO: 1対1の場合、これでは動かなさそう
        if prop.backref is None:
            relation_body += '\n    ' + foreign_table_name + many_variables_suffix + " = model.get_db_instance(model).relationship('" + foreign_class_name + "', back_populates='" + local_table_name + "', cascade='save-update, merge, delete', uselist=True)"
        else:
            relation_body += '\n    ' + foreign_table_name + " = model.get_db_instance(model).relationship('" + foreign_class_name + "', back_populates='" + local_table_name + many_variables_suffix + "', uselist=False)"
    body += relation_body
    # コンストラクタの設定
    body += '\n    def __init__(self):\n'
    body += '        model.__init__(self)\n'
    f.write(body)
    f.close()
