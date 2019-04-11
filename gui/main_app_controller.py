import tkinter as tk
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
        self._page1 = Page1View(self)
        self._page2 = Page2View(self)
        self._bottom_navbar = BottomNavbarView(self,self._refresh_callback)

        self._top_navbar.grid(row=0, columnspan=4, pady=10)
        self._page1.grid(row=1, columnspan=4, pady=10)
        self._curr_page = TopNavbarView.PAGE1
        self._bottom_navbar.grid(row=2, columnspan=4, pady=10)

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
        self._page1._list.delete(0,tk.END)
        self._page2._list.delete(0,tk.END)
        data = requests.get('http://127.0.0.1:5000/arena/characters/all').json()
        for i in data:
            if i['type'] == 'knight':
                self._page1._list.insert(data.index(i),(i['username'],i['health'],i['attack'],i['defence'],i['attack_speed'],i['type']))
            elif i['type'] =='mage':
                self._page2._list.insert(data.index(i),(i['username'],i['health'],i['attack'],i['defence'],i['attack_speed'],i['type']))


if __name__ == "__main__":
    root = tk.Tk()
    MainAppController(root).pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    root.mainloop()

