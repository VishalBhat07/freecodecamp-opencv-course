import cv2 as cv
 
capture = cv.VideoCapture("./videos/cat.MP4")
    
while True:
    ret, frame = capture.read()
    cv.imshow('Video',frame )
    
    if cv.waitKey(1) == ord('q'):
        break
 
# When everything done, release the capture
capture.release()
cv.destroyAllWindows()