import tkinter as tk
from tkinter import ttk


class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()

    def init_main(self):
        #Создание кнопки сверху
        toolbar = tk.Frame(bg='#d7d8e0', bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)
        # self.add_img = tk.PhotoImage(file='add.gif') Пикча по адресу file
        btn_open_dialog = tk.Button(toolbar, text='asd', command=self.open_child, bg='#d7d8e0', bd=0,
                                    compound=tk.TOP)#Расположение кнопки и её действие
        btn_open_dialog.pack(side=tk.LEFT)#Диалоговое окно слева

        self.tree = ttk.Treeview(self, columns=('ID', 'description', 'costs', 'total'), height=15, show='headings')
    #Разметка колонок в мэйн файле
        self.tree.column('ID', width=30, anchor=tk.CENTER)
        self.tree.column('description', width=360, anchor=tk.CENTER)
        self.tree.column('costs', width=150, anchor=tk.CENTER)
        self.tree.column('total', width=100, anchor=tk.CENTER)
#Надписи на колонках
        self.tree.heading('ID', text='ID')
        self.tree.heading('description', text='Наименование')
        self.tree.heading('costs', text='Статья дохода/расхода')
        self.tree.heading('total', text='Сумма')

        self.tree.pack()
    def open_child(self):
        Child()
class Child(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()
# Диалоговое окно, его заголовок и размеры
    def init_child(self):
        self.title('qwe')
        self.geometry('400x220+400+300')
        self.resizable(False, False)
#Названия и расположение названий полей в диалоговом окне
        label_decription = ttk.Label(self, text='Наименование:')
        label_decription.place(x=50, y=50)
        label_select = ttk.Label(self, text='Статья дохода/расхода:')
        label_select.place(x=50, y=80)
        label_sum = ttk.Label(self, text='Наименование')
        label_sum.place(x=50, y=110)
#Поля в диалоговом окне и их значения(пусто или выбор из доход/расход)
        self.entry_description = ttk.Entry(self)
        self.entry_description.place(x=200, y=50)

        self.entry_money = ttk.Entry(self)
        self.entry_money.place(x=200, y=110)

        self.combobox = ttk.Combobox(self, values=[u'Доход', u'Расход'])
        self.combobox.current(0)
        self.combobox.place(x=200, y=80)
#Названия и расположение кнопок в диалоговом окне
        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=300, y=170)

        btn_add = ttk.Button(self, text='Добавить')
        btn_add.place(x=220, y=170)
        btn_add.bind('<Button-1>')


        self.grab_set()
        self.focus_set()


if __name__ == '__main__':
    root =tk.Tk()
    app = Main(root)
    app.pack()
    root.title('visual window')
    root.geometry('650x450+300+200')
    root.resizable(False, False)
    root.mainloop()
