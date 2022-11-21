from tkinter import*
from tkinter import messagebox
from PIL import Image,ImageTk
import sqlite3
import os.path
from os import path
from Member import MemberClass
from Ladder import LadderClass
from Match import MatchClass

class Main_Menu:
    def __init__(self,root):
        self.root=root
        self.root.title("ATP Tournament")
        self.root.geometry("1350x700+380+170")
        self.root.config(bg="white")
        self.root.iconbitmap("@/home/eskey0/Documents/Python Projects/Tennis_Ladder/images/icon.xbm")
        self.root.focus_force()
        #===Icons===
        self.logo=Image.open("/home/eskey0/Documents/Python Projects/Tennis_Ladder/images/icon.ico")
        self.logo=ImageTk.PhotoImage(self.logo)
        #===Title===
        title=Label(self.root,text="Tennis Ladder Management System",padx=10,compound=LEFT,image=self.logo,font=("helvetica",20,"bold"),bg="#045cad",fg="white").place(x=0,y=0,relwidth=1,height=50)
        #===Menu===
        M_Frame=LabelFrame(self.root,text="Menus",font=("goudy old style",15),bg="white")
        M_Frame.place(x=110,y=70,width=1140,height=80)

        btn_addPlayer=Button(M_Frame,text="Manage Members",font=("helvetica",15),bg="#036eb9",fg="white",cursor="hand2",command=self.edit_memebers).place(x=20,y=5,width=400,height=40)
        #btn_delPlayer=Button(M_Frame,text="Delete Player",font=("goudy old style",15,"bold"),bg="#036eb9",fg="white",cursor="hand2").place(x=240,y=5,width=200,height=40)
        btn_showLadder=Button(M_Frame,text="Show Ladder",font=("helvetica",15),bg="#036eb9",fg="white",cursor="hand2",command=self.show_ladder).place(x=460,y=5,width=200,height=40)
        btn_showMatches=Button(M_Frame,text="Matches",font=("helvetica",15),bg="#036eb9",fg="white",cursor="hand2",command=self.matches).place(x=680,y=5,width=200,height=40)
        btn_exit=Button(M_Frame,text="Exit",font=("helvetica",15),bg="#036eb9",fg="white",cursor="hand2",command=root.destroy).place(x=900,y=5,width=200,height=40)

        #===Content Window===
        self.bg_img=Image.open("/home/eskey0/Documents/Python Projects/Tennis_Ladder/images/atptour.png")
        self.bg_img=self.bg_img.resize((920,350),Image.ANTIALIAS)
        self.bg_img=ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg=Label(self.root,image=self.bg_img).place(x=200,y=180,width=920,height=350)
        self.players=0
        self.t_matches=0
        self.fetch_info()

        #===Update Details====
        self.lbl_players=Label(self.root,text=f"Total Players\n{[self.players]}",font=("helvetica",20),bd=5,relief=RIDGE,bg="#35b4e4",fg="white").place(x=300,y=560,width=300,height=100)
        self.lbl_matches=Label(self.root,text=f"Total Matches\n{[self.t_matches]}",font=("helvetica",20),bd=5,relief=RIDGE,bg="#7bcdec",fg="white").place(x=700,y=560,width=300,height=100)

    def edit_memebers(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=MemberClass(self.new_win)

    def show_ladder(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=LadderClass(self.new_win)

    def matches(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=MatchClass(self.new_win)

    def fetch_info(self):
        conn=sqlite3.connect(database="ATP.db")
        c=conn.cursor()
        try:
            c.execute("SELECT rowid FROM leaderboard")
            rows=c.fetchall()

            if len(rows)>0:
                for row in rows:
                    self.players = row[0]
            c.execute("SELECT rowid FROM match")
            rows=c.fetchall()
            if len(rows)>0:
                for row in rows:
                    self.t_matches = row[0]
            conn.commit()
            conn.close()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

if __name__=="__main__":
    if not path.exists('ATP.db'):
        conn = sqlite3.connect(database='ATP.db')
        c = conn.cursor()
        try:
            c.execute("""CREATE TABLE leaderboard(
                		first_name text,
                		last_name text,
                		age integer,
                		Wins    INTEGER DEFAULT 0,
                			Losses    INTEGER DEFAULT 0
                )""")
        except sqlite3.Error as er:
            print('Table leaderboard already exists')
        try:
            c.execute("""CREATE TABLE match(
                            challenger text,
                            challengee text,
                            score text
                    )""")
        except sqlite3.Error as er:
            print('Table match already exists')

        conn.commit()
        conn.close()


    root=Tk()
    obj=Main_Menu(root)
    root.resizable(0,0)
    root.mainloop()