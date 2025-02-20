import tkinter as tk
from tkinter import filedialog, messagebox
import os

# Function to create folders from the structure
def create_folders_from_structure(structure, base_dir):
    lines = structure.strip().split("\n")
    stack = []
    
    for line in lines:
        stripped_line = line.lstrip()
        depth = (len(line) - len(stripped_line)) // 2
        folder_name = stripped_line
        
        while len(stack) > depth:
            stack.pop()
        
        current_path = os.path.join(base_dir, *stack, folder_name)
        os.makedirs(current_path, exist_ok=True)
        
        stack.append(folder_name)
    messagebox.showinfo("Success", f"Folders created in {os.path.abspath(base_dir)}")

# Function to open directory chooser
def choose_directory():
    directory = filedialog.askdirectory()
    if directory:
        base_dir_entry.delete(0, tk.END)
        base_dir_entry.insert(0, directory)

# Function to handle folder creation
def handle_create_folders():
    base_dir = base_dir_entry.get().strip()
    folder_structure = folder_structure_text.get("1.0", tk.END).strip()
    
    if not base_dir or not os.path.exists(base_dir):
        messagebox.showerror("Error", "Please select a valid base directory.")
        return
    
    if not folder_structure:
        messagebox.showerror("Error", "Please enter a folder structure.")
        return
    
    create_folders_from_structure(folder_structure, base_dir)

# Initialize Tkinter app
root = tk.Tk()
root.title("Folder Structure Creator")
root.geometry("600x500")

# UI Elements
frame = tk.Frame(root, padx=10, pady=10)
frame.pack(fill=tk.BOTH, expand=True)

tk.Label(frame, text="Base Directory:").grid(row=0, column=0, sticky="w")
base_dir_entry = tk.Entry(frame, width=50)
base_dir_entry.grid(row=0, column=1, padx=5, pady=5)
choose_dir_button = tk.Button(frame, text="Browse", command=choose_directory)
choose_dir_button.grid(row=0, column=2, padx=5, pady=5)

tk.Label(frame, text="Folder Structure (Use 2 spaces per level):").grid(row=1, column=0, columnspan=3, sticky="w")
folder_structure_text = tk.Text(frame, width=70, height=20)
folder_structure_text.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

create_button = tk.Button(frame, text="Create Folders", command=handle_create_folders, bg="green", fg="white")
create_button.grid(row=3, column=0, columnspan=3, pady=10)

# Run the app
root.mainloop()
