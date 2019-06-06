<?php

require_once(dirname(__FILE__) . DIRECTORY_SEPARATOR . '../user_multiple_select_repository.php');

/**
 * user_multiple_selectテーブルのデータ操作を行うリポジトリ
 */
class user_multiple_select_repository_impl extends base_repository_impl implements user_multiple_select_repository
{
  /**
   * コンストラクタ
   *
   * @param array $storage_handlers ストレージハンドラー配列
   */
  public function __construct(array $storage_handlers)
  {
    parent::__construct($storage_handlers, 'user_multiple_select', array('user_id', 'multiple_select_id'), array());
  }
}
