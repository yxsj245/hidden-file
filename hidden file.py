import os
import easygui as g
def yincang(num):
    os.system("attrib +s +h %s"%(num))
def xianshi(num1):
    os.system("attrib -s -h %s"%(num1))
def yincang1(num2):
    os.chdir("%s"%(num2))
def xianshi1(num3):
    os.chdir("%s"%(num3))
g.msgbox("欢迎使用隐藏文件小程序\n 说明：本程序由制作，隐藏文件绝对机密，尽管对方知道代码可是他不知道文件名照样无法发现\n 版本号1.0")
while True:
    cd = g.buttonbox("菜单","菜单",choices=["使用说明","隐藏/显示文件","退出"])
    if cd == "使用说明":
        g.msgbox("1.本软件隐藏文件分为两个，第一个为当前文件下就是程序运行的所在目录下需要隐藏的文件","使用说明1/9","下一页")
        g.msgbox("优点是直接输入文件名即可隐藏，缺点是只能隐藏该程序运行目录下的文件\t 第二种是其它路径下的，","使用说明2/9","下一页")
        g.msgbox("这个是可以指定隐藏文件夹的目录名称，不会受到程序运行的位置制约","使用说明3/9","下一页")
        g.msgbox("在哪都可以运行前提必须得知道隐藏文件的绝对路径\n ","使用说明4/9","下一页")
        g.msgbox("2.如果您选择的是当前路径，需要将该程序复制到需要隐藏文件或者文件夹的所在根目录双击\t","使用说明5/9","下一页")
        g.msgbox("如果您选择的是其它路径，这个时候需要填写隐藏文件的目录，请注意必须是绝对路径（包含盘符)","使用说明6/9","下一页")
        g.msgbox("个目录中间必须使用双斜杠(//)表示，定位到需要隐藏的文件或者文件夹所在的根目录就行\n ","使用说明7/9","下一页")
        g.msgbox("3.显示该文件和隐藏方法一样\n 注意：隐藏的文件夹或者文件必须要记住名称，切记必须要记住，否则目前为确保绝对安全，","使用说明8/9","下一页")
        g.msgbox("该程序没有做任何记录，是无法找回到的，如果是因为忘记文件c名称造成的文件丢失后果自负！！！","使用说明9/9","返回")
    if cd =="隐藏/显示文件":
        cd1 = g.buttonbox("请选择操作",choices=["1.隐藏文件","2.显示文件"])
        if cd1 == "1.隐藏文件":
            cd1_cd = g.buttonbox("请选择隐藏方式",choices=["当前路径","其它路径"])
            if cd1_cd == "当前路径":
                yin_1 = g.enterbox("请输入文件名称")
                yincang(yin_1)
                g.msgbox("隐藏成功")
            if cd1_cd =="其它路径":
                yin_2 = g.enterbox("请输入隐藏的文件绝对路径（例如C:\\1254\\124）必须使用双反斜杠")
                print(yin_2)
                if "\\" in yin_2:
                    print("校验通过")
                    print("已成功将CMD运行目录切换到%s"%yin_2)
                    yin_3 = g.enterbox("已成功切换到指定文件夹，请输入文件名")
                    yincang1(yin_2)
                    yincang(yin_3)
                else:
                    g.msgbox("检测到您输入的路径存在格式错误，已经中断了调用，请确认中间是否使用了双反斜杠\\")               
        if cd1 == "2.显示文件":
            cd1_cd = g.buttonbox("请选择显示方式",choices=["当前路径","其它路径"])
            if cd1_cd == "当前路径":
                yin_1 = g.enterbox("请输入文件名称")
                xianshi(yin_1)
                g.msgbox("显示成功")
            if cd1_cd == "其它路径":
                yin_2 = g.enterbox("请输入隐藏的文件绝对路径（例如C:\\1254\\124）必须使用双反斜杠")
                print("校验通过")
                print("已成功将CMD运行目录切换到%s"%yin_2)
                yin_3 = g.enterbox("已成功切换到指定文件夹，请输入文件名")
                xianshi1(yin_2)
                xianshi(yin_3)
            else:
                g.msgbox("检测到您输入的路径存在格式错误，已经中断了调用，请确认中间是否使用了双反斜杠\\")                  
    if cd =="退出":
        break;
            
