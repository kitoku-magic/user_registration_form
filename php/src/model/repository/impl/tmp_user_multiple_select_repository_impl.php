<?php

require_once(dirname(__FILE__) . DIRECTORY_SEPARATOR . '../tmp_user_multiple_select_repository.php');

/**
 * tmp_user_multiple_selectテーブルのデータ操作を行うリポジトリ
 */
class tmp_user_multiple_select_repository_impl extends base_repository_impl implements tmp_user_multiple_select_repository
{
  /**
   * コンストラクタ
   *
   * @param array $storage_handlers ストレージハンドラー配列
   */
  public function __construct(array $storage_handlers)
  {
    parent::__construct($storage_handlers, 'tmp_user_multiple_select', array('tmp_user_id', 'multiple_select_id'), array());
  }
}
