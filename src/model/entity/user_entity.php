<?php

require_once(dirname(__FILE__) . DIRECTORY_SEPARATOR . 'generated/user_entity_base.php');

class user_entity extends user_entity_base
{
  // user_multiple_select_entities
  public function set_user_multiple_select_entities(array $user_multiple_select_entities) { $this->user_multiple_select_entities = $user_multiple_select_entities; }
  public function get_user_multiple_select_entities() { return $this->user_multiple_select_entities; }
  public function get_user_multiple_select_entity($index) { return $this->user_multiple_select_entities[$index]; }
  public function add_user_multiple_select_entity(user_multiple_select_entity_base $user_multiple_select_entity) { $this->user_multiple_select_entities[] = $user_multiple_select_entity; }

  private $user_multiple_select_entities;
}
