import tkinter as tk
import adduser
import selUser
import tk1
import updPwd
import stuMange
import Stu
class MainWin():
    def __init__(self):
        self.win2=tk.Tk()
        self.win2.title("主窗体")
        self.win2.geometry('800x500')
        menu1=tk.Menu(self.win2)
        menu1_2 = tk.Menu(menu1, tearoff=False)#创建二级菜单
        menu1.add_cascade(label="用户管理",menu=menu1_2)#创建级联菜单
        menu1_2.add_command(label='用户注册',command=self.adduser)
        menu1_2.add_command(label='密码修改',command=self.updPwd)
        menu1_2.add_command(label='查询用户信息',command=self.seluser)
        menu1_2.add_command(label='重新登录', command=self.loginuser)
       # menu1.add_command(label='学生信息管理', command=self.win2.stuManage)
        menu1.add_command(label='退出系统',command=self.win2.quit)
        menu1.add_command(label="学生信息统计分析",command=self.stu)
        self.win2.config(menu=menu1_2)
        self.win2.config(menu=menu1)#显示菜单
    def adduser(self):
        self.win2.destroy()
        adduser.AddUser()
    def loginuser(self):
        self.win2.destroy()
        tk1.loginStu()
    def seluser(self):
        self.win2.destroy()
        selUser.SelUser()
    def updPwd(self):
        self.win2.destroy()
        updPwd.UpdPWD()
    def stu(self):
        self.win2.destroy()
        Stu.SStu()

