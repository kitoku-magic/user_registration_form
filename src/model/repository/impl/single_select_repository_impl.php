<?php

require_once(dirname(__FILE__) . DIRECTORY_SEPARATOR . '../single_select_repository.php');

/**
 * single_selectテーブルのデータ操作を行うリポジトリ
 */
class single_select_repository_impl extends base_repository_impl implements single_select_repository
{
  /**
   * コンストラクタ
   *
   * @param array $storage_handlers ストレージハンドラー配列
   */
  public function __construct(array $storage_handlers)
  {
    parent::__construct($storage_handlers, 'single_select', array('single_select_id'), array());
  }
}
