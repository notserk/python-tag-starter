import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style

def on_button_click():
    print("Button clicked!")

app = tk.Tk()
style = Style(theme='lumen')

# Create a new button
button = ttk.Button(app, text="Click Me!", command=on_button_click)
button.pack(pady=20)

# Run the application
app.mainloop()
