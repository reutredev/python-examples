import tkinter as tk
from tkinter import scrolledtext


class ChatbotGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Chatbot GUI")

        # Create scrolled text widget to display conversation history
        self.conversation_history = scrolledtext.ScrolledText(self.window, state='disabled', height=20, width=50)
        self.conversation_history.grid(column=0, row=0, padx=10, pady=10)

        # Create label and entry box for user input
        self.user_input_label = tk.Label(self.window, text="User input:")
        self.user_input_label.grid(column=0, row=1, padx=10, pady=10)
        self.user_input_entry = tk.Entry(self.window, width=50)
        self.user_input_entry.grid(column=1, row=1, padx=10, pady=10)

        # Create send button
        self.send_button = tk.Button(self.window, text="Send", command=self.send_message)
        self.send_button.grid(column=2, row=1, padx=10, pady=10)

        # Initialize conversation
        self.conversation_history.configure(state='normal')
        self.conversation_history.insert(tk.END, "Chatbot: Hello! How can I help you?\n")
        self.conversation_history.configure(state='disabled')

        self.window.mainloop()

    def send_message(self):
        # Get user input
        user_input = self.user_input_entry.get()

        # Clear user input box
        self.user_input_entry.delete(0, tk.END)

        # Add user message to conversation history
        self.conversation_history.configure(state='normal')
        self.conversation_history.insert(tk.END, "You: " + user_input + "\n")

        # Get chatbot response
        chatbot_response = "Chatbot: Sorry, I didn't understand. Can you please rephrase?"

        # Add chatbot response to conversation history
        self.conversation_history.insert(tk.END, chatbot_response + "\n")
        self.conversation_history.configure(state='disabled')


# Create chatbot GUI
chatbot_gui = ChatbotGUI()


# https://github.com/indently/chatbot_project_2023