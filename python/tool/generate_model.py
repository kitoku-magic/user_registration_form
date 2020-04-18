# モデルのエンティティクラスを自動生成するプログラム

import os
import shutil
import sys

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
    local_class_name = local_table_name + '_entity_base'
    base_path = current_directory + '/../src/model/entity/generate/'
    base_path += local_class_name + '.py'
    f = open(base_path, mode='w')
    entity_import_list = ['declared_attr', 'entity']
    entity_generate_import_list = ['Column', 'List', 'Type', 'TypeVar']
    length_body = ''
    length_property_body = ''
    property_body = ''
    created_at_body = ''
    updated_at_body = ''
    insert_column_name_list_body = '    def get_insert_column_name_list(self: Type[T]) -> List[str]:\n'
    insert_column_name_list_body += '        return ['
    update_column_name_list_body = '    def get_update_column_name_list(self: Type[T]) -> List[str]:\n'
    update_column_name_list_body += '        return ['
    is_use_timestamp_mixin = False
    columns = inspect_table.persist_selectable.columns._all_columns
    # 1カラムずつ処理
    for column in columns:
        column_attr_list = []
        # データ型の設定
        data_type_name = column.type.__class__.__name__
        # BLOBは、独自の拡張型にする
        if 'BLOB' == data_type_name:
            data_type_name = 'my_blob'
        # VARBINARYは、独自の拡張型にする
        if 'VARBINARY' == data_type_name:
            data_type_name = 'my_varbinary'
        data_type = data_type_name + '('
        data_type_attr_list = []
        if hasattr(column.type, 'unsigned') and column.type.unsigned is not None:
            data_type_attr_list.append('unsigned = ' + str(column.type.unsigned))
        if hasattr(column.type, 'length') and column.type.length is not None:
            # 桁数の数値は、定数にする
            upper_column_name = column.name.upper()
            data_type_attr_list.append(local_class_name + '.__' + upper_column_name + '_LENGTH')
            length_body += '    __' + upper_column_name + '_LENGTH: int = ' + str(column.type.length) + '\n'
            length_property_body += '    def get_' + column.name + '_length(cls: Type[T]) -> int:\n'
            length_property_body += '        return ' + local_class_name + '.__' + upper_column_name + '_LENGTH\n'
        data_type += ', '.join(data_type_attr_list) + ')'
        column_attr_list.append(data_type)
        # 外部キーの設定
        if hasattr(column, 'foreign_keys') and len(column.foreign_keys) > 0:
            for foreign_key in column.foreign_keys:
                column_attr_list.append("db.ForeignKey('" + foreign_key._colspec + "')")
        # NULLの設定
        if hasattr(column, 'nullable') and column.nullable is not None:
            column_attr_list.append('nullable = ' + str(column.nullable))
        # DEFAULTの設定（クラスの中の値に入っている）
        if hasattr(column, 'server_default') and \
           column.server_default is not None and \
           hasattr(column.server_default, 'arg') and \
           'TextClause' == column.server_default.arg.__class__.__name__:
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
        if 'created_at' == column.name:
            created_at_body += '    ' + column.name + ' = db.Column(' + ', '.join(column_attr_list) + ')\n'
        elif 'updated_at' == column.name:
            updated_at_body += '    ' + column.name + ' = db.Column(' + ', '.join(column_attr_list) + ')\n'
        else:
            property_body += '    @declared_attr\n'
            property_body += '    def ' + column.name + '(cls: Type[T]) -> Column:\n'
            property_body += '        return db.Column(' + ', '.join(column_attr_list) + ')\n'
        if data_type_name not in entity_import_list:
            entity_import_list.append(data_type_name)
        # 追加・更新可能カラムのリストを作成
        if hasattr(column, 'autoincrement') and column.autoincrement is True:
            continue
        insert_column_name_list_body += "'" + column.name + "', "
        if 'created_at' != column.name:
            update_column_name_list_body += "'" + column.name + "', "
    # リレーションの設定
    relation_body = ''
    many_variables_suffix = '_collection'
    for key in dir(inspect_table.relationships):
        # keyが「_」から始まらない場合は、リレーションプロパティ名が入っている
        if True == key.startswith('_'):
            continue
        prop = getattr(inspect_table.relationships, key)
        foreign_table_name = prop.mapper.persist_selectable.name
        foreign_class_name = foreign_table_name + '_entity'
        # リレーションが複数カラムかどうか
        if True == hasattr(prop.primaryjoin, 'clauses'):
            primaryjoin = "primaryjoin='" + prop.primaryjoin.operator.__name__ + "("
            for clause in prop.primaryjoin.clauses:
                primaryjoin += local_table_name + "_entity." + clause._orig[0].key + " == " + foreign_class_name + "." + clause._orig[1].key + ", "
            primaryjoin = primaryjoin.rstrip(', ') + ")', "
        else:
            primaryjoin = ''
        cascade = ",".join([x for x in sorted(prop._cascade)])
        # TODO: 1対1の場合、これでは動かなさそう
        relation_body += '    @declared_attr\n'
        if prop.backref is None:
            relation_body += '    def ' + foreign_table_name + many_variables_suffix + '(cls: Type[T]) -> RelationshipProperty:\n'
            relation_body += "        return db.relationship('" + foreign_class_name + "', " + primaryjoin + "back_populates='" + local_table_name + "', cascade='" + cascade + "', uselist=True)\n"
        else:
            relation_body += '    def ' + foreign_table_name + '(cls: Type[T]) -> RelationshipProperty:\n'
            relation_body += "        return db.relationship('" + foreign_class_name + "', " + primaryjoin + "back_populates='" + local_table_name + many_variables_suffix + "', cascade='" + cascade + "', uselist=False)\n"
        if 'RelationshipProperty' not in entity_generate_import_list:
            entity_generate_import_list.append('RelationshipProperty')
    timestamp_mixin_body = ''
    # created_atとupdated_atが両方存在するか調べる
    if '' != created_at_body:
        if '' != updated_at_body:
            timestamp_mixin_body += 'timestamp_mixin_entity, '
            is_use_timestamp_mixin = True
            entity_import_list.append('timestamp_mixin_entity')
        else:
            property_body += created_at_body
    elif '' != updated_at_body:
        property_body += updated_at_body
    body = ''
    body += 'from src.database import db\n'
    body += 'from src.model.entity import ' + ', '.join(entity_import_list) + '\n'
    body += 'from src.model.entity.generate import ' + ', '.join(entity_generate_import_list) + '\n'
    body += '\n'
    body += "T = TypeVar('T', bound='" + local_class_name + "')\n"
    body += '\n'
    body += 'class ' + local_class_name + '('
    body += timestamp_mixin_body
    body += 'entity):\n'
    body += '    """\n'
    body += '    ' + inspect_table.persist_selectable.comment + 'テーブルエンティティの基底クラス\n'
    body += '    """\n'
    body += "    __abstract__: bool = True\n"
    body += length_body + '\n'
    if '' != length_property_body:
        body += length_property_body + '\n'
    body += property_body
    body += relation_body + '\n'
    # コンストラクタの設定
    body += '    def __init__(self: Type[T]) -> None:\n'
    if True == is_use_timestamp_mixin:
        super_class_name = 'timestamp_mixin_entity'
    else:
        super_class_name = 'entity'
    body += '        ' + super_class_name + '.__init__(self)\n'
    body += '    def set_validation_setting(self: Type[T]) -> None:\n'
    body += '        pass\n'
    body += insert_column_name_list_body.rstrip(', ') + ']\n'
    body += update_column_name_list_body.rstrip(', ') + ']\n'
    f.write(body)
    f.close()
