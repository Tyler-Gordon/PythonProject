import tkinter as tk


class BottomNavbarView(tk.Frame):
    """ Navigation Bar """

    def __init__(self, parent, refresh_callback):
        """ Initialize the nav bar """
        tk.Frame.__init__(self, parent)
        self._parent = parent

        self._refresh_callback = refresh_callback
        self._create_widgets()

    def _create_widgets(self):
        self._refresh_button = tk.Button(self,
                                text='REFRESH',
                                fg='green',
                                command=self._refresh_callback)
        self._quit_button = tk.Button(self,
                                text='QUIT',
                                fg='red',
                                command=self.quit)

        self._refresh_button.grid(row=2,column=1)
        self._quit_button.grid(row=2,column=2)