import time
ticks = time.time()
import os
import easygui as g
#-------------------------全部方法-------------------------
#记录日志的方法
def loginon(loginl):
    Time = time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime())
    os.chdir("C:\concealData\login")
    file = open("login","a")
    file.write("%s----%s\n"%(Time,loginl))
#开启记录方法
def jilu():
    os.chdir("C:\concealData")
    os.mkdir("Data")
    loginon("开启成功")
#隐藏文件夹方法
def yincang(num):
    res = os.popen("attrib +s +h %s"%(num)).read()
    print(os.listdir())
    if res == "":
        g.msgbox("已成功隐藏")  
    else:
        g.msgbox("检测到操作异常，返回错误内容:%s"%res,"警告","查看帮助")
        g.msgbox("可能是您的文件已隐藏或者切换的目录不对或者您当前的目录没有这个文件夹，或者文件夹名称输入错误")
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
    print(mima)
    password = g.passwordbox("请输入访问授权码")
    if password == mima:
        file = open("jilulog","r")
        neirong = file.read()
        g.msgbox("%s"%neirong)
    else:
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
        cd = g.buttonbox("菜单","版本2.0",choices=["隐藏/显示文件","访问Github","设置","查看隐藏记录","更新日志","退出"])
        if cd =="隐藏/显示文件":
            loginon("您选择隐藏/显示文件")
            yin_2 = g.enterbox("请输入操作文件的绝对路径（例如C:\1254\124）如果确认后崩溃表示路径出现问题，需要确认路径")
            loginon("已引用切换文件夹方法")
            qiehuan(yin_2)
            loginon("切换成功")
            while True: 
                loginon("进入子菜单")               
                caidan = g.buttonbox("已成功切换到“%s”;请选择操作"%yin_2,"菜单",choices=["隐藏文件","显示文件","重新输入新路径","返回上级菜单"])
                if caidan == "显示文件":
                    loginon("您选择显示文件")
                    yin_3 = g.enterbox("请输入文件名")
                    loginon("已接收到文件名%s引用显示文件夹方法"%yin_3)
                    qiehuan(yin_2)
                    xianshi(yin_3)
                    loginon("显示成功")
                elif caidan == "隐藏文件":
                    loginon("您选择隐藏文件")
                    yin_3 = g.enterbox("请输入文件名") 
                    loginon("已接收到文件名%s引用隐藏文件夹方法"%yin_3)
                    qiehuan(yin_2)
                    yincang(yin_3)
                    loginon("显示成功")
                    loginon("准备检测额外功能")
                    if GN1:
                        loginon("已开启额外功能")
                        xuanze = g.buttonbox("是否保存记录",choices=["是","否"])
                        if xuanze == "是":
                            loginon("用户选择了保存")
                            save(yin_2,yin_3)                     
                elif caidan == "重新输入新路径":
                    loginon("您选择重新输入新路径")
                    yin_2 = g.enterbox("请输入操作文件的绝对路径（例如C:\1254\124）如果确认后崩溃表示路径出现问题，需要确认路径")
                    qiehuan(yin_2)
                else:
                    break;
        if cd =="设置":
            loginon("您选择设置")
            cd1 = g.buttonbox("请选择开启的功能","设置",choices=["记录隐藏文件路径和文件夹名称"])
            if cd1 == "记录隐藏文件路径和文件夹名称":
                if GN1:
                    g.msgbox("检测到您已经开启了此功能，请勿重复开启！")
                else:
                    jilu()
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
            g.msgbox("2022.10.20----2.0更新内容:本次是大版本更新，对代码进行规整，以下是新增的功能1.新增隐藏文件的路径和文件名查看\n 2.新增日志记录功能","返回")
            g.msgbox("2022.10.19----1.7更新内容:对使用逻辑进行了重新调整，优化使用体验","返回")
            g.msgbox("2022.10.16----1.5更新内容:1.exe版取消当前目录选择，强制输入绝对路径\n 2.删改一些无用代码，优化代码逻辑\n 3.删除使用帮助4.修复完善错误反馈输入文件夹名称错误不再崩溃\n 5.支持标准路径，不再要求使用双反斜杠","更新日志2/2","返回")
        if cd =="访问本项目Github":
            loginon("您选择访问本项目Github")
            os.system("start https://github.com/yxsj245/hidden-file")
else:
    #未安装
    os.mkdir("concealData")
    os.chdir("C:\concealData")
    os.mkdir("login")
    os.chdir("C:\\")
    os.popen("attrib +s +h concealData")
    g.msgbox("已完成环境配置，稍后请重新启动该程序")
    loginon("安装成功")
