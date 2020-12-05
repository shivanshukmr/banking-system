from tkinter import Label, Tk
from gui.assets.assets import colour, font_c, icon, bankcli_asciiart

# ======main window=====
root = Tk()
root.title("Banking System")
root.configure(bg=colour)
root.iconbitmap(icon)
title_image = Label(root, image=bankcli_asciiart)
title_image.pack()
version = Label(root, text="version 2.0", bg=colour, fg=font_c)
version.grid(row=2, column=1)
    
# ======mysql credentials=====

# ======initialize db=====

from core.db.initialize import initialize_db

initialize_db()

root.mainloop()