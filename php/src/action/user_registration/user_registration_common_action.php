<?php

require_once(dirname(__FILE__) . DIRECTORY_SEPARATOR . '../../model/repository/impl/multiple_select_category_repository_impl.php');
require_once(dirname(__FILE__) . DIRECTORY_SEPARATOR . '../../model/repository/impl/multiple_select_repository_impl.php');
require_once(dirname(__FILE__) . DIRECTORY_SEPARATOR . '../../model/repository/impl/single_select_category_repository_impl.php');
require_once(dirname(__FILE__) . DIRECTORY_SEPARATOR . '../../model/repository/impl/single_select_repository_impl.php');

/**
 * ユーザー登録共通アクションクラス
 *
 * ユーザー登録画面で複数回行われるビジネスロジックを定義
 */
abstract class user_registration_common_action extends file_upload_action
{
  /**
   * 全てのフォームデータをアサインする
   */
  protected function assign_all_form_data()
  {
    $template_convert = $this->get_template_convert();
    $properties = $this->get_form()->get_all_properties();
    foreach ($properties as $field => $value)
    {
      $template_convert->assign_single_array($field, $value);
    }
  }

  /**
   * 複数選択項目の表示内容を取得して設定
   */
  protected function set_multiple_value_item()
  {
    $template_convert = $this->get_template_convert();

    // 複数選択可能な項目のデータを取得
    $storage_handlers = $this->get_storage_handlers();
    $multiple_select_category_repository = new multiple_select_category_repository_impl(
      $storage_handlers,
      new multiple_select_repository_impl($storage_handlers)
    );
    $this->multiple_select_category_data = $multiple_select_category_repository->get_all_multiple_select();

    $category_mappings = array(
      // 連絡方法
      1 => array(
        'name' => 'contact_method',
        'names' => 'contact_methods',
      ),
      // 知ったきっかけ
      2 => array(
        'name' => 'knew_trigger',
        'names' => 'knew_triggeres',
      ),
    );
    foreach ($this->multiple_select_category_data as $multiple_select_category)
    {
      $template_convert->assign_single_array($category_mappings[$multiple_select_category->get_multiple_select_category_id()]['name'], $multiple_select_category->get_name());
      $template_convert->assign_bool_array($category_mappings[$multiple_select_category->get_multiple_select_category_id()]['names'], $multiple_select_category->get_multiple_select_entities());
    }

    // 単一選択な項目のデータを取得
    $single_select_category_repository = new single_select_category_repository_impl(
      $storage_handlers,
      new single_select_repository_impl($storage_handlers)
    );
    $single_select_category_data = $single_select_category_repository->get_all_single_select();

    $category_mappings = array(
      // 性別
      1 => array(
        'name' => 'sex',
        'names' => 'sexes',
      ),
      // 誕生日（年）
      2 => array(
        'name' => 'birth_year',
        'names' => 'birth_years',
      ),
      // 誕生日（月）
      3 => array(
        'name' => 'birth_month',
        'names' => 'birth_months',
      ),
      // 誕生日（日）
      4 => array(
        'name' => 'birth_day',
        'names' => 'birth_days',
      ),
      // 都道府県
      5 => array(
        'name' => 'prefectures',
        'names' => 'prefectureses',
      ),
      // 職業
      6 => array(
        'name' => 'job',
        'names' => 'jobs',
      ),
    );
    foreach ($single_select_category_data as $single_select_category)
    {
      $template_convert->assign_single_array($category_mappings[$single_select_category->get_single_select_category_id()]['name'], $single_select_category->get_name());
      $template_convert->assign_bool_array($category_mappings[$single_select_category->get_single_select_category_id()]['names'], $single_select_category->get_single_select_entities());
    }
  }

  /**
   * 複数選択項目の選択状態を設定
   */
  protected function select_multiple_value_item()
  {
    //---------------------------
    // 動的セレクトボックス（単一）を生成
    //---------------------------
    // 誕生日（年）
    $this->create_select_box('birth_year', '');

    // 誕生日（月）
    $this->create_select_box('birth_month', '');

    // 誕生日（日）
    $this->create_select_box('birth_day', '');

    // 都道府県
    $this->create_select_box('prefectures_id', '');

    //-----------------------
    // 動的ラジオボタンを生成
    //-----------------------
    // 性別
    $this->create_radio_box('sex_id', '1');

    // 職業ID
    $this->create_radio_box('job_id', '1');

    // 最新情報のお知らせ
    $this->create_radio_box('is_latest_news_hoped', '1');

    //-----------------------------------
    // 動的チェックボックス（単一）を生成
    //-----------------------------------
    // 個人情報の取扱同意
    $this->create_check_box('is_personal_information_provide_agreed', '');

    //-----------------------------------
    // 動的セレクトボックス（複数）を生成
    //-----------------------------------
    // 連絡方法
    $this->create_multiple_select_box('contact_method', 1, array());

    //-----------------------------------
    // 動的チェックボックス（複数）を生成
    //-----------------------------------
    // 知ったきっかけ
    $this->create_multiple_check_box('knew_trigger', 2, array());
  }

