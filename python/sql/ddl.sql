use `user_registration_form_python`;


-- varbinary型で、全角文字が入りそうな列は、
-- マスターテーブルの一部カラムを除き「許容文字数 * 4（絵文字を考慮）」の桁数にしています
DROP TABLE IF EXISTS `prefectures`;

CREATE TABLE `prefectures` (
  `prefecture_id` tinyint(3) unsigned NOT NULL AUTO_INCREMENT COMMENT '都道府県ID',
  `prefecture_name` varbinary(12) NOT NULL DEFAULT '' COMMENT '都道府県名',
  `created_at` bigint(20) unsigned NOT NULL DEFAULT '0' COMMENT '作成日時のタイムスタンプ',
  `updated_at` bigint(20) unsigned NOT NULL DEFAULT '0' COMMENT '更新日時のタイムスタンプ',
  PRIMARY KEY (`prefecture_id`),
  UNIQUE KEY `prefectures_prefecture_name_unique` (`prefecture_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin COMMENT='都道府県マスタ';


DROP TABLE IF EXISTS `zip_addresses`;

CREATE TABLE `zip_addresses` (
  `zip_address_id` mediumint(8) unsigned NOT NULL AUTO_INCREMENT COMMENT '郵便番号住所ID',
  `zip_code` varbinary(7) NOT NULL DEFAULT '' COMMENT '郵便番号',
  `prefecture_id` tinyint(3) unsigned NOT NULL DEFAULT '0' COMMENT '都道府県ID',
  `city_district_county` varbinary(64) NOT NULL DEFAULT '' COMMENT '市区群',
  `town_village_address` varbinary(128) NOT NULL DEFAULT '' COMMENT '町村番地',
  `created_at` bigint(20) unsigned NOT NULL DEFAULT '0' COMMENT '作成日時のタイムスタンプ',
  `updated_at` bigint(20) unsigned NOT NULL DEFAULT '0' COMMENT '更新日時のタイムスタンプ',
  PRIMARY KEY (`zip_address_id`),
  KEY `zip_addresses_zip_code_prefecture_id_index` (`zip_code`, `prefecture_id`),
  CONSTRAINT `zip_addresses_prefecture_id_foreign` FOREIGN KEY (`prefecture_id`) REFERENCES `prefectures` (`prefecture_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin COMMENT='郵便番号住所マスタ';


DROP TABLE IF EXISTS `contact_methods`;

CREATE TABLE `contact_methods` (
  `contact_method_id` tinyint(3) unsigned NOT NULL AUTO_INCREMENT COMMENT '連絡方法ID',
  `contact_method_name` varbinary(32) NOT NULL DEFAULT '' COMMENT '連絡方法名',
  `created_at` bigint(20) unsigned NOT NULL DEFAULT '0' COMMENT '作成日時のタイムスタンプ',
  `updated_at` bigint(20) unsigned NOT NULL DEFAULT '0' COMMENT '更新日時のタイムスタンプ',
  PRIMARY KEY (`contact_method_id`),
  UNIQUE KEY `contact_methods_contact_method_name_unique` (`contact_method_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin COMMENT='連絡方法マスタ';


DROP TABLE IF EXISTS `knew_triggers`;

CREATE TABLE `knew_triggers` (
  `knew_trigger_id` tinyint(3) unsigned NOT NULL AUTO_INCREMENT COMMENT '知ったきっかけID',
  `knew_trigger_name` varbinary(64) NOT NULL DEFAULT '' COMMENT '知ったきっかけ名',
  `created_at` bigint(20) unsigned NOT NULL DEFAULT '0' COMMENT '作成日時のタイムスタンプ',
  `updated_at` bigint(20) unsigned NOT NULL DEFAULT '0' COMMENT '更新日時のタイムスタンプ',
  PRIMARY KEY (`knew_trigger_id`),
  UNIQUE KEY `knew_triggers_knew_trigger_name_unique` (`knew_trigger_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin COMMENT='知ったきっかけマスタ';


DROP TABLE IF EXISTS `birth_days`;

CREATE TABLE `birth_days` (
  `birth_day_id` smallint(5) unsigned NOT NULL AUTO_INCREMENT COMMENT '誕生日ID',
  `birth_day` date NOT NULL DEFAULT '0001-01-01' COMMENT '誕生日',
  `created_at` bigint(20) unsigned NOT NULL DEFAULT '0' COMMENT '作成日時のタイムスタンプ',
  `updated_at` bigint(20) unsigned NOT NULL DEFAULT '0' COMMENT '更新日時のタイムスタンプ',
  PRIMARY KEY (`birth_day_id`),
  UNIQUE KEY `birth_days_birth_day_unique` (`birth_day`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin COMMENT='誕生日マスタ';


DROP TABLE IF EXISTS `jobs`;

CREATE TABLE `jobs` (
  `job_id` tinyint(3) unsigned NOT NULL AUTO_INCREMENT COMMENT '職業ID',
  `job_name` varbinary(32) NOT NULL DEFAULT '' COMMENT '職業名',
  `created_at` bigint(20) unsigned NOT NULL DEFAULT '0' COMMENT '作成日時のタイムスタンプ',
  `updated_at` bigint(20) unsigned NOT NULL DEFAULT '0' COMMENT '更新日時のタイムスタンプ',
  PRIMARY KEY (`job_id`),
  UNIQUE KEY `jobs_job_name_unique` (`job_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin COMMENT='職業マスタ';


DROP TABLE IF EXISTS `sexes`;

CREATE TABLE `sexes` (
  `sex_id` tinyint(3) unsigned NOT NULL AUTO_INCREMENT COMMENT '性別ID',
  `sex_name` varbinary(32) NOT NULL DEFAULT '' COMMENT '性別名',
  `created_at` bigint(20) unsigned NOT NULL DEFAULT '0' COMMENT '作成日時のタイムスタンプ',
  `updated_at` bigint(20) unsigned NOT NULL DEFAULT '0' COMMENT '更新日時のタイムスタンプ',
  PRIMARY KEY (`sex_id`),
  UNIQUE KEY `sexes_sex_name_unique` (`sex_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin COMMENT='性別マスタ';


DROP TABLE IF EXISTS `pre_users`;

CREATE TABLE `pre_users` (
  `pre_user_id` bigint(20) unsigned NOT NULL AUTO_INCREMENT COMMENT 'ユーザーID',
  `mail_address` varbinary(512) NOT NULL DEFAULT '' COMMENT 'メールアドレス',
  `token` varbinary(128) NOT NULL DEFAULT '' COMMENT 'トークン値',
  `created_at` bigint(20) unsigned NOT NULL DEFAULT '0' COMMENT '作成日時のタイムスタンプ',
  `updated_at` bigint(20) unsigned NOT NULL DEFAULT '0' COMMENT '更新日時のタイムスタンプ',
  PRIMARY KEY (`pre_user_id`),
  UNIQUE KEY `pre_users_mail_address_unique` (`mail_address`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin COMMENT='ユーザー事前登録情報';


DROP TABLE IF EXISTS `users`;

CREATE TABLE `users` (
  `user_id` bigint(20) unsigned NOT NULL AUTO_INCREMENT COMMENT 'ユーザーID',
  `mail_address` varbinary(512) NOT NULL DEFAULT '' COMMENT 'メールアドレス',
  `token` varbinary(128) NOT NULL DEFAULT '' COMMENT 'トークン値',
  `registration_status` tinyint(3) unsigned NOT NULL DEFAULT '0' COMMENT '登録状況',
  `last_name` varbinary(32) NOT NULL DEFAULT '' COMMENT '苗字',
  `first_name` varbinary(32) NOT NULL DEFAULT '' COMMENT '名前',
  `last_name_hiragana` varbinary(64) NOT NULL DEFAULT '' COMMENT '苗字（ひらがな）',
  `first_name_hiragana` varbinary(64) NOT NULL DEFAULT '' COMMENT '名前（ひらがな）',
  `sex_id` tinyint(3) unsigned NOT NULL DEFAULT '0' COMMENT '性別ID',
  `birth_day_id` smallint(5) unsigned NOT NULL DEFAULT '0' COMMENT '誕生日ID',
  `zip_code` varbinary(7) NOT NULL DEFAULT '' COMMENT '郵便番号',
  `prefecture_id` tinyint(3) unsigned NOT NULL DEFAULT '0' COMMENT '都道府県ID',
  `city_street_address` varbinary(256) NOT NULL DEFAULT '' COMMENT '市区町村・丁目・番地',
  `building_room_address` varbinary(128) NOT NULL DEFAULT '' COMMENT '建物名・室名',
  `telephone_number` varbinary(13) NOT NULL DEFAULT '' COMMENT '電話番号',
  `job_id` tinyint(3) unsigned NOT NULL DEFAULT '0' COMMENT '職業ID',
  `job_other` varbinary(64) NOT NULL DEFAULT '' COMMENT '職業その他',
  `is_latest_news_hoped` tinyint(1) unsigned NOT NULL DEFAULT '0' COMMENT '最新情報の希望状況',
  `file_name` varbinary(256) NOT NULL DEFAULT '' COMMENT 'ファイル名',
  `file_path` varbinary(512) NOT NULL DEFAULT '' COMMENT 'ファイルパス',
  `remarks` blob NOT NULL COMMENT '備考',
  `is_personal_information_provide_agreed` tinyint(1) unsigned NOT NULL DEFAULT '0' COMMENT '個人情報提供の同意状況',
  `created_at` bigint(20) unsigned NOT NULL DEFAULT '0' COMMENT '作成日時のタイムスタンプ',
  `updated_at` bigint(20) unsigned NOT NULL DEFAULT '0' COMMENT '更新日時のタイムスタンプ',
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `users_mail_address_unique` (`mail_address`),
  CONSTRAINT `users_sex_id_foreign` FOREIGN KEY (`sex_id`) REFERENCES `sexes` (`sex_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `users_birth_day_id_foreign` FOREIGN KEY (`birth_day_id`) REFERENCES `birth_days` (`birth_day_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `users_zip_code_prefecture_id_foreign` FOREIGN KEY (`zip_code`, `prefecture_id`) REFERENCES `zip_addresses` (`zip_code`, `prefecture_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `users_job_id_foreign` FOREIGN KEY (`job_id`) REFERENCES `jobs` (`job_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin COMMENT='ユーザー';


DROP TABLE IF EXISTS `user_contact_methods`;

CREATE TABLE `user_contact_methods` (
  `user_id` bigint(20) unsigned NOT NULL DEFAULT '0' COMMENT 'ユーザーID',
  `contact_method_id` tinyint(3) unsigned NOT NULL DEFAULT '0' COMMENT '連絡方法ID',
  `created_at` bigint(20) unsigned NOT NULL DEFAULT '0' COMMENT '作成日時のタイムスタンプ',
  `updated_at` bigint(20) unsigned NOT NULL DEFAULT '0' COMMENT '更新日時のタイムスタンプ',
  PRIMARY KEY (`user_id`,`contact_method_id`),
  CONSTRAINT `user_contact_methods_user_id_foreign` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `user_contact_methods_contact_method_id_foreign` FOREIGN KEY (`contact_method_id`) REFERENCES `contact_methods` (`contact_method_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin COMMENT='ユーザー連絡方法';


DROP TABLE IF EXISTS `user_knew_triggers`;

CREATE TABLE `user_knew_triggers` (
  `user_id` bigint(20) unsigned NOT NULL DEFAULT '0' COMMENT 'ユーザーID',
  `knew_trigger_id` tinyint(3) unsigned NOT NULL DEFAULT '0' COMMENT '知ったきっかけID',
  `created_at` bigint(20) unsigned NOT NULL DEFAULT '0' COMMENT '作成日時のタイムスタンプ',
  `updated_at` bigint(20) unsigned NOT NULL DEFAULT '0' COMMENT '更新日時のタイムスタンプ',
  PRIMARY KEY (`user_id`,`knew_trigger_id`),
  CONSTRAINT `user_knew_triggers_user_id_foreign` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `user_knew_triggers_knew_trigger_id_foreign` FOREIGN KEY (`knew_trigger_id`) REFERENCES `knew_triggers` (`knew_trigger_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin COMMENT='ユーザー知ったきっかけ';
