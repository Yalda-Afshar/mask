from PIL import Image
from skimage.morphology import thin, skeletonize
import matplotlib.pyplot as plt
import cv2
from numpy import *
import numpy as np
import scipy.ndimage
img1 = cv2.imread('1.bmp', 0)
ret, th1 = cv2.threshold(img1, 250, 255, cv2.THRESH_BINARY)
imgbw = ~th1
imgbw2 = imgbw/255
skeli = skeletonize(imgbw2)
skeli = skeli.astype(np.uint8)

#orib be rast va paeen
w1 = array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
#amudi
w2 = array([[0, 1, 0], [0, 1, 0], [0, 1, 0]])
#orib be chap va paeen
w3 = array([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
#ofoqi
w4 = array([[0, 0, 0], [1, 1, 1], [0, 0, 0]])
filteredpoint1 = scipy.ndimage.correlate(skeli, w1, mode='nearest').transpose()
filteredpoint2 = scipy.ndimage.correlate(skeli, w2, mode='nearest').transpose()
filteredpoint3 = scipy.ndimage.correlate(skeli, w3, mode='nearest').transpose()
filteredpoint4 = scipy.ndimage.correlate(skeli, w4, mode='nearest').transpose()

vertical_direction = (filteredpoint4 == 3).sum()
Diagonal_direction_left = (filteredpoint3 == 3).sum()
Diagonal_direction_right = (filteredpoint1 == 3).sum()
horizental_direction = (filteredpoint2 == 3).sum()

print(vertical_direction)
print(Diagonal_direction_left)
print(Diagonal_direction_right)
print(horizental_direction)