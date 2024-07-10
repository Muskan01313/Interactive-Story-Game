import tkinter as tk
from game import InteractiveFictionGame

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Interactive Fiction Game")
    game = InteractiveFictionGame(root)
    root.mainloop()
