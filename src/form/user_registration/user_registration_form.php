<?php

/**
 * ユーザー登録画面のフォームクラス
 */
class user_registration_form extends form
{
  public function __construct()
  {
    $this->init();
  }

  protected function init()
  {
    $this->set_mail_address(null);
    $this->set_mail_address_error(null);
    $this->set_password(null);
    $this->set_password_error(null);
    $this->set_last_name(null);
    $this->set_last_name_error(null);
    $this->set_first_name(null);
    $this->set_first_name_error(null);
    $this->set_last_name_hiragana(null);
    $this->set_last_name_hiragana_error(null);
    $this->set_first_name_hiragana(null);
    $this->set_first_name_hiragana_error(null);
    $this->set_sex_id(null);
    $this->set_sex_id_error(null);
    $this->set_birth_year(null);
    $this->set_birth_year_error(null);
    $this->set_birth_month(null);
    $this->set_birth_month_error(null);
    $this->set_birth_day(null);
    $this->set_birth_day_error(null);
    $this->set_birth_day_full(null);
    $this->set_birth_day_full_error(null);
    $this->set_zip_code(null);
    $this->set_zip_code_error(null);
    $this->set_prefectures_id(null);
    $this->set_prefectures_id_error(null);
    $this->set_city_street_address(null);
    $this->set_city_street_address_error(null);
    $this->set_building_room_address(null);
    $this->set_building_room_address_error(null);
    $this->set_telephone_number(null);
    $this->set_telephone_number_error(null);
    $this->set_job_id(null);
    $this->set_job_id_error(null);
    $this->set_job_other(null);
    $this->set_job_other_error(null);
    $this->set_contact_method(array());
    $this->set_contact_method_error(null);
    $this->set_knew_trigger(array());
    $this->set_knew_trigger_error(null);
    $this->set_is_latest_news_hoped(null);
    $this->set_is_latest_news_hoped_error(null);
    $this->set_file_name(null);
    $this->set_file_name_error(null);
    $this->set_file_path(null);
    $this->set_file_path_error(null);
    $this->set_remarks(null);
    $this->set_remarks_error(null);
    $this->set_is_personal_information_provide_agreed(null);
    $this->set_is_personal_information_provide_agreed_error(null);
    $this->set_clicked_button(null);
    $this->set_tmp_user_id(null);
    $this->set_token(null);
  }

  public function get_all_properties()
  {
    $properties = get_object_vars($this);

    return false === $properties ? array() : $properties;
  }

  public function set_mail_address($mail_address)
  {
    $this->mail_address = $mail_address;
  }

  public function get_mail_address()
  {
    return $this->mail_address;
  }

  public function set_mail_address_error($mail_address_error)
  {
    $this->mail_address_error = $mail_address_error;
  }

  public function get_mail_address_error()
  {
    return $this->mail_address_error;
  }

  public function set_password($password)
  {
    $this->password = $password;
  }

  public function get_password()
  {
    return $this->password;
  }

  public function set_password_error($password_error)
  {
    $this->password_error = $password_error;
  }

  public function get_password_error()
  {
    return $this->password_error;
  }

  public function set_last_name($last_name)
  {
    $this->last_name = $last_name;
  }

  public function get_last_name()
  {
    return $this->last_name;
  }

  public function set_last_name_error($last_name_error)
  {
    $this->last_name_error = $last_name_error;
  }

  public function get_last_name_error()
  {
    return $this->last_name_error;
  }

  public function set_first_name($first_name)
  {
    $this->first_name = $first_name;
  }

  public function get_first_name()
  {
    return $this->first_name;
  }

  public function set_first_name_error($first_name_error)
  {
    $this->first_name_error = $first_name_error;
  }

  public function get_first_name_error()
  {
    return $this->first_name_error;
  }

  public function set_last_name_hiragana($last_name_hiragana)
  {
    $this->last_name_hiragana = $last_name_hiragana;
  }

  public function get_last_name_hiragana()
  {
    return $this->last_name_hiragana;
  }

  public function set_last_name_hiragana_error($last_name_hiragana_error)
  {
    $this->last_name_hiragana_error = $last_name_hiragana_error;
  }

  public function get_last_name_hiragana_error()
  {
    return $this->last_name_hiragana_error;
  }

