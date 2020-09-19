# -*- coding: utf-8 -*-
import os
import sys
import random
import threading
import time
import global_config as localConfig

if sys.version_info.major != 3:
    print('Please run under Python3')
    exit(1)
try:
    from common import debug, config, screenshot, UnicodeStreamFilter
    from common.auto_adb import auto_adb
    from common import apiutil
    from common.compression import resize_image
except Exception as ex:
    print(ex)
    print('请将脚本放在项目根目录中运行')
    print('请检查项目根目录中的 common 文件夹是否存在')
    exit(1)

adb = auto_adb()
adb.test_device()
config = config.open_accordant_config()


def _random_bias(num):
    """
    random bias
    :param num:
    :return:
    """
    return random.randint(-num, num)


def next_page():
    """
    翻到下一页
    :return:
    """
    cmd = 'shell input swipe {x1} {y1} {x2} {y2} {duration}'.format(
        x1=config['center_point']['x'],
        y1=config['center_point']['y'] + config['center_point']['ry'],
        x2=config['center_point']['x'],
        y2=config['center_point']['y'],
        duration=200
    )
    adb.run(cmd)
    time.sleep(1.5)


# 获取下载视频的文件名字
def getName():
    cmd1 = 'ls ' + localConfig.address
    data = adb.run(cmd1)
    datas = data.split("\n")
    for mp4 in datas:
        if "mp4" in mp4:
            names = mp4.split(" ")
            return names[3]


def download():
    """
    下载视频到本地后删除模拟器视频
    :return:
    """
    cmd = 'shell input tap 1020 1566'
    adb.run(cmd)
    time.sleep(1.5)
    cmd = 'shell input tap 193 1801'
    adb.run(cmd)
    time.sleep(3)
    name = getName()
    # 模拟器视频绝对地址
    path = localConfig.address + name

    if not os.path.exists(localConfig.localVideoPath):
        os.makedirs(localConfig.localVideoPath)
    # 下载命令
    cmd = 'pull ' + path + ' ' + localConfig.localVideoPath
    adb.run(cmd)
    time.sleep(6)
    # 删除原视频
    cmd = 'shell rm ' + path
    adb.run(cmd)


def tap(x, y):
    cmd = 'shell input tap {x} {y}'.format(
        x=x + _random_bias(10),
        y=y + _random_bias(10)
    )
    adb.run(cmd)


def main():
    """
    main
    :return:
    """
    print('程序版本号：{}'.format(localConfig.VERSION))

    debug.dump_device_info()
    screenshot.check_screenshot()

    while True:
        next_page()

        time.sleep(1)
        screenshot.pull_screenshot()

        resize_image('autojump.png', 'optimized.png', 1024 * 1024)

        with open('optimized.png', 'rb') as bin_data:
            image_data = bin_data.read()

        image_obj = apiutil.AiPlatImage(localConfig.imageAk, localConfig.imageSk)
        ad_obj = apiutil.AiPlatWord(localConfig.adAk, localConfig.adSk)

        adResult = ad_obj.ad_detectface(image_data)
        if adResult:
            print("这是一条广告，跳过下一条")
            continue

        rsp = image_obj.face_detectface(image_data)

        major_total = 0
        minor_total = 0

        if rsp['result'] != None:
            beauty = 0
            for face in rsp['result']['face_list']:

                msg_log = '[INFO] gender: {gender} age: {age} expression: {expression} beauty: {beauty}'.format(
                    gender=face['gender']['type'],
                    age=face['age'],
                    expression=face['expression']['type'],
                    beauty=face['beauty'],
                )
                print(msg_log)
                if face['beauty'] > beauty and face['gender']['type'] == 'female':
                    beauty = face['beauty']
                if face['age'] > localConfig.GIRL_MIN_AGE:
                    major_total += 1
                else:
                    minor_total += 1

            if beauty > localConfig.BEAUTY_THRESHOLD and major_total > minor_total:
                print('发现漂亮妹子！！！')
                try:
                    # 下载视频
                    download()
                except Exception as e:
                    print(e)
                    continue
            else:
                continue


# 运行前请先确认global_config.py 中的配置是你本地的配置
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        adb.run('kill-server')
        exit(0)
