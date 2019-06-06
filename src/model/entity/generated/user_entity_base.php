<?php

class user_entity_base extends entity
{
  // user_id
  public function get_user_id() { return $this->user_id; }
  public function set_user_id($v) { $this->user_id = $v; }

  // mail_address
  public function get_mail_address() { return $this->mail_address; }
  public function set_mail_address($v) { $this->mail_address = $v; }

  // password
  public function get_password() { return $this->password; }
  public function set_password($v) { $this->password = $v; }

  // last_name
  public function get_last_name() { return $this->last_name; }
  public function set_last_name($v) { $this->last_name = $v; }

  // first_name
  public function get_first_name() { return $this->first_name; }
  public function set_first_name($v) { $this->first_name = $v; }

  // last_name_hiragana
  public function get_last_name_hiragana() { return $this->last_name_hiragana; }
  public function set_last_name_hiragana($v) { $this->last_name_hiragana = $v; }

  // first_name_hiragana
  public function get_first_name_hiragana() { return $this->first_name_hiragana; }
  public function set_first_name_hiragana($v) { $this->first_name_hiragana = $v; }

  // sex_id
  public function get_sex_id() { return $this->sex_id; }
  public function set_sex_id($v) { $this->sex_id = $v; }

  // birth_day
  public function get_birth_day() { return $this->birth_day; }
  public function set_birth_day($v) { $this->birth_day = $v; }

  // zip_code
  public function get_zip_code() { return $this->zip_code; }
  public function set_zip_code($v) { $this->zip_code = $v; }

  // prefectures_id
  public function get_prefectures_id() { return $this->prefectures_id; }
  public function set_prefectures_id($v) { $this->prefectures_id = $v; }

  // city_street_address
  public function get_city_street_address() { return $this->city_street_address; }
  public function set_city_street_address($v) { $this->city_street_address = $v; }

  // building_room_address
  public function get_building_room_address() { return $this->building_room_address; }
  public function set_building_room_address($v) { $this->building_room_address = $v; }

  // telephone_number
  public function get_telephone_number() { return $this->telephone_number; }
  public function set_telephone_number($v) { $this->telephone_number = $v; }

  // job_id
  public function get_job_id() { return $this->job_id; }
  public function set_job_id($v) { $this->job_id = $v; }

  // job_other
  public function get_job_other() { return $this->job_other; }
  public function set_job_other($v) { $this->job_other = $v; }

  // is_latest_news_hoped
  public function get_is_latest_news_hoped() { return $this->is_latest_news_hoped; }
  public function set_is_latest_news_hoped($v) { $this->is_latest_news_hoped = $v; }

  // file_name
  public function get_file_name() { return $this->file_name; }
  public function set_file_name($v) { $this->file_name = $v; }

  // file_path
  public function get_file_path() { return $this->file_path; }
  public function set_file_path($v) { $this->file_path = $v; }

  // remarks
  public function get_remarks() { return $this->remarks; }
  public function set_remarks($v) { $this->remarks = $v; }

  // is_personal_information_provide_agreed
  public function get_is_personal_information_provide_agreed() { return $this->is_personal_information_provide_agreed; }
  public function set_is_personal_information_provide_agreed($v) { $this->is_personal_information_provide_agreed = $v; }

  // created_at
  public function get_created_at() { return $this->created_at; }
  public function set_created_at($v) { $this->created_at = $v; }

  // updated_at
  public function get_updated_at() { return $this->updated_at; }
  public function set_updated_at($v) { $this->updated_at = $v; }

  public function get_table_columns()
  {
    return array(
      'user_id' => rdbms_storage_handler::PARAM_STR,
      'mail_address' => rdbms_storage_handler::PARAM_STR,
      'password' => rdbms_storage_handler::PARAM_STR,
      'last_name' => rdbms_storage_handler::PARAM_STR,
      'first_name' => rdbms_storage_handler::PARAM_STR,
      'last_name_hiragana' => rdbms_storage_handler::PARAM_STR,
      'first_name_hiragana' => rdbms_storage_handler::PARAM_STR,
      'sex_id' => rdbms_storage_handler::PARAM_INT,
      'birth_day' => rdbms_storage_handler::PARAM_STR,
      'zip_code' => rdbms_storage_handler::PARAM_STR,
      'prefectures_id' => rdbms_storage_handler::PARAM_INT,
      'city_street_address' => rdbms_storage_handler::PARAM_STR,
      'building_room_address' => rdbms_storage_handler::PARAM_STR,
      'telephone_number' => rdbms_storage_handler::PARAM_STR,
      'job_id' => rdbms_storage_handler::PARAM_INT,
      'job_other' => rdbms_storage_handler::PARAM_STR,
      'is_latest_news_hoped' => rdbms_storage_handler::PARAM_INT,
      'file_name' => rdbms_storage_handler::PARAM_STR,
      'file_path' => rdbms_storage_handler::PARAM_STR,
      'remarks' => rdbms_storage_handler::PARAM_STR,
      'is_personal_information_provide_agreed' => rdbms_storage_handler::PARAM_INT,
      'created_at' => rdbms_storage_handler::PARAM_INT,
      'updated_at' => rdbms_storage_handler::PARAM_INT,
    );
  }

  private $user_id;
  private $mail_address;
  private $password;
  private $last_name;
  private $first_name;
  private $last_name_hiragana;
  private $first_name_hiragana;
  private $sex_id;
  private $birth_day;
  private $zip_code;
  private $prefectures_id;
  private $city_street_address;
  private $building_room_address;
  private $telephone_number;
  private $job_id;
  private $job_other;
  private $is_latest_news_hoped;
  private $file_name;
  private $file_path;
  private $remarks;
  private $is_personal_information_provide_agreed;
  private $created_at;
  private $updated_at;
}
