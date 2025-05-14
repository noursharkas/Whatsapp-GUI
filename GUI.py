import tkinter as tk
from datetime import datetime

# --- Functions ---

def send_message():
    message = entry.get()
    if message and current_chat.get():
        time_now = datetime.now().strftime("%H:%M")
        chat_box.config(state='normal')
        chat_box.insert(tk.END, f"You ({time_now}): {message}\n", 'sent')
        # Simulate bot reply
        chat_box.insert(tk.END, f"{current_chat.get()} ({time_now}): Got your message!\n\n", 'received')
        chat_box.config(state='disabled')
        entry.delete(0, tk.END)

def select_contact(name):
    current_chat.set(name)
    chat_label.config(text=f"Chat with {name}")
    chat_box.config(state='normal')
    chat_box.delete('1.0', tk.END)
    chat_box.insert(tk.END, f"--- Chat started with {name} ---\n\n")
    chat_box.config(state='disabled')

def search_contacts():
    term = search_entry.get().lower()
    for btn in contact_buttons:
        if term in btn.cget("text").lower():
            btn.pack(fill=tk.X, padx=10, pady=2)
        else:
            btn.forget()

# --- Main window setup ---
root = tk.Tk()
root.title("Simple WhatsApp Chat")
root.geometry("450x600")
root.configure(bg="white")

current_chat = tk.StringVar(value="")

# --- Header with contact name ---
chat_label = tk.Label(root, text="Select a contact", bg="lightgreen", font=("Arial", 14), anchor="w")
chat_label.pack(fill=tk.X)

# --- Search bar ---
search_frame = tk.Frame(root, bg="white")
search_frame.pack(fill=tk.X, padx=10, pady=(5,0))

search_entry = tk.Entry(search_frame, font=("Arial", 12))
search_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

search_button = tk.Button(search_frame, text="Search", command=search_contacts)
search_button.pack(side=tk.LEFT, padx=5)

# --- Contact List ---
contact_frame = tk.Frame(root, bg="#f8f8f8")
contact_frame.pack(fill=tk.X, padx=10, pady=5)

contacts = ["Nour", "Ahmed", "Zeyad", "Mohamed"]
contact_buttons = []

for name in contacts:
    btn = tk.Button(contact_frame, text=name, command=lambda n=name: select_contact(n))
    btn.pack(fill=tk.X, padx=5, pady=2)
    contact_buttons.append(btn)

# --- Chat area ---
chat_box = tk.Text(root, bg="white", font=("Arial", 12), wrap=tk.WORD)
chat_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
chat_box.config(state='disabled')

# Tag for colors
chat_box.tag_config('sent', foreground='green')
chat_box.tag_config('received', foreground='gray')

# --- Entry and Send ---
entry = tk.Entry(root, font=("Arial", 12))
entry.pack(padx=10, pady=(0,5), fill=tk.X)

send_btn = tk.Button(root, text="Send", command=send_message)
send_btn.pack(pady=(0,10))

root.mainloop()


