import tkinter as tk
from tkinter import ttk
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class Win_Table():
    def __init__(self,window):
        self.Label_1 = tk.Label(window,text='Ссылка',font=('Arial',14,'bold')).grid(row=0,column=0,stick='w')
        self.entry_1 = tk.Entry(window)
        self.button_1 = tk.Button(window,text='Upload',command=lambda:[self.__table(),self.__combobox()])
        self.entry_1.grid(row=0,column=1)
        self.button_1.grid(row=1,column=0)

        self.flag = 0

        # self.button_1.bind("<Button-1>",self.__table)

        self.width_frame = 200
        self.height_frame = 300
        self.frame_add_table = tk.Frame(window, width=self.width_frame, height=self.height_frame,bg='green')
        self.frame_add_combobox = tk.Frame(window, width=self.width_frame, height=205)
        self.frame_add_chart = tk.Frame(window, width=685, height=480,bg='green',highlightbackground="black", highlightthickness=1)

        
        self.frame_add_table.grid(row=2,column=0,padx=10, pady=10)
        self.frame_add_table.pack_propagate(0)       # размеры Frame неизменяемые, таблица не будет расширяться за пределы окна

        self.frame_add_combobox.grid(row=3,column=0,pady=8, padx=10)
        self.frame_add_combobox.pack_propagate(0)
        
        self.frame_add_chart.grid(row=2,column=1,rowspan=2,padx=30,pady=10)
        self.frame_add_chart.pack_propagate(0)

        self.heads = []
        self.plots = ['Line graph','Bar chart', 'Scatterplot']

    def hide_table_frame(self):          # очищает страницу перед записью новых виджетов
        for widget in self.frame_add_table.winfo_children():
            widget.destroy()

    def hide_combobox_frame(self):          # очищает страницу перед записью новых виджетов
        for widget in self.frame_add_combobox.winfo_children():
            widget.destroy()

    def hide_chart_frame(self):          # очищает страницу перед записью новых виджетов
        for widget in self.frame_add_chart.winfo_children():
            widget.destroy()


    def check_label(self, head):
        for i in range(len(self.heads)):
            if head == self.heads[i]:
                x = i
        return x




    def __table(self):
        self.hide_table_frame()
        self.heads = []
        txt = self.entry_1.get()
        df = pd.read_csv(txt)
        self.df_values = df.values
        
        for col in df.columns:
            self.heads.append(col)
        
        table = ttk.Treeview(self.frame_add_table, show ='headings',height=self.height_frame)
        table['columns'] = self.heads
        for header in self.heads:
            table.heading(header,text=header,anchor='center')
            table.column(header,anchor='center',stretch=False)
        for row in self.df_values:
            row = tuple(row)
            table.insert('',tk.END, values=row)

        scroll_pane = tk.Scrollbar(self.frame_add_table,orient='horizontal', command=table.xview)
        scroll_pane.pack(side=tk.BOTTOM, fill=tk.X)

        scroll_pane_1 = tk.Scrollbar(self.frame_add_table,orient='vertical', command=table.yview)
        scroll_pane_1.pack(side=tk.RIGHT, fill=tk.Y)
        table.configure(xscrollcommand=scroll_pane.set, yscrollcommand=scroll_pane_1.set)
        table.pack(fill=tk.Y)
                
    def __combobox(self):
        self.hide_combobox_frame()
        self.frame_add_combobox.config(highlightbackground="grey", highlightthickness=1)
        label_1 = tk.Label(self.frame_add_combobox,text='Значение x:',font=('Arial',10,'bold'))
        self.combobox_1 = ttk.Combobox(self.frame_add_combobox,values=self.heads)
        label_2 = tk.Label(self.frame_add_combobox,text='Значение y:',font=('Arial',10,'bold'))
        self.combobox_2 = ttk.Combobox(self.frame_add_combobox,values=self.heads)
        label_3 = tk.Label(self.frame_add_combobox,text='Выбор графика:',font=('Arial',10,'bold'))
        self.combobox_3 = ttk.Combobox(self.frame_add_combobox,values=self.plots)
        button_1 = tk.Button(self.frame_add_combobox,text='Ввод', command=lambda: self.__chart())
        # if self.flag == 1:
        #     self.button_1.config(command=self.__chart())
        # else:
        #     self.flag = 1

        label_1.pack(pady=(20,0))
        self.combobox_1.pack()
        label_2.pack(pady=(5,0))
        self.combobox_2.pack()
        label_3.pack(pady=(5,0))
        self.combobox_3.pack()
        button_1.pack(pady=(5,0))
        
    def __chart(self):
        self.hide_chart_frame()
        self.X = []
        self.Y = []
        txt_1 = self.combobox_1.get()
        txt_2 = self.combobox_2.get()
        txt_3 = self.combobox_3.get()

        x_ind = self.check_label(txt_1) 
        y_ind = self.check_label(txt_2)
        

        for row in self.df_values:
            row = tuple(row)
            self.X.append(row[x_ind])

        for row in self.df_values:
            row = tuple(row)
            self.Y.append(row[y_ind])

        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)

        canvas = FigureCanvasTkAgg(self.figure, self.frame_add_chart)
        canvas.get_tk_widget().pack(fill=tk.BOTH)
        if txt_3 == 'Line graph':
            self.axes.plot(self.X,self.Y)
        
        elif txt_3 == 'Scatterplot':
            self.axes.scatter(self.X,self.Y)
        
        elif txt_3 == 'Bar chart':
            self.axes.hist(self.X)



def new_window_1():
    new_window_1 = tk.Toplevel(win)
    new_window_1.geometry('1000x600+300+100')
    widgets_1 = Win_Table(new_window_1)





win = tk.Tk()
win.title('График')

win.geometry('1000x600+300+100')
win.resizable(False,False)

label_1 = tk.Label(win, text='Выберите DataFrame',
                   font=('Arial',24,'bold'),
                   justify=tk.CENTER)




btn1 = tk.Button(win, text = 'Suicide rates',
                 font=('Arial',24,'bold'), 
                 width=20,)

btn2 = tk.Button(win, text = 'Movie analysis',
                 font=('Arial',24,'bold'), 
                 width=20,
                 )

btn3 = tk.Button(win, text = 'Upload a DataFrame',
                 font=('Arial',24,'bold'),
                 width=20, 
                 command= new_window_1)



label_1.pack()
btn1.pack(pady=50)
btn2.pack(pady=50)
btn3.pack(pady=50)

win.mainloop()
