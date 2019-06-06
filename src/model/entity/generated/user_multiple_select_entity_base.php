<?php

class user_multiple_select_entity_base extends entity
{
  // user_id
  public function get_user_id() { return $this->user_id; }
  public function set_user_id($v) { $this->user_id = $v; }

  // multiple_select_id
  public function get_multiple_select_id() { return $this->multiple_select_id; }
  public function set_multiple_select_id($v) { $this->multiple_select_id = $v; }

  // created_at
  public function get_created_at() { return $this->created_at; }
  public function set_created_at($v) { $this->created_at = $v; }

  // updated_at
  public function get_updated_at() { return $this->updated_at; }
  public function set_updated_at($v) { $this->updated_at = $v; }

  public function get_table_columns()
  {
    return array(
      'user_id' => rdbms_storage_handler::PARAM_STR,
      'multiple_select_id' => rdbms_storage_handler::PARAM_INT,
      'created_at' => rdbms_storage_handler::PARAM_INT,
      'updated_at' => rdbms_storage_handler::PARAM_INT,
    );
  }

  private $user_id;
  private $multiple_select_id;
  private $created_at;
  private $updated_at;
}
