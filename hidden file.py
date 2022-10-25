#-------------------------导入运行库#---------------------
import tkinter as tk
from tkinter import filedialog
import time
import os
import easygui as g
from tkinter import * 
from tkinter.filedialog import *
#-------------------------变量初始化-----------------------
ticks = time.time()
info = {"path":[]}
path = os.getcwd()
#-------------------------全部方法-------------------------
#记录日志的方法
def loginon(loginl):    
    Time = time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime())
    os.chdir("C:\concealData\login")
    file = open("login1","a")
    file.write("%s----%s\n"%(Time,loginl))
    file.close()
#开启记录方法
def jilu():
    os.chdir("C:\concealData")
    os.mkdir("Data")
    loginon("开启成功")
#隐藏文件夹方法
def yincang(xuanze23):
    window = Tk()
    g.msgbox("请在点击确认时选择隐藏的文件夹","提示","确认") 
    os.popen("attrib +s +h %s"%xuanze23)
    g.msgbox("隐藏成功")
#显示文件夹方法
def xianshi(num1):
    res = os.popen("attrib -s -h %s"%(num1)).read()    
    if res == "":
        g.msgbox("已成功显示")  
    else:
        g.msgbox("检测到操作异常，返回错误内容:%s"%res,"警告","查看帮助")
        g.msgbox("可能是您的文件已显示或者切换的目录不对或者您当前的目录没有这个文件夹，或者文件夹名称输入错误")
#切换文件夹目录方法
def qiehuan(num2):
    res = os.chdir("%s"%(num2))
#查看记录文件方法
def chakanwenjian():
    os.chdir("C:\concealData\Data")
    file = open("password","r")
    mima = file.read()
    password = g.passwordbox("请输入访问授权码(请注意：如果您是首次启用此功能并且直接查看会出现一直报授权码错误，请您重新运行程序即可，此问题暂时未查找的原因)")
    if password == mima:
        file = open("jilulog","r")
        neirong = file.read()
        g.msgbox("%s"%neirong)
    else:
        g.msgbox("授权码错误，如果忘记请联系管理员")
#判断授权码的方法(关闭记录)
def chakanwenjian1():
    os.chdir("C:\concealData\Data")
    file = open("password","r")
    mima = file.read()
    print(mima)
    password = g.passwordbox("请输入访问授权码")
    if password == mima:
        file.close()
        N1_2 = g.buttonbox("警告：关闭此功能将删除所有记录，请确保自己已全部记住三思后再进行","警告",choices=["是","否"])
        if N1_2 == "是":
            os.chdir("C:\concealData\Data")
            os.remove("jilulog")
            os.remove("password")
            os.chdir("C:\concealData")
            os.rmdir("Data")
            g.msgbox("关闭成功")
    else:
        #授权码输入错误
        g.msgbox("授权码错误，如果忘记请联系管理员")
#删除记录的方法
def clearjilulog():
    os.chdir("C:\concealData\Data")
    file = open("password","r")
    mima = file.read()
    print(mima)
    password = g.passwordbox("请输入访问授权码")
    if password == mima:
        file.close()
        N1_2 = g.buttonbox("警告：删除记录前请务必记得记录内容，否则会影响恢复！","警告",choices=["是","否"])
        if N1_2 == "是":
            os.chdir("C:\concealData\Data")
            os.remove("jilulog")
            g.msgbox("删除成功")
    else:
        #授权码输入错误
        g.msgbox("授权码错误，如果忘记请联系管理员")      
#保存记录的方法
def save(cs1,cs2):
    os.chdir("C:\concealData\Data")
    file = open("jilulog","a")
    #记录隐藏文件的路径
    file.write("路径:%s"%cs1)
    #记录隐藏文件夹的名称
    file.write("文件名:%s\n"%cs2)
    file.close
