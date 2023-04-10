import tkinter as tk
from tkinter import ttk
import pandas as pd

class Win_Table():
    def __init__(self,window):
        self.Label_1 = tk.Label(window,text='Ссылка',font=('Arial',14,'bold')).grid(row=0,column=0,stick='w')
        self.entry_1 = tk.Entry(window)
        self.button_1 = tk.Button(window,text='Upload')

        self.entry_1.grid(row=0,column=1)
        self.button_1.grid(row=1,column=0)

        self.button_1.bind("<Button-1>",self.__answer)

        self.width_frame = 200
        self.height_frame = 300
        self.frame_add_table = tk.Frame(window, width=self.width_frame, height=self.height_frame)
        self.frame_add_table.grid(row=3,column=0,pady=10, padx=10)
        self.frame_add_table.propagate(0)       # размеры Frame неизменяемые, таблица не будет расширяться за пределы окна

    def hide_all_frames(self):          # очищает страницу перед записью новых виджетов
        for widget in self.frame_add_table.winfo_children():
            widget.destroy()

    def __answer(self, event):
        self.hide_all_frames()
        heads = []
        txt = self.entry_1.get()
        df = pd.read_csv(txt)
        for col in df.columns:
            heads.append(col)

        table = ttk.Treeview(self.frame_add_table, show ='headings',height=self.height_frame)
        table['columns'] = heads
        for header in heads:
            table.heading(header,text=header,anchor='center')
            table.column(header,anchor='center',stretch=False)
        for row in df.values:
            row = tuple(row)
            table.insert('',tk.END, values=row)

        scroll_pane = tk.Scrollbar(self.frame_add_table,orient='horizontal', command=table.xview)
        scroll_pane.pack(side=tk.BOTTOM, fill=tk.X)

        scroll_pane_1 = tk.Scrollbar(self.frame_add_table,orient='vertical', command=table.yview)
        scroll_pane_1.pack(side=tk.RIGHT, fill=tk.Y)
        table.configure(xscrollcommand=scroll_pane.set, yscrollcommand=scroll_pane_1.set)
        table.pack(fill=tk.Y)
                

        

def get_entry(name):
    value = name.get()
    if value:
        print(value)



def new_window_1():
    new_window_1 = tk.Toplevel(win)
    new_window_1.geometry('700x400+300+150')
    table = Win_Table(new_window_1)








win = tk.Tk()
win.title('График')

win.geometry('700x400+300+150')
win.resizable(False,False)

label_1 = tk.Label(win, text='Выберите DataFrame',
                   font=('Arial',20,'bold'),
                   justify=tk.CENTER)




btn1 = tk.Button(win, text = 'Suicide rates',
                 font=('Arial',20,'bold'), 
                 width=20,)

btn2 = tk.Button(win, text = 'Movie analysis',
                 font=('Arial',20,'bold'), 
                 width=20,
                 )

btn3 = tk.Button(win, text = 'Upload a DataFrame',
                 font=('Arial',20,'bold'),
                 width=20, 
                 command= new_window_1)



label_1.pack()
btn1.pack(pady=10)
btn2.pack(pady=10)
btn3.pack(pady=10)

win.mainloop()
