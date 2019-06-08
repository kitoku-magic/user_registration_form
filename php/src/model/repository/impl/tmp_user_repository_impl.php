<?php

require_once(dirname(__FILE__) . DIRECTORY_SEPARATOR . '../../entity/generated/tmp_user_entity_base.php');
require_once(dirname(__FILE__) . DIRECTORY_SEPARATOR . '../tmp_user_repository.php');
require_once(dirname(__FILE__) . DIRECTORY_SEPARATOR . '../tmp_user_multiple_select_repository.php');

/**
 * tmp_userテーブルのデータ操作を行うリポジトリ
 */
class tmp_user_repository_impl extends base_repository_impl implements tmp_user_repository
{
  /**
   * コンストラクタ
   *
   * @param array $storage_handlers ストレージハンドラー配列
   * @param tmp_user_multiple_select_repository $tmp_user_multiple_select_repository tmp_user_multiple_select_repositoryインスタンス
   */
  public function __construct(array $storage_handlers, tmp_user_multiple_select_repository $tmp_user_multiple_select_repository)
  {
    parent::__construct($storage_handlers, 'tmp_user', array('tmp_user_id'), array('tmp_user_multiple_select'));
    $this->tmp_user_multiple_select_repository = $tmp_user_multiple_select_repository;
  }

