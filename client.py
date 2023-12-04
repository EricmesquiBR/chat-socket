import socket
import threading
import tkinter as tk
from tkinter import scrolledtext
import datetime

def receive_messages():
  while True:
      try:
          message = client.recv(1024).decode('utf-8')
          messages_text.insert(tk.END, message + '\n')
          messages_text.see(tk.END) # Scroll to the bottom of the text widget
      except:
          break

def send_message(event=None):
   message = message_entry.get()
   client.send(message.encode('utf-8'))
   message_entry.delete(0, tk.END)
   messages_text.insert(tk.END, f'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")} - {nickname}: {message}\n')
   messages_text.see(tk.END) # Scroll to the bottom of the text widget


nickname = input('Enter your nickname: ')
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 9001))
client.send(nickname.encode('utf-8'))

window = tk.Tk()
window.title('Chat')

messages_text = scrolledtext.ScrolledText(window)
messages_text.pack()

message_entry = tk.Entry(window)
message_entry.bind("<Return>", send_message)
message_entry.pack()

receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

window.mainloop()
