import sys
import tkinter as tk

class Application(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

        self.create_widgets()
    
    def create_widgets(self):
        pw_main = tk.PanedWindow(self.master)
        pw_main.pack(expand=True, fill=tk.BOTH)

        left_frame = tk.PanedWindow(pw_main, width = 300, bg="red")
        pw_main.add(left_frame)
        right_frame = tk.PanedWindow(pw_main, width = 300, bg="yellow")
        pw_main.add(right_frame)




# master_window
root = tk.Tk()
apps = Application(master=root)
# title
apps.master.title("Pass Manager")
# window size
apps.master.geometry("600x400")

# show window
apps.mainloop()
