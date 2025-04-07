import tkinter as tk
from tkinter import messagebox

def show_dialog():
    messagebox.showinfo("Dialog Box", "Hello! This is a simple dialog box.")

# Create the main window
root = tk.Tk()
root.title("Simple Dialog Box Example")

# Create a button to trigger the dialog
button = tk.Button(root, text="Show Dialog", command=show_dialog)
button.pack(pady=20)

# Run the application
root.mainloop()