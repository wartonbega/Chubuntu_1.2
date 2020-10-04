import cv2
import numpy as np

drawing = False
ix,iy = -1,-1

img = cv2.imread('DATA/dog_backpack.jpg')

def clicked(event,x,y,flags,param):

    global drawing,ix,iy

    #FOR LEFT CLICKING
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.rectangle(img,(ix,iy),(x,y),(255,0,0),-1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img,(ix,iy),(x,y),(255,0,0),-1)

    #FOR RIGHTCLICKING
    elif event == cv2.EVENT_RBUTTONDOWN:
        drawing = True
        ix,iy = x,y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.rectangle(img,(ix,iy),(x,y),(222,255,255),-1)
    elif event == cv2.EVENT_RBUTTONUP:
        drawing = False
        cv2.rectangle(img,(ix,iy),(x,y),(222,255,255),-1)

cv2.namedWindow(winname='backpackpup')
cv2.setMouseCallback('backpackpup',clicked)
while True:
    cv2.imshow('backpackpup',img)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows