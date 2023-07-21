import cv2 as cv
import numpy as np
from random import randint

INITIALSIZE = 5
FINALSIZE = 20

def placeimg2(img1,img2,times):
    rows,cols,channels = img1.shape
    rows2,cols2,channels2 = img2.shape
    
    for _ in range(times): 
        #resizes based on where it is in the picture
        ycoord = randint(0,rows-rows2//FINALSIZE) 
        alpha = ycoord/rows
        size = round(INITIALSIZE * (1 - alpha) + FINALSIZE * alpha)
        img3 = cv.resize(img2,(rows2//size, cols2//size))

        #choose the x coordinate
        rows3,cols3,channels3 = img3.shape
        xcoord = randint(0,cols - cols3)

        #copy the new image to image 1
        img3gray = cv.cvtColor(img3,cv.COLOR_BGR2GRAY)
        ret, mask = cv.threshold(img3gray, 0, 255, cv.THRESH_BINARY)
        mask_inv = cv.bitwise_not(mask)
        
        roi = img1[ycoord:ycoord + rows3, xcoord:xcoord + cols3]
        # print(xcoord,ycoord,rows3,cols3,size)
        img1_bg = cv.bitwise_and(roi,roi,mask = mask_inv)
        img3_fg = cv.bitwise_and(img3,img3,mask = mask)
        dst = cv.add(img1_bg,img3_fg)
        img1[ycoord:ycoord + rows3, xcoord:xcoord + cols3] = dst


spider = cv.imread('../../doodles/spider 2.png')
assert spider is not None, "no spider pic"

spiderr = cv.imread('../../doodles/spider 2r.png')
assert spiderr is not None, "no spider pic"

height = 2048
canvas = np.zeros((height*30,500,3), dtype=np.uint8)
# canvas = np.zeros((500,500,3),dtype=np.uint8)
e1 = cv.getTickCount()
for _ in range(100):
    placeimg2(canvas,spider, 50)
    placeimg2(canvas,spiderr, 50)
e2 = cv.getTickCount()
time = (e2 - e1)/ cv.getTickFrequency()
print(time)
for i in range(30):
    cv.imwrite(f'spidershow{i+1}.png',canvas[i*height:i*height+height-1,:])

# cv.imshow('canvas',canvas[i*height:i*(height+1)-1,0:500])
# cv.waitKey(0)
# cv.destroyAllWindows()