import tkinter as tk
from datetime import datetime
from PIL import Image, ImageTk

chat_windows = {}
def send_message(name, entry, chat_box):
    message = entry.get()
    if message:
        time_now = datetime.now().strftime("%H:%M")
        chat_box.config(state='normal')
        chat_box.insert(tk.END, f"You ({time_now}): {message}\n")
        chat_box.insert(tk.END, f"{name}: Hello! Nice to meet you.\n\n")
        chat_box.config(state='disabled')
        entry.delete(0, tk.END)
def open_chat_window(name):
    if name in chat_windows:
        chat_windows[name].lift()
        return

    win = tk.Toplevel()
    win.title(f"Chat with {name}")
    win.geometry("400x500")
    win.configure(bg="white")

    label = tk.Label(win, text=f"Chat with {name}", bg="lightgreen", font=("Arial", 12), anchor="w")
    label.pack(fill=tk.X)

    chat_box = tk.Text(win, bg="white", fg="black", font=("Arial", 12), state='disabled')
    chat_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    entry = tk.Entry(win, font=("Arial", 12))
    entry.pack(padx=50, pady=(0, 10), fill=tk.X)

    send_btn = tk.Button(win, text="Send", bg="green", fg="white",
                         command=lambda: send_message(name, entry, chat_box))
    send_btn.pack(pady=(0, 10))

    chat_windows[name] = win
    win.protocol("WM_DELETE_WINDOW", lambda: close_chat_window(name, win))
def close_chat_window(name, window):
    del chat_windows[name]
    window.destroy()

root = tk.Tk()
root.title("WhatsApp")
root.geometry("300x500")
root.configure(bg="white")

nav_frame = tk.Frame(root, bg="lightgray")
nav_frame.pack(fill=tk.X)

logo_img = Image.open("GUI logo/whatsapp-logo-24.png")
logo_photo = ImageTk.PhotoImage(logo_img)

logo_label = tk.Label(nav_frame, image=logo_photo, bg="lightgray")
logo_label.image = logo_photo
logo_label.pack(side=tk.LEFT, padx=5, pady=5)

title_label = tk.Label(nav_frame, text="WhatsApp", bg="lightgray", font=("Arial", 14, "bold"))
title_label.pack(side=tk.LEFT, padx=5, pady=5)

chats_btn = tk.Button(nav_frame, text="Chats", width=8)
chats_btn.pack(side=tk.LEFT, padx=5, pady=5)

status_btn = tk.Button(nav_frame, text="Status", width=8)
status_btn.pack(side=tk.LEFT, padx=5, pady=5)

groups_btn = tk.Button(nav_frame, text="Groups", width=8)
groups_btn.pack(side=tk.LEFT, padx=5, pady=5)

unread_btn = tk.Button(nav_frame, text="UnRead", width=8)
unread_btn.pack(side=tk.LEFT, padx=5 , pady=5)

search_entry = tk.Entry(root, font=("Arial", 12))
search_entry.pack(padx=10, pady=(10, 5), fill=tk.X)
def search_contacts():
    term = search_entry.get().lower()
    for btn in contact_buttons:
        if term in btn.cget("text").lower():
            btn.pack(fill=tk.X, padx=10, pady=2)
        else:
            btn.forget()

search_button = tk.Button(root, text="Search", command=search_contacts)
search_button.pack(pady=(0, 10))

contacts = ["Nour", "Ahmed", "Ali", "Muhammed", "Zeyad"]
contact_buttons = []

for name in contacts:
    btn = tk.Button(root, text=name, anchor="w", bg="#f0f0f0",
                    command=lambda n=name: open_chat_window(n))
    btn.pack(fill=tk.X, padx=10, pady=2)
    contact_buttons.append(btn)

root.mainloop()


