from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3

class LadderClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Ladder")
        self.root.geometry("600x480+460+340")
        self.root.config(bg="white")
        self.root.iconbitmap("@/home/eskey0/Documents/Python Projects/Tennis_Ladder/images/icon.xbm")
        self.root.resizable(0,0)
        #.focus_force() Πεταει το παραθυρο πανω απο απο το main window
        self.root.focus_force()
        #===Image===
        self.logo=Image.open("/home/eskey0/Documents/Python Projects/Tennis_Ladder/images/racket.png")
        self.logo=self.logo.resize((200,100),Image.ANTIALIAS)
        self.logo = ImageTk.PhotoImage(file="/home/eskey0/Documents/Python Projects/Tennis_Ladder/images/racket.png")
        #===Title===
        title=Label(self.root,text="Tournament Ladder Details",padx=10,compound=LEFT,image=self.logo,font=("helvetica",18,"bold"),bg="#045cad",fg="white").place(x=0,y=0,relwidth=1,height=50)

        self.var_search=StringVar()
        lbl_search_firstName=Label(self.root,text="Search by Name:",font=("helvetica",13),bg='white').place(x=25,y=60)
        txt_firstName = Entry(self.root, textvariable=self.var_search, font=("goudy old style", 15,"bold"),bg='lightyellow').place(x=175, y=60, width=190)
        btn_search=Button(self.root,text='Search',font=("helvetica",15),bg="#2196f3",fg="white",cursor="hand2",command=self.search).place(x=380,y=60,width=90,height=28)
        btn_clear=Button(self.root,text='Clear',font=("helvetica",15),bg="#607d8b",fg="white",cursor="hand2",command=self.clear_data).place(x=480,y=60,width=90,height=28)


        #===Ladder Window==========
        self.C_Frame=Frame(self.root,bd=2,relief=RIDGE)
        self.C_Frame.place(x=2,y=97,width=595,height=380)

        scrolly=Scrollbar(self.C_Frame,orient=VERTICAL)
        #scrollx=Scrollbar(self.C_Frame,orient=HORIZONTAL)
        self.MemberTable=ttk.Treeview(self.C_Frame,columns=("rank","f_name","l_name","age","wins","losses"),yscrollcommand=scrolly.set)

        #scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        #scrollx.config(command=self.MemberTable.xview)
        scrolly.config(command=self.MemberTable.yview)

        self.MemberTable.heading("rank",text="Rank")
        self.MemberTable.heading("f_name",text="First Name")
        self.MemberTable.heading("l_name",text="Last Name")
        self.MemberTable.heading("age",text="Age")
        self.MemberTable.heading("wins",text="Wins")
        self.MemberTable.heading("losses",text="Losses")
        self.MemberTable["show"]='headings'
        self.MemberTable.column("rank",width=10,anchor=CENTER)
        self.MemberTable.column("f_name",width=80)
        self.MemberTable.column("l_name",width=80)
        self.MemberTable.column("age",width=15,anchor=CENTER)
        self.MemberTable.column("wins",width=15,anchor=CENTER)
        self.MemberTable.column("losses",width=15,anchor=CENTER)

        self.MemberTable.pack(fill=BOTH,expand=1)
        #self.MemberTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()

    def show(self):
        conn=sqlite3.connect(database="ATP.db")
        c=conn.cursor()
        try:
            c.execute("SELECT rowid,* FROM leaderboard")
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
            c.execute(f"SELECT rowid,* FROM leaderboard WHERE last_name LIKE '%{self.var_search.get()}%' OR first_name LIKE '%{self.var_search.get()}%' ")
            rows=c.fetchall()
            self.MemberTable.delete(*self.MemberTable.get_children())
            for row in rows:
                self.MemberTable.insert('',END,values=row)
            conn.commit()
            conn.close()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}",parent=self.root)

    def clear_data(self):
        self.show()
        self.var_search.set("")