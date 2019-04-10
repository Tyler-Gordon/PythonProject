import tkinter as tk


class Page2View(tk.Frame):
    """ Page 2 """

    def __init__(self, parent):
        """ Initialize Page 1 """
        tk.Frame.__init__(self, parent, width=800, height=800)

        self._parent = parent

        self._create_widgets()

    def _create_widgets(self):
        """ Creates the widgets for Page 2 """
        self._list = tk.Listbox(self)
        self._list.grid(row=0,column=1)

        DeleteBtn = tk.Button(self,text='Delete',command=self._delete_callback)
        UpdateBtn = tk.Button(self,text='Update',command=self._update_callback)
        CreateBtn = tk.Button(self,text='Create',command=self._create_callback)

        DeleteBtn.grid(row=1,column=1)
        UpdateBtn.grid(row=2,column=1)
        CreateBtn.grid(row=3,column=1)

    def _delete_callback(self):
        selection = self._list.get(self._list.curselection())
        pass
    def _update_callback(self):
        selection = self._list.get(self._list.curselection())
        pass
    def _create_callback(self):
        pass


