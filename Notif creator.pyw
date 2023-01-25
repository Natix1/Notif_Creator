import tkinter as tk
from tkinter import messagebox, filedialog
from tkinter import ttk
from win10toast import ToastNotifier
import os
import threading
toaster = ToastNotifier()
def send_notification():
    title = title_var.get()
    message = message_var.get()
    threading.Thread(target=_send_notification, args=(title, message)).start()
    title_var.set("")
    message_var.set("")
    
def _send_notification(title, message):
    toaster.show_toast(title, message, duration=10)

def force_exit():
    os._exit(0)

root = tk.Tk()
root.title("Windows Notification")
root.configure(background='white')
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
icon_path = os.path.join(current_dir, 'icon.ico')
root.iconbitmap(icon_path)

# Set the weight of the columns
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)

# Set the weight of the rows
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)

title_var = tk.StringVar()
title_label = ttk.Label(root, text="Notification Title:", font=("Helvetica", 12))
title_label.grid(row=0, column=0, padx=10, pady=10,sticky='W')

title_entry = ttk.Entry(root, textvariable=title_var, font=("Helvetica", 12))
title_entry.grid(row=0, column=1, padx=10, pady=10,sticky='W')

message_var = tk.StringVar()
message_label = ttk.Label(root, text="Notification Message:", font=("Helvetica", 12))
message_label.grid(row=1, column=0, padx=10, pady=10,sticky='W')

message_entry = ttk.Entry(root, textvariable=message_var, font=("Helvetica", 12))
message_entry.grid(row=1, column=1, padx=10, pady=10,sticky='W')

send_button = ttk.Button(root, text="Send Notification", command=send_notification)
send_button.grid(row=2, column=0,padx=10,pady=10,columnspan=2,sticky='W')

exit_button = ttk.Button(root, text="Force Exit", command=force_exit)
exit_button.grid(row=3, column=0,padx=10,pady=10,columnspan=2,sticky='W')

root.mainloop()
