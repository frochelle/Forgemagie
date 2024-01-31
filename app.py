"""
Class for front
"""

import tkinter as tk
from tkinter import ttk


class App:

    def __init__(self, items):
        # Root declaration + dimensions
        root = tk.Tk()
        root.geometry('500x300')

        # Just some text
        label = tk.Label(root, text='Choose your item')
        label.pack(pady=10)

        # Picker to choose item to fm
        options = [item.name for item in items]
        self.selected_option = tk.StringVar()
        item_picker = ttk.Combobox(root, textvariable=self.selected_option, values=options)
        item_picker.pack(pady=10)

        # Button to confirm choice
        confirm_button = tk.Button(root, text='Confirm', command=self.confirm_click)
        confirm_button.pack(pady=10)

        root.mainloop()

    def confirm_click(self):
        print('option : ' + self.selected_option.get())
