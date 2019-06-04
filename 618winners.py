#!/usr/bin/env python
# -*- coding: utf8 -*-
# Power by Songe 2019-06-04 10:23:21


import os
import time
import random
from PIL import Image


# 截屏
def screencap():
    os.system('adb shell screencap -p /sdcard/618winners.png')  # 截屏活动页面
    os.system('adb pull /sdcard/618winners.png')    # 将截图发送至程序端


# 初始化上个页面位置
def initlocal():
    os.system('adb shell input swipe 900 500 900 800')  # 从上往下滑动，回到页面初始位置
    os.system('adb shell input tap 900 1670')   # 点击领喵币


# 返回上一页面
def goback():
    os.system('adb shell input keyevent KEYCODE_BACK')  # 返回


# 关闭“领喵币中心”弹窗
def closepop():
    os.system('adb shell input tap 995 420')    # 点击右上角关闭


# 逛店铺找猫猫得喵币
def guangdian():
    print('===== 领喵币中心，逛店铺 ======')
    for i in range(1, 51):
        initlocal()
        print('第 {} 次去逛店'.format(i))
        time.sleep(1)
        os.system('adb shell input tap 900 1100')   # 点击去逛店
        rtime = random.randint(12, 15)  # 随机等待12-15秒
        print('进入店铺，浏览中，请等待 {} 秒'.format(rtime))
        time.sleep(rtime)

        screencap()
        img = Image.open('618winners.png')
        # 两种不同的店铺展示页面
        if img.getpixel((970, 1110)) == (192, 48, 86, 255):
            os.system('adb shell input tap 970 1110')   # 点击得喵币
            print('成功抓到猫猫啦，现在返程')
            time.sleep(1)
            goback()
            time.sleep(1)
        elif img.getpixel((970, 1260)) == (57, 27, 28, 255):
            os.system('adb shell input tap 970 1260')   # 点击得喵币
            print('成功抓到猫猫啦，现在返程')
            time.sleep(1)
            goback()
            time.sleep(1)
        else:
            print('已完成 {} 次去逛店任务'.format(i))
            break
    print('已完成逛店铺找猫猫得喵币任务')


# 浏览会场10秒，三次会场一次小黑盒
def huichang():
    print('====== 领喵币中心，浏览会场 ======')
    for i in range(1, 5):
        initlocal()
        screencap()
        img = Image.open('618winners.png')
        # print(img.getpixel((900, 1288)))
        if img.getpixel((900, 1288)) == (244, 60, 74, 255):
            print('第 {} 次去浏览'.format(i))
            time.sleep(1)
            os.system('adb shell input tap 900 1288')   # 点击去浏览
            print('进入会场，浏览中，请等待 13 秒')
            time.sleep(13)
            if i == 4:  # 第四次是小黑盒会场，需点击得喵币
                os.system('adb shell input tap 970 1110')  # 点击得喵币
                print('成功抓到猫猫啦，现在返程')
                time.sleep(1)
            goback()
        else:
            print('已完成浏览会场得喵币任务')
            closepop()
            break
    print('已完成浏览会场得喵币任务')


# 浏览特卖会场10秒
def temai():
    print('====== 领喵币中心，浏览特卖 ======')
    initlocal()
    screencap()
    img = Image.open('618winners.png')
    # print(img.getpixel((900, 1462)))
    if img.getpixel((900, 1462)) == (244, 60, 74, 255):
        print('现在去浏览')
        time.sleep(1)
        os.system('adb shell input tap 900 1462')   # 点击去浏览
        print('进入会场，浏览中，请等待 13 秒')
        time.sleep(13)
        os.system('adb shell input tap 970 1260')  # 点击得喵币
        print('成功抓到猫猫啦，现在返程')
        time.sleep(1)
        goback()
    else:
        print('已完成浏览特卖会场得喵币任务')
        closepop()


# 浏览直播视频
def zhibo():
    print('====== 领喵币中心，浏览直播 ======')
    for i in range(1, 4):
        initlocal()
        screencap()
        img = Image.open('618winners.png')
        # print(img.getpixel((900, 1800)))
        if img.getpixel((900, 1800)) == (246, 64, 68, 255):
            print('第{}次去看直播'.format(i))
            time.sleep(1)
            os.system('adb shell input tap 900 1800')   # 点击去浏览
            print('进入直播，浏览中，请等待 15 秒')
            time.sleep(15)
            goback()
        else:
            print('已完成浏览直播视频得喵币任务')
            closepop()
            break
    print('已完成浏览直播视频得喵币任务')


guangdian()
huichang()
temai()
zhibo()
