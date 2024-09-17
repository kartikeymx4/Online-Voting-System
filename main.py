from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import datetime


class LibraryManagementSystem:
      def __init__(self,root):
            self.root=root
            self.root.title("Library Management System")
            self.root.geometry("1350x730+0+0")

#==============variable===============
            self.member_var=StringVar()
            self.prn_var=StringVar()
            self.id_var=StringVar()
            self.firstname_var=StringVar()
            self.lastname_var=StringVar()
            self.address_var=StringVar()
            self.postcode_var=StringVar()
            self.mobile_var=StringVar()
            self.bookid_var=StringVar()
            self.booktitle_var=StringVar()
            self.author_var=StringVar()
            self.dateborrowed_var=StringVar()
            self.datedue_var=StringVar()
            self.daysonbook=StringVar()
            self.lateratefine_var=StringVar()
            self.dateoverdue_var=StringVar()
            self.finalprice_var=StringVar()
#================dataframe===================
            l1=Label(self.root,text="LIBRARY MANAGEMENT SYSTEM",bg="powder blue",fg="green",bd=20,relief=RIDGE,font=("Times new roman",40,'bold'),padx=2,pady=6)
            l1.pack(side=TOP,fill=X)

            f1=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
            f1.place(x=0,y=120,width=1340,height=365)

            df=LabelFrame(f1,text="Membership Info",bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("Times new roman",12,'bold'))
            df.place(x=0,y=5,width=800,height=330)

            ml=Label(df,text="Member type",bg="powder blue",font=("Times new roman",12,'bold'),padx=2,pady=6)
            ml.grid(row=0,column=0,sticky='w')

            combo=ttk.Combobox(df,textvariable=self.member_var,font=("Times new roman",12,'bold'),width=27,state="readonly")
            combo["value"]=("Admin staff","Student","Faculty")
            combo.grid(row=0,column=1)

            m2=Label(df,text="PRN No.",bg="powder blue",font=("Times new roman",12,'bold'),padx=2,pady=6)
            m2.grid(row=1,column=0,sticky='w')
            tb_prn=Entry(df,font=("Times new roman",12,'bold'),width=29,textvariable=self.prn_var)
            tb_prn.grid(row=1,column=1)

            m3=Label(df,text="ID No.",bg="powder blue",font=("Times new roman",12,'bold'),padx=2,pady=6)
            m3.grid(row=2,column=0,sticky='w')
            tb_id=Entry(df,font=("Times new roman",12,'bold'),width=29,textvariable=self.id_var)
            tb_id.grid(row=2,column=1)

            m4=Label(df,text="FirstName",bg="powder blue",font=("Times new roman",12,'bold'),padx=2,pady=6)
            m4.grid(row=3,column=0,sticky='w')
            tb_fn=Entry(df,font=("Times new roman",12,'bold'),width=29,textvariable=self.firstname_var)
            tb_fn.grid(row=3,column=1)

            m5=Label(df,text="LastName",bg="powder blue",font=("Times new roman",12,'bold'),padx=2,pady=6)
            m5.grid(row=4,column=0,sticky='w')
            tb_ln=Entry(df,font=("Times new roman",12,'bold'),width=29,textvariable=self.lastname_var)
            tb_ln.grid(row=4,column=1)

            m6=Label(df,text="Address",bg="powder blue",font=("Times new roman",12,'bold'),padx=2,pady=6)
            m6.grid(row=5,column=0,sticky='w')
            tb_add=Entry(df,font=("Times new roman",12,'bold'),width=29,textvariable=self.address_var)
            tb_add.grid(row=5,column=1)

            m7=Label(df,text="PostCode",bg="powder blue",font=("Times new roman",12,'bold'),padx=2,pady=6)
            m7.grid(row=6,column=0,sticky='w')
            tb_pc=Entry(df,font=("Times new roman",12,'bold'),width=29,textvariable=self.postcode_var)
            tb_pc.grid(row=6,column=1)

            m8=Label(df,text="Phone no.",bg="powder blue",font=("Times new roman",12,'bold'),padx=2,pady=6)
            m8.grid(row=7,column=0,sticky='w')
            tb_ph=Entry(df,font=("Times new roman",12,'bold'),width=29,textvariable=self.mobile_var)
            tb_ph.grid(row=7,column=1)

            b1=Label(df,text="Book Id:",bg="powder blue",font=("Times new roman",12,'bold'),padx=2,pady=6)
            b1.grid(row=0,column=3,sticky='w')
            tb_bi=Entry(df,font=("Times new roman",12,'bold'),width=29,textvariable=self.bookid_var)
            tb_bi.grid(row=0,column=5)

            b2=Label(df,text="Book Title:",bg="powder blue",font=("Times new roman",12,'bold'),padx=2,pady=6)
            b2.grid(row=1,column=3,sticky='w')
            tb_bt=Entry(df,font=("Times new roman",12,'bold'),width=29,textvariable=self.booktitle_var)
            tb_bt.grid(row=1,column=5)

            b3=Label(df,text="Author Name:",bg="powder blue",font=("Times new roman",12,'bold'),padx=2,pady=6)
            b3.grid(row=2,column=3,sticky='w')
            tb_name=Entry(df,font=("Times new roman",12,'bold'),width=29,textvariable=self.author_var)
            tb_name.grid(row=2,column=5)

            b4=Label(df,text="Date Borrowed:",bg="powder blue",font=("Times new roman",12,'bold'),padx=2,pady=6)
            b4.grid(row=3,column=3,sticky='w')
            tb_db=Entry(df,font=("Times new roman",12,'bold'),width=29,textvariable=self.dateborrowed_var)
            tb_db.grid(row=3,column=5)

            b5=Label(df,text="Date Due:",bg="powder blue",font=("Times new roman",12,'bold'),padx=2,pady=6)
            b5.grid(row=4,column=3,sticky='w')
            tb_dd=Entry(df,font=("Times new roman",12,'bold'),width=29,textvariable=self.datedue_var)
            tb_dd.grid(row=4,column=5)

            b6=Label(df,text="Late Return fine:",bg="powder blue",font=("Times new roman",12,'bold'),padx=2,pady=6)
            b6.grid(row=5,column=3,sticky='w')
            tb_fine=Entry(df,font=("Times new roman",12,'bold'),width=29,textvariable=self.lateratefine_var)
            tb_fine.grid(row=5,column=5)

            b7=Label(df,text="Date Over Due:",bg="powder blue",font=("Times new roman",12,'bold'),padx=2,pady=6)
            b7.grid(row=6,column=3,sticky='w')
            tb_do=Entry(df,font=("Times new roman",12,'bold'),width=29,textvariable=self.dateoverdue_var)
            tb_do.grid(row=6,column=5)

            b8=Label(df,text="Actual Price:",bg="powder blue",font=("Times new roman",12,'bold'),padx=2,pady=6)
            b8.grid(row=7,column=3,sticky='w')
            tb_price=Entry(df,font=("Times new roman",12,'bold'),width=29,textvariable=self.finalprice_var)
            tb_price.grid(row=7,column=5)

            df2=LabelFrame(f1,text="Book Details",bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("Times new roman",12,'bold'))
            df2.place(x=810,y=5,width=470,height=330)

            self.txtbox=Text(df2,font=("Times new roman",12,'bold'),width=32,height=15,padx=4,pady=6)
            self.txtbox.grid(row=0,column=2)

            listscrollbar=Scrollbar(df2)
            listscrollbar.grid(row=0,column=1,sticky='ns')

            Books=["The Algorithm","Machine Learning","Artificial Intelligence","Data Structures and algorithm",
                         "Microprocessor 8085","Digital Electronics","Engineering Mathematics","IOT","Python","Java & C++"]


            def select_book(event=""):
                  value=str(listbox.get(listbox.curselection()))
                  x=value
                  if(x=="The Algorithm"):
                        self.bookid_var.set("K387")
                        self.booktitle_var.set("DSA")
                        self.author_var.set("Kartik Jain")
                        d1=datetime.datetime.today()
                        d2=datetime.timedelta(days=15)
                        d3=d1+d2
                        self.dateborrowed_var.set(d1)
                        self.datedue_var.set(d3)
                        self.lateratefine_var.set("Rs 50")
                        self.dateoverdue_var.set("NO")
                        self.finalprice_var.set("Rs 1200")
                  elif(x=="Machine Learning"):
                        self.bookid_var.set("A767")
                        self.booktitle_var.set("CS")
                        self.author_var.set("Xertius")
                        d1=datetime.datetime.today()
                        d2=datetime.timedelta(days=15)
                        d3=d1+d2
                        self.dateborrowed_var.set(d1)
                        self.datedue_var.set(d3)
                        self.lateratefine_var.set("Rs 50")
                        self.dateoverdue_var.set("NO")
                        self.finalprice_var.set("Rs 900")
                  elif(x=="Artificial Intelligence"):
                        self.bookid_var.set("S677")
                        self.booktitle_var.set("AI")
                        self.author_var.set("Mortoish")
                        d1=datetime.datetime.today()
                        d2=datetime.timedelta(days=15)
                        d3=d1+d2
                        self.dateborrowed_var.set(d1)
                        self.datedue_var.set(d3)
                        self.lateratefine_var.set("Rs 50")
                        self.dateoverdue_var.set("NO")
                        self.finalprice_var.set("Rs 1190")
                  elif(x=="Microprocessor 8085"):
                        self.bookid_var.set("M689")
                        self.booktitle_var.set("Electronics")
                        self.author_var.set("Mortus")
                        d1=datetime.datetime.today()
                        d2=datetime.timedelta(days=15)
                        d3=d1+d2
                        self.dateborrowed_var.set(d1)
                        self.datedue_var.set(d3)
                        self.lateratefine_var.set("Rs 50")
                        self.dateoverdue_var.set("NO")
                        self.finalprice_var.set("Rs 2000")
                  elif(x=="Data Structures and algorithm"):
                        self.bookid_var.set("D7565")
                        self.booktitle_var.set("DSA")
                        self.author_var.set("Kanishk")
                        d1=datetime.datetime.today()
                        d2=datetime.timedelta(days=15)
                        d3=d1+d2
                        self.dateborrowed_var.set(d1)
                        self.datedue_var.set(d3)
                        self.lateratefine_var.set("Rs 50")
                        self.dateoverdue_var.set("NO")
                        self.finalprice_var.set("Rs 1200")
                  elif(x=="IOT"):
                        self.bookid_var.set("W577")
                        self.booktitle_var.set("Embedded")
                        self.author_var.set("Kartik Jain")
                        d1=datetime.datetime.today()
                        d2=datetime.timedelta(days=15)
                        d3=d1+d2
                        self.dateborrowed_var.set(d1)
                        self.datedue_var.set(d3)
                        self.lateratefine_var.set("Rs 50")
                        self.dateoverdue_var.set("NO")
                        self.finalprice_var.set("Rs 1200")
                  elif(x=="Python"):
                        self.bookid_var.set("W187")
                        self.booktitle_var.set("Programming")
                        self.author_var.set("Deepit Sharma")
                        d1=datetime.datetime.today()
                        d2=datetime.timedelta(days=15)
                        d3=d1+d2
                        self.dateborrowed_var.set(d1)
                        self.datedue_var.set(d3)
                        self.lateratefine_var.set("Rs 50")
                        self.dateoverdue_var.set("NO")
                        self.finalprice_var.set("Rs 1200")
                  elif(x=="Digital Electronics"):
                        self.bookid_var.set("N8276")
                        self.booktitle_var.set("Electronics")
                        self.author_var.set("zipreen")
                        d1=datetime.datetime.today()
                        d2=datetime.timedelta(days=15)
                        d3=d1+d2
                        self.dateborrowed_var.set(d1)
                        self.datedue_var.set(d3)
                        self.lateratefine_var.set("Rs 50")
                        self.dateoverdue_var.set("NO")
                        self.finalprice_var.set("Rs 1200")
                  elif(x=="Engineering Mathematics"):
                        self.bookid_var.set("F7354")
                        self.booktitle_var.set("Mathematics")
                        self.author_var.set("Arya bhatt")
                        d1=datetime.datetime.today()
                        d2=datetime.timedelta(days=15)
                        d3=d1+d2
                        self.dateborrowed_var.set(d1)
                        self.datedue_var.set(d3)
                        self.lateratefine_var.set("Rs 50")
                        self.dateoverdue_var.set("NO")
                        self.finalprice_var.set("Rs 1200")
                  elif(x=="Java & C++"):
                        self.bookid_var.set("U8678")
                        self.booktitle_var.set("Programming")
                        self.author_var.set("niptun")
                        d1=datetime.datetime.today()
                        d2=datetime.timedelta(days=15)
                        d3=d1+d2
                        self.dateborrowed_var.set(d1)
                        self.datedue_var.set(d3)
                        self.lateratefine_var.set("Rs 50")
                        self.dateoverdue_var.set("NO")
                        self.finalprice_var.set("Rs 1200")
            listbox=Listbox(df2,font=("Times new roman",12,'bold'),width=20,height=15)
            listbox.bind("<<ListboxSelect>>",select_book)
            listbox.grid(row=0,column=0,padx=4)
            listscrollbar.config(command=listbox.yview)
            
            for item in Books:
                  listbox.insert(END,item)

