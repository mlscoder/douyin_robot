# -- coding: utf-8 --

# 当前版本
VERSION = "0.0.1"

DEBUG_SWITCH = True
FACE_PATH = 'face/'

# 你的adb安装目录 中间不能有空格
adb_path = "D:\\ClockworkMod\\Universal\\adb.exe"

# 视频下载目录 需要先创建目录 没有新增创建方法
localVideoPath = 'E:/download'

# 模拟器视频存放地址
# 我使用的逍遥模拟器，不同模拟器储存路径不一样，需要确认
address = '/storage/emulated/0/DCIM/Camera/'

# 百度开放人脸识别API Key
# 免费申请，可以用下面两个测试
imageAk = "RDFsfMmDLkWgeLPTjCV7NxEN"
imageSk = "GFmqeSnaEnUFQwMYqdkTx6R68zknWT03"

# 百度开放广告识别API Key
adAk = "50GBT3prXgpj5UanutFxL6Xp"
adSk = "5rS6gG2l8xLUvGchDlpnkF4Wb71nw9Ks"

# 自定义审美最低分数 超过此分数会被下载。分数范围（1-100）
BEAUTY_THRESHOLD = 50
# 自定义最小年龄
GIRL_MIN_AGE = 14
