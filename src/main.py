from tkinter import *
from gui.Assets.assets import colour_title, font_title, colour, font_c, icon
from gui.utils.users import userauthentication

# ======main window=====
root = Tk()
root.title("Banking System")
root.iconbitmap(icon)

# =======title frame=====
frame1 = Frame(root)
frame1.configure(bg=colour_title, bd=4, relief=RAISED, padx=5, pady=2)
frame1.grid(padx=2, pady=1, sticky=W + E)
title_image = Label(frame1, image=bankcli_asciiart)
title_image.pack()
version = Label(
    frame1,
    text="version 2.0",
    bg=colour_title,
    fg=font_title,
    anchor=W,
    padx=2,
    pady=5,
)
version.grid(row=2, column=1, columnspan=3, sticky=W + E)


# ======mysql credentials=====

# ======initialize db=====

# from core.db.initialize import initialize_db

# initialize_db()

# # =====main frame=====
# from core.utils import info

frame2 = Frame(root)
frame2.configure(bg=colour, bd=2)
frame2.grid(padx=2, pady=1)
label = Label(frame2, text="test", bg=colour, fg=font_c)
label.pack()
space1 = Label(frame2, text="", bg=colour).pack()
root.mainloop()