import cv2
import numpy as np  

cap = cv2.VideoCapture(0)
back = cv2.imread('./image.jpg')
kernel = np.ones((5,5), np.uint8)

while cap.isOpened():
    ret,frame = cap.read()
    
    if ret:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        # lower = hue-10 , higher = hue+10 , 255 ,255
        red = np.uint8([[[0,0,255]]]) # bgr value of red , b=0,g=0,r=full
        hsv_red = cv2.cvtColor(red, cv2.COLOR_BGR2HSV)
        # get hsv vslue of red from bgr
        print(hsv_red)
      

       # threshold the hsv value only to get red color
        l_red = np.array([0,100,100])
        u_red = np.array([10,255,255])

        mask = cv2.inRange(hsv, l_red, u_red)
        #cv2.imshow("mask" , mask) 

        # part 1 is all things red
        part1 = cv2.bitwise_and(back, back, mask=mask) #replace the red with background image
        #cv2.imshow("part1" , part1) 

        mask = cv2.bitwise_not(mask)

        #part 2 is all things not red
        part2 = cv2.bitwise_and(frame, frame, mask=mask)
        #cv2.imshow("part2" , part2) 

        
        img_erosion = cv2.erode(back, kernel, iterations=1)
        img_dilation = cv2.dilate(back, kernel, iterations=1)

        #cv2.imshow('Input',back)

        #cv2.imshow('Dilation',img_dilation)
        #cv2.imshow('Erosion',img_erosion)

        cv2.imshow("cloak" , part1 + part2)




        
        if cv2.waitKey(5) == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
