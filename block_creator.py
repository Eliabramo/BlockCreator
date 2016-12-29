# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 09:42:01 2016

@author: eli
"""
import cv2
import numpy as np

im = cv2.imread('image1.png',cv2.CV_LOAD_IMAGE_COLOR)

cv2.imshow('image',im)
cv2.waitKey(0)