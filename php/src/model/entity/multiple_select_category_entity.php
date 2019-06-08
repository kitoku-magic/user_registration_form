<?php

require_once(dirname(__FILE__) . DIRECTORY_SEPARATOR . 'generated/multiple_select_category_entity_base.php');

class multiple_select_category_entity extends multiple_select_category_entity_base
{
  // multiple_select_entities
  public function set_multiple_select_entities(array $multiple_select_entities) { $this->multiple_select_entities = $multiple_select_entities; }
  public function get_multiple_select_entities() { return $this->multiple_select_entities; }
  public function get_multiple_select_entity($index) { return $this->multiple_select_entities[$index]; }
  public function add_multiple_select_entity(multiple_select_entity_base $multiple_select_entity) { $this->multiple_select_entities[] = $multiple_select_entity; }

  private $multiple_select_entities;
}
