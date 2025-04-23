import tkinter as tk
from tkinter import messagebox,  filedialog
import folderOrganiser  # Importing the folderorganiser.py script

def run_organise():
    try:
        folderOrganiser.organise_folder(folderOrganiser.TARGET_FOLDER, dry_run=False)
        messagebox.showinfo("Success", "Files have been successfully organised!") 
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def run_dry_run():
    try:
        folderOrganiser.organise_folder(folderOrganiser.TARGET_FOLDER, dry_run=True)
        messagebox.showinfo("Dry Run", "Dry run complete! Check the console output for simulated moves.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def run_undo():
    try:
        folderOrganiser.undo_changes()
        messagebox.showinfo("Undo", "Changes have been undone successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Creating the main window
window =tk.Tk()
window.title("Folder Organiser")

#Creating buttons for each action
organise_button = tk.Button(window, text="Organise Files", command=run_organise, width=20)
dry_run_button = tk.Button(window, text="Dry Run", command=run_dry_run, width=20)
undo_button = tk.Button(window, text="Undo", command=run_undo, width=20)

# Placing the button in the window
organise_button.pack(pady=10)
dry_run_button.pack(pady=10)
undo_button.pack(pady=10)

# Start the GUI loop
window.mainloop()