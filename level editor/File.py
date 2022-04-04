import pickle
from tkinter import filedialog, Tk


class File:
    def __init__(self):
        self.world = []
        self.root = Tk()

    @staticmethod
    def save_file(lvl):
        root = Tk()
        file = filedialog.asksaveasfile(initialfile='lvl1.lvl', defaultextension=".lvl",
                                     filetypes=[("All Files", "*.*"), ("Platformer level file", "*.lvl")])

        fob = open(file.name, 'wb')
        pickle.dump(lvl, fob)
        fob.close()
        root.destroy()


    @staticmethod
    def load_file():
        root = Tk()
        file = filedialog.askopenfile( defaultextension=".lvl",
                                     filetypes=[("All Files", "*.*"), ("Platformer level file", "*.lvl")])

        fob = open(file.name, 'rb')
        world = pickle.load(fob)
        fob.close()
        root.destroy()
        return world
