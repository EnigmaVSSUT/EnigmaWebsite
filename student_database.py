from tkinter import *
import sqlite3 as s
import tkinter.messagebox as m
con=s.connect("G:/sms1.db")
c=con.cursor()

w=Tk()
S1=StringVar()
S2=IntVar()
S3=StringVar()
S2.set("")

class studentdatabase():
    def window(self):
        self.l1=Label(w,text="name  ",font=("arial",20,"bold"))
        self.l2=Label(w,text="mob no.",font=("arial",20,"bold"))
        self.l3=Label(w,text="email",font=("arial",20,"bold"))
        self.e1=Entry(w,textvariable=S1,font=("arial",20,"bold"))
        self.e2=Entry(w,textvariable=S2,font=("arial",20,"bold"))
        self.e3=Entry(w,textvariable=S3,font=("arial",20,"bold"))
        self.b1=Button(w,text="Submit",command=self.buttonclk)
        self.b2=Button(w,text="Reset",command=self.reset)
        self.l1.grid(row=1,column=1)
        self.l2.grid(row=2,column=1)
        self.l3.grid(row=3,column=1)
        self.e1.grid(row=1,column=2)
        self.e2.grid(row=2,column=2)
        self.e3.grid(row=3,column=2)
        self.b1.grid(row=4,column=1)
        self.b2.grid(row=4,column=2)
    def buttonclk(self):
        c.execute("create table if not exists student(name char(30),mob char(30),email char(40))")
        c.execute("insert into student values(?,?,?);",(S1.get(),S2.get(),S3.get()))
        con.commit()
        m.showinfo(title="submit",message="record submitted successfully")
        c.execute("select* from student")
        data = c.fetchall()
        print("updated data : ",data)
    def reset(self):
        S1.set("")
        S2.set("")
        S3.set("")

app=studentdatabase()
app.window()

w.mainloop()

con.close()
