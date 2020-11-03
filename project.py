from tkinter import*
from tkinter import font
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk #pip install pillow
import pymysql
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Tracing consignment")
        self.root.geometry("2000x1000+0+0")
        self.root.config(bg="green")

        #====BG Images====
       
        self.bg=ImageTk.PhotoImage(file="35.jpeg")
        bg = Label(self.root,image = self.bg).place(x=0,y=0,relwidth=1,relheight =1)
        #===left image====
        # self.left=ImageTk.PhotoImage(file="31.jpg")
        # left = Label(self.root,image = self.left,bg="white").place(x=80,y=100,width=400,height =500)
        
        #-------------------scroll bar
        # scrollbar1 = Scrollbar(root)
        # scrollbar1.pack(side=RIGHT,fill=Y)

        # listbox= Listbox(root,yscrollbarcommand=scrollbar1.set)

        # for i in range(344):
        #     listbox.insert(END,f"item{i}")
        # listbox.pack(fill="both")
        # scrollbar1.config(command=listbox.yview)
        #====Register Frame====
        frame1=Frame(self.root,bg="#36457b")
        frame1.place(x=480,y=100,width=700,height=500)


        title = Label(frame1,text="New User",font=("times new roman",30,"bold"),bg="white",fg="orange").place(x=50,y=10)
        #-----------row1
        f_name = Label(frame1,text="First Name",font=("times new roman",20,"bold"),bg="white",fg="gray").place(x=50,y=100)
        self.txt_fname = Entry(frame1,font=("times new roman",15),bg ="orange")
        self.txt_fname.place(x=30,y=130,width=250)
        
        l_name = Label(frame1,text="Last Name",font=("times new roman",20,"bold"),bg="white",fg="gray").place(x=370,y=100)
        self.txt_lname = Entry(frame1,font=("times new roman",15),bg ="orange")
        self.txt_lname.place(x=370,y=130,width=250)

        #--------------------------row2
        contact= Label(frame1,text="Contact No.",font=("times new roman",20,"bold"),bg="white",fg="gray").place(x=50,y=170)
        self.txt_contact= Entry(frame1,font=("times new roman",15),bg ="orange")
        self.txt_contact.place(x=30,y=200,width=250)


        email = Label(frame1,text="Email",font=("times new roman",20,"bold"),bg="white",fg="gray").place(x=370,y=170)
        self.txt_email = Entry(frame1,font=("times new roman",15),bg ="orange")
        self.txt_email.place(x=370,y=200,width=250)

        #--------------------row3
        question= Label(frame1,text="Security Question",font=("times new roman",20,"bold"),bg="white",fg="gray").place(x=50,y=240)
        self.cmb_quest= ttk.Combobox(frame1,font=("times new roman",15),state="readonly",justify=CENTER)
        self.cmb_quest['values']=("Select","Your Pet Name","Your Birth Place","Your Best Friend")
        self.cmb_quest.place(x=30,y=270,width=250)
        self.cmb_quest.current(0)
        answer = Label(frame1,text="Answer",font=("times new roman",20,"bold"),bg="white",fg="gray").place(x=370,y=240)
        self.txt_answer = Entry(frame1,font=("times new roman",15),bg ="orange")
        self.txt_answer.place(x=370,y=270,width=250)

         #--------------------------row4
        password= Label(frame1,text=" Password",font=("times new roman",20,"bold"),bg="white",fg="gray").place(x=50,y=310)
        self.txt_passward= Entry(frame1,font=("times new roman",15),bg ="orange")
        self.txt_passward.place(x=30,y=340,width=250)


        cpassword = Label(frame1,text=" Confirm Password",font=("times new roman",20,"bold"),bg="white",fg="gray").place(x=370,y=310)
        self.txt_cpassword = Entry(frame1,font=("times new roman",15),bg ="orange")
        self.txt_cpassword.place(x=370,y=340,width=250)
        
        self.var_chk=IntVar()
        chk = Checkbutton(frame1,text="I agree Terms and Conditions",variable=self.var_chk,onvalue=1,offvalue=0,bg="white",font=("times new roman",12)).place(x=50,y=380)
        btn_register = Button(frame1,text="Register Now",font=("times new roman",12,"bold"),fg="white",bg="#800857",cursor="hand2",command=self.register_data,bd = 0).place(x=280,y=420,width=150,height=60)
       
          #--------------------------------login form
        # title1 = Label(self.root,text="LOGIN",font=("times new roman",30,"bold"),bg="white",fg="orange").place(x=85,y=105)

        # f_name = Label(self.root,text="Username",font=("times new roman",20,"bold"),bg="white",fg="gray").place(x=150,y=170)
        # txt_fname = Entry(self.root,font=("times new roman",15),bg ="lightgray").place(x=150,y=200,width=250)

        # btn_login = Button(self.root,text="Login",font=("times new roman",25,"bold"),bg="white",fg="#800857",cursor="hand2",bd=0).place(x=190,y=520,width=150,height=40)

        frame2=Frame(self.root,bg="#35501e")
        frame2.place(x=80,y=100,width=400,height =500)

        title1 = Label(frame2,text="Login",font=("times new roman",30,"bold"),bg="white",fg="orange").place(x=50,y=10)
        #-------------username-----------------
        f_name2 = Label(frame2,text="Username",font=("times new roman",20,"bold"),bg="white",fg="gray").place(x=50,y=100)
        self.txt_fname2 = Entry(frame2,font=("times new roman",15),bg ="orange")
        self.txt_fname2.place(x=40,y=140,width=250,height=30)
        #------------password------------------
        password2= Label(frame2,text=" Password",font=("times new roman",20,"bold"),bg="white",fg="gray").place(x=50,y=210)
        self.txt_password2= Entry(frame2,font=("times new roman",15),bg ="orange")
        self.txt_password2.place(x=40,y=250,width=250,height=30)
        
        self.var_chk1 = IntVar()
        chk1 = Checkbutton(frame2,text="I'm Not Robot",onvalue=0,offvalue=1,variable=self.var_chk1,bg="white",fg="#800857",font=("times new roman",12)).place(x=50,y=310)
        btn_login = Button(frame2,text="Login",font=("times new roman",20,"bold"),fg="white",bg="#800857",cursor="hand2",command=self.login_data,bd = 0).place(x=50,y=340,width=150,height=60)

        #---------------tracking consigent-----------------
        frame3=Frame(self.root,bg="#1f6483")
        frame3.place(x=80,y=600,width=400,height =600)

        title4 = Label(frame3,text="Tracking",font=("times new roman",20,"bold"),fg="black").place(x=30,y=0)

        contact3= Label(frame3,text="Mobile No.",font=("times new roman",20,"bold"),bg="white",fg="gray").place(x=50,y=30)
        self.txt_contact3= Entry(frame3,font=("times new roman",15),bg ="orange")
        self.txt_contact3.place(x=40,y=70,width=250)

        tracking= Label(frame3,text="Track Id",font=("times new roman",20,"bold"),bg="white",fg="gray").place(x=50,y=100)
        self.txt_trackid= Entry(frame3,font=("times new roman",15),bg ="orange")
        self.txt_trackid.place(x=40,y=130,width=250)

        btn_track = Button(frame3,text="Track",font=("times new roman",20,"bold"),fg="white",bg="#800857",cursor="hand2",command=self.track_data,bd = 0).place(x=50,y=170,width=150,height=60)

        #------------------------
        frame4=Frame(self.root,bg="orange")
        frame4.place(x=180,y=0,width=900,height=100)
        title4 = Label(frame4,text="Courier Management System",font=("times new roman",30,"bold"),fg="white",bg="orange").place(x=100,y=10)

   
    def register_data(self):
        if self.txt_fname.get()=="" or self.txt_email.get()=="" or self.cmb_quest.get()=="Select" or self.txt_answer.get()=="" or self.txt_passward.get()=="" or self.txt_cpassword.get()=="" or self.txt_contact.get()=="":
            messagebox.showerror("Error","All Feild Are Required",parent=self.root)
         
        elif  self.txt_passward.get()!= self.txt_cpassword.get():
            messagebox.showerror("Error"," passward and confirm passward should same",parent=self.root)
        elif self.var_chk.get()==0:
           messagebox.showerror("Error","Please Agree Terms And Conditions",parent=self.root)  
        else:
            messagebox.showinfo("Success","Registration Successful",parent=self.root)

    def login_data(self):
        if self.txt_fname2.get()=="" or self.txt_password2.get()=="" :
            messagebox.showerror("Error","All Feild Are Required",parent=self.root)
        elif self.var_chk.get()==1:
           messagebox.showerror("Error","Please Check For Robot",parent=self.root)  
        else:
            messagebox.showinfo("Success","Login Successfully",parent=self.root)
    
    def track_data(self):
        if self.txt_contact3.get()=="" or self.txt_trackid.get()=="" :
            messagebox.showerror("Error","All Feild Are Required",parent=self.root)  
        else:
            messagebox.showinfo("Success","SMS has been sent to your device",parent=self.root)

                     

root = Tk()
obj = Register(root)
root.mainloop() 