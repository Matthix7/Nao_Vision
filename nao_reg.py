#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 08:45:16 2019

@author: adamph
"""
import cv2
from nao_vision import getCentreBall

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

     #Convert BGR to HSV
    found, error, center, radius = getCentreBall(frame)

# When everything done, release the capture
cap.release()
