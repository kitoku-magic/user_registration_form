<?php

interface zip_address_repository
{
  /**
   * 郵便番号から住所情報を取得する
   *
   * @param string $zip_code 郵便番号コード
   * @return zip_address_entity
   */
  public function get_street_address($zip_code);
}
