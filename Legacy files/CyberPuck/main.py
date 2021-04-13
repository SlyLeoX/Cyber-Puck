import pygame
from CyberPuck.Application import Application
import tkinter as tk
from tkinter import *
import tkinter.font as font
from PIL import ImageTk, Image

width = 1366
height = 768

root = tk.Tk()
Title = root.title("CyberPuck")
root.geometry("1366x768")
root.configure(bg='black')

img = ImageTk.PhotoImage(Image.open("logo1.png"))
label2 = tk.Label(root, image=img)

label2.pack(padx=100, pady=50)

def onclick():
    app = Application()
    app.menu()

    clock = pygame.time.Clock()

    while app.statut:
        tkey = pygame.key.get_pressed()
        for event in pygame.event.get():
            if tkey[pygame.K_TAB]:
                print("tab")

        app.update()
        clock.tick(30)


    root.destroy()

f = font.Font(size=30, weight="bold")
button = tk.Button(root, text="Click on this button to start...", bg='red', fg='white', command=onclick)
button.bind('<Button-1>', onclick)
button['font'] = f

button.pack()

root.mainloop()
pygame.quit()