<?php

interface tmp_user_repository
{
  /**
   * 一時ユーザーIDから一時ユーザー情報を取得する
   *
   * @param string $tmp_user_id 一時ユーザーID
   * @return tmp_user_entity
   */
  public function get_tmp_user($tmp_user_id);

  /**
   * 一時ユーザーIDとトークンから、全ての一時ユーザー情報を取得する
   *
   * @param string $tmp_user_id
   * @param string $token
   * @return array
   */
  public function get_all_tmp_user($tmp_user_id, $token);

  /**
   * tmp_userテーブルにレコードを追加する
   *
   * @param tmp_user_entity_base $tmp_user_entity
   * @param array $tmp_user_multiple_select_data
   * @return int
   */
  public function insert_tmp_user(tmp_user_entity_base $tmp_user_entity, array $tmp_user_multiple_select_data);

  /**
   * tmp_userテーブルのレコードを削除する
   *
   * @param string $tmp_user_id
   * @param string $token
   * @return int
   */
  public function delete_tmp_user($tmp_user_id, $token);
}