  /**
   * 動的セレクトボックスを生成する
   *
   */
  protected function create_select_box($key, $select_value)
  {
    $form = $this->get_form();

    // 遷移元を判断
    if ('previous_page' === $form->get_clicked_button())
    {
      if (0 === strpos($key, 'birth_'))
      {
        // 誕生日
        $form_value = $form->get_birth_day();
        if (null === $form_value)
        {
          // 初回表示時
          $value = $select_value;
        }
        else
        {
          // 上記以外
          $birth_days = explode('-', $form_value);
          if ('birth_year' === $key)
          {
            $value = $birth_days[0];
          }
          else if ('birth_month' === $key)
          {
            $value = ltrim($birth_days[1], '0');
          }
          else
          {
            $value = ltrim($birth_days[2], '0');
          }
        }
      }
      else
      {
        // フォームの値
        $form_value = $form->execute_accessor_method('get', $key);
        if (null === $form_value)
        {
          // 初回表示時
          $value = $select_value;
        }
        else
        {
          // 上記以外
          $value = $form_value;
        }
      }
    }
    else
    {
      // フォームの値
      $form_value = $form->execute_accessor_method('get', $key);
      if (null === $form_value)
      {
        // 初回表示時
        $value = $select_value;
      }
      else
      {
        // 上記以外
        $value = $form_value;
      }
    }

    // 初期選択状態にしたい値を設定
    $this->get_template_convert()->assign_multi_array($key, $value, 'selected="selected"', '');
  }

  /**
   * 動的ラジオボタンを生成する
   *
   */
  protected function create_radio_box($key, $select_value)
  {
    $form = $this->get_form();

    // フォームの値
    $form_value = $form->execute_accessor_method('get', $key);
    if (null === $form_value)
    {
      // 初回表示時
      $value = $select_value;
    }
    else
    {
      // 上記以外
      $value = $form_value;
    }

    // 初期選択状態にしたい値を設定
    $this->get_template_convert()->assign_multi_array($key, $value, 'checked="checked"', '');
  }

  /**
   * 動的チェックボックスを生成する
   *
   */
  protected function create_check_box($key, $select_value)
  {
    $form = $this->get_form();

    // フォームの値
    $form_value = $form->execute_accessor_method('get', $key);
    if (null === $form_value)
    {
      // 初回表示時
      $value = $select_value;
    }
    else
    {
      // 上記以外
      $value = $form_value;
    }

    // 初期選択状態にしたい値を設定
    $this->get_template_convert()->assign_multi_array($key, $value, 'checked="checked"', '');
  }

  /**
   * 動的セレクトボックス（複数）を生成する
   *
   */
  protected function create_multiple_select_box($key, $category_id, $select_value)
  {
    $form = $this->get_form();
    // 遷移元を判断
    if ('previous_page' === $form->get_clicked_button())
    {
      //-------------------------------
      // 確認画面から戻るボタンで遷移時
      //-------------------------------
      $value = array();
      $all_tmp_user = $this->get_all_tmp_user();
      foreach ($all_tmp_user as $tmp_user)
      {
        $tmp_user_multiple_select_entities = $tmp_user->get_tmp_user_multiple_select_entities();
        foreach ($tmp_user_multiple_select_entities as $tmp_user_multiple_select_entity)
        {
          foreach ($this->multiple_select_category_data as $multiple_select_category)
          {
            $multiple_select_entities = $multiple_select_category->get_multiple_select_entities();
            foreach ($multiple_select_entities as $multiple_select_entity)
            {
              if ($category_id === $multiple_select_category->get_multiple_select_category_id() &&
                  $tmp_user_multiple_select_entity->get_multiple_select_id() === $multiple_select_entity->get_multiple_select_id())
              {
                $value[] = $multiple_select_entity->get_value();
              }
            }
          }
        }
      }
    }
    else
    {
      //---------
      // 上記以外
      //---------
      // フォームの値
      $form_value = $form->execute_accessor_method('get', $key);
      if (null === $form_value)
      {
        // 初回表示時
        $value = $select_value;
      }
      else
      {
        // 上記以外
        $value = $form_value;
      }
    }

    // 初期選択状態にしたい値を設定
    $this->get_template_convert()->assign_multi_array($key, $value, 'selected="selected"', '');
  }

  /**
   * 動的チェックボックス（複数）を生成する
   *
   */
  protected function create_multiple_check_box($key, $category_id, $select_value)
  {
    $form = $this->get_form();
    // 遷移元を判断
    if ('previous_page' === $form->get_clicked_button())
    {
      //-------------------------------
      // 確認画面から戻るボタンで遷移時
      //-------------------------------
      $value = array();
      $all_tmp_user = $this->get_all_tmp_user();
      foreach ($all_tmp_user as $tmp_user)
      {
        $tmp_user_multiple_select_entities = $tmp_user->get_tmp_user_multiple_select_entities();
        foreach ($tmp_user_multiple_select_entities as $tmp_user_multiple_select_entity)
        {
          foreach ($this->multiple_select_category_data as $multiple_select_category)
          {
            $multiple_select_entities = $multiple_select_category->get_multiple_select_entities();
            foreach ($multiple_select_entities as $multiple_select_entity)
            {
              if ($category_id === $multiple_select_category->get_multiple_select_category_id() &&
                  $tmp_user_multiple_select_entity->get_multiple_select_id() === $multiple_select_entity->get_multiple_select_id())
              {
                $value[] = $multiple_select_entity->get_value();
              }
            }
          }
        }
      }
    }
    else
    {
      //---------
      // 上記以外
      //---------
      // フォームの値
      $form_value = $form->execute_accessor_method('get', $key);
      if (null === $form_value)
      {
        // 初回表示時
        $value = $select_value;
      }
      else
      {
        // 上記以外
        $value = $form_value;
      }
    }

    // 初期選択状態にしたい値を設定
    $this->get_template_convert()->assign_multi_array($key, $value, 'checked="checked"', '');
  }

  /**
   * 複数選択可能データ
   */
  private $multiple_select_category_data;
}
