# flie: p63_opencv.py
# desc: OpenCV 영상처리

import cv2

samplePath = '/Users/gukjinhan/Documents/GitHub/java-bigdata-2024/day09/earth.mp4'
cap = cv2.VideoCapture(samplePath) # 0은 웹캠 또는 문자열로 동영상 경로 삽입

while True:
    ret, frame = cap.read()
    

    if not ret:
        cap = cv2.VideoCapture(samplePath)
        continue
    
    ## 영상편집
    blur = cv2.blur(frame, (10,10))
    flip = cv2.flip(frame, 0) 
    
    cv2.imshow('original', frame)
    cv2.imshow('blur', blur)
    cv2.imshow('flip', flip)

    key = cv2.waitKey(5) # 5ms 동안 딜레이 
    if key == ord('q'): # esc = 27, q = ord('q')
        break
    elif key == ord('c'): # 화면캡쳐
        cv2.imwrite('/Users/gukjinhan/Documents/GitHub/java-bigdata-2024/day09/capt.jpg', frame)
        
cap.release()
cv2.destroyAllWindows()