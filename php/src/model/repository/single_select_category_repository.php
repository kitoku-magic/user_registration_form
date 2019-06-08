<?php

interface single_select_category_repository
{
  /**
   * 全ての単一選択項目情報を取得する
   * 
   * @return array
   */
  public function get_all_single_select();
}
