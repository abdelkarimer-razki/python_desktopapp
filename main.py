from classes.addressbook import AddressBook
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk

ad = AddressBook()
entries = []
selectedId = None

root = Tk()
root.title("Address Book")

def addcontact():
	ad.add(entries[0].get(),entries[1].get(),entries[2].get())
	clearEntries()
	updateTable()

def clearEntries():
	global selectedId
	selectedId = None
	
	for entry in entries:
		entry.delete(0, tk.END)


def deletecontact():
	if (selectedId is not None):
		ad.delete(selectedId)
		updateTable()
		clearEntries()

def modifier():
	if (selectedId is not None):
		ad.modifier(selectedId, entries[0].get(),entries[1].get(),entries[2].get())
		clearEntries()
		updateTable()

def updateTable():
	tree.delete(*tree.get_children())

	for contact in ad.list:
		values = (contact['id'],contact['nom'], contact['email'], contact['phone'])
		tree.insert('', tk.END, values=values)

def select_item(event):
	selected_items = tree.selection()
	if selected_items:
		item_id = selected_items[0]
		item_data = tree.item(item_id)['values']

		clearEntries()

		global selectedId
		selectedId = item_data[0]

		entries[0].insert(0, item_data[1])
		entries[1].insert(0, item_data[2])
		entries[2].insert(0, item_data[3])



# Adding a frame to the root window
frm = ttk.Frame(root, padding=10)
frm.grid()

# Adding text Areas
ttk.Label(frm, text="Nom complet").grid(column=0, row=0, sticky=tk.W)
ttk.Label(frm, text="E-mail").grid(column=0, row=1,sticky=tk.W)
ttk.Label(frm, text="Telephone").grid(column=0, row=2,sticky=tk.W)

entries.append(ttk.Entry(frm))
entries.append(ttk.Entry(frm))
entries.append(ttk.Entry(frm))

entries[0].grid(column=1, row=0, padx=10, pady=5)
entries[1].grid(column=1, row=1, padx=10, pady=5)
entries[2].grid(column=1, row=2, padx=10, pady=5)

# Adding buttons to control
ttk.Button(frm, text="Ajouter Contact", command=addcontact).grid(column=0, row=3, pady=5)
ttk.Button(frm, text="Supprimer Contact", command=deletecontact).grid(column=1, row=3, pady=5)
ttk.Button(frm, text="Modifier", command=modifier).grid(column=2, row=3, pady=5)


# Adding the table of data
columns = ('id','nom', 'email', 'phone')
tree = ttk.Treeview(frm, columns=columns, show='headings')

tree.heading('nom', text='First Name')
tree.heading('email', text='Last Name')
tree.heading('phone', text='Email')

tree.column("id", width=0, minwidth=0, stretch=tk.NO)
tree.column('nom', width=100, anchor=tk.W)
tree.column('nom', width=100, anchor=tk.W)
tree.column('email', width=100, anchor=tk.W)

for contact in ad.list:
	values = (contact['id'],contact['nom'], contact['email'], contact['phone'])
	tree.insert('', tk.END, values=values)

tree.grid(row=4,column=0, columnspan=3)

tree.bind("<<TreeviewSelect>>", select_item)
root.mainloop()