from customtkinter import *
from modules.frames import CopyWidgets, MoveWidgets, DeleteWidgets

app = CTk()
app.geometry("900x600")

set_appearance_mode("system")
set_default_color_theme("dark-blue")

move_widgets = MoveWidgets(master_app=app)
move_widgets.frame()

copy_widgets = CopyWidgets(master_app=app)
copy_widgets.frame()

rename_widgets = DeleteWidgets(master_app=app)
rename_widgets.frame()

app.mainloop()
