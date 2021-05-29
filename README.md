# MKScript
some scripts written by Merack

### 0.如何安装油猴脚本管理器
各大主流浏览器商店内都能搜到油猴脚本管理器, 推荐violentmonkey和tampermonkey  
以edge浏览器为例, 可以到以下链接中安装其中一个即可
[violentmonkey](https://microsoftedge.microsoft.com/addons/detail/violentmonkey/eeagobfjdenkkddmbclomhiblgggliao?hl=en-US)
[tampermonkey](https://microsoftedge.microsoft.com/addons/detail/tampermonkey/iikmkjmpaadaobahmlepeloendndfphd?hl=en-US)

### 1.HelloZhiHao
智豪校园网自动答题脚本. 由于智豪哥很好人提供无限试错的机会, 所以写了这个脚本暴力填写.
##### 使用说明
需先安装油猴脚本管理器, 参照第0点
然后  [点我](https://cdn.jsdelivr.net/gh/Merack/MKScript/HelloZhiHao.user.js)  进行安装

### 2.zhihaoDump
爬取智豪校园网中接入网的测试题和答案  
智豪哥说考试选择题在里面出, 在网站上面做太麻烦了, 所以写了个脚本爬下来方便复习
##### 使用说明
```
python zhihaoDump.py
```
之后会在与脚本同级的目录下生成`zhihao`文件夹, 题目和答案就存在其中
![zhihaodump.png](https://pic.rmb.bdstatic.com/bjh/2df6c3fdf7b274c306f892b053b2bfb6.png)