  public function set_first_name_hiragana($first_name_hiragana)
  {
    $this->first_name_hiragana = $first_name_hiragana;
  }

  public function get_first_name_hiragana()
  {
    return $this->first_name_hiragana;
  }

  public function set_first_name_hiragana_error($first_name_hiragana_error)
  {
    $this->first_name_hiragana_error = $first_name_hiragana_error;
  }

  public function get_first_name_hiragana_error()
  {
    return $this->first_name_hiragana_error;
  }

  public function set_sex_id($sex_id)
  {
    $this->sex_id = $sex_id;
  }

  public function get_sex_id()
  {
    return $this->sex_id;
  }

  public function set_sex_id_error($sex_id_error)
  {
    $this->sex_id_error = $sex_id_error;
  }

  public function get_sex_id_error()
  {
    return $this->sex_id_error;
  }

  public function set_birth_year($birth_year)
  {
    $this->birth_year = $birth_year;
  }

  public function get_birth_year()
  {
    return $this->birth_year;
  }

  public function set_birth_year_error($birth_year_error)
  {
    $this->birth_year_error = $birth_year_error;
  }

  public function get_birth_year_error()
  {
    return $this->birth_year_error;
  }

  public function set_birth_month($birth_month)
  {
    $this->birth_month = $birth_month;
  }

  public function get_birth_month()
  {
    return $this->birth_month;
  }

  public function set_birth_month_error($birth_month_error)
  {
    $this->birth_month_error = $birth_month_error;
  }

  public function get_birth_month_error()
  {
    return $this->birth_month_error;
  }

  public function set_birth_day($birth_day)
  {
    $this->birth_day = $birth_day;
  }

  public function get_birth_day()
  {
    return $this->birth_day;
  }

  public function set_birth_day_error($birth_day_error)
  {
    $this->birth_day_error = $birth_day_error;
  }

  public function get_birth_day_error()
  {
    return $this->birth_day_error;
  }

  public function set_birth_day_full($birth_day_full)
  {
    $this->birth_day_full = $birth_day_full;
  }

  public function get_birth_day_full()
  {
    return $this->birth_day_full;
  }

  public function set_birth_day_full_error($birth_day_full_error)
  {
    $this->birth_day_full_error = $birth_day_full_error;
  }

  public function get_birth_day_full_error()
  {
    return $this->birth_day_full_error;
  }

  public function set_zip_code($zip_code)
  {
    $this->zip_code = $zip_code;
  }

  public function get_zip_code()
  {
    return $this->zip_code;
  }

  public function set_zip_code_error($zip_code_error)
  {
    $this->zip_code_error = $zip_code_error;
  }

  public function get_zip_code_error()
  {
    return $this->zip_code_error;
  }

  public function set_prefectures_id($prefectures_id)
  {
    $this->prefectures_id = $prefectures_id;
  }

  public function get_prefectures_id()
  {
    return $this->prefectures_id;
  }

  public function set_prefectures_id_error($prefectures_id_error)
  {
    $this->prefectures_id_error = $prefectures_id_error;
  }

  public function get_prefectures_id_error()
  {
    return $this->prefectures_id_error;
  }

  public function set_city_street_address($city_street_address)
  {
    $this->city_street_address = $city_street_address;
  }

  public function get_city_street_address()
  {
    return $this->city_street_address;
  }

  public function set_city_street_address_error($city_street_address_error)
  {
    $this->city_street_address_error = $city_street_address_error;
  }

  public function get_city_street_address_error()
  {
    return $this->city_street_address_error;
  }

  public function set_building_room_address($building_room_address)
  {
    $this->building_room_address = $building_room_address;
  }

  public function get_building_room_address()
  {
    return $this->building_room_address;
  }

  public function set_building_room_address_error($building_room_address_error)
  {
    $this->building_room_address_error = $building_room_address_error;
  }

  public function get_building_room_address_error()
  {
    return $this->building_room_address_error;
  }

  public function set_telephone_number($telephone_number)
  {
    $this->telephone_number = $telephone_number;
  }

  public function get_telephone_number()
  {
    return $this->telephone_number;
  }

  public function set_telephone_number_error($telephone_number_error)
  {
    $this->telephone_number_error = $telephone_number_error;
  }

