import tkinter as tk
from tkinter import messagebox
from popup_view import PopupView
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
        if messagebox.askyesno('Verify', 'Really delete?'):
            # this is where delete api is
            pass

    def _update_callback(self):
        selection = self._list.get(self._list.curselection())
        username=selection[0]
        health = selection[1]
        attack = selection[2]
        defence = selection[3]
        attackspeed = selection[4]
        type=selection[5]
        # get selection stuff from api call and pass into popup
        popup_win = tk.Toplevel()
        popup = PopupView(popup_win,username,health,attack,defence,attackspeed,type,True)

    def _create_callback(self):
        popup_win = tk.Toplevel()
        popup = PopupView(popup_win)
        #popup.tkraise(self._parent)

