import cv2
import numpy as np

red  = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
black = (0,0,0)
yellow = (0,255,255)
colors = [red,green,blue,white,black,yellow]

im1 = np.zeros((170,170,3))
i = 0
for y in range(0,170,10):
    for x in range(0,170,10):
        im1[y:y+10,x:x+10] = colors[i%6]
        i = i+1
#im1[0:10,0:10,] = red
#im1[10:20,0:10,] = green
#im1[20:30,0:10,] = blue
#im1[30:40,0:10,] = white
#im1[40:50,0:10,] = black
#im1[50:60,0:10] = yellow

cv2.imwrite('image2.png', im1)
#cv2.imshow('',im1)
#cv2.waitKey(-1)