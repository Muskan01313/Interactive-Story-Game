import tkinter as tk
from story import Story

class InteractiveFictionGame:
    def __init__(self, root):
        self.root = root
        self.story = Story()
        self.create_widgets()
        self.update_scene()

    def create_widgets(self):
        self.text = tk.Text(self.root, height=10, width=50)
        self.text.pack()

        self.choice_entry = tk.Entry(self.root)
        self.choice_entry.pack()

        self.submit_button = tk.Button(self.root, text="Submit", command=self.process_choice)
        self.submit_button.pack()

    def update_scene(self):
        self.text.delete(1.0, tk.END)
        scene = self.story.get_scene()
        self.text.insert(tk.END, scene["text"])

    def process_choice(self):
        choice = self.choice_entry.get().lower()
        self.choice_entry.delete(0, tk.END)
        self.story.make_choice(choice)
        self.update_scene()

def create_widgets(self):
    self.text = tk.Text(self.root, height=10, width=50)
    self.text.grid(row=0, column=0, columnspan=2)

    self.choice_entry = tk.Entry(self.root)
    self.choice_entry.grid(row=1, column=0, sticky='ew')

    self.submit_button = tk.Button(self.root, text="Submit", command=self.process_choice)
    self.submit_button.grid(row=1, column=1)
