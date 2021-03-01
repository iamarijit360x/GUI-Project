import tkinter as tk
from PIL import Image,ImageTk
from dependencies import validation as vld
from dependencies import xls_append
from tkinter import ttk
import os

class app(tk.Frame):
    
    def __init__(self, master = None):
        
        super().__init__()
        self.master = master
        self.loc=os.path.dirname(__file__) +'\studentinfo.xlsx'
        xls_append.check_file(self.loc)
        self.breadth = 1050
        self.master.geometry(str(self.breadth)+'x700')
        self.master.title('Registration Form')
        self.master.resizable(0,0)
        self.pack()
        
        self.widget()
        
    def widget(self):
        
        #back canvas
        self.canvas_back = tk.Canvas(self,width = self.breadth,height = 700,bg = 'black', bd = 0, highlightthickness = 0)
        self.canvas_back.pack()
        
        
        #top canvas
        self.canvas_top = tk.Canvas(self.canvas_back,width = self.breadth,height = 353,bg = '#00004E', highlightbackground = 'black')
        self.canvas_back.create_window(525,50,window = self.canvas_top)
        
        
        #bottom scrollable canvas
        self.length = 1400
        
        frame = tk.Frame(self.canvas_back,highlightthickness = 0)
        self.canvas_back.create_window(525,463,window = frame)
        
        self.canvas_main=tk.Canvas(frame,bg='#A8DADC',width=self.breadth,height=self.length,scrollregion=(0,-350,0,self.length-300), bd = 0, highlightthickness = 0)
        self.canvas_main.pack(side='left',expand=True,fill='both')

        vbar=tk.Scrollbar(frame,orient='vertical')
        vbar.pack(side='right',fill='y')
        vbar.config(command=self.canvas_main.yview)
        self.canvas_main.config(width=self.breadth-20,height=467)
        self.canvas_main.config(yscrollcommand=vbar.set)
        self.scroll_binds()
        
        self.top_canvas_widget()
        self.bottom_canvas_widget()
        
    def top_canvas_widget(self):
        
        #ARIJIT:-
        #logo
        logo = Image.open('assets/logo.png')
        logo = ImageTk.PhotoImage(logo)
        logo_label = tk.Label(self.canvas_top,image = logo,bg="#001a5c",bd=0)
        logo_label.image = logo
        logo_label.place(x =40,y =147)
        
        #heading
        college_name=tk.Label(self.canvas_top,text="St. Thomas' College of Engineering & Technology",bg='#00004E',fg='white',font=('Arial',20))
        college_name.place(x=300,y=180)
        details=tk.Label(self.canvas_top,text="4,Diamond Harbour Road, Kidderpore, Kolkata - 700023\n\nAll Programmes (B.Tech in CSE, EE, ECE & IT) are NBA Accredited.",bg='#00004E',fg='white',font=('Arial',15))
        details.place(x=300,y=240)
        
    def scroll_binds(self):
        
        #scroll
        def on_mousewheel(event):
            self.canvas_main.yview_scroll(int(-1*(event.delta/120)), "units")
        
        #scroll bind
        def bound_to_mousewheel(event):
            self.canvas_main.bind_all("<MouseWheel>", on_mousewheel)   
        
        #scroll unbind
        def unbound_to_mousewheel(event):
            self.canvas_main.unbind_all("<MouseWheel>") 
        
        #scroll bind on enter
        self.canvas_main.bind('<Enter>', bound_to_mousewheel)
        
        #scroll unbind on exit
        self.canvas_main.bind('<Leave>', unbound_to_mousewheel)
        
    def bottom_canvas_widget(self):
        
        self.color = '#FFFFFF'
        
        #pallete canvas
        self.canvas_form = tk.Canvas(self.canvas_main,width = 1010,height = self.length-30, bg = '#FFFFFF',highlightbackground = 'black', bd = 0)
        self.canvas_main.create_window(515,350,window = self.canvas_form)
        
        self.form()
        
    def form(self):
        
        self.fonter = "Arial 14 bold"
        self.fg_font = "Arial 14"
        self.dialogbox()
        
        #ISHITA AND ANIKET:-
        
        #set of dd/mm/yy
        date = ['0'+ str(i) for i in range(1,10)] + [str(i) for i in range(10,32)]
        month = date[:12]
        year = ['98','99','00'] + date[:20]
        
        #departments
        dept = ['CSE','ECE','EE','IT']
        
        #boards
        board1=['CBSE','ICSE','WB','OTHERS']
        board2=['CBSE','ISC','WB','OTHERS']
        
        frame_1 = tk.Frame(self.canvas_form,bg = self.color)
        self.canvas_form.create_window(490,550,window = frame_1)
        
        #name
        name_frame=tk.Frame(frame_1,bg=self.color,borderwidth=1,relief='solid')
        name_frame.grid(row=0,columnspan=8)
        tk.Label(name_frame,text="NAME:",font=self.fonter,bg=self.color).pack(side='left',padx=10,pady=20)
        self.name=tk.StringVar()
        tk.Entry(name_frame,textvar=self.name,font=self.fg_font,width=76).pack(side='left',padx=10)
        
        tk.Label(frame_1,text="",bg=self.color).grid(row=1)
        #father's name
        father_frame=tk.Frame(frame_1,bg=self.color,borderwidth=1,relief='solid')
        father_frame.grid(row=3,columnspan=8)
        tk.Label(father_frame,text="FATHER'S NAME:",font=self.fonter,bg=self.color).pack(side='left',padx=10,pady=20)
        self.f_name=tk.StringVar()
        tk.Entry(father_frame,textvar=self.f_name,font=self.fg_font,width=67).pack(side='left',padx=10)
        
        tk.Label(frame_1,text="",bg=self.color).grid(row=4)
        #mother's name
        mother_frame=tk.Frame(frame_1,bg=self.color,borderwidth=1,relief='solid')
        mother_frame.grid(row=5,columnspan=8)
        tk.Label(mother_frame,text="MOTHER'S NAME:",font=self.fonter,bg=self.color).pack(side='left',padx=10,pady=20)
        self.m_name=tk.StringVar()
        tk.Entry(mother_frame,textvar=self.m_name,font=self.fg_font,width=66).pack(side='left',padx=10)
        
        tk.Label(frame_1,text="",bg=self.color).grid(row=6)
        #dob
        dob_frame=tk.Frame(frame_1,bg=self.color,borderwidth=1,relief='solid')
        dob_frame.grid(row=7,columnspan=2)
        tk.Label(dob_frame,text="DOB:",font=self.fonter,bg=self.color).pack(side='left',padx=10,pady=20)
        self.dd_combo=ttk.Combobox(dob_frame,value=date,width=6,font=self.fg_font,state="readonly")
        self.dd_combo.pack(side='left')
        self.dd_combo.set("DD")
        self.mm_combo=ttk.Combobox(dob_frame,value=month,width=6,font=self.fg_font,state="readonly")
        self.mm_combo.pack(side='left')
        self.mm_combo.set("MM")
        self.yy_combo=ttk.Combobox(dob_frame,value=year,width=6,font=self.fg_font,state="readonly")
        self.yy_combo.pack(side='left')
        self.yy_combo.set("YY")
        tk.Label(dob_frame,text="",bg=self.color).pack()
        
        tk.Label(frame_1,text="",bg=self.color).grid(row = 7,column=2)
        #gender
        gender_frame=tk.Frame(frame_1,bg=self.color,borderwidth=1,relief='solid')
        gender_frame.grid(row=7,column=3,columnspan=5)
        tk.Label(gender_frame,text="GENDER:",font=self.fonter,bg=self.color).pack(side='left',padx=8,pady=20)
        self.gender=tk.IntVar()
        self.gender.set(0)
        tk.Radiobutton(gender_frame,text="MALE",font=self.fg_font,bg=self.color,variable=self.gender,value=1).pack(side='left')
        tk.Radiobutton(gender_frame,text="FEMALE",font=self.fg_font,bg=self.color,variable=self.gender,value=2).pack(side='left')
        tk.Radiobutton(gender_frame,text="OTHERS",font=self.fg_font,bg=self.color,variable=self.gender,value=3).pack(side='left')
        tk.Label(gender_frame,text="",bg=self.color).pack()
        
        tk.Label(frame_1,text="",bg=self.color).grid(row=8)
        #SHOUNAK:-
        
        #father's phone number
        fatherph_frame=tk.Frame(frame_1,bg=self.color,borderwidth=1,relief='solid')
        fatherph_frame.grid(row = 9,columnspan=6)
        tk.Label(fatherph_frame,text="FATHER'S PHONE NUMBER:",font=self.fonter,bg=self.color).pack(side='left',pady=20,padx=10)
        self.fph=tk.StringVar()
        tk.Entry(fatherph_frame,textvar=self.fph,font=self.fg_font,width=40).pack(side='left',padx=10)
        self.fph.set('+91')
        
        tk.Label(frame_1,text="",bg=self.color).grid(row = 10)
        #mother's phone number
        motherph_frame=tk.Frame(frame_1,bg=self.color,borderwidth=1,relief='solid')
        motherph_frame.grid(row=11,columnspan=6)
        tk.Label(motherph_frame,text="MOTHER'S PHONE NUMBER:",font=self.fonter,bg=self.color).pack(side='left',padx=9,pady=20)
        self.mph=tk.StringVar()
        tk.Entry(motherph_frame,textvar=self.mph,font=self.fg_font,width=40).pack(side='left',padx=9)
        self.mph.set('+91')
        
        tk.Label(frame_1,text="",bg=self.color).grid(row = 12)
        #domicile
        domicile_frame=tk.Frame(frame_1,bg=self.color,borderwidth=1,relief='solid')
        domicile_frame.grid(row=13,columnspan=2,sticky='w')
        tk.Label(domicile_frame,text="DOMICILE:",font=self.fonter,bg=self.color).pack(side='left',padx=10,pady=20)
        self.domicile_combo=ttk.Combobox(domicile_frame,value=['YES','NO'],width=15,font=self.fg_font,state="readonly")
        self.domicile_combo.pack(side='left')
        tk.Label(domicile_frame,text="",bg=self.color).pack()
        
        #department
        dept_frame=tk.Frame(frame_1,bg=self.color,borderwidth=1,relief='solid')
        dept_frame.grid(row=13,column=3,columnspan=3)
        tk.Label(dept_frame,text="DEPARTMENT:",font=self.fonter,bg=self.color).pack(side='left',padx=10,pady=20)
        self.dept_combo=ttk.Combobox(dept_frame,value=dept,width=8,font=self.fg_font,state="readonly")
        self.dept_combo.pack(side='left')
        tk.Label(dept_frame,text="",bg=self.color).pack()
        
        tk.Label(frame_1,text="",bg=self.color).grid(row = 14)
        #ANKITA:-
        
        #email
        email_frame=tk.Frame(frame_1,bg=self.color,borderwidth=1,relief='solid')
        email_frame.grid(row=15,columnspan=7)
        tk.Label(email_frame,text="MAIL ID:",font=self.fonter,bg=self.color).pack(side='left',padx=10,pady=20)
        self.email = tk.StringVar()
        tk.Entry(email_frame,textvar=self.email,font=self.fg_font,width=66).pack(side='left',padx=10)
        
        tk.Label(frame_1,text="",bg=self.color).grid(row = 16)
        #present address
        presA_frame=tk.Frame(frame_1,bg=self.color,borderwidth=1,relief='solid')
        presA_frame.grid(row=17,columnspan=7,sticky='w')
        tk.Label(presA_frame,text="PRESENT ADDRESS:",font=self.fonter,bg=self.color).pack(side='left',padx=10,pady=20)
        self.presA = tk.Text(presA_frame,font=self.fg_font,width=56,height = 3)
        self.presA.pack(side='left',padx=10,pady=10)
        
        tk.Label(frame_1,text="",bg=self.color).grid(row = 18)
        #permanent address
        self.equal = tk.IntVar()
        permaA_frame=tk.Frame(frame_1,bg=self.color,borderwidth=1,relief='solid')
        permaA_frame.grid(row=19,columnspan=7)
        tk.Label(permaA_frame,text="PERMANENT ADDRESS:",font=self.fonter,bg=self.color).pack(side='left',padx=10,pady=20)
        check_frame = tk.Frame(permaA_frame,bg=self.color)
        check_frame.pack(anchor='sw')
        self.permaA = tk.Text(permaA_frame,font=self.fg_font,width=53,height = 3)
        tk.Checkbutton(check_frame,variable=self.equal,font=self.fg_font,bg=self.color,text='Same as above address',command = self.same_address).pack()
        self.permaA.pack(side='left',padx=10,pady=10)
        
        tk.Label(frame_1,text="",bg=self.color).grid(row = 16)
