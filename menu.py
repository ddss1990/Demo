# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     menu
   Description :
   Author :       Chris
   date：          2018/2/11
-------------------------------------------------
"""


def start():
    '''
    menu 的入口，供它人调用
    :return:
    '''
    printMenu()


def printMenu():
    '''
     打印菜单，让用户选择想要爬虫的网站
    :return:
    '''
    print "****************************************************"
    print "********        1. 豆瓣         ********************"
    print "********        0. 退出         ********************"
    print "****************************************************"
    print "Are these error code? please execute 'chcp 65001' to change the coding format to the 'utf-8';" \
          " the pre coding is 'gbk' and  execute 'chcp936' to got it "
    print "****************************************************"
    switchMenu()


def switchMenu():
    '''
     选择想要爬虫的网站
    :return:
    '''
    try:
        i = int(raw_input("请选择你想爬虫的网站："))
    except ValueError as e:
        i = -1

    if i == 1:
        print "豆瓣"
    elif i == 0:
        print "退出"
        return
    # 选择有误，重新选择
    else:
        print "你的选择有误，请重新选择！！！"
        switchMenu()
