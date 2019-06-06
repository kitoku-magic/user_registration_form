<?php

require_once(dirname(__FILE__) . DIRECTORY_SEPARATOR . 'generated/tmp_user_entity_base.php');

class tmp_user_entity extends tmp_user_entity_base
{
  // tmp_user_multiple_select_entities
  public function set_tmp_user_multiple_select_entities(array $tmp_user_multiple_select_entities) { $this->tmp_user_multiple_select_entities = $tmp_user_multiple_select_entities; }
  public function get_tmp_user_multiple_select_entities() { return $this->tmp_user_multiple_select_entities; }
  public function get_tmp_user_multiple_select_entity($index) { return $this->tmp_user_multiple_select_entities[$index]; }
  public function add_tmp_user_multiple_select_entity(tmp_user_multiple_select_entity_base $tmp_user_multiple_select_entity) { $this->tmp_user_multiple_select_entities[] = $tmp_user_multiple_select_entity; }

  private $tmp_user_multiple_select_entities;
}
