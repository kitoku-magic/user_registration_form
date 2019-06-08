<?php

require_once(dirname(__FILE__) . DIRECTORY_SEPARATOR . '../multiple_select_repository.php');

/**
 * multiple_selectテーブルのデータ操作を行うリポジトリ
 */
class multiple_select_repository_impl extends base_repository_impl implements multiple_select_repository
{
  /**
   * コンストラクタ
   *
   * @param array $storage_handlers ストレージハンドラー配列
   */
  public function __construct(array $storage_handlers)
  {
    parent::__construct($storage_handlers, 'multiple_select', array('multiple_select_id'), array());
  }

  /**
   * 全ての複数選択項目情報を取得する
   *
   * @return array
   */
  public function get_all_multiple_select()
  {
    $this->set_server_type('slave');

    $storage_handler = $this->get_storage_handler();

    $storage_handler->set_columns('*');
    $storage_handler->set_main_table_name($this->get_table_name());

    $result = $this->select();

    $entities = array();
    if (true === $result)
    {
      $entities = $this->fetch(rdbms_storage_handler::FETCH_ALL);
    }

    return $entities;
  }
}
