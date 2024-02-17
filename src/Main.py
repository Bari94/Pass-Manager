import sys
import tkinter as tk

class Application(tk.Frame):
    D_LOG = True
    def __init__(self, main):
        self.main = main

        self.create_widgets()
    
    def create_widgets(self):
         print('DEBUG:----{}----'.format(sys._getframe().f_code.co_name)) if self.D_LOG else ""


# main_window
root = tk.Tk()
apps = Application(root)
# title
apps.main.title("Pass Manager")
# window size
apps.main.geometry("800x400")

# show window
apps.main.mainloop()
