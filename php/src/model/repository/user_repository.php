<?php

interface user_repository
{
  /**
   * userテーブルにレコードを追加する
   *
   * @param user_entity_base $user_entity user_entity_baseインスタンス
   * @param array $user_multiple_select_data ユーザー複数選択項目データ
   * @param string $token トークン値
   * @return int 追加された行数
   */
  public function insert_user(user_entity_base $user_entity, array $user_multiple_select_data, $token = null);
}
