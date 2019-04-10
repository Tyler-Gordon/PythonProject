import tkinter as tk
from tkinter import messagebox as tkMessageBox
import json

class PopupView(tk.Frame):
    """ Popup Window """

    def __init__(self, parent,username='',health='',attack='',defence='',attackspeed='',chartype=None,isUpdate=False):
        """ Initialize the nav bar """
        tk.Frame.__init__(self, parent)
        self._parent = parent
        self._isUpdate = isUpdate
        self._username = username
        self._health = health
        self._attack = attack
        self._defence = defence
        self._attackspeed = attackspeed
        self._type = chartype

        self._create_widgets()

    def _create_widgets(self):
        """ Creates the widgets for the nav bar """
        username = tk.StringVar(value=self._username)
        health = tk.StringVar(value=self._health)
        attack = tk.StringVar(value=self._attack)
        defence = tk.StringVar(value=self._defence)
        attackspeed = tk.StringVar(value=self._attackspeed)
        self.typeInt = tk.IntVar(value=self._type)

        self.UsernameEntry = tk.Entry(self,textvariable=username)
        self.HealthEntry = tk.Entry(self,textvariable=health)
        self.AttackEntry = tk.Entry(self,textvariable=attack)
        self.DefenceEntry = tk.Entry(self,textvariable=defence)
        self.AttackSpeedEntry = tk.Entry(self,textvariable=attackspeed)
        
        if self._isUpdate:
            tk.Radiobutton(self,
                        text="Knight",
                        variable=self.typeInt,
                        value=1).grid(row=6, column=1)

            tk.Radiobutton(self,
                        text="Mage",
                        variable=self.typeInt,
                        value=2).grid(row=6, column=2)
        else:
            tk.Radiobutton(self,
                        text="Knight",
                        variable=self.typeInt,
                        state=tk.DISABLED,
                        value=1).grid(row=6, column=1)

            tk.Radiobutton(self,
                        text="Mage",
                        variable=self.typeInt,
                        state=tk.DISABLED,
                        value=2).grid(row=6, column=2)            

        SubmitBtn = tk.Button(self,text='Submit',command=self.submit)

        self.UsernameEntry.grid(row=1,column=2)
        UsernameLabel = tk.Label(self,text='Username')
        UsernameLabel.grid(row=1,column=1)

        self.HealthEntry.grid(row=2,column=2)
        HealthLabel = tk.Label(self,text='Health')
        HealthLabel.grid(row=2,column=1)

        self.AttackEntry.grid(row=3,column=2)
        AttackLabel = tk.Label(self,text='Attack')
        AttackLabel.grid(row=3,column=1)

        self.DefenceEntry.grid(row=4,column=2)
        DefenceLabel = tk.Label(self,text='Defence')
        DefenceLabel.grid(row=4,column=1)

        self.AttackSpeedEntry.grid(row=5,column=2)
        AttackSpeedLabel = tk.Label(self,text='Attack Speed')
        AttackSpeedLabel.grid(row=5,column=1)

        SubmitBtn.grid(row=7,column=1)
        print('Created all widgets')
        self.pack()

    def submit(self):

        print(self.typeInt.get())