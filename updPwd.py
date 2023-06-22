import tkinter as tk
import tkinter.ttk
import  tkinter.messagebox
import  db
import mainWin
class UpdPWD():
    def __init__(self):
        self.aa = db.Username
        self.winupd=tk.Tk()
        self.winupd.geometry('400x200')
        self.winupd.title("密码修改窗口")
        namelabel=tk.Label(self.winupd,text='账号：').grid(row=0,column=0,padx=10,pady=10)
        self.nametxt=tk.Entry(self.winupd)
        self.nametxt.grid(row=0,column=1)#disabled
        self.nametxt.insert(0,self.aa)

        labelpwd1=tk.Label(self.winupd,text='密码：').grid(row=1,column=0)
        self.pwd1=tk.Entry(self.winupd)
        self.pwd1.grid(row=1,column=1)

        labelpwd2=tk.Label(self.winupd,text='确认密码：').grid(row=2,column=0)
        self.pwd2 = tk.Entry(self.winupd)
        self.pwd2.grid(row=2, column=1)

        self.button=tk.Button(self.winupd,text="确定",command=self.updpwd).grid(row=3,column=0)
        self.button2 = tk.Button(self.winupd, text="主窗口", command=self.returnwin).grid(row=3, column=1)
        self.winupd.mainloop()
    def updpwd(self):
        bb=self.pwd1.get()
        aa=self.aa
        print(aa)
        print(bb)
        #rs=db.update("update tb_user set userPwd=%s where userName=%s",aa,bb)
        rs = db.update2("update tb_user set userPwd='"+bb+"' where userName='"+aa+"'")
        print(rs)
        if rs>0:
            tk.messagebox.showinfo("提示消息","密码修改成功")
        else:
            tk.messagebox.showinfo("提示消息", "修改失败")
            self.pwd1.delete(0)
            self.pwd2.delete(0)
    def returnwin(self):
        self.winupd.destroy()
        mainWin.MainWin()