import tkinter as tk
from PIL import Image,ImageTk

class app(tk.Frame):
    
    def __init__(self, master = None):
        
        super().__init__()
        self.master = master
        self.master.geometry('900x700')
        self.master.resizable(0,0)
        self.pack()
        
        self.widget()
        
    def widget(self):
        
        #back canvas
        self.canvas_back = tk.Canvas(self,width = 900,height = 700,bg = 'white')
        self.canvas_back.pack()
        
        
        #top canvas
        self.canvas_top = tk.Canvas(self.canvas_back,width = 900,height = 353,bg = '#00004E')
        self.canvas_back.create_window(450,50,window = self.canvas_top)
        
        
        #bottom scrollable canvas
        length = 700
        
        frame = tk.Frame(self.canvas_back)
        self.canvas_back.create_window(450,458,window = frame)
        
        self.canvas_main=tk.Canvas(frame,bg='red',width=900,height=length,scrollregion=(0,0,length,length))
        self.canvas_main.pack(side='left',expand=True,fill='both')

        vbar=tk.Scrollbar(frame,orient='vertical')
        vbar.pack(side='right',fill='y')
        vbar.config(command=self.canvas_main.yview)
        self.canvas_main.config(width=880,height=480)
        self.canvas_main.config(yscrollcommand=vbar.set)
        self.scroll_binds()
        
        self.top_canvas_widget()
        
    def top_canvas_widget(self):
        
        #logo
        logo = Image.open('assets/logo.png')
        logo = ImageTk.PhotoImage(logo)
        logo_label = tk.Label(self.canvas_top,image = logo,bg="#001a5c",bd=0)
        logo_label.image = logo
        logo_label.place(x =15,y =147)
        
    def scroll_binds(self):
        
        def on_mousewheel(event):
            self.canvas_main.yview_scroll(int(-1*(event.delta/120)), "units")
    
        def bound_to_mousewheel(event):
            self.canvas_main.bind_all("<MouseWheel>", on_mousewheel)   

        def unbound_to_mousewheel(event):
            self.canvas_main.unbind_all("<MouseWheel>") 
            
        self.canvas_main.bind('<Enter>', bound_to_mousewheel)
        self.canvas_main.bind('<Leave>', unbound_to_mousewheel)
            
if __name__ == '__main__':
    
    root = tk.Tk()
    a = app(root)
    a.mainloop()