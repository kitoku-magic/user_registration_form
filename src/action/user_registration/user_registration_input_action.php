<?php

require_once(dirname(__FILE__) . DIRECTORY_SEPARATOR . 'user_registration_common_action.php');
require_once(dirname(__FILE__) . DIRECTORY_SEPARATOR . '../../model/repository/impl/tmp_user_multiple_select_repository_impl.php');
require_once(dirname(__FILE__) . DIRECTORY_SEPARATOR . '../../model/repository/impl/tmp_user_repository_impl.php');

/**
 * ユーザー登録入力アクションクラス
 *
 * ユーザー登録入力画面で行われるビジネスロジックを定義
 */
class user_registration_input_action extends user_registration_common_action
{
  /**
   * ビジネスロジック実行
   */
  public function execute()
  {
    $form = $this->get_form();
    if ('previous_page' === $form->get_clicked_button())
    {
      $storage_handlers = $this->get_storage_handlers();
      $tmp_user_repository = new tmp_user_repository_impl(
        $storage_handlers,
        new tmp_user_multiple_select_repository_impl($storage_handlers)
      );
      $this->all_tmp_user = $tmp_user_repository->get_all_tmp_user($form->get_tmp_user_id(), $form->get_token());
      foreach ($this->all_tmp_user as $tmp_user)
      {
        $entity_table_columns = $tmp_user->get_table_columns();
        foreach ($entity_table_columns as $table_column => $value)
        {
          $getter = 'get_' . $table_column;
          if ('password' === $table_column)
          {
            // パスワードは表示させない
            $entity_value = '';
          }
          else
          {
            $entity_value = $tmp_user->$getter();
          }
          $form->execute_accessor_method('set', $table_column, $entity_value);
        }
      }
    }

    // フォームの初期値を設定する為の初期化
    $this->assign_all_form_data();

    // 複数選択項目の表示内容を取得して設定
    $this->set_multiple_value_item();

    // 複数選択項目の初期選択状態を設定
    $this->select_multiple_value_item();
  }

  protected function set_all_tmp_user($all_tmp_user)
  {
    $this->all_tmp_user = $all_tmp_user;
  }

  protected function get_all_tmp_user()
  {
    return $this->all_tmp_user;
  }

  private $all_tmp_user;
}
