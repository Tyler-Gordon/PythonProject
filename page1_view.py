import tkinter as tk
from popup_view import PopupView
from tkinter import messagebox
class Page1View(tk.Frame):
    """ Page 1 """

    def __init__(self, parent,current_characters):
        """ Initialize Page 1 """
        tk.Frame.__init__(self, parent, width=800, height=800)

        self._parent = parent
        self._create_widgets()
        
    def _create_widgets(self):
        """ Creates the widgets for Page 1 """
        self._list = tk.Listbox(self)

        self._list.bind("<Double-Button-1>",self._get_info)

        self._list.grid(row=0,column=1)
        DeleteBtn = tk.Button(self,text='Delete',command=self._delete_callback)
        UpdateBtn = tk.Button(self,text='Update',command=self._update_callback)
        CreateBtn = tk.Button(self,text='Create',command=self._create_callback)

        DeleteBtn.grid(row=1,column=1)
        UpdateBtn.grid(row=2,column=1)
        CreateBtn.grid(row=3,column=1)

    def _delete_callback(self):
        try:
            selection = self._list.get(self._list.curselection())    
            self._parent._delete_callback(selection)
        
        except:
            messagebox.showinfo('Error!','Select a character to delete!')

    def _update_callback(self):
        try:
            selection = self._list.get(self._list.curselection())
            username=selection[0]
            health = selection[1]
            attack = selection[2]
            defence = selection[3]
            attackspeed = selection[4]
            type=selection[5]
            popup_win = tk.Toplevel()
            charid = self._parent.get_id(selection)
            popup = PopupView(popup_win,username,health,attack,defence,attackspeed,type,True,charid=charid)
        except:
            messagebox.showinfo('Error!','Select a character to update!')

    def _create_callback(self):
        popup_win = tk.Toplevel()
        popup = PopupView(popup_win,isUpdate=False)

    def _get_info(self,event):
        try:
            selection = self._list.get(self._list.curselection())
            username=selection[0]
            health = selection[1]
            attack = selection[2]
            defence = selection[3]
            attackspeed = selection[4]
            type=selection[5]

            if type == 'knight':
                sword_crit_chance = selection[6]
                sword_crit_modifier = selection[7]
                shield_def_mod = selection[8]
                messagebox.showinfo('Character',("Username: {}\n Health: {}\n Attack: {}\n Defence: {}\n Atttack Speed: {}\n Type: {}\n Sword Crit Chance: {}\n Sword Crit Modifier: {}\n Shield Defence Modifier: {}\n".format(username,health,attack,defence,attackspeed,type,sword_crit_chance,sword_crit_modifier,shield_def_mod)))
            elif type == 'mage':
                spell_power = selection[6]
                spell_chance = selection[7]
                messagebox.showinfo('Character',("Username: {}\n Health: {}\n Attack: {}\n Defence: {}\n Atttack Speed: {}\n Type: {}\n Spell Chance: {}\n Spell Power: {}\n".format(username,health,attack,defence,attackspeed,type,spell_chance,spell_power)))
        except:
            messagebox.showinfo('Error', 'Please select a character to view')