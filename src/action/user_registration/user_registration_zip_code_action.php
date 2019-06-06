<?php

require_once(dirname(__FILE__) . DIRECTORY_SEPARATOR . 'user_registration_common_action.php');
require_once(dirname(__FILE__) . DIRECTORY_SEPARATOR . '../../model/repository/impl/zip_address_repository_impl.php');
require_once(dirname(__FILE__) . DIRECTORY_SEPARATOR . '../../model/repository/impl/single_select_repository_impl.php');

/**
 * ユーザー登録住所取得アクションクラス
 *
 * ユーザー登録住所取得処理で行われるビジネスロジックを定義
 */
class user_registration_zip_code_action extends user_registration_common_action
{
  /**
   * ビジネスロジック実行
   *
   */
  public function execute()
  {
    $form = $this->get_form();

    // 郵便番号から住所情報を取得
    $storage_handlers = $this->get_storage_handlers();
    $zip_address_repository = new zip_address_repository_impl(
      $storage_handlers
    );
    $zip_codes = explode('-', $form->get_zip_code());
    if (2 > count($zip_codes))
    {
      $zip_codes[0] = '';
      $zip_codes[1] = '';
    }
    $street_address_data = $zip_address_repository->get_street_address($zip_codes[0] . $zip_codes[1]);

    if (null !== $street_address_data)
    {
      $template_convert = $this->get_template_convert();
      $template_convert->assign_single_array('prefectures_id', $street_address_data->get_prefectures_id());
      $template_convert->assign_single_array('city_district_county', $street_address_data->get_city_district_county());
      $template_convert->assign_single_array('town_village_address', $street_address_data->get_town_village_address());
    }
  }
}
