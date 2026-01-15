from tkinter import *
from tkinter import ttk
import tkinter as tk

class authForm:
	def __init__(self, root):
		self.auth = ttk.Frame(root,padding=10)
		self.entries = []
		self.root = root
	
	def build(self):
		self.root.title("Authentification")
		self.auth.grid()
		ttk.Label(self.auth, text="E-mail").grid(column=0, row=0, sticky=tk.W)
		self.entries.append(ttk.Entry(self.auth))
		ttk.Label(self.auth, text="Mot de pass").grid(column=0, row=2, sticky=tk.W)
		self.entries.append(ttk.Entry(self.auth, show="*"))
		self.entries[0].grid(column=0, row=1, padx=10, pady=10, columnspan=2)
		self.entries[1].grid(column=0, row=3, padx=10, pady=10, columnspan=2)

		ttk.Button(self.auth, text="Se connecter").grid(column=0, row=5, padx=10)
		ttk.Button(self.auth, text="Creer un compte").grid(column=1, row=5, padx=10)

