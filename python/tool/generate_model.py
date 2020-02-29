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

number_data_type_list = {
    'BIGINT' : True,
    'MEDIUMINT' : True,
    'SMALLINT' : True,
    'TINYINT' : True,
}

string_data_type_list = {
    'VARBINARY' : True,
    'BLOB' : True,
}

date_data_type_list = {
    'DATE' : True,
}

# 1ファイル、1テーブルの関係
for table in Base.classes:
    inspect_table = inspect(table)
    local_table_name = inspect_table.persist_selectable.name
    # 自動生成するファイル名とクラス名は、オリジナルから変えておく
    local_class_name = local_table_name + '_entity_base'
    base_path = current_directory + '/../src/model/entity/generate/'
    base_path += local_class_name + '.py'
    body = ''
    f = open(base_path, mode='w')
    body += 'from src.model.entity import *\n'
    body += 'from src.model.entity.generate import *\n'
    body += 'from src.model.repository import repository\n'
    body += '\n'
    body += 'class ' + local_class_name + '('
    length_body = ''
    property_list = []
    length_property_body = ''
    property_body = ''
    created_at_body = ''
    updated_at_body = ''
    is_use_timestamp_mixin = False
    columns = inspect_table.persist_selectable.columns._all_columns
    for column in columns:
        column_attr_list = []
        # データ型の設定
        data_type_name = column.type.__class__.__name__
        if data_type_name in number_data_type_list:
            property_list.append("        '" + column.name + "' : 0,")
        elif data_type_name in string_data_type_list:
            property_list.append("        '" + column.name + "' : '',")
        elif data_type_name in date_data_type_list:
            property_list.append("        '" + column.name + "' : '0001-01-01',")
        data_type = data_type_name + '('
        data_type_attr_list = []
        if hasattr(column.type, 'unsigned') and column.type.unsigned is not None:
            data_type_attr_list.append('unsigned = ' + str(column.type.unsigned))
        if hasattr(column.type, 'length') and column.type.length is not None:
            # 桁数の数値は、定数にする
            upper_column_name = column.name.upper()
            data_type_attr_list.append(local_class_name + '.__' + upper_column_name + '_LENGTH')
            length_body += '    __' + upper_column_name + '_LENGTH = ' + str(column.type.length) + '\n'
            length_property_body += '    def get_' + column.name + '_length(cls):\n'
            length_property_body += '        return ' + local_class_name + '.__' + upper_column_name + '_LENGTH\n'
        data_type += ', '.join(data_type_attr_list) + ')'
        column_attr_list.append(data_type)
        # 外部キーの設定
        if hasattr(column, 'foreign_keys') and len(column.foreign_keys) > 0:
            for foreign_key in column.foreign_keys:
                column_attr_list.append("repository.get_db_instance(repository).ForeignKey('" + foreign_key._colspec + "')")
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
            created_at_body += '    ' + column.name + ' = repository.get_db_instance(repository).Column(' + ', '.join(column_attr_list) + ')\n'
        elif column.name == 'updated_at':
            updated_at_body += '    ' + column.name + ' = repository.get_db_instance(repository).Column(' + ', '.join(column_attr_list) + ')\n'
        else:
            property_body += '    @declared_attr\n'
            property_body += '    def ' + column.name + '(cls):\n'
            property_body += '        return repository.get_db_instance(repository).Column(' + ', '.join(column_attr_list) + ')\n'
    # リレーションの設定
    relation_body = ''
    many_variables_suffix = '_collection'
    for prop in inspect_table.relationships:
        foreign_table_name = prop.mapper.persist_selectable.name
        foreign_class_name = foreign_table_name + '_entity'
        # TODO: 1対1の場合、これでは動かなさそう
        relation_body += '    @declared_attr\n'
        if prop.backref is None:
            relation_body += '    def ' + foreign_table_name + many_variables_suffix + '(cls):\n'
            relation_body += "        return repository.get_db_instance(repository).relationship('" + foreign_class_name + "', back_populates='" + local_table_name + "', cascade='save-update, merge, delete', uselist=True)\n"
            property_list.append("        '" + foreign_table_name + many_variables_suffix + "' : [],")
        else:
            relation_body += '    def ' + foreign_table_name + '(cls):\n'
            relation_body += "        return repository.get_db_instance(repository).relationship('" + foreign_class_name + "', back_populates='" + local_table_name + many_variables_suffix + "', uselist=False)\n"
            property_list.append("        '" + foreign_table_name + "' : [],")
    # created_atとupdated_atが両方存在するか調べる
    if created_at_body != '':
        if updated_at_body != '':
            body += 'timestamp_mixin_entity, '
            is_use_timestamp_mixin = True
        else:
            property_body += created_at_body
    elif updated_at_body != '':
        property_body += updated_at_body
    body += 'entity):\n'
    body += "    __abstract__ = True\n"
    body += length_body + '\n'
    body += '    def get_all_properties(self):\n'
    body += '        return {\n    ' + '\n    '.join(property_list) + '\n        }\n\n'
    if length_property_body != '':
        body += length_property_body + '\n'
    body += property_body
    body += relation_body + '\n'
    # コンストラクタの設定
    body += '    def __init__(self):\n'
    if is_use_timestamp_mixin == True:
        super_class_name = 'timestamp_mixin_entity'
    else:
        super_class_name = 'entity'
    body += '        ' + super_class_name + '.__init__(self)\n'
    f.write(body)
    f.close()