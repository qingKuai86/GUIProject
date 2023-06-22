import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox
import db
class SelUser():
    def __init__(self):
        self.root = tk.Tk()#创建根窗口
        self.root.title("查询用户信息")#设置窗口标题
        self.create_gui()#调用窗口组件函数
        self.root.mainloop()#让程序继续执行，直到窗口关闭

    def create_gui(self):#定义图形用户界面函数
        self.create_top_right_labelframe()#查询条件组件设置
        self.create_records_treeview()#查询结果树形菜单组件设置

    def create_top_right_labelframe(self):#查询条件组件界面
        labelframe1 = tk.LabelFrame(self.root, text='用户信息', width=400)#标签框架组件
        labelframe1.grid(row=0, column=1, sticky='ew', padx=8, pady=8)

        tk.Label(labelframe1, text='  账号:').grid(row=1, column=1, sticky='w', pady=2)#账号标签

        self.namefield = tk.Entry(labelframe1)#账号输入框
        self.namefield.grid(row=1, column=2, sticky='w', padx=5, pady=2)

        tk.Label(labelframe1, text='  密码:').grid(row=2, column=1, sticky='w', pady=2)

        self.numfield = tk.Entry(labelframe1)
        self.numfield.grid(row=2, column=2, sticky='w', padx=5, pady=2)

        ttk.Button(labelframe1, text='查询',command=self.seluser).grid(row=3, column=1, sticky='e', padx=5, pady=2)

    def create_records_treeview(self):#显示记录信息
        treeview_columns = ['userId', 'userName', 'userPwd']
        self.record_treeview = ttk.Treeview(self.root, show='headings', height=5, columns=treeview_columns)
        self.record_treeview.grid(row=4, column=0, columnspan=3)

        self.record_treeview.heading('userId', text='序号')
        self.record_treeview.heading('userName', text='用户名')
        self.record_treeview.heading('userPwd', text='密码')#, anchor='center'

        self.record_treeview.column('userId', width=100)
        self.record_treeview.column('userName', width=120)
        self.record_treeview.column('userPwd', width=220)
    def seluser(self):
        name1=self.namefield.get()
        pwd1=self.numfield.get()
        rs,row = db.query2("select * from tb_user where userName like '%"+name1+"%' and userPwd like '%"+pwd1+"%'")
        print(row)
        for i in range(row):
            self.record_treeview.insert("",'end',values=rs[i])

