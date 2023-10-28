import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
import random
import dialogflow_v2 as dialogflow
import os

# Load your Google Cloud credentials
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'path/to/your/credentials.json'

# Create a Dialogflow client
client = dialogflow.SessionsClient()

# Function to generate a random response
def get_response(user_input):
    responses = [
        "Hello! How can I assist you?",
        "What can I do for you today?",
        "How can I help you?",
        "Nice to meet you! How may I assist you?"
    ]
    return random.choice(responses)

# Function to get Dialogflow response
def get_dialogflow_response(user_input):
    session = client.session_path('your-project-id', 'unique-session-id')
    text_input = dialogflow.TextInput(text=user_input, language_code='en')
    query_input = dialogflow.QueryInput(text=text_input)
    response = client.detect_intent(session=session, query_input=query_input)
    return response.query_result.fulfillment_text

# Function to handle user input
def send_message():
    user_input = entry.get()
    if user_input:
        chat_display.insert(tk.END, f"You: {user_input}\n")
        entry.delete(0, tk.END)
        response = get_dialogflow_response(user_input)
        chat_display.insert(tk.END, f"Amena: {response}\n")
    else:
        messagebox.showwarning("Empty Input", "Please enter a message.")

# Create the main window
root = tk.Tk()
root.title("Amena Chatbot")

# Create a chat display
chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10)
chat_display.pack(padx=10, pady=10)

# Create an entry field for user input
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# Create a send button
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack()

# Run the main loop
root.mainloop()

