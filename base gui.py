import tkinter
import tkinter as tk
from datetime import datetime
from tkinter import PhotoImage

from GUI import search_contacts


def open_chat(contact_name):
    chat_window = tk.Toplevel(window)
    chat_window.title(f"{contact_name}'s chat")
    chat_window.geometry("600x600")

    header_frame = tk.Frame(chat_window)
    header_frame.pack(side=tk.TOP, fill=tk.X)

    header_label = tk.Label(header_frame, text="Welcome to your Chats!",fg="green")
    header_label.pack(side=tk.LEFT)

    exit_button = tk.Button(header_frame, text="x", command=chat_window.destroy, bg="red", fg="white")
    exit_button.pack(side=tk.RIGHT)

    chat_area = tk.Label(chat_window, text="", anchor='nw', justify='left')
    chat_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    input_frame = tk.Frame(chat_window)
    input_frame.pack(side=tk.BOTTOM, fill=tk.X)

    message_entry = tk.Entry(input_frame, bd=2, width=60)
    message_entry.pack(side=tk.LEFT)

    send_button = tk.Button(input_frame, text="Send",
                            command=lambda: send_message(chat_area, message_entry),
                            bg="green", fg="white")
    send_button.pack(side=tk.RIGHT, padx=10, pady=10)

def send_message(chat_area, message_entry):
    message = message_entry.get()
    if message:
        current_text = chat_area.cget("text")
        timestamp = datetime.now().strftime('%H:%M')
        updated_text = current_text + "\n" + message + "   " + timestamp
        chat_area.config(text=updated_text)
        message_entry.delete(0, tk.END)
        response = generate_response(message)
        response_time = datetime.now().strftime('%H:%M')
        updated_text += f"\nWhatsapp: {response}   {response_time}"
        chat_area.config(text=updated_text)
def generate_response(user_message):
        if "hello" in user_message.lower():
            return "Hi there! How can I help you today?"
        elif "bye" in user_message.lower():
            return "Goodbye! Have a nice day."
        else:
            return "Hi, I'm here to help!"

window = tk.Tk()
window.title("WhatsApp")
window.geometry("670x650")

top_frame = tk.Frame(window)
top_frame.pack(side=tk.TOP, fill=tk.X, pady=10)

left_top = tk.Frame(top_frame)
left_top.pack(side=tk.LEFT, padx=10)

logo = tk.PhotoImage(file="GUI logo/whatsapp-logo-24.png")
L1 = tk.Label(left_top, image=logo)
L2 = tk.Label(left_top,text="WhatsApp",fg="black")
L1.pack(side=tk.TOP)
L2.pack()

center_top = tk.Frame(top_frame)
center_top.pack(side=tk.TOP)

button1 = tk.Button(center_top, text="Chats", width=50,bg="green",fg="white")
button2 = tk.Button(center_top, text="ArchivedChats", width=50,bg="green",fg="white")
button3 = tk.Button(center_top, text="Status", width=50,bg="green",fg="white")
button4 = tk.Button(center_top, text="Exit", width=5, bg="green",fg="white")

button1.pack(side=tk.LEFT, padx=2)
button2.pack(side=tk.LEFT, padx=2)
button3.pack(side=tk.LEFT, padx=2)
button4.pack(side=tk.LEFT, padx=2)

contact_frame = tk.Frame(window)
contact_frame.pack(side=tk.LEFT)
contacts = ["Sameh", "Ahmed", "Karen", "Jana", "Nour"]

left_frame = tk.Frame( bg="#f0f0f0", width=200)
left_frame.pack(side=tk.LEFT, fill=tk.Y)
search_entry = tk.Entry(left_frame, font=("Arial", 12))
search_entry.pack(padx=10, pady=(10, 5), fill=tk.X)
search_button = tk.Button(left_frame, text="Search", command=search_contacts)

for contact in contacts:
    contact_button = tk.Button(contact_frame, text=contact, width=60, pady=5,
                               command=lambda name=contact: open_chat(name))
    contact_button.pack(pady=2)
window.mainloop()