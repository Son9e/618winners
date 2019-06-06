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


# 浏览会场10秒，三次会场一次家电会场一次小黑盒
def huichang():
    print('====== 领喵币中心，浏览会场 ======')
    for i in range(1, 6):
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
            if i == 4:  # 第四次是家电会场，需点击得喵币
                os.system('adb shell input tap 970 1110')  # 点击得喵币
                print('成功抓到猫猫啦，现在返程')
                time.sleep(1)
            if i == 5:  # 第五次是小黑盒会场，需点击得喵币
                os.system('adb shell input tap 970 1500')  # 点击开盒领喵币图标
                time.sleep(3)
                os.system('adb shell input tap 555 1260')  # 点击开盒领喵币按钮
                print('成功领到喵币，现在返程')
                time.sleep(1)
                goback()
                time.sleep(1)
            goback()
        else:
            print('已完成浏览会场得喵币任务')
            closepop()
            break
    print('已完成浏览会场得喵币任务')


# 浏览聚划算会场、特卖会场
def juhuasuan():
    print('====== 领喵币中心，浏览聚划算 ======')
    for i in range(1, 4):
        initlocal()
        screencap()
        img = Image.open('618winners.png')
        # print(img.getpixel((900, 1462)))
        if img.getpixel((900, 1462)) == (244, 60, 74, 255):
            print('第 {} 次去浏览'.format(i))
            time.sleep(1)
            os.system('adb shell input tap 900 1462')   # 点击去浏览
            if i == 1:  # 第二次是进特卖会场，需点击得喵币
                print('进入聚划算会场，浏览三个商品')
                time.sleep(5)
                os.system('adb shell input tap 960 1200')   # 跳转商品列表页
                time.sleep(2)
                print('点击第一个商品')
                os.system('adb shell input tap 290 640')   # 点击第一个商品
                time.sleep(2)
                goback()
                print('点击第二个商品')
                os.system('adb shell input tap 800 640')   # 点击第二个商品
                time.sleep(2)
                goback()
                print('点击第三个商品')
                os.system('adb shell input tap 290 1400')   # 点击第三个商品
                time.sleep(2)
                goback()
                print('成功获得喵币，现在返程')
                time.sleep(1)
            if i == 2:  # 第二次是进特卖会场，需点击得喵币
                print('进入特卖会场，浏览中，请等待 13 秒')
                time.sleep(13)
                os.system('adb shell input tap 970 1260')  # 点击得喵币
                print('成功抓到猫猫啦，现在返程')
                time.sleep(1)
            goback()
        else:
            print('已完成浏览会场得喵币任务')
            closepop()
            break


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
juhuasuan()
zhibo()
