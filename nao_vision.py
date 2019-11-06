# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 10:23:40 2019

@author: Matthieu
"""

import cv2
import numpy as np


def getCentreBall(frame):
    
    rows,cols,height = frame.shape
    
    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # define range of blue color in HSV
    # voir https://www.google.com/search?client=firefox-b&q=%23D9E80F
    # convertir valeur dans [0,179], [0,255], [0,255]
    
    teinte_min = 30
    teinte_max = 70
    sat_min = 30
    sat_max = 255
    val_min = 50
    val_max = 255
    
    lower_yellow = np.array([int(teinte_min/2),int(sat_min*255/100),int(val_min*255/100)])
    upper_yellow = np.array([int(teinte_max/2),int(sat_max*255/100),int(val_max*255/100)])

    
    # Threshold the HSV image to get only yellow/green colors
    mask1 = cv2.inRange(hsv, lower_yellow, upper_yellow)
    mask1 = cv2.medianBlur(mask1, 11)
    
    
    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask1)
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask1)
    cv2.imshow('res',res)
    
    
    
    ret1,thresh1 = cv2.threshold(mask1,127,255,0)
    im2,contours1,hierarchy1 = cv2.findContours(thresh1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cnt1 = contours1[0]
    
    
    (x1,y1),radius1 = cv2 .minEnclosingCircle(cnt1)
    center1 = (int(x1),int(y1))
    radius1 = int(radius1)
    
    cv2.circle(frame,center1,radius1,(255,0,0),2)
    
    print("Centre balle 1 :", center1)
    
    cv2.imshow('Reco_balles',frame)
#    cv2.waitKey(0)

    centreError = ((center1[0]-rows/2)*100/rows, (center1[1]-cols/2)*100/cols)
    
    if radius1 > 10:
        found = True
    else:
        found = False
    
    return found, centreError, center1, radius1



# Real images
for i in range(422):
    print("NewImage", str(i).zfill(4))
    try:
        image = cv2.imread("/home/matthieu/Documents/Annee_3/UV56_Visual_Servoing/naorealimgs/naoreal_"+str(i).zfill(4)+".png")
        c, r = getCentreBall(image)
    except:
        print("Unable to read that image")
    key = cv2.waitKey(0) & 0xFF
    if key == 27:
        break




#Simu images
#for i in range(131):
#    print("NewImage", str(i).zfill(4))
#    try:
#        image = cv2.imread("/home/matthieu/Documents/Annee_3/UV56_Visual_Servoing/naosimimgs/naosimimg_"+str(i).zfill(4)+".png")
#        c, r = getCentreBall(image)
#    except:
#        print("Unable to read that image")
#    key = cv2.waitKey(0) & 0xFF
#    if key == 27:
#        break

















