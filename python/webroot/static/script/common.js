// 優先度中：可能な限り、CSS側で制御したい

/**
 * 指定IDにフォーカスを移す
 *
 * @param id エレメントのID
 */
function setFocus(id)
{
  document.getElementById(id).focus();
}

/**
 * 指定した色に背景色を変更する(優先度中：ここはCSSで出来るはず)
 *
 * @param element 要素名
 * @param back_ground_color 変更したい背景色
 */
function setBackGroundColor(element, back_ground_color)
{
  element.style.backgroundColor = back_ground_color;
}

/**
 * 指定したアクションにフォーム送信する
 *
 * @param form_id フォームのID名
 * @param action フォームのアクション値（リクエスト先のURL）
 * @param method フォームメソッド名（POSTなど）
 */
function submitForm(form_id, action, method)
{
  var target = document.getElementById(form_id);
  target.method = method;
  target.action = action;
  target.submit();

  return false;
}
