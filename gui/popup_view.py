import tkinter as tk
from tkinter import messagebox
import json
import requests
class PopupView(tk.Frame):
    """ Popup Window """

    def __init__(self, parent,username='',health=0,attack=0,defence=0,attackspeed=0,chartype=None,
                 isUpdate=False,swordcritch=0,swordcritmod=0,shielddefmod=0,spellchance=0,spellpower=0,charid=0):
        """ Initialize the nav bar """
        tk.Frame.__init__(self, parent)
        # All types have these
        self._parent       = parent
        self._isUpdate     = isUpdate
        self._username     = username
        self._health       = health
        self._attack       = attack
        self._defence      = defence
        self._attackspeed  = attackspeed
        self._charid       = charid
        # Knight variables
        self._swordcritch  = swordcritch
        self._swordcritmod = swordcritmod
        self._shielddefmod =  shielddefmod

        # Mage variables
        self._spellchance  = spellchance
        self._spellpower   = spellpower

        self._type = 0
        if chartype == 'knight':
            self._type = 1
        elif chartype == 'mage':
            self._type = 2
        self._create_widgets()

    def _create_widgets(self):
        """ Creates the widgets for the nav bar """
        
        # All types have these
        username = tk.StringVar(value=self._username)
        health = tk.IntVar(value=self._health)
        attack = tk.IntVar(value=self._attack)
        defence = tk.IntVar(value=self._defence)
        attackspeed = tk.IntVar(value=self._attackspeed)
        
        # Knight variables
        self.swordcritchancevar = tk.IntVar(value=self._swordcritch)
        self.swordcritmodvar= tk.IntVar(value=self._swordcritmod)
        self.shielddefmodvar = tk.IntVar(value=self._shielddefmod)
        
        # Mage variables        
        self.spellpowervar = tk.IntVar(value=self._spellpower)
        self.spellchancevar = tk.IntVar(value=self._spellchance)


        self.typeInt = tk.IntVar(value=self._type)

        self.UsernameEntry = tk.Entry(self,textvariable=username)
        self.HealthEntry = tk.Entry(self,textvariable=health)
        self.AttackEntry = tk.Entry(self,textvariable=attack)
        self.DefenceEntry = tk.Entry(self,textvariable=defence)
        self.AttackSpeedEntry = tk.Entry(self,textvariable=attackspeed)

        self.SwordCriticalChanceEntry = tk.Entry(self,textvariable=self.swordcritchancevar)
        self.SwordCriticalModifierEntry = tk.Entry(self,textvariable=self.swordcritmodvar)
        self.ShieldDefenceModifierEntry = tk.Entry(self,textvariable=self.shielddefmodvar)
            
        self.CritChanceLabel = tk.Label(self,text='Critical Chance')
        self.CritModifierLabel = tk.Label(self,text='Critical Modifier')
        self.ShieldDefenceModifierLabel = tk.Label(self,text='Shield Defence Modifier')
        
        self.SpellPowerLabel = tk.Label(self,text='Spell Power')
        self.SpellChanceLabel = tk.Label(self,text='Spell Chance')


        self.SpellPowerEntry = tk.Entry(self,textvariable=self.spellpowervar)
        self.SpellChanceEntry = tk.Entry(self,textvariable=self.spellchancevar)

        if self._isUpdate:
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
        else:
            tk.Radiobutton(self,
                        text="Knight",
                        variable=self.typeInt,
                        value=1,
                        command=self._createtypewidgets
                        ).grid(row=6, column=1)
            tk.Radiobutton(self,
                        text="Mage",
                        variable=self.typeInt,
                        command=self._createtypewidgets,
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

        SubmitBtn.grid(row=11,column=1)
        self.pack()

    def submit(self):
        try:
            chartype = ''
            if self.typeInt.get() == 1:
                chartype = 'knight'
                character = {
                    "username": self.UsernameEntry.get(),
                    "health": int(self.HealthEntry.get()), 
                    "attack": int(self.AttackEntry.get()), 
                    "defence": int(self.DefenceEntry.get()), 
                    "attack_speed": int(self.AttackSpeedEntry.get()), 
                    "type": chartype,
                    "sword_crit_chance" : int(self.SwordCriticalChanceEntry.get()),
                    "sword_crit_modifier" : int(self.SwordCriticalModifierEntry.get()),
                    "shield_defence_modifier" : int(self.ShieldDefenceModifierEntry.get())
                }
                if self._isUpdate:
                    requests.put('http://127.0.0.1:5000/arena/characters/'+str(self._charid),json=character)
                else:
                    requests.post('http://127.0.0.1:5000/arena/characters',json=character)
                self._parent.destroy()
                
            elif self.typeInt.get() == 2:
                chartype = 'mage'
                character = {
                    "username": self.UsernameEntry.get(),
                    "health": int(self.HealthEntry.get()), 
                    "attack": int(self.AttackEntry.get()), 
                    "defence": int(self.DefenceEntry.get()), 
                    "attack_speed": int(self.AttackSpeedEntry.get()), 
                    "type": chartype,
                    'spell_power' : int(self.SpellPowerEntry.get()),
                    'spell_chance' : int(self.SpellChanceEntry.get())
                }
                if self._isUpdate:
                    requests.put('http://127.0.0.1:5000/arena/characters/'+str(self._charid),json=character)
                else:
                    requests.post('http://127.0.0.1:5000/arena/characters',json=character)
                self._parent.destroy()
        except:
            messagebox.showinfo('Error','Invalid info')
            self._parent.destroy()

    def _createtypewidgets(self):
        if self.typeInt.get() == 1:
            if self.SpellPowerEntry.winfo_exists() == 1 or self.SpellChanceEntry.winfo_exists() == 1:
                self.SpellPowerEntry.destroy()
                self.SpellChanceEntry.destroy()
                self.SpellChanceLabel.destroy()
                self.SpellPowerLabel.destroy()


            self.SwordCriticalChanceEntry = tk.Entry(self,textvariable=self.swordcritchancevar)
            self.SwordCriticalModifierEntry = tk.Entry(self,textvariable=self.swordcritmodvar)
            self.ShieldDefenceModifierEntry = tk.Entry(self,textvariable=self.shielddefmodvar)
            self.CritChanceLabel = tk.Label(self,text='Critical Chance')
            self.CritModifierLabel = tk.Label(self,text='Critical Modifier')
            self.ShieldDefenceModifierLabel = tk.Label(self,text='Shield Defence Modifier')
        


            self.SwordCriticalChanceEntry.grid(row=8,column=2)
            self.CritChanceLabel.grid(row=8,column=1)

            self.SwordCriticalModifierEntry.grid(row=9,column=2)
            self.CritModifierLabel.grid(row=9,column=1)

            self.ShieldDefenceModifierEntry.grid(row=10,column=2)
            self.ShieldDefenceModifierLabel.grid(row=10,column=1)

        elif self.typeInt.get() == 2:   
            if self.SwordCriticalChanceEntry.winfo_exists() == 1 or self.SwordCriticalModifierEntry.winfo_exists() == 1 or self.ShieldDefenceModifierEntry.winfo_exists() == 1:
                self.ShieldDefenceModifierEntry.destroy()
                self.SwordCriticalChanceEntry.destroy()
                self.SwordCriticalModifierEntry.destroy()
                self.CritChanceLabel.destroy()
                self.CritModifierLabel.destroy()
                self.ShieldDefenceModifierLabel.destroy()


            self.SpellPowerLabel = tk.Label(self,text='Spell Power')
            self.SpellChanceLabel = tk.Label(self,text='Spell Chance')
            self.SpellPowerEntry = tk.Entry(self,textvariable=self.spellpowervar)
            self.SpellChanceEntry = tk.Entry(self,textvariable=self.spellchancevar)


            self.SpellPowerEntry.grid(row=8,column=2)
            self.SpellPowerLabel.grid(row=8,column=1)

            self.SpellChanceEntry.grid(row=9,column=2)
            self.SpellChanceLabel.grid(row=9,column=1)