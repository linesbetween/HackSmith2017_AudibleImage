from PIL import Image
import time
import pygame
from pygame import *

def main():
    filename = input("Enter filename: ")
    image = Image.open(filename)
    image.show() 
    pixels = image.load()
    width, height = image.size

    for x in range(0,width,10):
        for y in range(0,height,10):
            cpixel = pixels[x, y]
            
            m = (cpixel.index(max(cpixel)))

            if (cpixel[0] == cpixel[1] ==cpixel[2]):
                #pygame.init()
                #pygame.mixer.init()
                mixer.music.load("ChordB.wav")
                mixer.music.play()
                print("I am here")
                
            elif (m == 0):
                pygame.init()
                pygame.mixer.init()
                mixer.music.load("ChordA.wav")
                mixer.music.play()

            elif (m ==1 ):
                pygame.init()
                pygame.mixer.init()
                mixer.music.load("MiddleC.wav")
                mixer.music.play()

            elif (m ==2 ):
                pygame.init()
                pygame.mixer.init()
                mixer.music.load("ChordC.wav")
                mixer.music.play()
    
main()
