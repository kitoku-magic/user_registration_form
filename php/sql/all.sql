drop database if exists `user_registration_form`;

CREATE DATABASE `user_registration_form` CHARACTER SET utf8 COLLATE utf8_bin;

use `user_registration_form`;

-- mysql --local_infile=1 -uroot -p < sql/all.sqlで実行している前提
source sql/ddl.sql

source sql/dml.sql

source sql/load_data_local_infile_ken_all_csv.sql
