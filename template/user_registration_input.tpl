<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="ja" lang="ja">
<head>
<meta http-equiv="content-type" content="text/html; charset=utf-8" />
<link rel="stylesheet" href="css/style.css" type="text/css" media="all" />
<script type="text/javascript" src="script/common.js" charset="utf-8"></script>
<title>ユーザー登録</title>
</head>
<body onload="setFocus('mail_address');">
<div id="layout">
  <form id="user_registration_input" action="index.php?screen=user_registration&process=confirm" method="post" enctype="multipart/form-data">
    <table id="user_form_table">
      <tr>
        <th id="user_form_midashi" colspan="2">
          ユーザー情報
        </th>
      </tr>
      <tr>
        <th>メールアドレス</th>
        <td>
          <input type="text" id="mail_address" name="mail_address" maxlength="128" size="35" value=";;;mail_address;;;" onfocus="setBackGroundColor(this, '#d0ffd0');"
          onblur="setBackGroundColor(this, '#ffffff');" /><br />
          <p class="error_message">;;;mail_address_error;;;</p>
        </td>
      </tr>
      <tr>
        <th>パスワード</th>
        <td>
          <input type="password" id="password" name="password" maxlength="256" size="20" value=";;;password;;;"
          onfocus="setBackGroundColor(this, '#d0ffd0');" onblur="setBackGroundColor(this, '#ffffff');" /> &lt;8文字以上半角英数字&gt;<br />
          <p class="error_message">;;;password_error;;;</p>
        </td>
      </tr>
      <tr>
        <th>氏名</th>
        <td>
          (姓) <input type="text" id="last_name" name="last_name" maxlength="8" size="14" value=";;;last_name;;;"
          onfocus="setBackGroundColor(this, '#d0ffd0');" onblur="setBackGroundColor(this, '#ffffff');" />
          (名) <input type="text" id="first_name" name="first_name" maxlength="8" size="14" value=";;;first_name;;;"
          onfocus="setBackGroundColor(this, '#d0ffd0');" onblur="setBackGroundColor(this, '#ffffff');" /><br />
          <p class="error_message">;;;last_name_error;;;</p>
          <p class="error_message">;;;first_name_error;;;</p>
        </td>
      </tr>
      <tr>
        <th>氏名（ふりがな）</th>
        <td>
          (姓) <input type="text" id="last_name_hiragana" name="last_name_hiragana" maxlength="16" size="14" value=";;;last_name_hiragana;;;"
          onfocus="setBackGroundColor(this, '#d0ffd0');" onblur="setBackGroundColor(this, '#ffffff');" />
          (名) <input type="text" id="first_name_hiragana" name="first_name_hiragana" maxlength="16" size="14" value=";;;first_name_hiragana;;;"
          onfocus="setBackGroundColor(this, '#d0ffd0');" onblur="setBackGroundColor(this, '#ffffff');" /><br />
          <p class="error_message">;;;last_name_hiragana_error;;;</p>
          <p class="error_message">;;;first_name_hiragana_error;;;</p>
        </td>
      </tr>
      <tr>
        <th>;;;sex;;;</th>
        <td>
          |||sexes|||
          <input type="radio" name="sex_id" value=";;;value;;;" :::sex_id@;;;value;;;:::>;;;name;;;</input>
          |||/sexes|||
          <br />
          <p class="error_message">;;;sex_id_error;;;</p>
        </td>
      </tr>
      <tr>
        <th>誕生日</th>
        <td>
          <select id="birth_year" name="birth_year" onfocus="setBackGroundColor(this, '#d0ffd0');" onblur="setBackGroundColor(this, '#ffffff');">
            <option value="" :::birth_year@:::>-</option>
            |||birth_years|||
            <option value=";;;value;;;" :::birth_year@;;;value;;;:::>;;;name;;;</option>
            |||/birth_years|||
          </select>
          年
          <select id="birth_month" name="birth_month" onfocus="setBackGroundColor(this, '#d0ffd0');" onblur="setBackGroundColor(this, '#ffffff');">
            <option value="" :::birth_month@:::>-</option>
            |||birth_months|||
            <option value=";;;value;;;" :::birth_month@;;;value;;;:::>;;;name;;;</option>
            |||/birth_months|||
          </select>
          月
          <select id="birth_day" name="birth_day" onfocus="setBackGroundColor(this, '#d0ffd0');" onblur="setBackGroundColor(this, '#ffffff');">
            <option value="" :::birth_day@:::>-</option>
            |||birth_days|||
            <option value=";;;value;;;" :::birth_day@;;;value;;;:::>;;;name;;;</option>
            |||/birth_days|||
          </select>
          日<br />
          <p class="error_message">;;;birth_year_error;;;</p>
          <p class="error_message">;;;birth_month_error;;;</p>
          <p class="error_message">;;;birth_day_error;;;</p>
          <p class="error_message">;;;birth_day_full_error;;;</p>
        </td>
      </tr>
      <tr>
        <th>郵便番号</th>
        <td>
          <input type="text" id="zip_code" name="zip_code" maxlength="8" size="14" value=";;;zip_code;;;"
          onfocus="setBackGroundColor(this, '#d0ffd0');" onblur="setBackGroundColor(this, '#ffffff');" /> &lt;要ハイフン&gt;<br />
          <button type="submit" id="street_address_search" name="clicked_button" value="street_address_search" />住所検索</button><br />
          <p class="error_message">;;;zip_code_error;;;</p>
        </td>
      </tr>
      <tr>
        <th>;;;prefectures;;;</th>
        <td>
          <select id="prefectures_id" name="prefectures_id" onfocus="setBackGroundColor(this, '#d0ffd0');" onblur="setBackGroundColor(this, '#ffffff');">
            <option value="" :::prefectures_id@:::>▼選択してください</option>
            |||prefectureses|||
            <option value=";;;value;;;" :::prefectures_id@;;;value;;;:::>;;;name;;;</option>
            |||/prefectureses|||
          </select><br />
          <p class="error_message">;;;prefectures_id_error;;;</p>
        </td>
      </tr>
      <tr>
        <th>市区町村・丁目・番地</th>
        <td>
          <input type="text" id="city_street_address" name="city_street_address" value=";;;city_street_address;;;" maxlength="64" size="70"
          onfocus="setBackGroundColor(this, '#d0ffd0');" onblur="setBackGroundColor(this, '#ffffff');" /><br />
          <p class="error_message">;;;city_street_address_error;;;</p>
        </td>
      </tr>
      <tr>
        <th>建物名・室名</th>
        <td>
          <input type="text" id="building_room_address" name="building_room_address" value=";;;building_room_address;;;" maxlength="64" size="70"
          onfocus="setBackGroundColor(this, '#d0ffd0');" onblur="setBackGroundColor(this, '#ffffff');" /><br />
          <p class="error_message">;;;building_room_address_error;;;</p>
        </td>
      </tr>
      <tr>
        <th>電話番号</th>
        <td>
          <input type="text" id="telephone_number" name="telephone_number" maxlength="13" size="27" value=";;;telephone_number;;;"
          onfocus="setBackGroundColor(this, '#d0ffd0');" onblur="setBackGroundColor(this, '#ffffff');" /> &lt;要ハイフン&gt;<br />
          <p class="error_message">;;;telephone_number_error;;;</p>
        </td>
      </tr>
      <tr>
        <th>;;;job;;;</th>
        <td>
          |||jobs|||
          <input type="radio" name="job_id" value=";;;value;;;" :::job_id@;;;value;;;:::>;;;name;;;</input>
          |||/jobs|||
          <input type="radio" name="job_id" value="0" :::job_id@0:::>その他</input>
          <br />
          <p class="error_message">;;;job_id_error;;;</p>
        </td>
      </tr>
      <tr>
        <th>職業その他</th>
        <td>
          <input type="text" id="job_other" name="job_other" value=";;;job_other;;;" maxlength="16" size="20"
          onfocus="setBackGroundColor(this, '#d0ffd0');" onblur="setBackGroundColor(this, '#ffffff');" /><br />
          <p class="error_message">;;;job_other_error;;;</p>
        </td>
      </tr>
      <tr>
        <th>;;;contact_method;;;</th>
        <td>
          <select id="contact_method" name="contact_method[]" multiple onfocus="setBackGroundColor(this, '#d0ffd0');" onblur="setBackGroundColor(this, '#ffffff');">
            |||contact_methods|||
            <option value=";;;value;;;" :::contact_method@;;;value;;;:::>;;;name;;;</option>
            |||/contact_methods|||
          </select><br />
          <p class="error_message">;;;contact_method_error;;;</p>
        </td>
      </tr>
      <tr>
        <th>;;;knew_trigger;;;</th>
        <td>
          |||knew_triggeres|||
          <input type="checkbox" name="knew_trigger[]" value=";;;value;;;" :::knew_trigger@;;;value;;;:::>;;;name;;;</input>
          |||/knew_triggeres|||
          <p class="error_message">;;;knew_trigger_error;;;</p>
        </td>
      </tr>
      <tr>
        <th>最新情報の希望状況</th>
        <td>
          <input type="radio" name="is_latest_news_hoped" value="1" :::is_latest_news_hoped@1:::>希望する</input>
          <input type="radio" name="is_latest_news_hoped" value="0" :::is_latest_news_hoped@0:::>希望しない</input><br />
          <p class="error_message">;;;is_latest_news_hoped_error;;;</p>
        </td>
      </tr>
      <tr>
        <th>添付ファイル</th>
        <td>
          <input type="file" name="file_name" value=";;;file_name;;;" onfocus="setBackGroundColor(this, '#d0ffd0');" onblur="setBackGroundColor(this, '#ffffff');" /><br />
          <p class="error_message">;;;file_name_error;;;</p>
        </td>
      </tr>
      <tr>
        <th>備考</th>
        <td>
          <textarea id="remarks" name="remarks" maxlength="1000" rows="10" cols="70" onfocus="setBackGroundColor(this, '#d0ffd0');" onblur="setBackGroundColor(this, '#ffffff');">;;;remarks;;;</textarea><br />
          <p class="error_message">;;;remarks_error;;;</p>
        </td>
      </tr>
      <tr>
        <th>個人情報提供の同意状況</th>
        <td>
          <input type="checkbox" name="is_personal_information_provide_agreed" value="1" :::is_personal_information_provide_agreed@1:::>同意する</input>
          <p class="error_message">;;;is_personal_information_provide_agreed_error;;;</p>
        </td>
      </tr>
    </table>
    <div id="submit">
      <p><button type="submit" id="next_page" name="clicked_button" value="next_page" />次へ</button></p>
    </div>
  </form>
</div>
</body>
</html>
