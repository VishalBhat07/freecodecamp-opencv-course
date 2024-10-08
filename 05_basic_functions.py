import cv2 as cv

img = cv.imread("./photos/cat1.jpg")
cv.imshow("Cat",img)

# 1. Converting an image to greyscale

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray Cat",gray)

# 2. Blur an image --> Guassian blur

blur = cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow("Blurred Cat",blur)

# 3. Edge cascade in an image --> Canny edge detection

canny = cv.Canny(blur,125,175)
cv.imshow("Edge Cat",canny)

# 4. Dilating an image

dilated = cv.dilate(canny,(3,3),iterations=3)
cv.imshow("Dilated Cat",dilated)

# 5. Eroding an image

eroded = cv.erode(dilated,(3,3),iterations=3)
cv.imshow("Eroded Cat",eroded)

# 5. Resizing an image

resized = cv.resize(img,(340,160),interpolation=cv.INTER_CUBIC)
cv.imshow("Resized Cat",resized)

# 6. Cropping an image

cropped = img[20:350,100:450]
cv.imshow("Cropped Cat",cropped)


cv.waitKey(0)