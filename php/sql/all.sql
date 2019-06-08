drop database if exists `user_registration_form`;

CREATE DATABASE `user_registration_form` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

use `user_registration_form`;

-- mysql -uroot -p < sql/all.sqlで実行している前提
source sql/ddl.sql

source sql/dml.sql

source sql/load_data_local_infile_ken_all_csv.sql
