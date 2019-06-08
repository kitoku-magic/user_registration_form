<?php

class multiple_select_category_entity_base extends entity
{
  // multiple_select_category_id
  public function get_multiple_select_category_id() { return $this->multiple_select_category_id; }
  public function set_multiple_select_category_id($v) { $this->multiple_select_category_id = $v; }

  // name
  public function get_name() { return $this->name; }
  public function set_name($v) { $this->name = $v; }

  // created_at
  public function get_created_at() { return $this->created_at; }
  public function set_created_at($v) { $this->created_at = $v; }

  // updated_at
  public function get_updated_at() { return $this->updated_at; }
  public function set_updated_at($v) { $this->updated_at = $v; }

  public function get_table_columns()
  {
    return array(
      'multiple_select_category_id' => true,
      'name' => true,
      'created_at' => true,
      'updated_at' => true,
    );
  }

  private $multiple_select_category_id;
  private $name;
  private $created_at;
  private $updated_at;
}
