import os
import easygui as g
def yincang(num):
    res = os.popen("attrib +s +h %s"%(num)).read()
    if res == "":
        g.msgbox("已成功隐藏")  
    else:
        g.msgbox("检测到操作异常，返回错误内容:%s"%res,"警告","查看帮助")
        g.msgbox("可能是您的文件已隐藏或者切换的目录不对或者您当前的目录没有这个文件夹，或者文件夹名称输入错误")
def xianshi(num1):
    res = os.popen("attrib -s -h %s"%(num1)).read()
    if res == "":
        g.msgbox("已成功显示")  
    else:
        g.msgbox("检测到操作异常，返回错误内容:%s"%res,"警告","查看帮助")
        g.msgbox("可能是您的文件已显示或者切换的目录不对或者您当前的目录没有这个文件夹，或者文件夹名称输入错误")
def yincang1(num2):
    res = os.chdir("%s"%(num2))
    print(res)
g.msgbox("欢迎使用隐藏文件小程序（.exe版）\n 说明：本程序由小朱制作，隐藏文件绝对机密，尽管对方知道代码可是他不知道文件名照样无法发现\n 版本号1.5")
while True:
    cd = g.buttonbox("菜单","菜单",choices=["隐藏/显示文件","访问Github","更新日志","退出"])
    if cd =="隐藏/显示文件":
        cd1 = g.buttonbox("请选择操作",choices=["1.隐藏文件","2.显示文件"])
        if cd1 == "1.隐藏文件":
                yin_2 = g.enterbox("请输入隐藏的文件绝对路径（例如C:\1254\124）如果确认后崩溃表示路径出现问题，需要确认路径")
                yincang1(yin_2)
                print("已成功将CMD运行目录切换到%s"%yin_2)                
                yin_3 = g.enterbox("已成功切换到指定文件夹，请输入文件名;请务必记住文件名和路径，否则此文件可能无法恢复")
                yincang(yin_3)                                 
        if cd1 == "2.显示文件":
                yin_2 = g.enterbox("请输入隐藏的文件绝对路径（例如C:\1254\124）如果确认后崩溃表示路径出现问题，需要确认路径")
                yincang1(yin_2)
                yin_3 = g.enterbox("已成功切换到指定文件夹，请输入文件名")                
                xianshi(yin_3)            
    if cd =="退出":
        g.msgbox("欢迎您再次使用")
        break;
    if cd =="更新日志":
        g.msgbox("2022.10.16----1.5更新内容:1.exe版取消当前目录选择，强制输入绝对路径\n 2.删改一些无用代码，优化代码逻辑\n 3.删除使用帮助4.修复完善错误反馈输入文件夹名称错误不再崩溃\n 5.支持标准路径，不再要求使用双反斜杠","更新日志1/1","返回")
    if cd =="访问Github":
        os.system("start https://github.com/yxsj245/hidden-file")           
