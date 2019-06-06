<?php

require_once(dirname(__FILE__) . DIRECTORY_SEPARATOR . 'generated/single_select_category_entity_base.php');

class single_select_category_entity extends single_select_category_entity_base
{
  // single_select_entities
  public function set_single_select_entities(array $single_select_entities) { $this->single_select_entities = $single_select_entities; }
  public function get_single_select_entities() { return $this->single_select_entities; }
  public function get_single_select_entity($index) { return $this->single_select_entities[$index]; }
  public function add_single_select_entity(single_select_entity_base $single_select_entity) { $this->single_select_entities[] = $single_select_entity; }

  private $single_select_entities;
}
