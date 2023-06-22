import tkinter as tk
import tkinter.messagebox
import db
import mainWin
import tk1
class AddUser():
    def __init__(self):
        self.win1=tk.Tk()
        self.win1.title("新用户注册")
        self.win1.geometry('400x200')
        userlabel=tk.Label(self.win1,text="用户名:",font=10)
        userlabel.grid(row=0,column=0,padx=15,pady=15)
        self.userentry=tk.Entry(self.win1)
        self.userentry.grid(row=0,column=1)
        pwdlabel=tk.Label(self.win1,text="密  码:",font=10)
        pwdlabel.grid(row=1,column=0,padx=15,pady=5)
        self.pwdentry=tk.Entry(self.win1,width=20,show='*')
        self.pwdentry.grid(row=1,column=1)
        self.okbutton=tk.Button(self.win1,text='提交',font=10,command=self.addUser)
        self.okbutton.grid(row=3,column=0)
        self.cancelbutton=tk.Button(self.win1,text='取消',font=10,command=self.win1.destroy)
        self.cancelbutton.grid(row=3,column=1)
        self.cancelbutton = tk.Button(self.win1, text='登陆', font=10, command=self.loginuser).grid(row=3,column=2)
        self.win1.mainloop()
    def addUser(self):
        username = self.userentry.get()
        userpwd = self.pwdentry.get()
        if username.strip() == "" or userpwd.strip() == "":
            tk.messagebox.showerror("ss", "用户名或密码不能为空")
            return False
        else:
            rs1=db.query('select * from tb_user where userName=%s',username)
            if len(rs1)>0:
                tk.messagebox.showinfo("注册失败","该用户名已经存在")
                self.userentry.delete(0)
                self.pwdentry.delete(0)
            else:
                rs = db.update("insert into tb_user(userName,userPwd) values(%s,%s)",username,userpwd)
                if rs > 0:
                    tk.messagebox.showinfo("用户", "添加成功")
                else:
                    self.userentry.delete(0)
                    self.pwdentry.delete(0)
    def loginuser(self):
        self.win1.destroy()
        tk1.loginStu()