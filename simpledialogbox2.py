import tkinter as tk
from tkinter import messagebox

# Function to display a message when the button is clicked
def show_message():
    messagebox.showinfo("Dialog Box", "Hello! This is a simple dialog box.")

# Create the main application window
root = tk.Tk()
root.title("Simple Dialog Box")

# Set the size of the window
root.geometry("300x150")

# Add a label to the window
label = tk.Label(root, text="Click the button to see a dialog box:")
label.pack(pady=20)

# Add a button to trigger the dialog box
button = tk.Button(root, text="Show Dialog", command=show_message)
button.pack(pady=10)

# Run the application
root.mainloop()
