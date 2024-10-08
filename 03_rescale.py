import cv2 as cv
 
capture = cv.VideoCapture(0)
    
def rescaleFrame(frame,scale = 0.75):
    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)
    
    dimensions =( width , height)
    
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

def changeRes(width,height) :
    capture.set(3,width)
    capture.set(4,height)
    
while True:
    isTrue, frame = capture.read()

    cv.imshow('Video',rescaleFrame(frame) )
    
    if cv.waitKey(1) == ord('q'):
        break
 
# When everything done, release the capture
capture.release()
cv.destroyAllWindows()