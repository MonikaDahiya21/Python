import tkinter as tk
import pyautogui

root= tk.Tk()

size1 = tk.Canvas(root, width = 300, height = 300)
size1.pack()

def takesnap():
      screenshot = pyautogui.screenshot()
      screenshot.save(r'C:\Users\Monika Swami\Desktop\Screenshot.png')
Button1 = tk.Button(text='take snaapy', command=takesnap, bg='Red',fg='White', font=10)
size1.create_window(150, 150, window=Button1)



root.mainloop()

