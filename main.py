import tkinter as tk
from tkinter import ttk

def get_entry(name):
    value = name.get()
    if value:
        print(value)



def new_window_1():
    new_window_1 = tk.Toplevel(win)
    new_window_1.geometry('700x400+300+150')
    # new_window_1.resizable(False,False)
    tk.Label(new_window_1,text='Ссылка',font=('Arial',14,'bold')).grid(row=0,column=0,stick='w')
    name = tk.Entry(new_window_1)
    tk.Button(new_window_1,text='Upload',command=lambda: get_entry(name)).grid(row=1,column=0)
    name.grid(row=0,column=1)
    width_frame = 150
    frame_add_table = tk.Frame(new_window_1, width= width_frame, height= 150, bg='green')


    frame_add_table.grid(row=3,column=0,pady=10, padx=10)
    new_window_1.grid_columnconfigure(0, minsize=100)
    new_window_1.grid_columnconfigure(1, minsize=200)
    

    # canvas=tk.Canvas(
    #     frame_add_table,
    #     bg='#4A7A8C',
    #     width=100,
    #     height=200,
    #     scrollregion=(0,0,700,700)
    #     )

    # vertibar=tk.Scrollbar(
    #     frame_add_table,
    #     orient=tk.VERTICAL
    #     )
    # vertibar.pack(side=tk.RIGHT,fill=tk.Y)
    # vertibar.config(command=canvas.yview)

    # horibar=tk.Scrollbar(
    #     frame_add_table,
    #     orient=tk.HORIZONTAL
    #     )
    # horibar.pack(side=tk.BOTTOM,fill=tk.X)
    # horibar.config(command=canvas.xview)

    # canvas.config(width=100,height=200)

    # canvas.config(
    #     xscrollcommand=horibar.set, 
    #     yscrollcommand=vertibar.set
    #     )
    # canvas.pack(expand=False,side=tk.LEFT,fill=tk.BOTH)




    # table_1 = tk.Canvas(frame_add_table, width=150,height=150,scrollregion=(0,0,150,150))
    # scroll_pane_1 = tk.Scrollbar(frame_add_table,orient='horizontal')
    # scroll_pane_1.pack(side=tk.BOTTOM, fill=tk.X)
    # scroll_pane_1.config(command=table_1.xview)

    # scroll_pane_2 = tk.Scrollbar(frame_add_table)
    # scroll_pane_2.pack(side=tk.RIGHT, fill=tk.Y)
    # scroll_pane_2.config(command=table_1.yview)

    # table_1.config(width=400,height=400)
    # table_1.config(xscrollcommand=scroll_pane_1.set, yscrollcommand=scroll_pane_2.set)

    # table_1.pack(expand=True,side=tk.LEFT,fill=tk.BOTH)

    lst = [(1,'Audi','Pete',19),
       (2,'BMW','Max',18),
       (3,'Vw','Pete',20),
       (4,'Mercedes','Kurt',21),
       (5,'Audi','Pete',23),
       (6,'Mercedes','Max',25),
       (7,'Audi','Pete',19),
       (8,'BMW','Max',20),
       (9,'Mercedes','Pete',30),
       (10,'BMW','Max',29),
       (11,'Audi','Pete',21),
       (12,'BMW','Max',18),
       (13,'Audi','Pete',19),
       (14,'BMW','Max',28),
       (15,'BMW','Max',35)]

    heads = ['id', 'model', 'owner', 'price']
    table = ttk.Treeview(frame_add_table, show ='headings',selectmode='extended')
    table['columns'] = heads
    for header in heads:
        table.heading(header,text=header,anchor='center')
        table.column(header,anchor='center',stretch=False, width=int(width_frame/len(heads)))
    for row in lst:
        table.insert('',tk.END, values=row)
    scroll_pane = tk.Scrollbar(frame_add_table,orient='horizontal', command=table.xview)
    scroll_pane.pack(side=tk.BOTTOM, fill=tk.X)

    scroll_pane_1 = tk.Scrollbar(frame_add_table,orient='vertical', command=table.yview)
    scroll_pane_1.pack(side=tk.RIGHT, fill=tk.Y)

    table.configure(xscrollcommand=scroll_pane.set, yscrollcommand=scroll_pane_1.set)
    table.pack(fill='x')








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
