import tkinter as tk


class TopNavbarView(tk.Frame):
    """ Navigation Bar """

    PAGE1 = 1
    PAGE2 = 2

    def __init__(self, parent, page_callback):
        """ Initialize the nav bar """
        tk.Frame.__init__(self, parent)
        self._parent = parent

        self._page_callback = page_callback

        self._page = tk.IntVar()
        self._create_widgets()

    def _create_widgets(self):
        """ Creates the widgets for the nav bar """
        tk.Label(self,
                 text="Select Type:").grid(row=0, column=0)

        self.curr_page = tk.IntVar()

        tk.Radiobutton(self,
                       text="Knight",
                       variable=self.curr_page,
                       command=self._page_callback,
                       value=TopNavbarView.PAGE1).grid(row=0, column=1)

        tk.Radiobutton(self,
                       text="Mage",
                       variable=self.curr_page,
                       command=self._page_callback,
                       value=TopNavbarView.PAGE2).grid(row=0, column=2)

        self.curr_page.set(TopNavbarView.PAGE1)

        self._page.set(1)