  /**
   * 一時ユーザーIDから一時ユーザー情報を取得する
   *
   * @param string $tmp_user_id 一時ユーザーID
   * @return tmp_user_entity
   */
  public function get_tmp_user($tmp_user_id)
  {
    $entity = null;

    $this->set_server_type('slave');

    $storage_handler = $this->get_storage_handler();
    $storage_handler->set_columns('*');
    $storage_handler->set_main_table_name($this->get_table_name());
    $storage_handler->set_where(array(
      array(
        'name' => 'tmp_user_id',
        'bracket' => '=',
        'value' => '?',
        'conjunction' => '',
      )
    ));
    $storage_handler->set_bind_params(array(
      $tmp_user_id,
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

  /**
   * 一時ユーザーIDとトークンから、全ての一時ユーザー情報を取得する
   *
   * @param string $tmp_user_id
   * @param string $token
   * @return array
   */
  public function get_all_tmp_user($tmp_user_id, $token)
  {
    $this->set_server_type('slave');

    $storage_handler = $this->get_storage_handler();

    $storage_handler->set_is_column_unique(true);
    $storage_handler->set_columns(array(
      array($this->get_table_name(), 'tmp_user_id'),
      array($this->get_table_name(), 'token'),
      array($this->get_table_name(), 'mail_address'),
      array($this->get_table_name(), 'password'),
      array($this->get_table_name(), 'last_name'),
      array($this->get_table_name(), 'first_name'),
      array($this->get_table_name(), 'last_name_hiragana'),
      array($this->get_table_name(), 'first_name_hiragana'),
      array($this->get_table_name(), 'sex_id'),
      array($this->get_table_name(), 'birth_day'),
      array($this->get_table_name(), 'zip_code'),
      array($this->get_table_name(), 'prefectures_id'),
      array($this->get_table_name(), 'city_street_address'),
      array($this->get_table_name(), 'building_room_address'),
      array($this->get_table_name(), 'telephone_number'),
      array($this->get_table_name(), 'job_id'),
      array($this->get_table_name(), 'job_other'),
      array($this->get_table_name(), 'is_latest_news_hoped'),
      array($this->get_table_name(), 'file_name'),
      array($this->get_table_name(), 'file_path'),
      array($this->get_table_name(), 'remarks'),
      array($this->get_table_name(), 'is_personal_information_provide_agreed'),
      array($this->tmp_user_multiple_select_repository->get_table_name(), 'tmp_user_id'),
      array($this->tmp_user_multiple_select_repository->get_table_name(), 'multiple_select_id'),
    ));
    $storage_handler->set_main_table_name($this->get_table_name());
    $storage_handler->set_join(array(
      array(
        'join_type' => 'INNER',
        'join_table' => $this->tmp_user_multiple_select_repository->get_table_name(),
        'join_where' => array(
          array(
            'main_table' => $this->get_table_name(),
            'main_column' => 'tmp_user_id',
            'bracket' => '=',
            'relation_table' => $this->tmp_user_multiple_select_repository->get_table_name(),
            'relation_column' => 'tmp_user_id',
            'conjunction' => '',
          ),
        ),
      ),
    ));
    $storage_handler->set_where(array(
      array(
        'table' => $this->get_table_name(),
        'name' => 'tmp_user_id',
        'bracket' => '=',
        'value' => '?',
        'conjunction' => 'AND',
      ),
      array(
        'table' => $this->get_table_name(),
        'name' => 'token',
        'bracket' => '=',
        'value' => '?',
        'conjunction' => '',
      ),
    ));
    $storage_handler->set_bind_params(array(
      $tmp_user_id,
      $token,
    ));
    $storage_handler->set_bind_types(array(
      rdbms_storage_handler::PARAM_STR,
      rdbms_storage_handler::PARAM_STR,
    ));

    $result = $this->select();

    $entities = array();
    if (true === $result)
    {
      $entities = $this->fetch_all_associated_entity();
    }

    return $entities;
  }

  /**
   * tmp_userテーブルにレコードを追加する
   *
   * @param tmp_user_entity_base $tmp_user_entity
   * @param array $tmp_user_multiple_select_data
   * @return int
   */
  public function insert_tmp_user(tmp_user_entity_base $tmp_user_entity, array $tmp_user_multiple_select_data)
  {
    $this->begin();

    $storage_handler = $this->get_storage_handler();
    $storage_handler->set_main_table_name($this->get_table_name());

    $table_columns = $tmp_user_entity->get_table_columns();
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
        $bind_param = $tmp_user_entity->$getter();
      }
      $bind_params[] = $bind_param;
      $bind_types[] = $bind_type;
    }
    $storage_handler->set_bind_params($bind_params);
    $storage_handler->set_bind_types($bind_types);

    // tmp_userテーブルにレコードを追加する
    $affected_rows = $this->insert();

    if (0 < $affected_rows)
    {
      $this->tmp_user_multiple_select_repository->begin();

      $tmp_user_id = $tmp_user_entity->get_tmp_user_id();

      $storage_handler = $this->tmp_user_multiple_select_repository->get_storage_handler();
      $storage_handler->set_main_table_name($this->tmp_user_multiple_select_repository->get_table_name());
      $storage_handler->set_columns(array('tmp_user_id', 'multiple_select_id', 'created_at', 'updated_at'));
      $storage_handler->set_values(array('?', '?', '?', '?'));

      foreach ($tmp_user_multiple_select_data as $multiple_select_id)
      {
        $storage_handler->set_bind_params(array(
          $tmp_user_id,
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

        // tmp_user_multiple_selectテーブルにレコードを追加する
        $affected_rows = $this->tmp_user_multiple_select_repository->insert();
        if (1 > $affected_rows)
        {
          break;
        }
      }

      if (0 < $affected_rows)
      {
        $this->tmp_user_multiple_select_repository->commit();
        $this->commit();
      }
      else
      {
        $this->tmp_user_multiple_select_repository->rollback();
        $this->rollback();
      }
    }
    else
    {
      $this->rollback();
    }

    return $affected_rows;
  }

  /**
   * tmp_userテーブルのレコードを削除する
   *
   * @param string $tmp_user_id
   * @param string $token
   * @return int
   */
  public function delete_tmp_user($tmp_user_id, $token)
  {
    $storage_handler = $this->get_storage_handler();
    $storage_handler->set_main_table_name($this->get_table_name());

    $storage_handler->set_where(array(
      array(
        'name' => 'tmp_user_id',
        'bracket' => '=',
        'value' => '?',
        'conjunction' => 'AND',
      ),
      array(
        'name' => 'token',
        'bracket' => '=',
        'value' => '?',
        'conjunction' => '',
      ),
    ));
    $storage_handler->set_bind_params(array(
      $tmp_user_id,
      $token,
    ));
    $storage_handler->set_bind_types(array(
      rdbms_storage_handler::PARAM_STR,
      rdbms_storage_handler::PARAM_STR,
    ));

    return $this->delete();
  }

  private $tmp_user_multiple_select_repository;
}
