from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3


class MatchClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Matches")
        self.root.geometry("1200x480+460+340")
        self.root.config(bg="white")
        self.root.iconbitmap("@/home/eskey0/Documents/Python Projects/Tennis_Ladder/images/icon.xbm")
        self.root.resizable(0,0)
        #.focus_force() Πεταει το παραθυρο πανω απο απο το main window
        self.root.focus_force()
        #===Image===
        self.logo=Image.open("images/vs.png")
        self.logo=self.logo.resize((200,100),Image.ANTIALIAS)
        self.logo=ImageTk.PhotoImage(file="images/vs.png")
        #===Title===
        title=Label(self.root,text="Create and see Matches",padx=10,compound=LEFT,image=self.logo,font=("goudy old style",20,"bold"),bg="#045cad",fg="white").place(x=0,y=0,relwidth=1,height=50)
        #===Variables===
        self.var_challenger=StringVar()
        self.var_challengee=StringVar()
        self.var_score=StringVar()



        #===Widgets=====
        lbl_challenger=Label(self.root,text="Challenger:",font=("goudy old style",15,'bold'),bg='white').place(x=70,y=110)
        lbl_challengee=Label(self.root,text="Challengee:",font=("goudy old style",15,'bold'),bg='white').place(x=70,y=250)
        lbl_score1=Label(self.root,text="Sets:",font=("goudy old style",15,'bold'),bg='white').place(x=70,y=180)
        lbl_score2 = Label(self.root, text="Sets:", font=("goudy old style", 15, 'bold'), bg='white').place(x=70,y=320)
        #===Entry Boxes====

        #===Buttons===
        #add Button
        self.btn_add=Button(self.root,text='Create Match',font=("goudy old style",15,"bold"),bg="#2196f3",fg="white",cursor="hand2",command=self.new_match)
        self.btn_add.place(x=70,y=380,width=130,height=40)
        #Clear Button
        self.btn_clear=Button(self.root,text='Clear',font=("goudy old style",15,"bold"),bg="#607d8b",fg="white",cursor="hand2",command=self.clear_data)
        self.btn_clear.place(x=210,y=380,width=110,height=40)

        #===Search=====
        self.var_search=StringVar()
        lbl_search_firstName=Label(self.root,text="Search by Name:",font=("goudy old style",15,'bold'),bg='white').place(x=690,y=60)
        txt_firstName = Entry(self.root, textvariable=self.var_search, font=("goudy old style", 15, 'bold'),bg='lightyellow').place(x=840, y=60, width=220)
        btn_search=Button(self.root,text='Search',font=("goudy old style",15,"bold"),bg="#2196f3",fg="white",cursor="hand2",command=self.search).place(x=1070,y=60,width=90,height=28)

        #====Content======
        self.C_Frame=Frame(self.root,bd=2,relief=RIDGE)
        self.C_Frame.place(x=690,y=100,width=470,height=340)

        scrolly=Scrollbar(self.C_Frame,orient=VERTICAL)
        self.MatchTable=ttk.Treeview(self.C_Frame,columns=("challenger","challengee","score"),yscrollcommand=scrolly.set)
        scrolly.pack(side=RIGHT,fill=Y)
        scrolly.config(command=self.MatchTable.yview)

        self.MatchTable.heading("challenger",text="Challenger")
        self.MatchTable.heading("challengee",text="Challengee")
        self.MatchTable.heading("score",text="Score")


        self.MatchTable["show"]='headings'
        self.MatchTable.column("challenger",width=80)
        self.MatchTable.column("challengee",width=80)
        self.MatchTable.column("score",width=40,anchor=CENTER)

        self.player_list=[]


        self.var_score1_1=StringVar()
        self.var_score1_2 = StringVar()
        self.var_score1_3 = StringVar()

        self.var_score2_1=StringVar()
        self.var_score2_2 = StringVar()
        self.var_score2_3 = StringVar()

        self.txt_challenger=ttk.Combobox(self.root,textvariable=self.var_challenger,font=("goudy old style",10,'bold'),state='readonly',justify=CENTER,postcommand=self.fetch_player)
        self.txt_challenger.place(x=210,y=110,width=200)
        self.txt_challenger.set("Please Select")
        self.txt_challengee=ttk.Combobox(self.root,textvariable=self.var_challengee,font=("goudy old style",10,'bold'),state='readonly',justify=CENTER,postcommand=self.fetch_player)
        self.txt_challengee.place(x=210,y=250,width=200)
        self.txt_challengee.set("Please Select")
        # txt_score=Entry(self.root,textvariable=self.var_score,font=("goudy old style",15,'bold'),bg='lightyellow').place(x=210,y=180,width=200)
        # txt_score2 = Entry(self.root, textvariable=self.var_score,font=("goudy old style",15,'bold'),bg='lightyellow').place(x=210, y=320, width=200)

        self.lista=[0,1,2,3,4,5,6,7]

        self.txt_score1_1=ttk.Combobox(self.root,textvariable=self.var_score1_1,values=self.lista,font=("goudy old style",10,'bold'),state='readonly',justify=CENTER)
        self.txt_score1_1.place(x=210,y=180,width=40)
        self.txt_score1_1.set("_")

        self.txt_score1_2=ttk.Combobox(self.root,textvariable=self.var_score1_2,values=self.lista,font=("goudy old style",10,'bold'),state='readonly',justify=CENTER)
        self.txt_score1_2.place(x=270,y=180,width=40)
        self.txt_score1_2.set("_")

        self.txt_score1_3=ttk.Combobox(self.root,textvariable=self.var_score1_3,values=self.lista,font=("goudy old style",10,'bold'),state='readonly',justify=CENTER)
        self.txt_score1_3.place(x=330,y=180,width=40)
        self.txt_score1_3.set("_")

        self.txt_score2_1=ttk.Combobox(self.root,textvariable=self.var_score2_1,values=self.lista,font=("goudy old style",10,'bold'),state='readonly',justify=CENTER)
        self.txt_score2_1.place(x=210,y=320,width=40)
        self.txt_score2_1.set("_")

        self.txt_score2_2=ttk.Combobox(self.root,textvariable=self.var_score2_2,values=self.lista,font=("goudy old style",10,'bold'),state='readonly',justify=CENTER)
        self.txt_score2_2.place(x=270,y=320,width=40)
        self.txt_score2_2.set("_")

        self.txt_score2_3=ttk.Combobox(self.root,textvariable=self.var_score2_3,values=self.lista,font=("goudy old style",10,'bold'),state='readonly',justify=CENTER)
        self.txt_score2_3.place(x=330,y=320,width=40)
        self.txt_score2_3.set("_")



        self.MatchTable.pack(fill=BOTH,expand=1)
        #self.MatchTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()

