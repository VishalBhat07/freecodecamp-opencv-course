import cv2 as cv
import numpy as np

img = cv.imread("./photos/cat1.jpg")

# Creating a blank image
blank = np.zeros((500, 500, 3), dtype="uint8")

# cv.imshow("Blank",blank)

#  Paint the entire image green

# blank[200:200,300:400] = 0,255,0
# cv.imshow("Green",blank)

# blank[:] = 0,0,255q
# cv.imshow("Red",blank)

# blank[:] = 255,0,0
# cv.imshow("Blue",blank)

# blank[200:400,200:400] = 255,0,0

# Drawing a rectangle

cv.rectangle(blank, (0, 0),(blank.shape[0]//2, blank.shape[1]//2), (0, 0, 255), thickness=cv.FILLED)

#  Drawing a circle
cv.circle(blank, (350, 350), 50, (0, 255, 0), thickness=3)

# Drawing a line
cv.line(blank, (0, 0),(blank.shape[0]//2, blank.shape[1]//2), (255, 255, 255), thickness=5)

#  Write text on an image
text = input("Enter some text : ")
cv.putText(blank, text, (100, 350),cv.FONT_HERSHEY_SCRIPT_COMPLEX, 1.0, (0, 255, 0), 2)

cv.imshow("Drawing Shapes", blank)

cv.waitKey(0)
