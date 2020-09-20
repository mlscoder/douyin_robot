# douyin_robot
**如何教抖音自己刷视频** 

> 站在巨人的肩膀上能节约很多事
> 参考：https://github.com/wangshub/Douyin-Bot

## 改进：
1. 原来的腾讯ai因为某些原因现在不能使用，切换到百度云ai平台
2. 加入下载功能
3. 加入广告区分
4. 新功能开发中ing
5. 真机改用模拟器 我使用的是[逍遥模拟器](https://www.xyaz.cn/)

## 原理
* 打开模拟器《抖音短视频》APP，进入主界面
* 获取手机截图，并对截图进行压缩 (Size < 1MB)；
* 请求 [图文识别 API](https://cloud.baidu.com/product/ocr_general) 判断当前页面是否是广告
* 请求 [人脸识别 API](https://cloud.baidu.com/product/face) 判断当前页面人脸性别、年龄、颜值打分
* 当颜值大于门限值 BEAUTY_THRESHOLD（个人定义阈值）时，下载视频
* 将安卓系统下载的视频下载到window本地，并且删除原视频
* 重新进行第一步操作

## 使用教程
* Python版本：3.0及以上
* 相关软件工具安装和使用步骤请参考 ADB [Android 操作步骤](https://github.com/wangshub/wechat_jump_game/wiki/Android-%E5%92%8C-iOS-%E6%93%8D%E4%BD%9C%E6%AD%A5%E9%AA%A4) 
* 在 [百度智能云](https://login.bce.baidu.com/) 免费申请 AK(API Key)和 SK(Secret Key) ,注意需要申请两个 图文识别 和 人脸识别

1. 获取源码 git clone  https://github.com/mlscoder/douyin_robot.git
2. 安装需要的包，缺少的包安装最新版本即可
3. 运行程序 python douyin-bot.py 

## tips 
* 安装adb路径中不能带空格，安装后需要将路径配置到环境变量
* global_config.py中的路径为D:\\ClockworkMod\\Universal\\adb.exe 需要更换成你本地的路径
* 安装模拟器可设置分辨率，请选择1920*1080，并且开启开发者选项
