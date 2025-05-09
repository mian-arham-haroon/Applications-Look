import ttkbootstrap as ttk
from ttkbootstrap.constants import *

app=ttk.Window(themename="cyborg")
app.geometry("600x500")
app.title("Login")

label=ttk.Label(app,text="Contact Infromation")
label.pack(padx=30)
label.config(font=("arial",20,"bold"))

name_frame=ttk.Frame(app)
name_frame.pack(padx=10,pady=15,fill="x")
ttk.Label(name_frame,text="Name").pack(side="left",padx=5)
ttk.Entry(name_frame).pack(side="left",fill="x",expand=True,padx=5)

email_frame=ttk.Frame(app)
email_frame.pack(padx=10,pady=15,fill="x")
ttk.Label(email_frame,text="Email").pack(side="left",padx=5)
ttk.Entry(email_frame).pack(side="left",fill="x",expand=True,padx=5)

chack_box_frame=ttk.Frame(app)
chack_box_frame.pack(padx=10,pady=15,fill="x")
ttk.Checkbutton(chack_box_frame,bootstyle="round-toggle",text="Remember Info").pack(side="left",padx=10)

button_frame=ttk.Frame(app)
button_frame.pack(padx=10,pady=50,fill="x")
ttk.Button(button_frame,text="Submit",bootstyle=SUCCESS).pack(side="left",padx=10)
ttk.Button(button_frame,text="Cancal",bootstyle=SECONDARY).pack(side="left",padx=10)





app.mainloop()