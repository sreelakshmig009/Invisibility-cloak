import cv2
cap = cv2.VideoCapture(0) #opening my webcam

while cap.isOpened():
    ret,back = cap.read() #read my image
    if ret:
        cv2.imshow("image",back)
        if cv2.waitKey(5) == ord('q'): #ord gives the unicode value of q
            #when q is pressed,image is saved
            cv2.imwrite('image.jpg', back)
            break

cap.release()
cv2.destroyAllWindows()
