<?php

class single_select_entity_base extends entity
{
  // single_select_id
  public function get_single_select_id() { return $this->single_select_id; }
  public function set_single_select_id($v) { $this->single_select_id = $v; }

  // single_select_category_id
  public function get_single_select_category_id() { return $this->single_select_category_id; }
  public function set_single_select_category_id($v) { $this->single_select_category_id = $v; }

  // name
  public function get_name() { return $this->name; }
  public function set_name($v) { $this->name = $v; }

  // value
  public function get_value() { return $this->value; }
  public function set_value($v) { $this->value = $v; }

  // created_at
  public function get_created_at() { return $this->created_at; }
  public function set_created_at($v) { $this->created_at = $v; }

  // updated_at
  public function get_updated_at() { return $this->updated_at; }
  public function set_updated_at($v) { $this->updated_at = $v; }

  public function get_table_columns()
  {
    return array(
      'single_select_id' => true,
      'single_select_category_id' => true,
      'name' => true,
      'value' => true,
      'created_at' => true,
      'updated_at' => true,
    );
  }

  private $single_select_id;
  private $single_select_category_id;
  private $name;
  private $value;
  private $created_at;
  private $updated_at;
}
