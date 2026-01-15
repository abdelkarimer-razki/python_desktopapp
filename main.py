from tkinter import *
from frames.dashborad import dashboardFrame
from frames.authentification import authForm




root = Tk()
root.grid_columnconfigure(0, weight=1)

dash = dashboardFrame(root)
dash.build()

# auth = authForm(root)
# auth.build()

root.mainloop()