import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog

# --- Basic Setup ---
# We need a root window to own the dialogs, but we don't necessarily want to see it.
root = tk.Tk()
root.withdraw()  # Hide the main root window

# --- 1. Information Message Box ---
print("Showing Info Box...")
messagebox.showinfo("Info Title", "This is an information message.")
print("Info Box closed.")

# --- 2. Warning Message Box ---
print("\nShowing Warning Box...")
messagebox.showwarning("Warning Title", "This is a warning message!")
print("Warning Box closed.")

# --- 3. Error Message Box ---
print("\nShowing Error Box...")
messagebox.showerror("Error Title", "An error occurred!")
print("Error Box closed.")

# --- 4. Yes/No Question Box ---
print("\nShowing Yes/No Question Box...")
# Returns True for Yes, False for No
response_yesno = messagebox.askyesno("Question Title", "Do you like Python?")
if response_yesno:
    print("User clicked Yes")
else:
    print("User clicked No")
print("Yes/No Box closed.")

# --- 5. OK/Cancel Question Box ---
print("\nShowing OK/Cancel Question Box...")
# Returns True for OK, False for Cancel
response_okcancel = messagebox.askokcancel("Confirmation Title", "Proceed with action?")
if response_okcancel:
    print("User clicked OK")
else:
    print("User clicked Cancel")
print("OK/Cancel Box closed.")

# --- 6. Simple Text Input Box ---
print("\nShowing Text Input Box...")
# Returns the entered string, or None if Cancel is clicked
user_name = simpledialog.askstring("Input Title", "What is your name?")
if user_name:
    print(f"User entered: {user_name}")
elif user_name == "": # User pressed OK but entered nothing
    print("User entered an empty string.")
else: # User pressed Cancel
    print("User cancelled the input.")
print("Text Input Box closed.")

# --- 7. Simple Integer Input Box ---
print("\nShowing Integer Input Box...")
# Returns the entered integer, or None if Cancel is clicked
user_age = simpledialog.askinteger("Input Title", "What is your age?", minvalue=0, maxvalue=120) # Optional limits
if user_age is not None:
    print(f"User entered age: {user_age}")
else:
    print("User cancelled the input.")
print("Integer Input Box closed.")

# --- 8. Open File Dialog ---
print("\nShowing Open File Dialog...")
# Returns the full path to the selected file as a string, or an empty string/tuple if Cancelled
# You can specify file types
file_path_open = filedialog.askopenfilename(
    title="Select a file to open",
    filetypes=[("Text files", "*.txt"), ("Python files", "*.py"), ("All files", "*.*")]
)
if file_path_open:
    print(f"User selected file to open: {file_path_open}")
else:
    print("User cancelled file selection.")
print("Open File Dialog closed.")


# --- 9. Save File Dialog ---
print("\nShowing Save As File Dialog...")
# Returns the full path where the user wants to save as a string, or an empty string/tuple if Cancelled
file_path_save = filedialog.asksaveasfilename(
    title="Save file as...",
    defaultextension=".txt", # Suggests an extension
    filetypes=[("Text files", "*.txt"), ("CSV files", "*.csv"), ("All files", "*.*")]
)
if file_path_save:
    print(f"User chose to save file as: {file_path_save}")
else:
    print("User cancelled save.")
print("Save As File Dialog closed.")

# --- 10. Select Directory Dialog ---
print("\nShowing Select Directory Dialog...")
# Returns the path to the selected directory, or an empty string/tuple if Cancelled
dir_path = filedialog.askdirectory(
    title="Select a Folder"
)
if dir_path:
    print(f"User selected directory: {dir_path}")
else:
    print("User cancelled directory selection.")
print("Select Directory Dialog closed.")


# --- Cleanup (Optional) ---
# Since the script ends here, explicitly destroying the root isn't strictly needed,
# but good practice in larger apps.
# root.destroy()

print("\n--- All Dialog Examples Complete ---")

# If you were running a full Tkinter app, you would end with root.mainloop()
# But for just showing dialogs sequentially like this, it's not needed.