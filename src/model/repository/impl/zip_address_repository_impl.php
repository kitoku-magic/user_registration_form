<?php

require_once(dirname(__FILE__) . DIRECTORY_SEPARATOR . '../zip_address_repository.php');

/**
 * zip_addressテーブルのデータ操作を行うリポジトリ
 */
class zip_address_repository_impl extends base_repository_impl implements zip_address_repository
{
  /**
   * コンストラクタ
   *
   * @param array $storage_handlers ストレージハンドラー配列
   */
  public function __construct(array $storage_handlers)
  {
    parent::__construct($storage_handlers, 'zip_address', array('zip_address_id'), array());
  }

  /**
   * 郵便番号から住所情報を取得する
   *
   * @param string $zip_code 郵便番号コード
   * @return zip_address_entity
   */
  public function get_street_address($zip_code)
  {
    $entity = null;

    $this->set_server_type('slave');

    $storage_handler = $this->get_storage_handler();
    $storage_handler->set_columns(array('prefectures_id', 'city_district_county', 'town_village_address'));
    $storage_handler->set_main_table_name($this->get_table_name());
    $storage_handler->set_where(array(
      array(
        'name' => 'zip_code',
        'bracket' => '=',
        'value' => '?',
        'conjunction' => '',
      )
    ));
    $storage_handler->set_bind_params(array(
      $zip_code,
    ));
    $storage_handler->set_bind_types(array(
      rdbms_storage_handler::PARAM_STR,
    ));

    $result = $this->select();

    if (true === $result)
    {
      $entity = $this->fetch(rdbms_storage_handler::FETCH_ONE);
    }

    return $entity;
  }
}
