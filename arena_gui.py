import tkinter as tk
from tkinter import messagebox
from page1_view import Page1View
from page2_view import Page2View
from bottom_navbar_view import BottomNavbarView
from top_navbar_view import TopNavbarView
from popup_view import PopupView
import requests
import json
class MainAppController(tk.Frame):
    """ Main Application for GUI """
    
    def __init__(self, parent):
        """ Initialize Main Application """
        tk.Frame.__init__(self, parent)        
        self._top_navbar = TopNavbarView(self, self._page_callback) #self._page_popup_callback)
        self._bottom_navbar = BottomNavbarView(self,self._refresh_callback)

        self._top_navbar.grid(row=0, columnspan=4, pady=10)
        self._bottom_navbar.grid(row=2, columnspan=4, pady=10)
        self._current_characters = {}
        self._page1 = Page1View(self,self._current_characters)
        self._page2 = Page2View(self,self._current_characters)
        self._page1.grid(row=1, columnspan=4, pady=10)
        self._curr_page = TopNavbarView.PAGE1
    def _page_callback(self):
        """ Handle Switching Between Pages """
        curr_page = self._top_navbar.curr_page.get()
        if (self._curr_page != curr_page and self._curr_page == TopNavbarView.PAGE1):
            self._page1.grid_forget()
            self._page2.grid(row=1, columnspan=4)
            self._curr_page = TopNavbarView.PAGE2
        elif (self._curr_page != curr_page and self._curr_page == TopNavbarView.PAGE2):
            self._page2.grid_forget()
            self._page1.grid(row=1, columnspan=4)
            self._curr_page = TopNavbarView.PAGE1

    def _refresh_callback(self):
        try:
            self._page1._list.delete(0,tk.END)
            self._page2._list.delete(0,tk.END)
            data = requests.get('http://127.0.0.1:5000/arena/characters/all').json()
            self._current_characters = {}
            for i in data:
                self._current_characters[i[1]] = i[0]
                index = i[1]
                i = i[0]
                if i['type'] == 'knight':
                    self._page1._list.insert(index,(i['username'],i['health'],i['attack'],i['defence'],i['attack_speed'],i['type'],i['sword_crit_chance'],i['sword_crit_modifier'],i['shield_defence_modifier']))
                elif i['type'] =='mage':
                    self._page2._list.insert(index,(i['username'],i['health'],i['attack'],i['defence'],i['attack_speed'],i['type'],i['spell_power'],i['spell_chance']))
        except:
            messagebox.showinfo('Error','Not connected to API!')
    def _delete_callback(self,selection):
        for chars in self._current_characters.items():
            if chars[1]['username'] == selection[0]:
                if messagebox.askyesno('Verify', 'Are you sure you want to delete this character?'):
                    requests.delete('http://127.0.0.1:5000/arena/characters/'+str(chars[0]))
    def get_id(self,selection):
        for chars in self._current_characters.items():
            if chars[1]['username'] == selection[0]:
                return(chars[0])
if __name__ == "__main__":
    root = tk.Tk()
    MainAppController(root).pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    root.mainloop()

