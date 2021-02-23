import cv2
import numpy as np
import pandas as pd
import os

cwd = os.getcwd()
print(cwd)


img = cv2.imread("lena-image.jpg",0)
img2 = cv2.imread("lena-image.jpg",1)
img3 = cv2.imread("lena-image.jpg",-1)

print("PARAM 0: \n")
print(img)

print("\n\n\n\nPARAM 1: \n")
print(img2)

print("\n\n\n\nPARAM -1: \n")
print(img3)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()