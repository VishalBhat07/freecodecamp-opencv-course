import cv2 as cv

img = cv.imread("./photos/cat1.jpg")
 
cv.imshow("Display window", img)

k = cv.waitKey(0)
