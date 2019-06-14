import os
import random
import time

import pyautogui
from PIL import ImageGrab
from PIL import Image
from PIL import ImageOps
import win32gui
import numpy as np


def random_num(num):
    """ 生成0~num之间的随机值"""
    return random_range(0, num)


def random_range(start, end):
    """生成start~end之间的随机值"""
    return random.randint(start, end)


def get_current_time():
    """获取当前系统时间 格式化成2016-03-20 11:45:39形式"""
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


def sleep_random(sleep_time):
    """程序休眠随机数毫秒"""
    time.sleep(random_num(sleep_time) * 0.001)


def get_image_list(path):
    """获取目录下文件名称"""
    return os.listdir(path)


def get_window_info():
    """获取程序窗口信息"""
    return win32gui.GetWindowRect(win32gui.FindWindow(0, u'吕工'))


def get_image_locate(image):
    """获取当前截图的位置(x, y, width, height)，x、y 为截图的左上角坐标，width、height 为截图的宽高"""
    window_info = get_window_info()
    # 目标窗口图像
    src_image = ImageGrab.grab(window_info)
    # 目标图像
    tar_image = Image.open(image)

    # 相对阴阳师窗口的位置
    relative_pos = pyautogui.locate(tar_image, src_image)
    if relative_pos is None:
        print_log('未找到', image)
        return None
    # 绝对窗口位置
    target_pos = [relative_pos[0] + window_info[0], relative_pos[1] + window_info[1], relative_pos[2], relative_pos[3]]
    return target_pos


def get_random_locate(locate):
    """根据坐标位置，生成坐标区域内的随机坐标点"""
    return locate[0] + random_num(locate[2]), locate[1] + random_num(locate[3])


def print_log(*log):
    """打印日志输出"""
    print(get_current_time(), log)


def click_image(image):
    """点击指定截图"""
    try:
        # 获取当前截图的位置(x, y, width, height)，x、y 为截图的左上角坐标，width、height 为截图的宽高
        locate = get_image_locate(image)
        if locate is not None:
            sleep_random(250)
            random_locate = get_random_locate(locate)
            pyautogui.click(random_locate[0], random_locate[1])
            # print_log("点击图片：", image)
            # 每次点击截图前，程序休眠0~1000毫秒
            sleep_random(250)
            random_locate = get_random_locate(locate)
            pyautogui.click(random_locate[0], random_locate[1])
            print_log("点击图片：", image)
    except Exception as ex:
        str_error = ex.args[2]
        sleep_random(2000)
        if '无效的窗口句柄。' == str_error:
            print_log('异常信息', '请先打开程序窗口')
        else:
            print_log('异常信息', str_error)
        # 如果程序出现异常,捕获之,但不处理,继续执行


def start_job():
    """开启任务"""
    # 每次点击之后暂停2.5秒
    # pyautogui.PAUSE = 2.5
    # 当pyautogui.FAILSAFE = True时，如果把鼠标光标在屏幕左上角，PyAutoGUI函数就会产生pyautogui.FailSafeException异常。
    pyautogui.FAILSAFE = True

    # 一个while循环，程序一直在这里循环执行
    # 在命令行中同时按下Ctrl + C，能停止程序运行
    while True:
        # 获取截图目录下的截图列表
        image_list = get_image_list(".\\images")
        # 遍历截图列表
        for image in image_list:
            # 扫描当前屏幕，点击与当前截图相类似的位置
            click_image(".\\images\\" + image)


if __name__ == '__main__':
    """程序执行入口"""
    # start_job()
    # 窗口位置信息
    window_info = get_window_info()
    # 窗口位置图像信息
    src_image = ImageGrab.grab(window_info)
    # 保存图片
    src_image.save('F:\image_test.png')
    # 打开图片
    open_image = Image.open('F:\image_test.png')
    # 图像像素信息
    image_data = np.asarray(src_image.getdata())
    print(image_data)
