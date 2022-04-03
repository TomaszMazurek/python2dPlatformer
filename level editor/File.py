import os
from tkinter import filedialog


FILEBROWSER_PATH = os.path.join(os.getenv('WINDIR'), 'explorer.exe')

class File:
    def __init__(self):
        self.world = []

    @staticmethod
    def save_file():
        file = filedialog.asksaveasfile(initialfile='lvl1.lvl', defaultextension=".lvl",
                                     filetypes=[("All Files", "*.*"), ("Platformer level file", "*.lvl")])
        fob = open(file, 'w')
        fob.close()
