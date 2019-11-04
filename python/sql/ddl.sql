use `user_registration_form_python`;


-- varbinary型で、全角文字が入りそうな列は、「許容文字数 * 4」の桁数にしています
drop table if exists `zip_address`;

CREATE TABLE `zip_address` (
  `zip_address_id` mediumint unsigned NOT NULL AUTO_INCREMENT comment '郵便番号住所ID',
  `zip_code` varbinary(7) DEFAULT '' NOT NULL comment '郵便番号',
  `prefectures_id` tinyint unsigned DEFAULT 0 NOT NULL comment '都道府県ID',
  `city_district_county` varbinary(64) DEFAULT '' NOT NULL comment '市区群',
  `town_village_address` varbinary(128) DEFAULT '' NOT NULL comment '町村番地',
  PRIMARY KEY(`zip_address_id`)
) ENGINE=MyISAM comment='郵便番号住所';

CREATE INDEX `idx_zip_address_zip_code` ON `zip_address` (`zip_code`);


drop table if exists `single_select_category`;

create table `single_select_category` (
  `single_select_category_id` mediumint unsigned NOT NULL AUTO_INCREMENT comment '単一選択項目カテゴリーID',
  `name` varbinary(64) DEFAULT '' NOT NULL comment '単一選択項目カテゴリー名',
  `created_at` bigint unsigned DEFAULT 0 NOT NULL comment '作成日時のタイムスタンプ',
  `updated_at` bigint unsigned DEFAULT 0 NOT NULL comment '更新日時のタイムスタンプ',
  PRIMARY KEY(`single_select_category_id`)
) ENGINE=InnoDB comment='単一選択項目カテゴリーマスタ';


drop table if exists `single_select`;

