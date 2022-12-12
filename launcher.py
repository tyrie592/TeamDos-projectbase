import tkinter as tk

root = tk.Tk()
img = tk.Image("photo", file="/Users/jose.pacheco/Downloads/TC-001")
root.iconphoto(True, img)  # you may also want to try this.
root.tk.call('wm', 'icon-photo', root._w, img)

root.mainloop()
