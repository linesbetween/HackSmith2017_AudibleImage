import tkinter as tk
from tkinter import *
from PIL import Image,ImageTk
import pygame
from pygame import *
import numpy as np
from sklearn.cluster import KMeans

center_array = None #dominant colors RGB
image_path = 'kumamon.jpg'

def displayImg(): #place image in window

    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)
    
    imageLbl = tk.Label(image = photo)
    imageLbl.image = photo
    imageLbl.pack(side= "bottom")


def analyzeImg(): #find dominant color #pass image obj! #returns colors
    im = Image.open( image_path )
    farray = np.asarray(im, dtype = np.uint8)
    farray = farray.reshape((farray.shape[0] * farray.shape[1], 3))
    kmeans = KMeans(n_clusters=3, random_state=0).fit(farray)
    print (kmeans.cluster_centers_)
    global center_array
    center_array  = kmeans.cluster_centers_.astype(int)
    draw_color_bar(center_array)

def draw_color_bar(center_array):
    
     canvas = tk.Canvas()
     canvas.create_rectangle(30, 10, 150, 40, 
            fill=rgb_to_hex(center_array[0,0], center_array[0,1], center_array[0,2]))
     canvas.create_rectangle(150, 10, 270, 40, 
            fill=rgb_to_hex(center_array[1,0], center_array[1,1], center_array[1,2]))
     canvas.create_rectangle(270, 10, 390, 40, 
            fill=rgb_to_hex(center_array[2,0], center_array[2,1], center_array[2,2]))            
     canvas.pack(fill=BOTH, expand=1)
     canvas.pack(side = "top")

def rgb_to_hex(red, green, blue):
    """Return color as #rrggbb for the given color values."""
    return '#%02x%02x%02x' % (red, green, blue)

def playMusic(): # play music according to center_array
    pygame.mixer.init()
    pygame.init()
    mixer.music.load("Chord.wav")
    mixer.music.play()

def printArray():
    print ("now\n")
    global center_array
    print (center_array)

    
def main():
  
    root = Tk()
    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Display Image", command=displayImg)
    filemenu.add_command(label="Dominant Color", command=analyzeImg)
    filemenu.add_command(label="Play Music", command=palyMusic)
    menubar.add_cascade(label="File", menu=filemenu)

    root.config(menu=menubar)
    root.mainloop()

if __name__ == '__main__':
    main()  

