<?php

require_once(dirname(__FILE__) . DIRECTORY_SEPARATOR . '../../entity/generated/user_entity_base.php');
require_once(dirname(__FILE__) . DIRECTORY_SEPARATOR . '../user_repository.php');
require_once(dirname(__FILE__) . DIRECTORY_SEPARATOR . '../user_multiple_select_repository.php');
require_once(dirname(__FILE__) . DIRECTORY_SEPARATOR . '../tmp_user_repository.php');

/**
 * userテーブルのデータ操作を行うリポジトリ
 */
class user_repository_impl extends base_repository_impl implements user_repository
{
  /**
   * コンストラクタ
   *
   * @param array $storage_handlers ストレージハンドラー配列
   * @param user_multiple_select_repository $user_multiple_select_repository user_multiple_select_repositoryインスタンス
   * @param tmp_user_repository $tmp_user_repository tmp_user_repositoryインスタンス
   */
  public function __construct(
    array $storage_handlers,
    user_multiple_select_repository $user_multiple_select_repository,
    tmp_user_repository $tmp_user_repository = null
  ) {
    parent::__construct($storage_handlers, 'user', array('user_id'), array('user_multiple_select'));
    $this->user_multiple_select_repository = $user_multiple_select_repository;
    $this->tmp_user_repository = $tmp_user_repository;
  }

  public function get_user_multiple_select_repository()
  {
    return $this->user_multiple_select_repository;
  }

  public function get_tmp_user_repository()
  {
    return $this->tmp_user_repository;
  }

  /**
   * userテーブルにレコードを追加する
   *
   * @param user_entity_base $user_entity user_entity_baseインスタンス
   * @param array $user_multiple_select_data ユーザー複数選択項目データ
   * @param string $token トークン値
   * @return int 追加された行数
   */
  public function insert_user(user_entity_base $user_entity, array $user_multiple_select_data, $token = null)
  {
    $storage_handler = $this->get_storage_handler();
    $storage_handler->set_main_table_name($this->get_table_name());

    $table_columns = $user_entity->get_table_columns();
    $storage_handler->set_columns(array_keys($table_columns));
    $storage_handler->set_values(array_pad(array(), count($table_columns), '?'));
    $bind_params = array();
    $bind_types = array();
    foreach ($table_columns as $table_column => $bind_type)
    {
      if ('created_at' === $table_column ||
          'updated_at' === $table_column)
      {
        $bind_param = utility::get_current_time_stamp();
      }
      else
      {
        $getter = 'get_' . $table_column;
        $bind_param = $user_entity->$getter();
      }
      $bind_params[] = $bind_param;
      $bind_types[] = $bind_type;
    }
    $storage_handler->set_bind_params($bind_params);
    $storage_handler->set_bind_types($bind_types);

    // userテーブルにレコードを追加する
    $affected_rows = $this->insert();

    if (0 < $affected_rows)
    {
      $user_id = $user_entity->get_user_id();

      $storage_handler = $this->user_multiple_select_repository->get_storage_handler();
      $storage_handler->set_main_table_name($this->user_multiple_select_repository->get_table_name());
      $storage_handler->set_columns(array('user_id', 'multiple_select_id', 'created_at', 'updated_at'));
      $storage_handler->set_values(array('?', '?', '?', '?'));

      foreach ($user_multiple_select_data as $multiple_select_id)
      {
        $storage_handler->set_bind_params(array(
          $user_id,
          $multiple_select_id,
          utility::get_current_time_stamp(),
          utility::get_current_time_stamp()
        ));
        $storage_handler->set_bind_types(array(
          rdbms_storage_handler::PARAM_STR,
          rdbms_storage_handler::PARAM_INT,
          rdbms_storage_handler::PARAM_INT,
          rdbms_storage_handler::PARAM_INT
        ));

        // user_multiple_selectテーブルにレコードを追加する
        $affected_rows = $this->user_multiple_select_repository->insert();
        if (1 > $affected_rows)
        {
          break;
        }
      }

      if (0 < $affected_rows)
      {
        // トークンが設定されている場合には、tmp_userテーブルのデータも削除する
        if (null !== $token)
        {
          $affected_rows = $this->tmp_user_repository->delete_tmp_user($user_id, $token);
        }
      }
    }

    return $affected_rows;
  }

  private $user_multiple_select_repository;

  private $tmp_user_repository;
}
