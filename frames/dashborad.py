from tkinter import *
from tkinter import ttk
import tkinter as tk
from classes.addressbook import AddressBook


class dashboardFrame:
	def __init__(self, root):
		self.ad = AddressBook()
		self.dashboard = ttk.Frame(root, padding=10)
		self.root = root
		self.entries = []
		self.selectedId = None
		self.tree = ttk.Treeview(self.dashboard, columns=('id','nom', 'email', 'phone', 'date', 'modify'), show='headings')

	def updateTable(self):
		self.tree.delete(*self.tree.get_children())

		for contact in self.ad.list:
			values = (contact['id'],contact['nom'], contact['email'], contact['phone'], contact['addedTime'], contact['lastTimeEdited'])
			self.tree.insert('', tk.END, values=values)

	def clearentries(self):
		global selectedId
		selectedId = None
		
		for entry in self.entries:
			entry.delete(0, tk.END)
		self.updateTable()

	def addcontact(self):
		self.ad.add(self.entries[0].get(),self.entries[1].get(),self.entries[2].get())
		self.clearentries()

	def deletecontact(self):
		if (selectedId is not None):
			self.ad.delete(selectedId)
			self.clearentries()

	def modifier(self):
		if (selectedId is not None):
			self.ad.modifier(selectedId, self.entries[0].get(),self.entries[1].get(),self.entries[2].get())
			self.clearentries()

	def select_item(self,event):
		selected_items = self.tree.selection()
		if selected_items:
			item_id = selected_items[0]
			item_data = self.tree.item(item_id)['values']

			self.clearentries()

			global selectedId
			selectedId = item_data[0]

			self.entries[0].insert(0, item_data[1])
			self.entries[1].insert(0, item_data[2])
			self.entries[2].insert(0, item_data[3])

	def on_key_release(self,event):
		current_text = event.widget.get()
		if current_text == '':
			self.updateTable()
		else:
			data = self.ad.list
			self.tree.delete(*self.tree.get_children())
			for contact in data:
				if (contact['nom'].startswith(current_text)):
					values = (contact['id'],contact['nom'], contact['email'], contact['phone'])
					self.tree.insert('', tk.END, values=values)

	def build(self):
		self.dashboard.grid()
		self.root.title("Tableau de board")
		# Adding text Areas
		ttk.Label(self.dashboard, text="Nom complet").grid(column=0, row=0, sticky=tk.W)
		ttk.Label(self.dashboard, text="E-mail").grid(column=0, row=1,sticky=tk.W)
		ttk.Label(self.dashboard, text="Telephone").grid(column=0, row=2,sticky=tk.W)

		self.entries.append(ttk.Entry(self.dashboard))
		self.entries.append(ttk.Entry(self.dashboard))
		self.entries.append(ttk.Entry(self.dashboard))

		self.entries[0].grid(column=1, row=0, padx=10, pady=5)
		self.entries[1].grid(column=1, row=1, padx=10, pady=5)
		self.entries[2].grid(column=1, row=2, padx=10, pady=5)

		# Adding buttons to control
		ttk.Button(self.dashboard, text="Ajouter Contact", command=self.addcontact).grid(column=0, row=3, pady=5)
		ttk.Button(self.dashboard, text="Supprimer Contact", command=self.deletecontact).grid(column=1, row=3, pady=5)
		ttk.Button(self.dashboard, text="Modifier", command=self.modifier).grid(column=2, row=3, pady=5)

		ttk.Label(self.dashboard, text="Recherche par Nom:").grid(column=0, row=4,sticky=tk.W)
		self.entries.append(ttk.Entry(self.dashboard))
		self.entries[3].grid(row=5, column=0, sticky='we', padx=10, pady=10,columnspan="3")
		self.entries[3].bind("<KeyRelease>", self.on_key_release)

		self.tree.heading('nom', text='Nom complet')
		self.tree.heading('email', text='E-mail')
		self.tree.heading('phone', text='Telephone')
		self.tree.heading('date', text='Date de creation')
		self.tree.heading('modify', text='Dernier Date de modification')

		self.tree.column("id", width=0, minwidth=0, stretch=tk.NO)
		self.tree.column('nom', width=100, anchor=tk.W)
		self.tree.column('nom', width=100, anchor=tk.W)
		self.tree.column('email', width=100, anchor=tk.W)
		self.tree.column('date', width=200, anchor=tk.W)
		self.tree.column('modify', width=200, anchor=tk.W)
		self.tree.grid(row=6,column=0, columnspan=3)
		self.tree.bind("<<TreeviewSelect>>", self.select_item)
		self.updateTable()