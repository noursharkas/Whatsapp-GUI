import tkinter as tk
from datetime import datetime
from PIL import Image, ImageTk
chat_windows = {}
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

def close_chat_window(name, window):
    del chat_windows[name]
    window.destroy()

root = tk.Tk()
root.title("WhatsApp")
root.geometry("300x500")
root.configure(bg="white")

nav_frame = tk.Frame(root, bg="lightgreen")
nav_frame.pack(fill=tk.X)

logo_img = Image.open("GUI logo/whatsapp-logo-24.png")
logo_photo = ImageTk.PhotoImage(logo_img)

logo_label = tk.Label(nav_frame, image=logo_photo, bg="lightgreen")
logo_label.image = logo_photo
logo_label.pack(side=tk.LEFT, padx=5, pady=5)

title_label = tk.Label(nav_frame, text="WhatsApp", bg="lightgreen", font=("Arial", 14, "bold"))
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
            btn.pack(fill=tk.X, padx=5, pady=2)
        else:
            btn.forget()

search_button = tk.Button(root, text="Search",bg="lightgreen", command=search_contacts)
search_button.pack(pady=(0, 10))

contacts = ["Nour", "Ahmed", "Ali", "Muhammed", "Zeyad"]
contact_buttons = []

profileImg = Image.open("GUI logo/test/profilephoto.png").resize((30, 30))
profilePhoto = ImageTk.PhotoImage(profileImg)

for name in contacts:
    frame = tk.Frame(root, bg="white")
    frame.pack(fill=tk.X, padx=5, pady=2)

    img_label = tk.Label(frame, image=profilePhoto, bg="white")
    img_label.image = profilePhoto
    img_label.pack(side=tk.LEFT, padx=5)

    btn = tk.Button(frame, text=name, anchor="w", bg="white",
                    command=lambda n=name: open_chat_window(n))
    btn.pack(side=tk.LEFT, fill=tk.X, expand=True)
    contact_buttons.append(frame)
def send_message(name, entry, chat_box):
    message = entry.get()
    if message:
        time_now = datetime.now().strftime("%H:%M")
        chat_box.config(state='normal')
        chat_box.tag_config("sent", foreground="green")
        chat_box.tag_config("received", foreground="blue")
        chat_box.insert(tk.END, f"You ({time_now}): {message}\n", "sent")
        chat_box.insert(tk.END, f"{name} {time_now}: Hello! Nice to meet you.\n\n", "received")

        chat_box.config(state='disabled')
        entry.delete(0, tk.END)
root.mainloop()


