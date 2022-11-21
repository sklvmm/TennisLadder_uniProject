from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3

class MemberClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Members")
        self.root.geometry("1200x480+460+340")
        self.root.config(bg="white")
        self.root.iconbitmap("@/home/eskey0/Documents/Python Projects/Tennis_Ladder/images/icon.xbm")
        self.root.resizable(0,0)
        #.focus_force() Πεταει το παραθυρο πανω απο απο το main window
        self.root.focus_force()
        #===Image===
        self.logo=Image.open("/home/eskey0/Documents/Python Projects/Tennis_Ladder/images/mem.png")
        self.logo=self.logo.resize((200,100),Image.ANTIALIAS)
        self.logo = ImageTk.PhotoImage(file="/home/eskey0/Documents/Python Projects/Tennis_Ladder/images/mem.png")
        #===Title===
        title=Label(self.root,text="Manage Player Details",padx=10,compound=LEFT,image=self.logo,font=("helvetica",20,"bold"),bg="#045cad",fg="white").place(x=0,y=0,relwidth=1,height=50)
        #===Variables===
        self.var_rowid=StringVar()
        self.var_first_name=StringVar()
        self.var_last_name=StringVar()
        self.var_age=StringVar()

        #===Widgets=====
        lbl_firstName=Label(self.root,text="First Name:",font=("helvetica",15),bg='white').place(x=70,y=110)
        lbl_lastName=Label(self.root,text="Last Name:",font=("helvetica",15),bg='white').place(x=70,y=180)
        lbl_age=Label(self.root,text="Age:",font=("helvetica",15),bg='white').place(x=70,y=250)
        #===Entry Boxes====
        txt_firstName=Entry(self.root,textvariable=self.var_first_name,font=("goudy old style",15,'bold'),bg='lightyellow').place(x=210,y=110,width=200)
        txt_lastName=Entry(self.root,textvariable=self.var_last_name,font=("goudy old style",15,'bold'),bg='lightyellow').place(x=210,y=180,width=200)
        txt_ageName=Entry(self.root,textvariable=self.var_age,font=("goudy old style",15,'bold'),bg='lightyellow').place(x=210,y=250,width=200)

        #===Buttons===
        #add Button
        self.btn_add=Button(self.root,text='Save',font=("helvetica",15),bg="#2196f3",fg="white",cursor="hand2",command=self.add)
        self.btn_add.place(x=70,y=350,width=110,height=40)
        #Upadte Button
        self.btn_update=Button(self.root,text='Update',font=("helvetica",15),bg="#4caf50",fg="white",cursor="hand2",command=self.update)
        self.btn_update.place(x=190,y=350,width=110,height=40)
        #Delete Button
        self.btn_delete=Button(self.root,text='Delete',font=("helvetica",15),bg="#f44336",fg="white",cursor="hand2",command=self.delete)
        self.btn_delete.place(x=310,y=350,width=110,height=40)
        #Clear Button
        self.btn_clear=Button(self.root,text='Clear',font=("helvetica",15),bg="#607d8b",fg="white",cursor="hand2",command=self.clear_data)
        self.btn_clear.place(x=430,y=350,width=110,height=40)

        #===Search=====
        self.var_search=StringVar()
        lbl_search_firstName=Label(self.root,text="Search by Name:",font=("helvetica",12,'bold'),bg='white').place(x=690,y=60)
        txt_firstName = Entry(self.root, textvariable=self.var_search, font=("goudy old style", 15, 'bold'),bg='lightyellow').place(x=840, y=60, width=220)
        btn_search=Button(self.root,text='Search',font=("helvetica",15),bg="#2196f3",fg="white",cursor="hand2",command=self.search).place(x=1070,y=60,width=90,height=28)

        #====Content======
        self.C_Frame=Frame(self.root,bd=2,relief=RIDGE)
        self.C_Frame.place(x=690,y=100,width=470,height=340)

        scrolly=Scrollbar(self.C_Frame,orient=VERTICAL)
        #scrollx=Scrollbar(self.C_Frame,orient=HORIZONTAL)
        self.MemberTable=ttk.Treeview(self.C_Frame,columns=("rank","f_name","l_name","age"),yscrollcommand=scrolly.set)

        #scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        #scrollx.config(command=self.MemberTable.xview)
        scrolly.config(command=self.MemberTable.yview)

        self.MemberTable.heading("rank",text="Rank")
        self.MemberTable.heading("f_name",text="First Name")
        self.MemberTable.heading("l_name",text="Last Name")
        self.MemberTable.heading("age",text="Age")
        #self.MemberTable.heading("wins",text="Wins")
        #self.MemberTable.heading("losses",text="Losses")
        self.MemberTable["show"]='headings'
        self.MemberTable.column("rank",width=10,anchor=CENTER)
        self.MemberTable.column("f_name",width=80)
        self.MemberTable.column("l_name",width=80)
        self.MemberTable.column("age",width=15,anchor=CENTER)
        #self.MemberTable.column("wins",width=15)
        #self.MemberTable.column("losses",width=15)

        self.MemberTable.pack(fill=BOTH,expand=1)
        self.MemberTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
