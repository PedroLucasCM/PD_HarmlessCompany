import tkinter as tk
from tkinter import messagebox
from src.junk.read_junk import junk_list


class InterfaceGrafica:

    junk_items = junk_list()
    def __init__(self, root):
        self.root = root
        self.root.title("Harmless Company")
        self.total_weight = 0
        self.backpack_contents = tk.Listbox(self.root, width=50, height=10, font=('Perfect DOS VGA 437', 10))
        self.junk_listbox = tk.Listbox(self.root, width=50, height=15, font=('Perfect DOS VGA 437', 10))
        self.backpack_items = []

        self.MAX_WEIGHT = 45  # Maximum weight of the backpack]

        self.create_widgets()


    def add_to_backpack(self, item):
        if self.total_weight + item.weight <= self.self.MAX_WEIGHT:
            self.total_weight += item.weight
            self.total_backpack += item.value
            self.backpack_contents.insert(tk.END, str(item))  
            self.backpack_items.append(item)  
            self.update_weight_label()
            self.update_value_label()
        else:
            messagebox.showwarning("Warning", "Exceeding backpack weight limit!")

    def remove_from_backpack(self, ):
        try:
            selected_index = self.backpack_contents.curselection()[0]
            item = self.backpack_items.pop(selected_index)  
            self.backpack_contents.delete(selected_index)
            self.total_weight -= item.weight
            self.total_backpack -= item.value
            self.update_weight_label()
            self.update_value_label()
        except IndexError:
            messagebox.showwarning("Warning", "No item selected to remove")

    def update_weight_label(self):
        self.weight_label.config(text=f"Total Weight: {self.total_weight}Kg / {self.MAX_WEIGHT}Kg")

    def update_value_label(self):
        self.self.value_label.config(text=f"Total Value in Backpack: ${self.total_backpack}")

    def calculate_total_value(self, items):
        return sum(item.value for item in items)

    def create_widgets(self):
        self.junk_listbox.pack(pady=10)

        for item in self.junk_items:
            self.junk_listbox.insert(tk.END, str(item))

        add_button = tk.Button(self.root, text="Add to Backpack", command=lambda: self.add_to_backpack(self.junk_items[self.junk_listbox.curselection()[0]]))
        add_button.pack(pady=5)

        remove_button = tk.Button(self.root, text="Remove from Backpack", command=self.remove_from_backpack)
        remove_button.pack(pady=5)

        self.total_weight = 0
        self.weight_label = tk.Label(self.root, text=f"Total Weight: {self.total_weight}Kg / {self.MAX_WEIGHT}Kg")
        self.weight_label.pack(pady=5)

        self.total_backpack = 0
        self.value_label = tk.Label(self.root, text=f"Total Value in Backpack: ${self.total_backpack}")
        self.value_label.pack(pady=5)

        total_value_label = tk.Label(self.root, text=f"Total Value of All Items: ${self.calculate_total_value(self.junk_items)}")
        total_value_label.pack(pady=5)

        self.backpack_contents.pack(pady=10)