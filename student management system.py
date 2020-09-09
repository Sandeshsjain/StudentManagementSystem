import tkinter
from tkinter import *
from tkinter import ttk
import pymysql
class Student:
    def __init__(self,root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1500x750+0+0")

        title = Label(self.root ,text="Student Management System ",bd=10,relief=GROOVE,font=("Times new roman",40,"bold"),bg="yellow",fg="red")
        title.pack(side=TOP, fill = X)


    #------------ All Variables---------------
        self.Roll_No_var = StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.gender_var = StringVar()
        self.contact_var = StringVar()
        self.dob_var = StringVar()

        self.search_by = StringVar()
        self.search_txt = StringVar()



        # --------MANAGE FRAME--------

        Manage_frame = Frame(self.root , bd = 4 ,relief = RIDGE,bg = "crimson")
        Manage_frame.place(x=20,y=100,width = 600,height = 640)

        M_title = Label(Manage_frame, text = "Manage Students" , bg = "crimson" , fg = "white",font=("Times new roman",30,"bold") )
        M_title.grid(row = 0 , columnspan=2 , pady = 20)
            #--------ROLL NO.----------
        lbl_roll = Label(Manage_frame, text = "Roll No." , bg = "crimson" , fg = "white",font=("Times new roman",20,"bold") )
        lbl_roll.grid(row =1,column = 0 , pady= 10 , padx= 20 , sticky = "w")

        txt_Roll = Entry(Manage_frame ,textvariable=self.Roll_No_var, font=("times new roman",15,"bold") , bd =5 , relief = GROOVE)
        txt_Roll.grid(row=1, column=1, pady=10, padx=20, sticky="w")

            #-------NAME---------
        lbl_name = Label(Manage_frame, text="Name", bg="crimson", fg="white", font=("Times new roman", 20, "bold"))
        lbl_name.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        txt_name = Entry(Manage_frame,textvariable=self.name_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_name.grid(row=2, column=1, pady=10, padx=20, sticky="w")

            #-------EMAIL--------
        lbl_email = Label(Manage_frame, text="Email", bg="crimson", fg="white", font=("Times new roman", 20, "bold"))
        lbl_email.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        txt_email = Entry(Manage_frame,textvariable=self.email_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_email.grid(row=3, column=1, pady=10, padx=20, sticky="w")

            #-------GENDER-------
        lbl_gender = Label(Manage_frame, text="Gender", bg="crimson", fg="white", font=("Times new roman", 20, "bold"))
        lbl_gender.grid(row=4, column=0 , pady=10, padx=20 , sticky="w")

        combo_gender=ttk.Combobox(Manage_frame,textvariable=self.gender_var,font=("times new roman", 13, "bold") , state = "readonly")
        combo_gender["values"]=("Male","Female","others")
        combo_gender.grid(row=4 , column=1 , padx = 10 , pady = 20)


            #-----CONTACT-------
        lbl_contact = Label(Manage_frame, text="contact", bg="crimson", fg="white", font=("Times new roman", 20, "bold"))
        lbl_contact.grid(row=5, column=0, pady=10, padx=20, sticky="w")

        txt_contact = Entry(Manage_frame,textvariable=self.contact_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_contact.grid(row=5, column=1, pady=10, padx=20, sticky="w")

            #-------DATE OF BIRTH-------
        lbl_dob = Label(Manage_frame, text="D.O.B.", bg="crimson", fg="white",font=("Times new roman", 20, "bold"))
        lbl_dob.grid(row=6, column=0, pady=10, padx=20, sticky="w")

        txt_dob = Entry(Manage_frame,textvariable=self.dob_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_dob.grid(row=6, column=1, pady=10, padx=20, sticky="w")

            #------ADDRESS----------
        lbl_address = Label(Manage_frame, text="Address", bg="crimson", fg="white",font=("Times new roman", 20, "bold"))
        lbl_address.grid(row=7, column=0, pady=10, padx=20, sticky="w")
        self.txt_address = Text(Manage_frame,width = 26 , height = 4)
        self.txt_address.grid(row=7 ,column=1 ,padx=20 , pady=10)
#--------BUTTON FRAME
        btn_frame =Frame(Manage_frame , bd = 4 , relief= RIDGE , bg = "crimson")
        btn_frame.place(x= 10 , y =530 ,width=430)

        add_btn = Button(btn_frame,command=self.add_students,text="ADD" , width = 11 ,).grid(row=0,column=0 , padx =10,pady =10)
        update_btn = Button(btn_frame,command =self.update_data, text="UPDATE", width=11).grid(row=0, column=1, padx=10, pady=10)
        delete_btn = Button(btn_frame,command = self.delete_data, text="DELETE", width=11).grid(row=0, column=2, padx=10, pady=10)
        clear_btn = Button(btn_frame,command = self.clear, text="CLEAR", width=11).grid(row=0, column=3, padx=10, pady=10)

        #--------DETAIL FRAME---------


        Detail_frame = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        Detail_frame.place(x=670, y=100, width=800, height=640)

        lbl_search = Label(Detail_frame, text="Search By . ", bg="crimson", fg="white", font=("Times new roman", 20, "bold"))
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        combo_search= ttk.Combobox(Detail_frame,textvariable=self.search_by, font=("times new roman", 10, "bold"), state="readonly")
        combo_search["values"] = ("roll", "name", "contact")
        combo_search.grid(row=0, column=1, padx=10, pady=20)

        txt_search = Entry(Detail_frame,textvariable=self.search_txt, width=20)
        txt_search.grid(row=0, column=2, padx=20, pady=10)

        search_btn = Button(Detail_frame,command = self.Search_data, text="Search", width=11, ).grid(row=0, column=3, padx=10, pady=10)
        showall_btn = Button(Detail_frame,command=self.fetch_data, text="Show All", width=11, ).grid(row=0, column=4, padx=10, pady=10)


#----------------------TABLE FRAME--------------------------

        Table_frame = Frame(Detail_frame , bd=4 , relief =RIDGE ,bg = 'crimson')
        Table_frame.place(x=10,y=70,width=770,height=525)
        scroll_x=Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_frame,orient =VERTICAL)
        self.Student_table=ttk.Treeview(Table_frame,columns=("roll","name","email","gender","contact","dob","address"), xscrollcommand=scroll_x.set , yscrollcommand = scroll_y.set)
        scroll_x.pack(side =BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)

        self.Student_table.heading("roll",text="ROll No.")
        self.Student_table.heading("name", text="Name")
        self.Student_table.heading("email", text="E-mail")
        self.Student_table.heading("gender", text="Gender")
        self.Student_table.heading("contact", text="Contact")
        self.Student_table.heading("dob", text="Date of Birth")
        self.Student_table.heading("address", text="Address")
        self.Student_table["show"]="headings"
        self.Student_table.column("roll",width=100)
        self.Student_table.column("name", width=200)
        self.Student_table.column("email", width=200)
        self.Student_table.column("gender", width=100)
        self.Student_table.column("contact", width=200)
        self.Student_table.column("dob", width=200)
        self.Student_table.column("address", width=200)
        self.Student_table.pack(fill = BOTH , expand=1)
        self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
    def add_students(self):
        con = pymysql.connect(host='localhost',user='root',passwd='Sandesh@123',database='sandesh')
        cur=con.cursor()
        cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)",(self.Roll_No_var.get(),
                                                                         self.name_var.get(),
                                                                         self.email_var.get(),
                                                                         self.gender_var.get(),
                                                                         self.contact_var.get(),
                                                                         self.dob_var.get(),
                                                                         self.txt_address.get("1.0",END)
                                                                         ))        #--self.txt_address.get(line_no(here line no 1) TO end)
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

    def fetch_data(self):
        con = pymysql.connect(host='localhost', user='root', passwd='Sandesh@123', database='sandesh')
        cur = con.cursor()
        cur.execute("select * from students")
        rows = cur.fetchall()
        if len(rows) !=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert("",END,values=row)
                con.commit()
        con.close()
    def clear(self):
        self.Roll_No_var.set(''),
        self.name_var.set(''),
        self.email_var.set(''),
        self.gender_var.set(''),
        self.contact_var.set(''),
        self.dob_var.set(''),
        self.txt_address.delete("1.0", END)
    def get_cursor(self,ev):
        cursor_row = self.Student_table.focus()
        content = self.Student_table.item(cursor_row)
        row = content['values']
        self.Roll_No_var.set(row[0]),
        self.name_var.set(row[1]),
        self.email_var.set(row[2]),

        self.gender_var.set(row[3]),
        self.contact_var.set(row[4]),
        self.dob_var.set(row[5]),
        self.txt_address.delete("1.0", END)
        self.txt_address.insert(END,row[6])
    def update_data(self):
        con = pymysql.connect(host='localhost', user='root', passwd='Sandesh@123', database='sandesh')
        cur = con.cursor()
        cur.execute("update students"
                    " set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s "
                    "where roll_no=%s",(
                                        self.name_var.get(),
                                        self.email_var.get(),
                                        self.gender_var.get(),
                                        self.contact_var.get(),
                                        self.dob_var.get(),
                                        self.txt_address.get("1.0", END),
                                        self.Roll_No_var.get()
                                        ))
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()

    def delete_data(self):
        con = pymysql.connect(host='localhost', user='root', passwd='Sandesh@123', database='sandesh')
        cur = con.cursor()
        cur.execute("delete from students where roll_no = %s",self.Roll_No_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()

    def Search_data(self):
        con = pymysql.connect(host='localhost', user='root', passwd='Sandesh@123', database='sandesh')
        cur = con.cursor()
        cur.execute("select * from Students where " +str(self.search_by.get())+"="+str(self.search_txt.get()))
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert("", END, values=row)
                con.commit()
        con.close()







root=Tk()
ob = Student(root)
root.mainloop()