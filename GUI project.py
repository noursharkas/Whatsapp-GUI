import tkinter as tk
from datetime import datetime

# Function to send message
def send_message():
    message = entry.get()
    if message:
        time_now = datetime.now().strftime("%H:%M")
        chat_box.config(state='normal')
        chat_box.insert(tk.END, f"You ({time_now}): {message}\n")
        chat_box.insert(tk.END, f"Bot: I got your message!\n\n")
        chat_box.config(state='disabled')
        entry.delete(0, tk.END)

# Main window
root = tk.Tk()
root.title("WhatsApp Chat")
root.geometry("400x550")
root.configure(bg="white")

# --- TOP NAVIGATION (Chats, Status, Groups) ---
nav_frame = tk.Frame(root, bg="lightgray")
nav_frame.pack(fill=tk.X)

chats_btn = tk.Button(nav_frame, text="Chats", width=10)
chats_btn.pack(side=tk.LEFT, padx=5, pady=5)

status_btn = tk.Button(nav_frame, text="Status", width=10)
status_btn.pack(side=tk.LEFT, padx=5, pady=5)

groups_btn = tk.Button(nav_frame, text="Groups", width=10)
groups_btn.pack(side=tk.LEFT, padx=5, pady=5)

# --- SEARCH BAR ---
search_label = tk.Label(root, text=" Search...", bg="#f0f0f0", anchor="w", font=("Arial", 12))
search_label.pack(fill=tk.X, padx=10, pady=(5, 0))

# --- CHAT AREA ---
chat_box = tk.Text(root, bg="white", fg="black", font=("Arial", 12))
chat_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
chat_box.config(state='disabled')

# --- MESSAGE ENTRY ---
entry = tk.Entry(root, font=("Arial", 12))
entry.pack(padx=10, pady=(0,10), fill=tk.X)

send_btn = tk.Button(root, text="Send", command=send_message)
send_btn.pack(pady=(0,10))

# Run app
root.mainloop()