#=======================================================================================
#====================FUNCTIONS==========================================================
#=======================================================================================
    def get_data(self,ev):
        r=self.MemberTable.focus()
        content=self.MemberTable.item(r)
        row=content["values"]
        if len(row) != 0:
            self.var_rowid.set(row[0])
            self.var_first_name.set(row[1])
            self.var_last_name.set(row[2])
            self.var_age.set(row[3])

    def clear_data(self):
        self.show()
        self.var_rowid.set("")
        self.var_first_name.set("")
        self.var_last_name.set("")
        self.var_age.set("")
        self.var_search.set("")

    def add(self):
        conn=sqlite3.connect(database="ATP.db")
        c=conn.cursor()
        try:
            if self.var_first_name.get()=="" or self.var_last_name.get()=="" or self.var_age.get()=="":
                messagebox.showerror("Error","All fields are required",parent=self.root)

            else:
                try:
                    if int(self.var_age.get()) < 12:
                        messagebox.showerror('Error!',"A member can't be younger than 12 years",parent=self.root)
                        return
                    elif int(self.var_age.get()) > 90:
                        messagebox.showerror('Error!', "A member can't be older than 90 years",parent=self.root)
                        return
                except ValueError:
                    messagebox.showerror('Error!', "Age must be a number!",parent=self.root)

                c.execute("INSERT INTO leaderboard(first_name,last_name,age) VALUES (?,?,?)", (
                    self.var_first_name.get(),
                    self.var_last_name.get(),
                    self.var_age.get()
                ))
                messagebox.showinfo("Success","Member added successfully",parent=self.root)
            conn.commit()
            conn.close()
            self.clear_data()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}",parent=self.root)

    def update(self):
        conn=sqlite3.connect(database="ATP.db")
        c=conn.cursor()
        try:
            if self.var_first_name.get()=="" or self.var_last_name.get()=="" or self.var_age.get()=="":
                messagebox.showerror("Error","All fields are required",parent=self.root)
            else:
                try:
                    if int(self.var_age.get()) < 12:
                        messagebox.showerror('Error!',"A member can't be younger than 12 years",parent=self.root)
                        return
                    elif int(self.var_age.get()) > 90:
                        messagebox.showerror('Error!',"A member can't be older than 90 years",parent=self.root)
                        return
                except ValueError:
                    messagebox.showerror('Error!', "Age must be a number!",parent=self.root)

                c.execute("UPDATE leaderboard set first_name=?,last_name=?,age=? WHERE rowid=? ", (
                    self.var_first_name.get(),
                    self.var_last_name.get(),
                    self.var_age.get(),
                    self.var_rowid.get()

                ))
                messagebox.showinfo("Success","Member updated successfully",parent=self.root)

            conn.commit()
            conn.close()
            self.clear_data()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}",parent=self.root)

    def show(self):
        conn=sqlite3.connect(database="ATP.db")
        c=conn.cursor()
        try:
            c.execute("SELECT rowid,first_name,last_name,age FROM leaderboard")
            rows=c.fetchall()
            self.MemberTable.delete(*self.MemberTable.get_children())
            for row in rows:
                self.MemberTable.insert('',END,values=row)
            conn.commit()
            conn.close()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}",parent=self.root)

    def search(self):
        conn=sqlite3.connect(database="ATP.db")
        c=conn.cursor()
        try:
            c.execute(f"SELECT rowid,first_name,last_name,age FROM leaderboard WHERE last_name LIKE '%{self.var_search.get()}%' OR first_name LIKE '%{self.var_search.get()}%' ")
            rows=c.fetchall()
            self.MemberTable.delete(*self.MemberTable.get_children())
            for row in rows:
                self.MemberTable.insert('',END,values=row)
            conn.commit()
            conn.close()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}",parent=self.root)

    def delete(self):
        conn=sqlite3.connect(database="ATP.db")
        c=conn.cursor()
        try:
            if self.var_first_name.get()=="" or self.var_last_name.get()=="" or self.var_age.get()=="":
                messagebox.showerror("Error","All fields are required",parent=self.root)
            else:

                c.execute("SELECT * FROM leaderboard WHERE rowid=?",(self.var_rowid.get(),))
                row=c.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please select a member from the list", parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Are you sure you want to delete?",parent=self.root)
                    if op==True:
                        c.execute("SELECT rowid, * FROM leaderboard")
                        data = c.fetchall()
                        if int(self.var_rowid.get()) < len(data):  # κάνει edit με την σειρά τα ονόματα και κάνει delete το τελευτέο
                            for i in range(int(self.var_rowid.get()), len(data)):
                                try:
                                    c.execute(
                                        "UPDATE leaderboard SET first_name = ?,last_name = ?,age = ?, Wins = ?, Losses = ? WHERE rowid = ?",
                                        (data[i][1], data[i][2], data[i][3], data[i][4], data[i][5], i))
                                except sqlite3.Error as er:
                                    print('Error')
                            try:
                                c.execute("DELETE FROM leaderboard WHERE rowid = ?", (len(data),))
                            except sqlite3.Error as er:
                                print('Error')
                        elif int(self.var_rowid.get()) == len(data):
                            c.execute("DELETE FROM leaderboard WHERE rowid = ?", (self.var_rowid.get(),))
                        messagebox.showinfo("Delete","Member deleted successfully!",parent=self.root)


            conn.commit()
            conn.close()
            self.clear_data()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}",parent=self.root)
        conn.close()