#button==========================================       
            f2=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
            f2.place(x=0,y=480,width=1340,height=75)

            addbtn=Button(f2,text="Add Data",command=self.add_data,font=("Times new roman",12,'bold'),width=23,bg="blue",fg="white")
            addbtn.grid(row=0,column=0,pady=6)

            shwbtn=Button(f2,text="Show",command=self.showdata,font=("Times new roman",12,'bold'),width=23,bg="blue",fg="white")
            shwbtn.grid(row=0,column=1,pady=6)

            updbtn=Button(f2,text="Update",font=("Times new roman",12,'bold'),width=23,bg="blue",fg="white")
            updbtn.grid(row=0,column=2,pady=6)

            delbtn=Button(f2,text="Delete",font=("Times new roman",12,'bold'),width=23,bg="blue",fg="white")
            delbtn.grid(row=0,column=3,pady=6)

            rstbtn=Button(f2,text="Reset",command=self.reset,font=("Times new roman",12,'bold'),width=23,bg="blue",fg="white")
            rstbtn.grid(row=0,column=4,pady=6)

            extbtn=Button(f2,text="Exit",command=self.iExit,font=("Times new roman",12,'bold'),width=21,bg="blue",fg="white")
            extbtn.grid(row=0,column=5,pady=6)
#database======================================
            f3=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
            f3.place(x=0,y=550,width=1340,height=155)

            tableframe=Frame(f3,bd=6,relief=RIDGE,bg="powder blue")
            tableframe.place(x=0,y=2,width=1260,height=140)

            xscroll=ttk.Scrollbar(tableframe,orient=HORIZONTAL)
            yscroll=ttk.Scrollbar(tableframe,orient=VERTICAL)

            self.library_table=ttk.Treeview(tableframe,column=("membertype","prnno","title","Firstname","Lastname",
                                                               "address","postid","mobile","bookid","author","dateborrowed",
                                                               "datedue","latereturnfine","dateoverdue","finalprice"),
                                            xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)
            xscroll.pack(side=BOTTOM,fill=X)
            yscroll.pack(side=RIGHT,fill=Y)

            xscroll.config(command=self.library_table.xview)
            yscroll.config(command=self.library_table.yview)
            self.library_table.heading("membertype",text="Member Type")
            self.library_table.heading("prnno",text="PRN NO")
            self.library_table.heading("title",text="Title")
            self.library_table.heading("Firstname",text="First Name")
            self.library_table.heading("Lastname",text="Last Name")
            self.library_table.heading("address",text="Address")
            self.library_table.heading("postid",text="Post Code")
            self.library_table.heading("mobile",text="Mobile No.")
            self.library_table.heading("bookid",text="Book Id")
            #self.library_table.heading("booktitle",text="Book Title")
            self.library_table.heading("author",text="Author")
            self.library_table.heading("dateborrowed",text="Date Borrowed")
            self.library_table.heading("datedue",text="Date Due")
            self.library_table.heading("latereturnfine",text="fine")
            self.library_table.heading("dateoverdue",text="DateOverDue")
            self.library_table.heading("finalprice",text="Final price")

            self.library_table["show"]="headings"
            self.library_table.pack(fill=BOTH,expand=1)
            self.fetch_data()
            self.library_table.bind("<<ButtonRelease=1>>",self.getcursor)
      def add_data(self):
            conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="libray")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into lib values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                              (self.member_var.get(),
            self.prn_var.get(),
            self.id_var.get(),
            self.firstname_var.get(),
            self.lastname_var.get(),
            self.address_var.get(),
            self.postcode_var.get(),
            self.mobile_var.get(),
            self.bookid_var.get(),
            self.author_var.get(),
            self.dateborrowed_var.get(),
            self.datedue_var.get(),
            self.lateratefine_var.get(),
            self.dateoverdue_var.get(),
            self.finalprice_var.get()))
            
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success","Member inserted")
      def fetch_data(self):
            conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="libray")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from lib")
            rows=my_cursor.fetchall()

            if len(rows)!=0:
                  self.library_table.delete(*self.library_table.get_children())
                  for i in rows:
                        self.library_table.insert("",END,value=i)
                  conn.commit()
            conn.close()

      def showdata(self):
            self.txtbox.insert(END,"Member Type:\t\t"+self.member_var.get()+"\n")                        
            
      def reset(self):
            self.member_var.set("")
            self.prn_var.set("")
            self.id_var.set("")
            self.firstname_var.set("")
            self.lastname_var.set("")
            self.address_var.set("")
            self.postcode_var.set("")
            self.mobile_var.set("")
            self.bookid_var.set("")
            self.booktitle_var.set("")
            self.author_var.set("")
            self.dateborrowed_var.set("")
            self.datedue_var.set("")
            self.lateratefine_var.set("")
            self.dateoverdue_var.set("")
            self.finalprice_var.set("")

      def iExit(self):
            iexit=messagebox.askyesno("Libraray management System","Do you want to exit")
            if iexit>0:
                  self.root.destroy()
                  return

      def getcursor(self,event=''):
            cursor_row=self.library_table.focus()
            content=self.library_table.item(cursor_row)
            row=content['values']

            self.member_var.set(row[0]),
            self.prn_var.set(row[1]),
            self.id_var.set(row[2]),
            self.firstname_var.set(row[3]),
            self.lastname_var.set(row[4]),
            self.address_var.set(row[5]),
            self.postcode_var.set(row[6]),
            self.mobile_var.set(row[7]),
            self.bookid_var.set(row[8]),
            self.booktitle_var.set(row[9]),
            self.author_var.set(row[10]),
            self.dateborrowed_var.set(row[11]),
            self.datedue_var.set(row[12]),
            self.lateratefine_var.set(row[13]),
            self.dateoverdue_var.set(row[14]),
            self.finalprice_var.set(row[15])
if __name__=="__main__":
      root=Tk()
      obj=LibraryManagementSystem(root)
      root.mainloop()
