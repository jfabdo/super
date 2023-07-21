import cv2 as cv
from random import randint

def placeimg2(img1,img2,times):
    rows,cols,channels = img1.shape
    rows2,cols2,channels2 = img2.shape
    # roi = img1[0:-rows,0:-cols]
    img2gray = cv.cvtColor(img2,cv.COLOR_BGR2GRAY)
    ret, mask = cv.threshold(img2gray, 10, 255, cv.THRESH_BINARY)
    mask_inv = cv.bitwise_not(mask)
    for _ in range(times): 
        #add a resizer to resize based on where it is in the picture
        xcoord = randint(0,rows-rows2)
        ycoord = randint(0,cols-cols2)
        roi = img1[xcoord:xcoord+rows,ycoord:ycoord+cols]
        img1_bg = cv.bitwise_and(roi,roi,mask = mask_inv)
        img2_fg = cv.bitwise_and(img2,img2,mask = mask)
        dst = cv.add(img1_bg,img2_fg)
        img1[0:rows, 0:cols ] = dst



spider = cv.imread('doodles/spider 2.png')
cv.imshow('spider',spider)
cv.waitKey(0)
cv.destroyAllWindows()