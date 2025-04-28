import tkinter as tk
from tkinter import ttk,messagebox

class retaurantordermanagement:
    def __init__(self,root):
        self.root=root
        self.root.title('restaurant managememt app')
        self.menu_items={'fries meal':2,'lunch meal':2,'burger meal':3,'pizza meal':4,'cheese burger':2.5,'drinks':1}

        self.exchange_rate=82

        self.setup_background(root)

        frame=ttk.Frame(root)
        frame.place(relx=0.5,rely=0.5,anchor=tk.CENTER)

        ttk.Label(frame,text='restaurant order management ',font=('aerial',28,'hold')).grid(row=0,columnspan=3,padx=10,pady=10)

        self.menu_labels={}
        self.menu_quantities={}

        for i,(item,price) in enumerate(self.menu_labels.items(),start=1):
            label=ttk.Label(frame,text=f"(item) ($(price)):",font=("aerial",12))
            label.grid(row=1,column=0,padx=10,pady=5)
            self.menu_labels[item]=label

            quantity_entry=tk.Entry(frame,width=5)
            