create table `single_select` (
  `single_select_id` mediumint unsigned NOT NULL AUTO_INCREMENT comment '単一選択項目ID',
  `single_select_category_id` mediumint unsigned DEFAULT 0 NOT NULL comment '単一選択項目カテゴリーID',
  `name` varbinary(64) DEFAULT '' NOT NULL comment '単一選択項目名',
  `value` varbinary(64) DEFAULT '' NOT NULL comment '単一選択項目値',
  `created_at` bigint unsigned DEFAULT 0 NOT NULL comment '作成日時のタイムスタンプ',
  `updated_at` bigint unsigned DEFAULT 0 NOT NULL comment '更新日時のタイムスタンプ',
  PRIMARY KEY(`single_select_id`),
  CONSTRAINT fk_single_select_single_select_category_id FOREIGN KEY (single_select_category_id)
  REFERENCES single_select_category (single_select_category_id)
  ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB comment='単一選択項目マスタ';


drop table if exists `multiple_select_category`;

create table `multiple_select_category` (
  `multiple_select_category_id` mediumint unsigned NOT NULL AUTO_INCREMENT comment '複数選択項目カテゴリーID',
  `name` varbinary(64) DEFAULT '' NOT NULL comment '複数選択項目カテゴリー名',
  `created_at` bigint unsigned DEFAULT 0 NOT NULL comment '作成日時のタイムスタンプ',
  `updated_at` bigint unsigned DEFAULT 0 NOT NULL comment '更新日時のタイムスタンプ',
  PRIMARY KEY(`multiple_select_category_id`)
) ENGINE=InnoDB comment='複数選択項目カテゴリーマスタ';


drop table if exists `multiple_select`;

create table `multiple_select` (
  `multiple_select_id` mediumint unsigned NOT NULL AUTO_INCREMENT comment '複数選択項目ID',
  `multiple_select_category_id` mediumint unsigned DEFAULT 0 NOT NULL comment '複数選択項目カテゴリーID',
  `name` varbinary(64) DEFAULT '' NOT NULL comment '複数選択項目名',
  `value` varbinary(64) DEFAULT '' NOT NULL comment '複数選択項目値',
  `created_at` bigint unsigned DEFAULT 0 NOT NULL comment '作成日時のタイムスタンプ',
  `updated_at` bigint unsigned DEFAULT 0 NOT NULL comment '更新日時のタイムスタンプ',
  PRIMARY KEY(`multiple_select_id`),
  CONSTRAINT fk_multiple_select_multiple_select_category_id FOREIGN KEY (multiple_select_category_id)
  REFERENCES multiple_select_category (multiple_select_category_id)
  ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB comment='複数選択項目マスタ';


drop table if exists `user`;

create table `user` (
  `user_id` bigint unsigned NOT NULL AUTO_INCREMENT comment 'ユーザーID',
  `mail_address` varbinary(512) DEFAULT '' NOT NULL comment 'メールアドレス',
  `token` varbinary(128) DEFAULT '' NOT NULL comment 'トークン値',
  `registration_status` tinyint unsigned DEFAULT 0 NOT NULL comment '登録状況',
  `last_name` varbinary(32) DEFAULT '' NOT NULL comment '苗字',
  `first_name` varbinary(32) DEFAULT '' NOT NULL comment '名前',
  `last_name_hiragana` varbinary(64) DEFAULT '' NOT NULL comment '苗字（ひらがな）',
  `first_name_hiragana` varbinary(64) DEFAULT '' NOT NULL comment '名前（ひらがな）',
  `sex_id` tinyint unsigned DEFAULT 0 NOT NULL comment '性別ID',
  `birth_day` date DEFAULT '0001-01-01' NOT NULL comment '誕生日',
  `zip_code` varbinary(8) DEFAULT '' NOT NULL comment '郵便番号',
  `prefectures_id` tinyint unsigned DEFAULT 0 NOT NULL comment '都道府県ID',
  `city_street_address` varbinary(256) DEFAULT '' NOT NULL comment '市区町村・丁目・番地',
  `building_room_address` varbinary(256) DEFAULT '' NOT NULL comment '建物名・室名',
  `telephone_number` varbinary(13) DEFAULT '' NOT NULL comment '電話番号',
  `job_id` tinyint unsigned DEFAULT 0 NOT NULL comment '職業ID',
  `job_other` varbinary(64) DEFAULT '' NOT NULL comment '職業その他',
  `is_latest_news_hoped` tinyint(1) unsigned DEFAULT 0 NOT NULL comment '最新情報の希望状況',
  `file_name` varbinary(256) DEFAULT '' NOT NULL comment 'ファイル名',
  `file_path` varbinary(512) DEFAULT '' NOT NULL comment 'ファイルパス',
  `remarks` BLOB NOT NULL comment '備考',
  `is_personal_information_provide_agreed` tinyint(1) unsigned DEFAULT 0 NOT NULL comment '個人情報提供の同意状況',
  `created_at` bigint unsigned DEFAULT 0 NOT NULL comment '作成日時のタイムスタンプ',
  `updated_at` bigint unsigned DEFAULT 0 NOT NULL comment '更新日時のタイムスタンプ',
  PRIMARY KEY(`user_id`),
  UNIQUE KEY `uniq_user_mail_address` (`mail_address`)
) ENGINE=InnoDB comment='ユーザー';


drop table if exists `user_multiple_select`;

create table `user_multiple_select` (
  `user_id` bigint unsigned DEFAULT 0 NOT NULL comment 'ユーザーID',
  `multiple_select_id` mediumint unsigned DEFAULT 0 NOT NULL comment '複数選択項目ID',
  `created_at` bigint unsigned DEFAULT 0 NOT NULL comment '作成日時のタイムスタンプ',
  `updated_at` bigint unsigned DEFAULT 0 NOT NULL comment '更新日時のタイムスタンプ',
  PRIMARY KEY(`user_id`, `multiple_select_id`),
  CONSTRAINT fk_user_multiple_select_user_id FOREIGN KEY (user_id)
  REFERENCES `user` (user_id)
  ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT fk_user_multiple_select_multiple_select_id FOREIGN KEY (multiple_select_id)
  REFERENCES `multiple_select` (multiple_select_id)
  ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB comment='ユーザー複数選択項目';