#保存隐藏的文件记录的方法（调用Windows资源管理器的）
def saveFile(cs2):
    os.chdir("C:\concealData\Data")
    file = open("jilulog","a")
    file.write("路径及文件名称:%s\n"%cs2)
    file.close
#保存隐藏的文件记录的方法（调用Windows资源管理器的）
def saveFileW(cs2):
    os.chdir("C:\concealData\Data")
    file = open("jilulog","a")
    file.write("路径及文件夹名称:%s\n"%cs2)
    file.close
#打开隐藏程序列表的软件方法
def app():
    os.chdir("C:\concealData\Data")
    file = open("password","r")
    mima = file.read()
    print(mima)
    password = g.passwordbox("请输入访问授权码")
    if password == mima:    
        os.chdir(path)
        g.msgbox("准备打开程序，按下确认按钮打开，随后请注意您的任务栏是否已出现。如果弹出权限窗口请点击是。","温馨提示","确认")
        os.popen(".\HideUL1.0\HideUL.exe")
    else:
        g.msgbox("授权码错误，如果忘记请联系管理员")  
#--------------------------------------------------
os.chdir("C:\\")
wenjian = os.listdir()
if "concealData" in wenjian:
    loginon("检测到已安装")
    #已安装
    while True:
        #检测是否开启了记录功能
        GN1 = False
        os.chdir("C:\concealData")
        wenjian1 = os.listdir()
        if "Data" in wenjian1:
            loginon("检测到已开启记录文件功能")
            GN1 = True
            print("记录文件名称功能已开启")
        else:
            loginon("检测到未开启文件记录功能")
            print("记录文件名称功能未开启")
        #主程序
        loginon("已进入菜单")
        cd = g.buttonbox("欢迎使用隐藏文件程序","版本2.7",choices=["隐藏/显示文件","访问Github","设置","查看隐藏记录","删除隐藏记录","更新日志","实验性功能","内测内容","退出"])
        if cd =="隐藏/显示文件":
            while True:
                XU = g.buttonbox("请选择您的操作","菜单",choices=["显示文件夹","隐藏文件","隐藏文件夹","返回主菜单"])
                if XU=="显示文件夹":
                    loginon("您选择隐藏/显示文件")
                    yin_2 = g.enterbox("请输入操作文件的绝对路径（例如C:\1254\124）如果确认后崩溃表示路径出现问题，需要确认路径")
                    loginon("已引用切换文件夹方法")
                    qiehuan(yin_2)
                    loginon("切换成功")
                    while True: 
                        loginon("进入子菜单")               
                        caidan = g.buttonbox("已成功切换到“%s”;请选择操作"%yin_2,"菜单",choices=["显示文件夹/显示文件","重新输入新路径","返回上级菜单"])
                        if caidan == "显示文件夹/显示文件":
                            loginon("您选择显示文件")
                            yin_3 = g.enterbox("请输入文件名")
                            loginon("已接收到文件名%s引用显示文件夹方法"%yin_3)
                            qiehuan(yin_2)
                            xianshi(yin_3)
                            loginon("显示成功")
                        else:
                            break;
                elif XU=="隐藏文件夹":
                    loginon("您选择隐藏文件夹")
                    xuanze23 = filedialog.askdirectory()
                    yincang(xuanze23)
                    loginon("隐藏成功")
                    loginon("准备检测额外功能")
                    if GN1:
                        loginon("已开启额外功能")
                        xuanze = g.buttonbox("是否保存记录",choices=["是","否"])
                        if xuanze == "是":
                            loginon("用户选择了保存")
                            saveFileW(xuanze23)
                            loginon("保存记录成功")                    
                elif XU=="隐藏文件":
                    loginon("您选择隐藏文件")
                    g.msgbox("请在点击确认时选择隐藏的文件","提示","确认") 
                    file_names = askopenfilenames()
                    yincang(file_names)
                    loginon("隐藏成功")
                    loginon("准备检测额外功能")
                    if GN1:
                        loginon("已开启额外功能")
                        xuanze = g.buttonbox("是否保存记录",choices=["是","否"])
                        if xuanze == "是":
                            loginon("用户选择了保存")
                            saveFile(file_names)
                            loginon("保存记录成功")
                else:
                    break
        if cd =="删除隐藏记录":
            clearjilulog()
        if cd =="设置":
            loginon("您选择设置")
            cd1 = g.buttonbox("请选择开启的功能","设置",choices=["记录隐藏文件路径和文件夹名称"])
            if cd1 == "记录隐藏文件路径和文件夹名称":
                if GN1:
                    GN1_1 = g.buttonbox("检测到您已经开启了此功能，是否关闭此功能","功能",choices=["是","否"])
                    if GN1_1 == "是":
                        chakanwenjian1()
                else:
                    jilu()
                    os.chdir("C:\concealData\Data")
                    file = open("jilulog","a")
                    password = g.passwordbox("请输入要注册的查看授权码")
                    os.chdir("C:\concealData\Data")
                    file = open("password","w")
                    file.write("%s"%password)
                    file.close
                    g.msgbox("开启成功")
        if cd =="退出":
            loginon("您选择退出")
            g.msgbox("欢迎您再次使用")
            break;
        if cd =="查看隐藏记录":
            loginon("您选择查看隐藏记录")
            chakanwenjian()
        if cd =="更新日志":
            loginon("您选择更新日志")
            g.msgbox("2022.10.25----3.0更新内容:本次是功能优化内容性更新1.新增实验性内容\n 2.新增内测入口\n 3.支持调用Windows资源管理器进行文件夹和文件的选择\n 4.支持清除记录功能\n 5.修复日志保存问题\n 6.支持关闭记录文件的功能","更新日志1/4","下一页")
            g.msgbox("2022.10.20----2.0更新内容:本次是大版本更新，对代码进行规整，以下是新增的功能1.新增隐藏文件的路径和文件名查看\n 2.新增日志记录功能","更新日志2/4","下一页")
            g.msgbox("2022.10.19----1.7更新内容:对使用逻辑进行了重新调整，优化使用体验","3/4","下一页")
            g.msgbox("2022.10.16----1.5更新内容:1.exe版取消当前目录选择，强制输入绝对路径\n 2.删改一些无用代码，优化代码逻辑\n 3.删除使用帮助4.修复完善错误反馈输入文件夹名称错误不再崩溃\n 5.支持标准路径，不再要求使用双反斜杠","更新日志4/4","返回")
        if cd =="访问本项目Github":
            loginon("您选择访问本项目Github")
            os.system("start https://github.com/yxsj245/hidden-file")
        if cd =="实验性功能":
            os.chdir("C:\concealData\Data")
            file = open("password","r")
            mima = file.read()
            password = g.passwordbox("请输入访问授权码(请注意：如果您是首次启用此功能并且直接查看会出现一直报授权码错误，请您重新运行程序即可，此问题暂时未查找的原因)")
            if password == mima:
                g.msgbox("实验性功能简介：这里是本程序引入最新的技术，可能存在不稳定情况或者无法使用","什么是实验性功能？","我知道了")
                cd1 = g.buttonbox("请选择功能","更多功能",choices=["隐藏应用程序列表"])
                if cd1 == "隐藏应用程序列表":
                    app()                
            else:
                g.msgbox("授权码错误，如果忘记请联系管理员")
        if cd =="内测内容":
            password = g.passwordbox("请输入测试授权码")
            if password == "123-5846-693-47855":
                g.msgbox("恭喜您获得内测内容，目前尚未有测试内容")
            else:
                g.msgbox("测试授权码错误")

else:
    #未安装
    os.mkdir("concealData")
    os.chdir("C:\concealData")
    os.mkdir("login")
    os.chdir("C:\\")
    os.popen("attrib +s +h concealData")
    g.msgbox("已完成环境配置，稍后请重新启动该程序")
    loginon("安装成功")
