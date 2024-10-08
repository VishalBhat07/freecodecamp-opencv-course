import cv2 as cv
import numpy as np

img = cv.imread('./photos/cat1.jpg')

cv.imshow('Cat', img)


def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)


translated = translate(img, 100, 100)

cv.imshow('Rotated image', translated)

def rotate(img,angle,rotPoint = None):
    (height,width) = img.shape[:2]


cv.waitKey(0)
