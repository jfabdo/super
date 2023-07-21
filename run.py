import cv2 as cv
from random import randint

INITIALSIZE = 2
FINALSIZE = 20

def placeimg2(img1,img2,times):
    rows,cols,channels = img1.shape
    rows2,cols2,channels2 = img2.shape
    
    for _ in range(times): 
        #resizes based on where it is in the picture
        ycoord = randint(0,rows-rows2//FINALSIZE) 
        alpha = ycoord/rows
        size = round(INITIALSIZE * (1 - alpha) + FINALSIZE * alpha)
        img3 = img2[::size]

        #choose the x coordinate
        rows3,cols3,channels3 = img3.shape
        xcoord = randint(0,cols - cols3)

        #copy the new image to image 1
        img3gray = cv.cvtColor(img3,cv.COLOR_BGR2GRAY)
        ret, mask = cv.threshold(img3gray, 10, 255, cv.THRESH_BINARY)
        mask_inv = cv.bitwise_not(mask)
        
        roi = img1[ycoord:ycoord + rows, xcoord:xcoord + cols]
        img1_bg = cv.bitwise_and(roi,roi,mask = mask_inv)
        img3_fg = cv.bitwise_and(img3,img3,mask = mask)
        dst = cv.add(img1_bg,img3_fg)
        img1[ycoord:ycoord + rows, xcoord:xcoord + cols] = dst



spider = cv.imread('doodles/spider 2.png')
cv.imshow('spider',spider)
cv.waitKey(0)
cv.destroyAllWindows()