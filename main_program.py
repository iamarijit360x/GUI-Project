import tkinter as tk
from PIL import Image,ImageTk

class app(tk.Frame):
    
    def __init__(self, master = None):
        
        super().__init__()
        self.master = master
        self.master.geometry('900x700')
        self.master.title('Registration Form')
        self.master.resizable(0,0)
        self.pack()
        
        self.widget()
        
    def widget(self):
        
        #back canvas
        self.canvas_back = tk.Canvas(self,width = 900,height = 700,bg = 'black', bd = 0, highlightthickness = 0)
        self.canvas_back.pack()
        
        
        #top canvas
        self.canvas_top = tk.Canvas(self.canvas_back,width = 900,height = 353,bg = '#00004E', highlightbackground = 'black')
        self.canvas_back.create_window(450,50,window = self.canvas_top)
        
        
        #bottom scrollable canvas
        self.length = 700
        
        frame = tk.Frame(self.canvas_back,highlightthickness = 0)
        self.canvas_back.create_window(450,463,window = frame)
        
        self.canvas_main=tk.Canvas(frame,bg='#A8DADC',width=900,height=self.length,scrollregion=(0,0,self.length,self.length), bd = 0, highlightthickness = 0)
        self.canvas_main.pack(side='left',expand=True,fill='both')

        vbar=tk.Scrollbar(frame,orient='vertical')
        vbar.pack(side='right',fill='y')
        vbar.config(command=self.canvas_main.yview)
        self.canvas_main.config(width=880,height=467)
        self.canvas_main.config(yscrollcommand=vbar.set)
        self.scroll_binds()
        
        self.top_canvas_widget()
        self.bottom_canvas_widget()
        
    def top_canvas_widget(self):
        
        #logo
        logo = Image.open('assets/logo.png')
        logo = ImageTk.PhotoImage(logo)
        logo_label = tk.Label(self.canvas_top,image = logo,bg="#001a5c",bd=0)
        logo_label.image = logo
        logo_label.place(x =15,y =160)
        
        #heading
        college_name=tk.Label(self.canvas_top,text="St. Thomas' College of Engineering & Technology",bg='#00004E',fg='white',font=('Arial',20))
        college_name.place(x=240,y=180)
        details=tk.Label(self.canvas_top,text="4,Diamond Harbour Road, Kidderpore, Kolkata - 700023\n\nAll Programmes (B.Tech in CSE, EE, ECE & IT) are NBA Accredited.",bg='#00004E',fg='white',font=('Arial',15))
        details.place(x=240,y=240)
        
    def scroll_binds(self):
        
        def on_mousewheel(event):
            self.canvas_main.yview_scroll(int(-1*(event.delta/120)), "units")
    
        def bound_to_mousewheel(event):
            self.canvas_main.bind_all("<MouseWheel>", on_mousewheel)   

        def unbound_to_mousewheel(event):
            self.canvas_main.unbind_all("<MouseWheel>") 
            
        self.canvas_main.bind('<Enter>', bound_to_mousewheel)
        self.canvas_main.bind('<Leave>', unbound_to_mousewheel)
        
    def bottom_canvas_widget(self):
        
        #pallete canvas
        self.canvas_form = tk.Canvas(self.canvas_main,width = 870,height = self.length-30, bg = '#FFFFFF',highlightbackground = 'black', bd = 0)
        self.canvas_main.create_window(440,350,window = self.canvas_form)
        
        self.form()
        
    def form(self):
        pass

if __name__ == '__main__':
    
    root = tk.Tk()
    a = app(root)
    a.mainloop()