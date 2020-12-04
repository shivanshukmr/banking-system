from tkinter import Label, Tk, Frame
from gui.Assets.assets import colour, font_c, icon, bankcli_asciiart

# ======main window=====
root = Tk()
root.title("Banking System")
root.iconbitmap(icon)

# =======title frame=====
frame1 = Frame(root)
frame1.configure(bg=colour_1)
frame1.pack()
title_image = Label(frame1, image=bankcli_asciiart)
title_image.pack()
version = Label(frame1, text="version 2.0", bg=colour_1, fg=font_c)
version.grid(row=2, column=1)

# ======mysql credentials=====

# ======initialize db=====

from core.db.initialize import initialize_db

initialize_db()

# =====main frame=====
frame2 = Frame(root)
frame2.configure(bg=colour)
frame2.pack()

root.mainloop()