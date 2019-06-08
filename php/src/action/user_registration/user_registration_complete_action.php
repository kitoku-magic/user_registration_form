<?php

require_once(dirname(__FILE__) . DIRECTORY_SEPARATOR . 'user_registration_common_action.php');
require_once(dirname(__FILE__) . DIRECTORY_SEPARATOR . '../../model/entity/user_entity.php');
require_once(dirname(__FILE__) . DIRECTORY_SEPARATOR . '../../model/repository/impl/tmp_user_repository_impl.php');
require_once(dirname(__FILE__) . DIRECTORY_SEPARATOR . '../../model/repository/impl/tmp_user_multiple_select_repository_impl.php');
require_once(dirname(__FILE__) . DIRECTORY_SEPARATOR . '../../model/repository/impl/user_repository_impl.php');
require_once(dirname(__FILE__) . DIRECTORY_SEPARATOR . '../../model/repository/impl/user_multiple_select_repository_impl.php');

/**
 * ユーザー登録完了アクションクラス
 *
 * ユーザー登録完了画面で行われるビジネスロジックを定義
 */
class user_registration_complete_action extends user_registration_common_action
{
  /**
   * ビジネスロジック実行
   */
  public function execute()
  {
    $form = $this->get_form();

    if ('next_page' !== $form->get_clicked_button())
    {
      throw new custom_exception('不正なリクエストです', __CLASS__ . ':' . __FUNCTION__);
    }

    $storage_handlers = $this->get_storage_handlers();

    $tmp_user_repository = new tmp_user_repository_impl(
      $storage_handlers,
      new tmp_user_multiple_select_repository_impl($storage_handlers)
    );

    $token = $form->get_token();
    $all_tmp_user = $tmp_user_repository->get_all_tmp_user($form->get_tmp_user_id(), $token);

    if (0 < count($all_tmp_user))
    {
      $all_tmp_user = $all_tmp_user[0];
      $all_tmp_user_token = $all_tmp_user->get_token();
      // CSRF対策用のトークン値のチェック
      if (true === security::check_csrf_token($token, $all_tmp_user_token))
      {
        $config = config::get_instance();
        $user_repository = new user_repository_impl(
          $storage_handlers,
          new user_multiple_select_repository_impl($storage_handlers),
          $tmp_user_repository
        );

        $user_entity = new user_entity();
        $user_multiple_select_data = array();
        $old_file_path = '';
        $user_table_columns = $user_entity->get_table_columns();
        foreach ($user_table_columns as $user_table_column => $value)
        {
          $setter = 'set_' . $user_table_column;
          $prefix = '';
          if ('user_id' === $user_table_column)
          {
            $prefix = 'tmp_';
          }
          $getter = 'get_' . $prefix . $user_table_column;
          $set_value = $all_tmp_user->$getter();
          if ('file_path' === $user_table_column)
          {
            $old_file_path = $set_value;
            $set_value = str_replace($config->search('app_file_tmp_save_path'), $config->search('app_file_save_path'), $set_value);
          }
          $user_entity->$setter($set_value);
        }
        $user_entity->set_user_id($all_tmp_user->get_tmp_user_id());

        $tmp_user_multiple_select_entities = $all_tmp_user->get_tmp_user_multiple_select_entities();
        foreach ($tmp_user_multiple_select_entities as $tmp_user_multiple_select_entity)
        {
          $user_multiple_select_data[] = $tmp_user_multiple_select_entity->get_multiple_select_id();
        }

        // 入力された内容を、ユーザー情報テーブルに保存
        $user_repository->begin();
        $user_repository->get_user_multiple_select_repository()->begin();
        $user_repository->get_tmp_user_repository()->begin();
        $affected_rows = $user_repository->insert_user($user_entity, $user_multiple_select_data, $all_tmp_user_token);
        if (0 < $affected_rows)
        {
					$new_file_path = $user_entity->get_file_path();
					if ('' === $new_file_path)
					{
						// アップロードされていない時
						$user_repository->get_tmp_user_repository()->commit();
						$user_repository->get_user_multiple_select_repository()->commit();
						$user_repository->commit();
					}
					else
					{
						$new_dir = dirname($new_file_path);
						$ret = utility::make_directory($new_dir);
						if (true === $ret)
						{
							chmod($new_dir, 0700);
							$ret = rename($old_file_path, $new_file_path);
							if (true === $ret)
							{
								chmod($new_file_path, 0600);
								$user_repository->get_tmp_user_repository()->commit();
								$user_repository->get_user_multiple_select_repository()->commit();
								$user_repository->commit();
							}
							else
							{
								$user_repository->get_tmp_user_repository()->rollback();
								$user_repository->get_user_multiple_select_repository()->rollback();
								$user_repository->rollback();
								throw new custom_exception('添付ファイルの保存に失敗しました', __CLASS__ . ':' . __FUNCTION__);
							}
						}
						else
						{
							$user_repository->get_tmp_user_repository()->rollback();
							$user_repository->get_user_multiple_select_repository()->rollback();
							$user_repository->rollback();
							throw new custom_exception('添付ファイルの保存先の作成に失敗しました', __CLASS__ . ':' . __FUNCTION__);
						}
					}
        }
        else
        {
          $user_repository->get_tmp_user_repository()->rollback();
          $user_repository->get_user_multiple_select_repository()->rollback();
          $user_repository->rollback();
          throw new custom_exception('ユーザー情報テーブルへの保存に失敗しました', __CLASS__ . ':' . __FUNCTION__);
        }
      }
      else
      {
        throw new custom_exception('不正なリクエストです', __CLASS__ . ':' . __FUNCTION__);
      }
    }
    else
    {
      throw new custom_exception('該当のユーザー情報が存在しませんでした', __CLASS__ . ':' . __FUNCTION__);
    }
  }
}
