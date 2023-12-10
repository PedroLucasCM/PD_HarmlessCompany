import tkinter as tk
from tkinter import messagebox
from read_json import junk_list

def add_to_backpack(item):
    global total_weight, total_value_in_backpack
    if total_weight + item.weight <= MAX_WEIGHT:
        total_weight += item.weight
        total_value_in_backpack += item.value
        backpack_contents.insert(tk.END, str(item))  # Insert a string representation
        backpack_items.append(item)  # Keep track of the Junk object
        update_weight_label()
        update_value_label()
    else:
        messagebox.showwarning("Warning", "Exceeding backpack weight limit!")

def remove_from_backpack():
    global total_weight, total_value_in_backpack
    try:
        selected_index = backpack_contents.curselection()[0]
        item = backpack_items.pop(selected_index)  # Remove the Junk object
        backpack_contents.delete(selected_index)
        total_weight -= item.weight
        total_value_in_backpack -= item.value
        update_weight_label()
        update_value_label()
    except IndexError:
        messagebox.showwarning("Warning", "No item selected to remove")

def update_weight_label():
    weight_label.config(text=f"Total Weight: {total_weight}Kg / {MAX_WEIGHT}Kg")

def update_value_label():
    value_label.config(text=f"Total Value in Backpack: ${total_value_in_backpack}")

def calculate_total_value(items):
    return sum(item.value for item in items)

# Constants
MAX_WEIGHT = 45  # Maximum weight of the backpack

# Load junk items
junk_items = junk_list()

# GUI setup
root = tk.Tk()
root.title("Junk Item Selector")

# Listbox for junk items
junk_listbox = tk.Listbox(root, width=50, height=15)
junk_listbox.pack(pady=10)

# Add items to the listbox
for item in junk_items:
    junk_listbox.insert(tk.END, str(item))  # Insert a string representation

# Button to add item to backpack
add_button = tk.Button(root, text="Add to Backpack", command=lambda: add_to_backpack(junk_items[junk_listbox.curselection()[0]]))
add_button.pack(pady=5)

# Button to remove item from backpack
remove_button = tk.Button(root, text="Remove from Backpack", command=remove_from_backpack)
remove_button.pack(pady=5)

# Label for total weight
total_weight = 0
weight_label = tk.Label(root, text=f"Total Weight: {total_weight}Kg / {MAX_WEIGHT}Kg")
weight_label.pack(pady=5)

# Label for total value in backpack
total_value_in_backpack = 0
value_label = tk.Label(root, text=f"Total Value in Backpack: ${total_value_in_backpack}")
value_label.pack(pady=5)

# Label for total value of all items
total_value_label = tk.Label(root, text=f"Total Value of All Items: ${calculate_total_value(junk_items)}")
total_value_label.pack(pady=5)

# Listbox for backpack contents
backpack_contents = tk.Listbox(root, width=50, height=10)
backpack_contents.pack(pady=10)

# List to keep track of Junk objects in the backpack
backpack_items = []

root.mainloop()