#         #class 10 board name
#         xboard_frame=tk.Frame(frame_1,bg=self.color,borderwidth=1,relief='solid')
#         xboard_frame.grid(row=17,columnspan=2)
#         tk.Label(xboard_frame,text="CLASS X BOARD NAME:",font=self.fonter,bg=self.color).pack(side='left',padx=10,pady=20)
#         self.xboard_combo=ttk.Combobox(xboard_frame,value=board1,width=6,font=self.fg_font,state="readonly")
#         self.xboard_combo.pack(side='left')
#         tk.Label(xboard_frame,text="",bg=self.color).pack()
        
        
        #error
        self.error = tk.Label(self.canvas_form,fg = 'red',bg = self.color, text = '')
        self.canvas_form.create_window(500,self.length - 85, window = self.error )
        
        #submission button
        submit = tk.Button(self.canvas_form,text = 'Submit',bg = '#6AE16A',fg = 'black',font = self.fonter,bd = 2,command=self.execution)
        self.canvas_form.create_window(500,self.length - 50,window = submit)
        
    def execution(self):
        
        #name validation
        if not vld.name_validation(self.name.get()):
            self.error.config(text = 'Wrong input in "NAME"')
            return
        else:
            self.error.config(text = '')
        
        #father's name validation
        if not vld.name_validation(self.f_name.get()):
            self.error.config(text = 'Wrong input in "FATHER\'s NAME"')
            return
        else:
            self.error.config(text = '')
        
        #mother's name validation
        if not vld.name_validation(self.m_name.get()):
            self.error.config(text = 'Wrong input in "MOTHER\'s NAME"')
            return
        else:
            self.error.config(text = '')
        
        #dob validation
        if (self.dd_combo.get()=='DD' and self.mm_combo.get()=='MM' and self.yy_combo.get()=='YY'):
            self.error.config(text = 'Choose a valid "DOB"')
            return
        else:
            self.error.config(text = '')
        
        #gender validation
        if self.gender.get() == 0:
            self.error.config(text = 'Please select a option from "GENDER"')
            return
        else:
            self.error.config(text = '')
        
        #father's phone number validation
        if not vld.phone_number_validation(self.fph.get()[3:]):
            self.error.config(text = 'Wrong number in "FATHER\'S PHONE NUMBER"')
            return
        else:
            self.error.config(text = '')
        
        #mother's phone number validation
        if not vld.phone_number_validation(self.mph.get()[3:]):
            self.error.config(text = 'Wrong number in "MOTHER\'S PHONE NUMBER"')
            return
        else:
            self.error.config(text = '')
        
        #domicile validation
        if self.domicile_combo.get()=='':
            self.error.config(text = 'Choose a valid option from "DOMICILE"')
            return
        else:
            self.error.config(text = '')
        
        #department validation
        if self.dept_combo.get()=='':
            self.error.config(text = 'Choose a valid option from "DEPT"')
            return
        else:
            self.error.config(text = '')
        
        #email validation
        if not vld.email_validation(self.email.get()):
            self.error.config(text = 'Wrong input in "EMAIL"')
            return
        else:
            self.error.config(text = '')
        
        #address validation
        if elf.presA.get(1,'end') == '':
            self.error.config(text = 'Wrong input in "PRESENT ADDRESS"')
            return
        elif self.check.get() == 0 and self.permaA.get(1,'end') == '':
            self.error.config(text = 'Wrong input in "PERMANENT ADDRESS"')
            return
        else:
            self.error.config(text = '')
        
        #readying data to write
        dob = self.dd_combo.get() + '/' + self.mm_combo.get() + '/' + self.yy_combo.get()
        g = {1:'Male',2:'Female',3:'Others'}
        gender = g[self.gender.get()]
        permanent_address = ''
        if self.equal.get() == 1:
            permanent_address = self.presA.get(1,'end')
        else:
            permanent_address = self.permaA.get(1,'end')
        at_list = [self.name.get(), dob,self.f_name.get(), self.m_name.get(), gender, self.dept_combo.get(), self.domicile_combo.get(), self.mph.get(), self.fph.get(), self.email.get(), self.presA.get(1,'end'), permanent_address]
        
        #write to excel
        xls_append.save_xls_file(at_list,self.loc)
        
        self.dialogbox()
        
    def same_address(self):
        
        if self.equal.get() == 1:
                self.permaA.config(state='disabled',bg='#D3D3D3')
                self.permaA.delete(1,'end')
        else:
            self.permaA.config(state='normal',bg='white')
            
    def dialogbox(self):
        
        dbox = tk.Toplevel(self)
        dbox.geometry('300x100')
        dbox.title('Dialog Box')
        dbox.config(bg=self.color)
        tk.Label(dbox,text='Entry is saved',font=self.fonter,bg=self.color).pack(pady=10,padx=10)
        tk.Button(dbox,text='OK',font=self.fonter,bg='green').pack(pady=10,padx=10)

if __name__ == '__main__':
    
    root = tk.Tk()
    a = app(root)
    a.mainloop()