#=======================================================================================
#====================FUNCTIONS==========================================================
#=======================================================================================
    def get_data(self,ev):
        r=self.MatchTable.focus()
        content=self.MatchTable.item(r)
        row=content["values"]
        self.var_challenger.set(row[0])
        self.var_challengee.set(row[1])
        self.var_score.set(row[2])

    def clear_data(self):
        self.show()
        self.var_challenger.set("Please Select")
        self.var_challengee.set("Please Select")
        self.var_score1_1.set("_")
        self.var_score1_2.set("_")
        self.var_score1_3.set("_")
        self.var_score2_1.set("_")
        self.var_score2_2.set("_")
        self.var_score2_3.set("_")
        self.var_search.set("")
        self.fetch_player()

    def new_match(self):
        conn=sqlite3.connect(database="ATP.db")
        c=conn.cursor()

        try:
            if self.var_challenger.get()=="Please Select" or self.var_challengee.get()=="" or self.var_score1_1.get()=="Please Select" or self.var_score2_1.get()=="_" or self.var_score1_2.get()=="_" or self.var_score2_2.get()=="_" or self.var_score1_3.get()=="_" or self.var_score2_3.get()=="_":
                messagebox.showerror("Error","All fields are required",parent=self.root)
            else:
                name_1 = self.var_challenger.get()
                name_1 = name_1.split(".")
                name_2 = self.var_challengee.get()
                name_2 = name_2.split(".")
                score1_1 = self.var_score1_1.get()
                score1_2 = self.var_score1_2.get()
                score1_3 = self.var_score1_3.get()

                score2_1 = self.var_score2_1.get()
                score2_2 = self.var_score2_2.get()
                score2_3 = self.var_score2_3.get()
                try:
                    score1=0
                    score2=0
                    if int(score1_1) < 6 and int(score2_1) < 6:
                        messagebox.showerror('Error!', "Player can't win with less than 6 games",parent=self.root)
                        return
                    if int(score1_2) < 6 and int(score2_2) < 6:
                        messagebox.showerror('Error!', "Player can't win with less than 6 games",parent=self.root)
                        return
                    if int(score1_3) < 6 and int(score2_3) < 6:
                        messagebox.showerror('Error!', "Player can't win with less than 6 games",parent=self.root)
                        return

                    if int(score1_1) > int(score2_1):
                        score1+=1
                    elif int(score1_1) < int(score2_1):
                        score2+=1
                    else:
                        messagebox.showerror('Error!', "Result can't be a draw!",parent=self.root)
                        return

                    if int(score1_2) > int(score2_2):
                        score1+=1
                    elif int(score1_2) < int(score2_2):
                        score2+=1
                    else:
                        messagebox.showerror('Error!', "Result can't be a draw!",parent=self.root)
                        return

                    if int(score1_3) > int(score2_3):
                        score1+=1
                    elif int(score1_3) < int(score2_3):
                        score2+=1
                    else:
                        messagebox.showerror('Error!', "Result can't be a draw!",parent=self.root)
                        return
                except Exception as ex:
                    messagebox.showerror("Error", f"Error due to 1o {str(ex)}",parent=self.root)

                try:
                    if int(name_1[0]) > int(name_2[0]):
                        if int(name_1[0]) - int(name_2[0]) <= 5:
                            if (score1 > score2) and (score1 >= 0) and (score1 <= 5) and (score2 >= 0) and (score2 <= 5):
                                score = str(score1) + " - " + str(score2)
                                self.challenge_win(int(name_1[0]), int(name_2[0]), str(score))
                            elif (score1 < score2) and (score1 >= 0) and (score1 <= 5) and (score2 >= 0) and (score2 <= 5):
                                score = str(score1) + " - " + str(score2)
                                self.challenge_lose(int(name_1[0]), int(name_2[0]), score)
                            else:
                                messagebox.showerror('Error!', "Invalid Score!",parent=self.root)
                                return
                        else:
                            messagebox.showerror('Error!', "The challenger can't be more than 5 spots below the challengee!",parent=self.root)
                            return
                    else:
                        messagebox.showerror('Error!', "The challenger can't be a higher rank than the chalengee!",parent=self.root)
                        return
                except ValueError:
                    messagebox.showerror('Error!', "Invalid type",parent=self.root)
                    return
                messagebox.showinfo("Success","Match created successfully!",parent=self.root)
                self.show()
                self.clear_data()
            conn.commit()
            conn.close()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to 2o {str(ex)}",parent=self.root)

    def fetch_player(self):
        conn=sqlite3.connect(database="ATP.db")
        c=conn.cursor()
        try:
            c.execute("SELECT rowid,first_name,last_name FROM leaderboard")
            rows=c.fetchall()
            self.player_list=[]
            if len(rows)>0:
                for row in rows:
                    self.player_list.append(str(row[0]) + '. ' + row[1] + ' ' + row[2])
            self.txt_challenger['values'] = self.player_list
            self.txt_challengee['values'] = self.player_list
            conn.commit()
            conn.close()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}",parent=self.root)

    def show(self):
        conn=sqlite3.connect(database="ATP.db")
        c=conn.cursor()
        try:
            c.execute("SELECT challenger,challengee,score FROM match")
            rows=c.fetchall()
            self.MatchTable.delete(*self.MatchTable.get_children())
            for row in rows:
                self.MatchTable.insert('',END,values=row)
            conn.commit()
            conn.close()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}",parent=self.root)

    def search(self):
        conn=sqlite3.connect(database="ATP.db")
        c=conn.cursor()
        try:
            c.execute(f"SELECT challenger,challengee,score FROM match WHERE challenger LIKE '%{self.var_search.get()}%' OR challengee LIKE '%{self.var_search.get()}%' ")
            rows=c.fetchall()
            self.MatchTable.delete(*self.MatchTable.get_children())
            for row in rows:
                self.MatchTable.insert('',END,values=row)
            conn.commit()
            conn.close()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}",parent=self.root)

    def challenge_win(self,p1,p2,sk):
        conn = sqlite3.connect('ATP.db')
        c = conn.cursor()
        try:
            c.execute("SELECT rowid, * FROM leaderboard")
        except sqlite3.Error as er:
            print('Error')
        data = c.fetchall()
        q1 = data[p1-1][1] + " " + data[p1-1][2]
        q2 = data[p2-1][1] + " " + data[p2-1][2]
        try:
            c.execute("UPDATE leaderboard SET first_name = ?,last_name = ?,age = ?, Wins = ?, Losses = ? WHERE rowid = ?",(data[p1-1][1],data[p1-1][2],data[p1-1][3],data[p1-1][4],data[p1-1][5],p2))
        except sqlite3.Error as er:
            print('Error')

        for i in range(p2,p1):							#Για να γίνετε update με επανάληψη (δηλαδή να αλλάζουν οι θέσεις των παικτών) όταν νικάει
            try:
                c.execute("UPDATE leaderboard SET first_name = ?,last_name = ?,age = ?, Wins = ?, Losses = ? WHERE rowid = ?",(data[i-1][1],data[i-1][2],data[i-1][3],data[i-1][4],data[i-1][5],i+1))
            except sqlite3.Error as er:
                print('Error')
        try:
            c.execute("INSERT INTO match VALUES (?,?,?)", (q1, q2, sk)) 		#Για να μπαίνουν στο show_match ονοματα και score
        except sqlite3.Error as er:
            print('Error')
        oi = int(data[p2-1][5]) + 1 						#Για να μπαίνουν win και lose σε κάθε παίκτη στο leaderboard
        try:
            c.execute("UPDATE leaderboard SET Losses = ? WHERE rowid = ?",(oi,p2+1))
        except sqlite3.Error as er:
            print('Error')
        ai = int(data[p1-1][4]) + 1
        try:
            c.execute("UPDATE leaderboard SET Wins = ? WHERE rowid = ?",(ai,p2))
        except sqlite3.Error as er:
            print('Error')
        conn.commit()
        conn.close()

    def challenge_lose(self,p1,p2,sk):
        conn = sqlite3.connect('ATP.db')
        c = conn.cursor()
        try:
            c.execute("SELECT rowid, * FROM leaderboard")
        except sqlite3.Error as er:
            print('Error')
        data = c.fetchall()
        q1 = data[p1-1][1] + " " + data[p1-1][2]
        q2 = data[p2-1][1] + " " + data[p2-1][2]
        oi = int(data[p1-1][5]) + 1
        ai = int(data[p2-1][4]) + 1  #Για να μπαίνουν win και lose σε κάθε παίκτη στο leaderboard

        try:
            c.execute("UPDATE leaderboard SET Losses = ? WHERE rowid = ?", (oi, p1))
            c.execute("UPDATE leaderboard SET Wins = ? WHERE rowid = ?",(ai,p2))
            c.execute("INSERT INTO match VALUES (?,?,?)", (q1, q2, sk))

        except sqlite3.Error as er:
            print('Error')

        conn.commit()
        conn.close()



