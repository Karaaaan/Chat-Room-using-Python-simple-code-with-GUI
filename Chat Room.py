from tkinter import *
from tkinter import messagebox

# Main window
window = Tk()
window.title("Chat Room")
window.geometry("800x800")

# Global list to store all chat messages
chat_list = []

# Title label
title = Label(window, text="CHAT ROOM", font=("Arial", 25))
title.pack()

# Chat name label and entry
Label(window, text="ENTER YOUR CHATNAME:", font=("Arial", 25)).pack()
chatname = Entry(window)
chatname.pack()

# Function to validate and enter the chat room
def enter_room():
    if chatname.get() == "":
        messagebox.showwarning("Error", "Name is missing")
    else:
        # Open chat room window
        room = Toplevel()
        room.title("Chatroom")
        room.geometry("600x600")
        
        # Title for the chatroom window
        Label(room, text="CHATROOM", font=("Arial", 25)).pack()

        # Text widget to display messages
        message_display = Text(room, wrap=WORD, font=("Arial", 14))
        message_display.pack(expand=True, fill=BOTH)

        # Display all existing messages
        for msg in chat_list:
            message_display.insert(END, msg + "\n")

        # Entry to type a new message
        message_entry = Entry(room)
        message_entry.pack(pady=10)

        # Function to send a new message
        def send_message():
            if message_entry.get() == "":
                messagebox.showwarning("Error", "No message to send")
            else:
                # Format the message with the username and message text
                data = f"{chatname.get()}: {message_entry.get()}"
                chat_list.append(data)
                message_display.insert(END, data + "\n")
                message_entry.delete(0, END)  # Clear message entry after sending

        # Button to send the message
        send_button = Button(room, text="Send", command=send_message)
        send_button.pack()

# Button to retrieve name and enter room
retrieve_name_button = Button(window, text="Enter", command=enter_room)
retrieve_name_button.pack()

# Run main loop
window.mainloop()
