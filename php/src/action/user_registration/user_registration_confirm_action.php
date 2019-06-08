<?php

require_once(dirname(__FILE__) . DIRECTORY_SEPARATOR . 'user_registration_common_action.php');
require_once(dirname(__FILE__) . DIRECTORY_SEPARATOR . '../../model/entity/tmp_user_entity.php');
require_once(dirname(__FILE__) . DIRECTORY_SEPARATOR . '../../model/repository/impl/tmp_user_multiple_select_repository_impl.php');
require_once(dirname(__FILE__) . DIRECTORY_SEPARATOR . '../../model/repository/impl/tmp_user_repository_impl.php');
require_once(dirname(__FILE__) . DIRECTORY_SEPARATOR . '../../model/repository/impl/zip_address_repository_impl.php');
require_once(dirname(__FILE__) . DIRECTORY_SEPARATOR . '../../validator/user_registration/user_registration_form_validator.php');

/**
 * ユーザー登録確認アクションクラス
 *
 * ユーザー登録確認画面で行われるビジネスロジックを定義
 */
class user_registration_confirm_action extends user_registration_common_action
{
  /**
   * ビジネスロジック実行
   */
  public function execute()
  {
    $form = $this->get_form();
    $form->trim_all_data();
    $properties = $form->get_all_properties();
    foreach ($properties as $field => $value)
    {
      if ('last_name' === $field ||
          'first_name' === $field)
      {
        $value = mb_convert_kana($value, 'KV');
      }
      else if ('last_name_hiragana' === $field ||
              'first_name_hiragana' === $field)
      {
        $value = mb_convert_kana($value, 'HVc');
      }
      else if ('zip_code' === $field ||
              'telephone_number' === $field)
      {
        $value = mb_convert_kana($value, 'n');
        $value = utility::replace_hyphen($value, '-');
      }
      else if ('city_street_address' === $field ||
              'building_room_address' === $field ||
              'job_other' === $field)
      {
        $value = mb_convert_kana($value, 'NSKV');
        $value = utility::replace_hyphen($value, 'ー');
      }

      $form->execute_accessor_method('set', $field, $value);
    }

    $birth_year = $form->get_birth_year();
    $birth_month = $form->get_birth_month();
    $birth_day = $form->get_birth_day();
    if (true === utility::is_empty($birth_year) &&
        true === utility::is_empty($birth_month) &&
        true === utility::is_empty($birth_day))
    {
      $birth_day_full = null;
    }
    else
    {
      $birth_day_full = $birth_year . '-' . sprintf('%02d', $birth_month) . '-' . sprintf('%02d', $birth_day);
    }
    $form->set_birth_day_full($birth_day_full);

    $zip_code = $form->get_zip_code();
    $zip_codes = explode('-', $zip_code);
    if (2 > count($zip_codes))
    {
      $zip_codes[0] = '';
      $zip_codes[1] = '';
    }

    // 郵便番号から住所情報を取得
    $storage_handlers = $this->get_storage_handlers();
    $zip_address_repository = new zip_address_repository_impl(
      $storage_handlers
    );
    $street_address_data = $zip_address_repository->get_street_address(
      $zip_codes[0] . $zip_codes[1]
    );

    $config = config::get_instance();
    if ('street_address_search' === $form->get_clicked_button())
    {
      $is_next_page_forward = false;

      if (null === $street_address_data)
      {
        $form->set_zip_code_error($config->search('zip_code_error'));
        $form->set_prefectures_id('');
        $form->set_city_street_address('');
      }
      else
      {
        $form->set_prefectures_id($street_address_data->get_prefectures_id());
        $form->set_city_street_address($street_address_data->get_city_district_county() . $street_address_data->get_town_village_address());
      }
    }
    else if ('next_page' === $form->get_clicked_button())
    {
      $is_next_page_forward = true;
      // バリデーション
      $validator = new user_registration_form_validator();
      $validator->set_form($form);
      $validator->set_validation_setting();
      $is_next_page_forward = $validator->validate();
      // 郵便番号の存在結果
      if (null === $form->get_zip_code_error() && null === $street_address_data)
      {
        $is_next_page_forward = false;
        $form->set_zip_code_error($config->search('zip_code_error'));
        $form->set_prefectures_id('');
        $form->set_city_street_address('');
      }
      // 複数の項目の組み合わせのチェック
      // アップロードされたファイルのチェックとアップロードファイルのデータの設定
      $file_upload_settings = array(
        array(
          'name' => 'file_name',
          'path' => 'file_path',
          'show_name' => '添付ファイル',
          'required' => false,
          'max_file_size' => 1048576,
          // 以下のコメントアウト箇所は、バージョンが新しい場合には有効だが
          // PHP5.2.17とPECLのFileinfo-1.0.4ではNG
          'allow_mime_types' => array(
            'image/gif' => true,
            'image/png' => true,
            'image/jpeg' => true,
            'application/pdf' => true,
            //'application/vnd.ms-excel' => true,
            //'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' => true,
            //'application/msword' => true,
            //'application/vnd.openxmlformats-officedocument.wordprocessingml.document' => true,
          ),
          'allow_extensions' => array(
            'image/gif' => array('gif' => true),
            'image/png' => array('png' => true),
            'image/jpeg' => array('jpg' => true, 'jpeg' => true),
            'application/pdf' => array('pdf' => true),
            //'application/vnd.ms-excel' => array('xls' => true),
            //'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' => array('xlsx' => true),
            //'application/msword' => array('doc' => true),
            //'application/vnd.openxmlformats-officedocument.wordprocessingml.document' => array('docx' => true),
          ),
          'is_file_name_check' => true,
          'max_length' => 64,
          'save_path_identifier' => $config->search('file_upload_identifier_user_registration'),
        ),
      );
      $res = $this->check_and_set_file_upload($file_upload_settings);
      if (0 < count($res))
      {
        $is_next_page_forward = false;
      }
    }
    else
    {
      throw new custom_exception('不正なリクエストです', __CLASS__ . ':' . __FUNCTION__);
    }

    if (true === $is_next_page_forward)
    {
      $tmp_user_repository = new tmp_user_repository_impl(
        $storage_handlers,
        new tmp_user_multiple_select_repository_impl($storage_handlers)
      );
      $tmp_user_id = '';
      $is_tmp_user_exist = true;
      for ($i = 0; $i < 5; $i++)
      {
        // 一意なIDを作成
        $tmp_user_id = utility::get_unique_id();
        // 一意なIDの存在チェック
        $tmp_user_data = $tmp_user_repository->get_tmp_user(
          $tmp_user_id
        );
        if (null === $tmp_user_data)
        {
          $is_tmp_user_exist = false;
          break;
        }
      }
      if (true === $is_tmp_user_exist)
      {
        // まず来ないと思うが
        throw new custom_exception('一意なIDの作成に失敗しました', __CLASS__ . ':' . __FUNCTION__);
      }
      else
      {
        $multiple_select_repository = new multiple_select_repository_impl(
          $storage_handlers,
          new multiple_select_repository_impl($storage_handlers)
        );
        $multiple_select_data = $multiple_select_repository->get_all_multiple_select();

        $tmp_user_entity = new tmp_user_entity();
        $tmp_user_multiple_select_data = array();
        $tmp_user_table_columns = $tmp_user_entity->get_table_columns();
        $properties = $form->get_all_properties();
        foreach ($properties as $field => $value)
        {
          if (true === array_key_exists($field, $tmp_user_table_columns))
          {
            if ('birth_year' === $field ||
              'birth_month' === $field ||
              'birth_day' === $field)
            {
            }
            else
            {
              $method_name = 'set_' . $field;
              if ('password' === $field)
              {
                // パスワードをハッシュ化
                $authentication = new authentication_id_pass();
                $authentication->set_id($tmp_user_id);
                $authentication->set_pass($value);
                $value = $authentication->get_password_to_hash();
              }
              else if ('file_name' === $field)
              {
                // 配列の時はアップロードされていない
                if (true === is_array($value))
                {
                  $form->set_file_name('');
                  $value = '';
                }
              }
              else if ('file_path' === $field)
              {
                // nullの時はアップロードされていない
                if (null === $value)
                {
                  $value = '';
                }
              }
              $tmp_user_entity->$method_name($value);
            }
          }
          else
          {
            if ('birth_day_full' === $field)
            {
              $tmp_user_entity->set_birth_day($value);
            }
            else if ('contact_method' === $field ||
                'knew_trigger' === $field)
            {
              if ('contact_method' === $field)
              {
                $multiple_select_category_id = 1;
              }
              else
              {
                $multiple_select_category_id = 2;
              }
              foreach ($value as $val)
              {
                foreach ($multiple_select_data as $multiple_select)
                {
                  if ($multiple_select->get_multiple_select_category_id() === $multiple_select_category_id &&
                    $multiple_select->get_value() === $val)
                  {
                    $tmp_user_multiple_select_data[] = $multiple_select->get_multiple_select_id();
                    break;
                  }
                }
              }
            }
          }
        }
        // ユーザー情報の一時保存テーブルに一意なIDのレコードが存在しなかったら、CSRFトークンセット
        $tmp_user_entity->set_tmp_user_id($tmp_user_id);
        $tmp_user_entity->set_token(security::get_token());
        // 入力された内容を、ユーザー情報の一時保存テーブルに保存
        $affected_rows = $tmp_user_repository->insert_tmp_user($tmp_user_entity, $tmp_user_multiple_select_data);
        if (1 > $affected_rows)
        {
          throw new custom_exception('ユーザー情報の一時保存テーブルへの保存に失敗しました', __CLASS__ . ':' . __FUNCTION__);
        }
        $form->set_tmp_user_id($tmp_user_entity->get_tmp_user_id());
        $form->set_token($tmp_user_entity->get_token());
      }
    }
    else
    {
      $this->set_template_file_path(self::PREVIOUS_TEMPLATE_FILE);
    }

    // 全てのフォームデータをアサインする
    $this->assign_all_form_data();

    // 複数選択項目の表示内容を取得して設定
    $this->set_multiple_value_item();

    // 複数選択項目の選択状態を設定
    $this->select_multiple_value_item();
  }

  /**
   * 遷移元画面のテンプレートファイル名
   */
  const PREVIOUS_TEMPLATE_FILE = 'user_registration_input.tpl';
}