  public function get_telephone_number_error()
  {
    return $this->telephone_number_error;
  }

  public function set_job_id($job_id)
  {
    $this->job_id = $job_id;
  }

  public function get_job_id()
  {
    return $this->job_id;
  }

  public function set_job_id_error($job_id_error)
  {
    $this->job_id_error = $job_id_error;
  }

  public function get_job_id_error()
  {
    return $this->job_id_error;
  }

  public function set_job_other($job_other)
  {
    $this->job_other = $job_other;
  }

  public function get_job_other()
  {
    return $this->job_other;
  }

  public function set_job_other_error($job_other_error)
  {
    $this->job_other_error = $job_other_error;
  }

  public function get_job_other_error()
  {
    return $this->job_other_error;
  }

  public function set_contact_method($contact_method)
  {
    $this->contact_method = $contact_method;
  }

  public function get_contact_method()
  {
    return $this->contact_method;
  }

  public function set_contact_method_error($contact_method_error)
  {
    $this->contact_method_error = $contact_method_error;
  }

  public function get_contact_method_error()
  {
    return $this->contact_method_error;
  }

  public function set_knew_trigger($knew_trigger)
  {
    $this->knew_trigger = $knew_trigger;
  }

  public function get_knew_trigger()
  {
    return $this->knew_trigger;
  }

  public function set_knew_trigger_error($knew_trigger_error)
  {
    $this->knew_trigger_error = $knew_trigger_error;
  }

  public function get_knew_trigger_error()
  {
    return $this->knew_trigger_error;
  }

  public function set_is_latest_news_hoped($is_latest_news_hoped)
  {
    $this->is_latest_news_hoped = $is_latest_news_hoped;
  }

  public function get_is_latest_news_hoped()
  {
    return $this->is_latest_news_hoped;
  }

  public function set_is_latest_news_hoped_error($is_latest_news_hoped_error)
  {
    $this->is_latest_news_hoped_error = $is_latest_news_hoped_error;
  }

  public function get_is_latest_news_hoped_error()
  {
    return $this->is_latest_news_hoped_error;
  }

  public function set_file_name($file_name)
  {
    $this->file_name = $file_name;
  }

  public function get_file_name()
  {
    return $this->file_name;
  }

  public function set_file_name_error($file_name_error)
  {
    $this->file_name_error = $file_name_error;
  }

  public function get_file_name_error()
  {
    return $this->file_name_error;
  }

  public function set_file_path($file_path)
  {
    $this->file_path = $file_path;
  }

  public function get_file_path()
  {
    return $this->file_path;
  }

  public function set_file_path_error($file_path_error)
  {
    $this->file_path_error = $file_path_error;
  }

  public function get_file_path_error()
  {
    return $this->file_path_error;
  }

  public function set_remarks($remarks)
  {
    $this->remarks = $remarks;
  }

  public function get_remarks()
  {
    return $this->remarks;
  }

  public function set_remarks_error($remarks_error)
  {
    $this->remarks_error = $remarks_error;
  }

  public function get_remarks_error()
  {
    return $this->remarks_error;
  }

  public function set_is_personal_information_provide_agreed($is_personal_information_provide_agreed)
  {
    $this->is_personal_information_provide_agreed = $is_personal_information_provide_agreed;
  }

  public function get_is_personal_information_provide_agreed()
  {
    return $this->is_personal_information_provide_agreed;
  }

  public function set_is_personal_information_provide_agreed_error($is_personal_information_provide_agreed_error)
  {
    $this->is_personal_information_provide_agreed_error = $is_personal_information_provide_agreed_error;
  }

  public function get_is_personal_information_provide_agreed_error()
  {
    return $this->is_personal_information_provide_agreed_error;
  }

  public function set_clicked_button($clicked_button)
  {
    $this->clicked_button = $clicked_button;
  }

  public function get_clicked_button()
  {
    return $this->clicked_button;
  }

  public function set_tmp_user_id($tmp_user_id)
  {
    $this->tmp_user_id = $tmp_user_id;
  }

  public function get_tmp_user_id()
  {
    return $this->tmp_user_id;
  }

  public function set_token($token)
  {
    $this->token = $token;
  }

  public function get_token()
  {
    return $this->token;
  }

  /**
   * メールアドレス
   *
   */
  private $mail_address;

