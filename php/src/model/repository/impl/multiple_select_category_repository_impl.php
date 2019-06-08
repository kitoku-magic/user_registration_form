<?php

require_once(dirname(__FILE__) . DIRECTORY_SEPARATOR . '../multiple_select_category_repository.php');

/**
 * multiple_select_categoryテーブルのデータ操作を行うリポジトリ
 */
class multiple_select_category_repository_impl extends base_repository_impl implements multiple_select_category_repository
{
  /**
   * コンストラクタ
   *
   * @param array $storage_handlers ストレージハンドラー配列
   * @param multiple_select_repository $multiple_select_repository multiple_select_repositoryインスタンス
   */
  public function __construct(array $storage_handlers, multiple_select_repository $multiple_select_repository)
  {
    parent::__construct(
      $storage_handlers,
      'multiple_select_category',
      array('multiple_select_category_id'),
      array('multiple_select')
    );
    $this->multiple_select_repository = $multiple_select_repository;
  }

  public function get_multiple_select_repository()
  {
    return $this->multiple_select_repository;
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

    $storage_handler->set_is_column_unique(true);
    $storage_handler->set_columns(array(
      array($this->get_table_name(), 'multiple_select_category_id'),
      array($this->get_table_name(), 'name'),
      array($this->get_multiple_select_repository()->get_table_name(), 'multiple_select_id'),
      array($this->get_multiple_select_repository()->get_table_name(), 'multiple_select_category_id'),
      array($this->get_multiple_select_repository()->get_table_name(), 'name'),
      array($this->get_multiple_select_repository()->get_table_name(), 'value'),
    ));
    $storage_handler->set_main_table_name($this->get_table_name());
    $storage_handler->set_join(array(
      array(
        'join_type' => 'INNER',
        'join_table' => $this->get_multiple_select_repository()->get_table_name(),
        'join_where' => array(
          array(
            'main_table' => $this->get_table_name(),
            'main_column' => 'multiple_select_category_id',
            'bracket' => '=',
            'relation_table' => $this->get_multiple_select_repository()->get_table_name(),
            'relation_column' => 'multiple_select_category_id',
            'conjunction' => '',
          ),
        ),
      ),
    ));

    $result = $this->select();

    $entities = array();
    if (true === $result)
    {
      $entities = $this->fetch_all_associated_entity();
    }

    return $entities;
  }

  private $multiple_select_repository;
}
