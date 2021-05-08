// ==UserScript==
// @name         HelloZhiHao
// @namespace    https://merack.top/
// @version      0.1
// @description  complete homework automatically in www.zhihao.com!
// @author       Merack
// @e-mail       Merack@qq.com
// @updateURL    https://cdn.jsdelivr.net/gh/Merack/MKScript/HelloZhiHao.user.js
// @match        http://www.zhihao.com/jrwtest*/*.asp
// @match        http://www.zhihao.com/jrwtest*/*.htm
// @require      https://cdn.bootcdn.net/ajax/libs/jquery/3.6.0/jquery.slim.min.js
// @grant        GM_setValue
// @grant        GM_getValue
// ==/UserScript==

"use strict";

const FLAG = "optionFlag";

var doc = $("body").text();
if (doc.indexOf("开始答题") > 0 || doc.indexOf("开始答题") == 0) {
  $("a")[0].click();
}

var flag = GM_getValue(FLAG, 0);

var ans = $('input[name="answer1"]');
var submit = $('input[type="submit"]');
if (ans.length) {
  ans.eq(flag).click();
  submit.click();
}
if (doc.indexOf("答案错误") > 0 || doc.indexOf("答案错误") == 0) {
  flag++;
  GM_setValue(FLAG, flag);
  // console.log(flag);
  $("a")[0].click();
}

if (doc.indexOf("答案正确") > 0 || doc.indexOf("答案正确") == 0) {
  GM_setValue(FLAG, 0);
  $("a")[0].click();
}

// console.log(doc);
// console.log(flag);
// console.log(ans);
