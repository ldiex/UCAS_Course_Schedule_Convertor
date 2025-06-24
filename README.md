# 国科大自动获取课表信息并导出ics文件脚本
## 使用
Google Calender 直接支持导入`ics`文件. 如果你想要在 Apple Calendar 上使用, 可以先导入 Google Calendar, 然后直接在 iOS / macOS 中登录你的 Google Account 启用日历的同步; 你也可以打开 Google Calender 对应日历的分享功能, 然后在任何支持 iCal 链接的日历 App 中使用. 
## 鸣谢
本脚本的爬虫基于由热心学长开发的[UCAS Score Update Monitor](https://github.com/ljs-2002/UCAS_ScoreUpdateMonitor)
## 程序配置
和[UCAS Score Update Monitor](https://github.com/ljs-2002/UCAS_ScoreUpdateMonitor)一致，引用如下：

- 所有平台都具有的基本文件结构及基本配置过程如下：

  1. 打开`./config/userInfo.json`文件，在`userName`字段填入登陆`SEP`的用户名，在`password`字段填入登陆`SEP`的密码；

     - 这两个字段用于模拟登陆；
  2. 首次使用/若上次登陆sep时使用的浏览器与之前使用的浏览器不同/手动登陆sep时出现了重新认证提示，请打开`./config/config.json`文件，修改**User-Agent**字段为最新的浏览器User-Agent。
     - 附获取浏览器User-Agent的方法：在浏览器地址栏输入**about:version**，打开的页面中的**用户代理**，或**User-Agent**，或**UA**即为所需User-Agent。
## 程序运行
如无报错，执行`python main.py`后，该脚本将在运行目录下输出`course_schedule.ics`文件
