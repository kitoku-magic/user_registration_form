use `user_registration_form`;


drop table if exists `single_select_category`;

create table `single_select_category` (
  `single_select_category_id` bigint unsigned NOT NULL AUTO_INCREMENT comment '単一選択項目カテゴリーID',
  `name` varbinary(48) DEFAULT '' NOT NULL comment '単一選択項目カテゴリー名',
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP NOT NULL comment '作成日時',
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP NOT NULL comment '更新日時',
  PRIMARY KEY(`single_select_category_id`)
) ENGINE=InnoDB comment='単一選択項目カテゴリーマスタ';


drop table if exists `single_select`;

create table `single_select` (
  `single_select_id` bigint unsigned NOT NULL AUTO_INCREMENT comment '単一選択項目ID',
  `single_select_category_id` bigint unsigned DEFAULT 0 NOT NULL comment '単一選択項目カテゴリーID',
  `name` varbinary(48) DEFAULT '' NOT NULL comment '単一選択項目名',
  `value` varbinary(48) DEFAULT '' NOT NULL comment '単一選択項目値',
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP NOT NULL comment '作成日時',
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP NOT NULL comment '更新日時',
  PRIMARY KEY(`single_select_id`),
  CONSTRAINT fk_single_select_single_select_category_id FOREIGN KEY (single_select_category_id)
  REFERENCES single_select_category (single_select_category_id)
  ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB comment='単一選択項目マスタ';


drop table if exists `multiple_select_category`;

create table `multiple_select_category` (
  `multiple_select_category_id` bigint unsigned NOT NULL AUTO_INCREMENT comment '複数選択項目カテゴリーID',
  `name` varbinary(48) DEFAULT '' NOT NULL comment '複数選択項目カテゴリー名',
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP NOT NULL comment '作成日時',
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP NOT NULL comment '更新日時',
  PRIMARY KEY(`multiple_select_category_id`)
) ENGINE=InnoDB comment='複数選択項目カテゴリーマスタ';


drop table if exists `multiple_select`;

create table `multiple_select` (
  `multiple_select_id` bigint unsigned NOT NULL AUTO_INCREMENT comment '複数選択項目ID',
  `multiple_select_category_id` bigint unsigned DEFAULT 0 NOT NULL comment '複数選択項目カテゴリーID',
  `name` varbinary(48) DEFAULT '' NOT NULL comment '複数選択項目名',
  `value` varbinary(48) DEFAULT '' NOT NULL comment '複数選択項目値',
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP NOT NULL comment '作成日時',
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP NOT NULL comment '更新日時',
  PRIMARY KEY(`multiple_select_id`),
  CONSTRAINT fk_multiple_select_multiple_select_category_id FOREIGN KEY (multiple_select_category_id)
  REFERENCES multiple_select_category (multiple_select_category_id)
  ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB comment='複数選択項目マスタ';


drop table if exists `user`;

create table `user` (
  `user_id` bigint unsigned NOT NULL AUTO_INCREMENT comment 'ユーザーID',
  `mail_address` varbinary(128) DEFAULT '' NOT NULL comment 'メールアドレス',
  `password` varbinary(256) DEFAULT '' NOT NULL comment 'パスワード',
  `last_name` varbinary(24) DEFAULT '' NOT NULL comment '苗字',
  `first_name` varbinary(24) DEFAULT '' NOT NULL comment '名前',
  `last_name_hiragana` varbinary(48) DEFAULT '' NOT NULL comment '苗字（ひらがな）',
  `first_name_hiragana` varbinary(48) DEFAULT '' NOT NULL comment '名前（ひらがな）',
  `sex_id` tinyint unsigned DEFAULT 0 NOT NULL comment '性別ID',
  `birth_year` smallint unsigned DEFAULT 0 NOT NULL comment '生年',
  `birth_month` tinyint unsigned DEFAULT 0 NOT NULL comment '生月',
  `birth_day` tinyint unsigned DEFAULT 0 NOT NULL comment '生日',
  `zip_code_before` varbinary(8) DEFAULT '' NOT NULL comment '郵便番号（前半）',
  `zip_code_after` varbinary(8) DEFAULT '' NOT NULL comment '郵便番号（後半）',
  `prefectures_id` tinyint unsigned DEFAULT 0 NOT NULL comment '都道府県ID',
  `city_street_address` varbinary(192) DEFAULT '' NOT NULL comment '市区町村・丁目・番地',
  `building_room_address` varbinary(192) DEFAULT '' NOT NULL comment '建物名・室名',
  `telephone_number_first` varbinary(8) DEFAULT '' NOT NULL comment '電話番号（最初）',
  `telephone_number_middle` varbinary(8) DEFAULT '' NOT NULL comment '電話番号（中間）',
  `telephone_number_last` varbinary(8) DEFAULT '' NOT NULL comment '電話番号（最後）',
  `job_id` tinyint unsigned DEFAULT 0 NOT NULL comment '職業ID',
  `job_other` varbinary(48) DEFAULT '' NOT NULL comment '職業その他',
  `is_latest_news_hoped` tinyint(1) unsigned DEFAULT 0 NOT NULL comment '最新情報の希望状況',
  `file_name` varbinary(192) DEFAULT '' NOT NULL comment 'ファイル名',
  `file_path` varbinary(512) DEFAULT '' NOT NULL comment 'ファイルパス',
  `remarks` BLOB NOT NULL comment '備考',
  `is_personal_information_provide_agreed` tinyint(1) unsigned DEFAULT 0 NOT NULL comment '個人情報提供の同意状況',
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP NOT NULL comment '作成日時',
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP NOT NULL comment '更新日時',
  PRIMARY KEY(`user_id`)
) ENGINE=InnoDB comment='ユーザー';


drop table if exists `user_single_select`;

create table `user_single_select` (
  `user_id` bigint unsigned DEFAULT 0 NOT NULL comment 'ユーザーID',
  `single_select_id` bigint unsigned DEFAULT 0 NOT NULL comment '単一選択項目ID',
  -- `is_selected` tinyint(1) DEFAULT 0 NOT NULL comment '選択済み状態',
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP NOT NULL comment '作成日時',
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP NOT NULL comment '更新日時',
  PRIMARY KEY(`user_id`, `single_select_id`),
  CONSTRAINT fk_user_single_select_user_id FOREIGN KEY (user_id)
  REFERENCES `user` (user_id)
  ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT fk_user_single_select_single_select_id FOREIGN KEY (single_select_id)
  REFERENCES `single_select` (single_select_id)
  ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB comment='ユーザー単一選択項目';


drop table if exists `user_multiple_select`;

create table `user_multiple_select` (
  `user_id` bigint unsigned DEFAULT 0 NOT NULL comment 'ユーザーID',
  `multiple_select_id` bigint unsigned DEFAULT 0 NOT NULL comment '複数選択項目ID',
  -- `is_selected` tinyint(1) DEFAULT 0 NOT NULL comment '選択済み状態',
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP NOT NULL comment '作成日時',
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP NOT NULL comment '更新日時',
  PRIMARY KEY(`user_id`, `multiple_select_id`),
  CONSTRAINT fk_user_multiple_select_user_id FOREIGN KEY (user_id)
  REFERENCES `user` (user_id)
  ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT fk_user_multiple_select_multiple_select_id FOREIGN KEY (multiple_select_id)
  REFERENCES `multiple_select` (multiple_select_id)
  ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB comment='ユーザー複数選択項目';