  /**
   * メールアドレスエラー
   *
   */
  private $mail_address_error;

  /**
   * パスワード
   *
   */
  private $password;

  /**
   * パスワードエラー
   *
   */
  private $password_error;

  /**
   * 氏名(姓)
   *
   */
  private $last_name;

  /**
   * 氏名(姓)エラー
   *
   */
  private $last_name_error;

  /**
   * 氏名(名)
   *
   */
  private $first_name;

  /**
   * 氏名(名)エラー
   *
   */
  private $first_name_error;

  /**
   * 氏名(ふりがな)(姓)
   *
   */
  private $last_name_hiragana;

  /**
   * 氏名(ふりがな)(姓)エラー
   *
   */
  private $last_name_hiragana_error;

  /**
   * 氏名(ふりがな)(名)
   *
   */
  private $first_name_hiragana;

  /**
   * 氏名(ふりがな)(名)エラー
   *
   */
  private $first_name_hiragana_error;

  /**
   * 性別ID
   *
   */
  private $sex_id;

  /**
   * 性別IDエラー
   *
   */
  private $sex_id_error;

  /**
   * 誕生日（年）
   *
   */
  private $birth_year;

  /**
   * 誕生日（年）エラー
   *
   */
  private $birth_year_error;

  /**
   * 誕生日（月）
   *
   */
  private $birth_month;

  /**
   * 誕生日（月）エラー
   *
   */
  private $birth_month_error;

  /**
   * 誕生日（日）
   *
   */
  private $birth_day;

  /**
   * 誕生日（日）エラー
   *
   */
  private $birth_day_error;

  /**
   * 誕生日
   *
   */
  private $birth_day_full;

  /**
   * 誕生日エラー
   *
   */
  private $birth_day_full_error;

  /**
   * 郵便番号
   *
   */
  private $zip_code;

  /**
   * 郵便番号エラー
   *
   */
  private $zip_code_error;

  /**
   * 都道府県ID
   *
   */
  private $prefectures_id;

  /**
   * 都道府県IDエラー
   *
   */
  private $prefectures_id_error;

  /**
   * 市区町村・丁目・番地
   *
   */
  private $city_street_address;

  /**
   * 市区町村・丁目・番地エラー
   *
   */
  private $city_street_address_error;

  /**
   * 建物名・室名
   *
   */
  private $building_room_address;

  /**
   * 建物名・室名エラー
   *
   */
  private $building_room_address_error;

  /**
   * 電話番号
   *
   */
  private $telephone_number;

  /**
   * 電話番号エラー
   *
   */
  private $telephone_number_error;

  /**
   * 職業ID
   *
   */
  private $job_id;

  /**
   * 職業IDエラー
   *
   */
  private $job_id_error;

  /**
   * 職業その他
   *
   */
  private $job_other;

  /**
   * 職業その他エラー
   *
   */
  private $job_other_error;

  /**
   * 連絡方法
   *
   */
  private $contact_method;

  /**
   * 連絡方法エラー
   *
   */
  private $contact_method_error;

  /**
   * 知ったきっかけ
   *
   */
  private $knew_trigger;

  /**
   * 知ったきっかけエラー
   *
   */
  private $knew_trigger_error;

  /**
   * 最新情報の希望状況
   *
   */
  private $is_latest_news_hoped;

  /**
   * 最新情報の希望状況エラー
   *
   */
  private $is_latest_news_hoped_error;

  /**
   * ファイル名
   *
   */
  private $file_name;

  /**
   * ファイル名エラー
   *
   */
  private $file_name_error;

  /**
   * ファイルパス
   *
   */
  private $file_path;

  /**
   * ファイルパスエラー
   *
   */
  private $file_path_error;

  /**
   * 備考
   *
   */
  private $remarks;

  /**
   * 備考エラー
   *
   */
  private $remarks_error;

  /**
   * 個人情報提供の同意状況
   *
   */
  private $is_personal_information_provide_agreed;

  /**
   * 個人情報提供の同意状況エラー
   *
   */
  private $is_personal_information_provide_agreed_error;

  /**
   * クリックされたボタン
   *
   */
  private $clicked_button;

  /**
   * 一時ユーザーID
   *
   */
  private $tmp_user_id;

  /**
   * トークン
   *
   */
  private $token;
}
