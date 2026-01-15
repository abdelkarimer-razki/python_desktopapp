from tkinter import *
from tkinter import ttk
import tkinter as tk
from frames.dashborad import dashboardFrame




root = Tk()
root.title("Address Book")
root.grid_columnconfigure(0, weight=1)

dash = dashboardFrame(root)
dash.build()

root.mainloop()