<?php

/**
 * ユーザー登録画面のバリデータークラス
 */
class user_registration_form_validator extends validator
{
  public function __construct()
  {
    parent::__construct();
  }

  public function set_validation_setting()
  {
    $form = $this->get_form();

    $validation_settings = array(
      array(
        'name' => 'mail_address',
        'show_name' => 'メールアドレス',
        'rules' => array(
          'required' => array(),
          'not_empty' => array(),
          'max_length' => array('value' => 128),
          'mail_format' => array(),
        ),
      ),
      array(
        'name' => 'password',
        'show_name' => 'パスワード',
        'rules' => array(
          'required' => array(),
          'not_empty' => array(),
          'min_length' => array('value' => 8),
          'max_length' => array('value' => 256),
          'alpha_num' => array(),
        ),
      ),
      array(
        'name' => 'last_name',
        'show_name' => '氏名（姓）',
        'rules' => array(
          'required' => array(),
          'not_empty' => array(),
          'max_length' => array('value' => 8),
          'japanese' => array(),
        ),
      ),
      array(
        'name' => 'first_name',
        'show_name' => '氏名（名）',
        'rules' => array(
          'required' => array(),
          'not_empty' => array(),
          'max_length' => array('value' => 8),
          'japanese' => array(),
        ),
      ),
      array(
        'name' => 'last_name_hiragana',
        'show_name' => '氏名（ひらがな）（姓）',
        'rules' => array(
          'required' => array(),
          'not_empty' => array(),
          'max_length' => array('value' => 16),
          'hiragana' => array(),
        ),
      ),
      array(
        'name' => 'first_name_hiragana',
        'show_name' => '氏名（ひらがな）（名）',
        'rules' => array(
          'required' => array(),
          'not_empty' => array(),
          'max_length' => array('value' => 16),
          'hiragana' => array(),
        ),
      ),
      array(
        'name' => 'sex_id',
        'show_name' => '性別',
        'rules' => array(
          'required' => array(),
          'not_empty' => array(),
          'integer' => array(),
          'range' => array('min' => 1, 'max' => 3),
        ),
      ),
      array(
        'name' => 'birth_year',
        'show_name' => '誕生日（年）',
        'rules' => array(
          'required' => array(),
          'not_empty' => array(),
          'integer' => array(),
          'range' => array('min' => 1900, 'max' => 2019),
        ),
      ),
      array(
        'name' => 'birth_month',
        'show_name' => '誕生日（月）',
        'rules' => array(
          'required' => array(),
          'not_empty' => array(),
          'integer' => array(),
          'range' => array('min' => 1, 'max' => 12),
        ),
      ),
      array(
        'name' => 'birth_day',
        'show_name' => '誕生日（日）',
        'rules' => array(
          'required' => array(),
          'not_empty' => array(),
          'integer' => array(),
          'range' => array('min' => 1, 'max' => 31),
        ),
      ),
      array(
        'name' => 'birth_day_full',
        'show_name' => '誕生日',
        'rules' => array(
          'allow_empty' => array(),
          'date' => array('format' => 'Y-m-d'),
        ),
      ),
      array(
        'name' => 'zip_code',
        'show_name' => '郵便番号',
        'rules' => array(
          'required' => array(),
          'not_empty' => array(),
          'max_length' => array('value' => 8),
          'zip_code_format' => array('is_include_hyphen' => true),
        ),
      ),
      array(
        'name' => 'prefectures_id',
        'show_name' => '都道府県',
        'rules' => array(
          'required' => array(),
          'not_empty' => array(),
          'integer' => array(),
          'range' => array('min' => 1, 'max' => 47),
        ),
      ),
      array(
        'name' => 'city_street_address',
        'show_name' => '市区町村・丁目・番地',
        'rules' => array(
          'required' => array(),
          'not_empty' => array(),
          'max_length' => array('value' => 64),
          'japanese_extend' => array(),
        ),
      ),
      array(
        'name' => 'building_room_address',
        'show_name' => '建物名・室名',
        'rules' => array(
          'allow_empty' => array(),
          'max_length' => array('value' => 64),
          'japanese_extend' => array(),
        ),
      ),
      array(
        'name' => 'telephone_number',
        'show_name' => '電話番号',
        'rules' => array(
          'required' => array(),
          'not_empty' => array(),
          'max_length' => array('value' => 13),
          'telephone_format' => array('is_include_hyphen' => true),
        ),
      ),
      array(
        'name' => 'job_id',
        'show_name' => '職業',
        'rules' => array(
          'required' => array(),
          'not_empty' => array(),
          'integer' => array(),
          'range' => array('min' => 0, 'max' => 5),
        ),
      ),
    );

    $job_other_setting = array(
      'name' => 'job_other',
      'show_name' => '職業その他',
    );

    $rules = array();
    // 職業でその他を選択時のみ必須
    if ('0' === $form->get_job_id())
    {
      $rules['required'] = array();
      $rules['not_empty'] = array();
    }
    else
    {
      $rules['allow_empty'] = array();
    }

    $rules['max_length'] = array('value' => 16);
    $rules['japanese_extend'] = array();

    $job_other_setting['rules'] = $rules;

    $validation_settings[] = $job_other_setting;

    $add_validation_settings = array(
      array(
        'name' => 'contact_method',
        'show_name' => '連絡方法',
        'rules' => array(
          'required' => array(),
          'not_empty' => array(),
          'integer' => array(),
          'range' => array('min' => 1, 'max' => 4),
        ),
      ),
      array(
        'name' => 'knew_trigger',
        'show_name' => '知ったきっかけ',
        'rules' => array(
          'allow_empty' => array(),
          'integer' => array(),
          'range' => array('min' => 1, 'max' => 6),
        ),
      ),
      array(
        'name' => 'is_latest_news_hoped',
        'show_name' => '最新情報の希望状況',
        'rules' => array(
          'required' => array(),
          'not_empty' => array(),
          'integer' => array(),
          'range' => array('min' => 0, 'max' => 1),
        ),
      ),
      array(
        'name' => 'remarks',
        'show_name' => '備考',
        'rules' => array(
          'allow_empty' => array(),
          'max_length' => array('value' => 1000),
        ),
      ),
      array(
        'name' => 'is_personal_information_provide_agreed',
        'show_name' => '個人情報提供の同意状況',
        'rules' => array(
          'required' => array(),
          'not_empty' => array(),
          'integer' => array(),
          'range' => array('min' => 1, 'max' => 1),
        ),
      ),
    );

    $validation_settings = array_merge($validation_settings, $add_validation_settings);

    foreach ($validation_settings as $validation_setting)
    {
      $this->add_validation_settings(
        $validation_setting['name'],
        $validation_setting['show_name'],
        $validation_setting['rules']
      );
    }
  }
}
