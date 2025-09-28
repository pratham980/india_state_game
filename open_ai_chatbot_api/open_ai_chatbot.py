import tkinter as tk
from tkinter import scrolledtext, messagebox
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key="your_api_key")  # replace with your key

# Conversation history
messages = [{"role": "system", "content": "You are a helpful chatbot."}]

# Function to send user input
def send_message():
    user_input = entry.get()
    if not user_input.strip():
        return
    # Display user message
    chat_area.configure(state='normal')
    chat_area.insert(tk.END, "You: " + user_input + "\n")
    chat_area.configure(state='disabled')
    chat_area.see(tk.END)
    
    entry.delete(0, tk.END)
    
    # Append user message to conversation
    messages.append({"role": "user", "content": user_input})
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages
        )
        bot_reply = response.choices[0].message.content
    except Exception as e:
        bot_reply = "Error: " + str(e)
    
    # Display bot reply
    chat_area.configure(state='normal')
    chat_area.insert(tk.END, "Bot: " + bot_reply + "\n")
    chat_area.configure(state='disabled')
    chat_area.see(tk.END)
    
    # Append bot reply to conversation
    messages.append({"role": "assistant", "content": bot_reply})

# Tkinter GUI setup
root = tk.Tk()
root.title("Chatbot GUI")

chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20, state='disabled')
chat_area.pack(padx=10, pady=10)

entry_frame = tk.Frame(root)
entry_frame.pack(padx=10, pady=5)

entry = tk.Entry(entry_frame, width=50)
entry.pack(side=tk.LEFT, padx=(0,5))

send_btn = tk.Button(entry_frame, text="Send", command=send_message)
send_btn.pack(side=tk.LEFT)

# Bind Enter key to send message
entry.bind("<Return>", lambda event: send_message())

root.mainloop()

