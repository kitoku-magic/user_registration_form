<?php

class zip_address_entity_base extends entity
{
  // zip_address_id
  public function get_zip_address_id() { return $this->zip_address_id; }
  public function set_zip_address_id($v) { $this->zip_address_id = $v; }

  // zip_code
  public function get_zip_code() { return $this->zip_code; }
  public function set_zip_code($v) { $this->zip_code = $v; }

  // prefectures_id
  public function get_prefectures_id() { return $this->prefectures_id; }
  public function set_prefectures_id($v) { $this->prefectures_id = $v; }

  // city_district_county
  public function get_city_district_county() { return $this->city_district_county; }
  public function set_city_district_county($v) { $this->city_district_county = $v; }

  // town_village_address
  public function get_town_village_address() { return $this->town_village_address; }
  public function set_town_village_address($v) { $this->town_village_address = $v; }

  public function get_table_columns()
  {
    return array(
      'zip_address_id' => true,
      'zip_code' => true,
      'prefectures_id' => true,
      'city_district_county' => true,
      'town_village_address' => true,
    );
  }

  private $zip_address_id;
  private $zip_code;
  private $prefectures_id;
  private $city_district_county;
  private $town_village_address;
}
