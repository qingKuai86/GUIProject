import tkinter as tk
import tkinter.messagebox
import db
import mainWin
import adduser
import Stu
#安装itchat模块
class loginStu:
    def __init__(self):
        self.win=tk.Tk()
        self.win.title("登陆")
        self.win.geometry('300x200')
        userlabel=tk.Label(self.win,text="用户名:",font=10)
        userlabel.grid(row=0,column=0,padx=30,pady=15)
        self.userentry=tk.Entry(self.win)
        self.userentry.grid(row=0,column=1)
        self.userentry.insert(0,'11')
        pwdlabel=tk.Label(self.win,text="密  码:",font=10)
        pwdlabel.grid(row=1,column=0,padx=15,pady=5)
        self.pwdentry=tk.Entry(self.win,width=20,show='*')
        self.pwdentry.grid(row=1,column=1)
        self.pwdentry.insert(0,'11')
        self.okbutton=tk.Button(self.win,text='提交',font=10,command=self.openMain)
        self.okbutton.grid(row=3,column=0)
        self.cancelbutton=tk.Button(self.win,text='取消',font=10,command=self.win.destroy)
        self.cancelbutton.grid(row=3,column=1)
        self.addbutton = tk.Button(self.win, text='用户注册', font=10, command=self.adduser)
        self.addbutton.grid(row=4, column=1)
        self.win.mainloop()
    def openMain(self):
        username=self.userentry.get()
        userpwd=self.pwdentry.get()
        if username.strip()=="" or userpwd.strip()=="":
            tk.messagebox.showerror("登录失败","用户名或密码不能为空")
            return False
        else:
            #rs=db.query("select * from tb_user where userName=%s and userPwd = %s",username,userpwd)
            try:
                #rs = db.query2("select * from tb_user where userName='"+username+"' and userPwd = '"+userpwd+"'")
                rs = db.query("select * from tb_user where userName=%s and userPwd = %s", username, userpwd)
                if len(rs)>0:
                    print(len(rs))
                    db.Username=username
                    self.win.destroy()
                    tt=mainWin.MainWin()
                    tt.win2.mainloop()
                else:
                    tk.messagebox.showinfo("ee", "你输入的信息不正确，请重新输入")
            except Exception as e:
                print("登陆异常")
                print(e)
    def adduser(self):
        self.win.destroy()
        adduser.AddUser()
if __name__ == "__main__":
    loginStu()

