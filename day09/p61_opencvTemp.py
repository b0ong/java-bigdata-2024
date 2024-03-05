# flie: p61_opencv.py
# desc: OpenCV 계속

import cv2

image = cv2.imread('/Users/gukjinhan/Documents/GitHub/java-bigdata-2024/day09/coby.jpeg', cv2.IMREAD_UNCHANGED) # 원본

height, width, channels = image.shape

cv2.imshow('Coby the cat', image) # 원본

cv2.waitKey(0)
cv2.destroyAllWindows()