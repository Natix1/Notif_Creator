import os
import threading
from win10toast import ToastNotifier

toaster = ToastNotifier()

def send_notification():
    title = input("Enter the title of the notification: ")
    message = input("Enter the message of the notification: ")
    threading.Thread(target=_send_notification, args=(title, message)).start()
    show_options()

def _send_notification(title, message):
    toaster.show_toast(title, message, duration=10)

def force_exit():
    os._exit(0)

def show_options():
    print(
"""
 __  _  __ _____ _ ___    ______ ___  __ _____ __  ___  
|  \| |/__\_   _| | __|  / _/ _ \ __|/  \_   _/__\| _ \ 
| | ' | \/ || | | | _|  | \_| v / _|| /\ || || \/ | v / 
|_|\__|\__/ |_| |_|_|    \__/_|_\___|_||_||_| \__/|_|_\
    
"""
    )
    print("1. Send Notification")
    print("2. Force Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        send_notification()
    elif choice == '2':
        force_exit()
    else:
        print("Invalid choice")

show_options()