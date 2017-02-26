import tkinter as tk
from tkinter import *
from PIL import Image,ImageTk
import pygame
from pygame import *
import numpy as np
from sklearn.cluster import KMeans
from scipy.io.wavfile import write
from numpy import linspace,sin,pi,int16, concatenate

center_array = None #dominant colors RGB
image_path = 'flower.jpg'
sound_name = 'soundDemo.wav'

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
    generateMusic()


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
    mixer.music.load(sound_name)
    mixer.music.play()

def printArray():
    print ("now\n")
    global center_array
    print (center_array)

# tone synthesis
def note(freq, len, amp=1, rate=44100):
     t = linspace(0,len,len*rate)
     data = sin(2*pi*freq*t)*amp
     return data.astype(int16)

# 
def generateMusic():
    global center_array
    freqChart = [261,277,293,311,329,349,370,392,415,440,466,493]
    bright1 = (center_array[0,0] + center_array[0,1] + center_array[0,2])/3;
    bright2 = (center_array[1,0] + center_array[1,1] + center_array[1,2])/3;
    bright3 = (center_array[2,0] + center_array[2,1] + center_array[2,2])/3;
    f1=440
    f2=440
    f3=440
    
    b =[bright1,bright2,bright2]
    freqs= [f1,f2,f3]

    for i in range(3):
        if (b[i] < 20 ):
            freqs[i] = freqChart[0]
        if (b[i] >= 20 and b[i] <40 ):
            freqs[i] = freqChart[1]
        if (b[i] >= 40 and b[i] <60 ):
            freqs[i] = freqChart[2]
        if (b[i] >= 60 and b[i] <80 ):
            freqs[i] = freqChart[3]
        if (b[i] >= 80 and b[i] <100 ):
            freqs[i] = freqChart[4]
        if (b[i] >= 100 and b[i] <120 ):
            freqs[i] = freqChart[5]
        if (b[i] >= 120 and b[i] <140 ):
            freqs[i] = freqChart[6]
        if (b[i] >= 140 and b[i] <160 ):
            freqs[i] = freqChart[7]
        if (b[i]>= 160 and b[i] <180 ):
            freqs[i] = freqChart[8]
        if (b[i] >= 180 and b[i] <200 ):
            freqs[i] = freqChart[9]
        if (b[i] >= 200 and b[i] <220 ):
            freqs[i] = freqChart[10]
        if (b[i] >= 220 and b[i] <240 ):
            freqs[i] = freqChart[11]

    
    print (freqs[0])
    print (freqs[1])
    print (freqs[2])
    tone1 = note(freqs[0],0.3,amp=20000)
    tone2 = note(freqs[1],0.3,amp=20000)
    tone3 = note(freqs[2],0.3,amp=20000)
    tone4 = note(freqs[0],0.3,amp=20000)
    tone5 = note(freqs[1],0.3,amp=20000)
    tone6 = note(freqs[2],0.3,amp=20000)

    tone = concatenate ((tone1,tone2,tone3,tone6,tone5,tone4),axis = 0)
    write(sound_name,44100,tone) 

    
def main():
  
    root = Tk()
    root.wm_title('Audible Image')
    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Display Image", command=displayImg)
    filemenu.add_command(label="Dominant Color", command=analyzeImg)
    filemenu.add_command(label="Play Music", command=playMusic)
    menubar.add_cascade(label="File", menu=filemenu)

    root.config(menu=menubar)
    root.mainloop()

if __name__ == '__main__':
    main()  

