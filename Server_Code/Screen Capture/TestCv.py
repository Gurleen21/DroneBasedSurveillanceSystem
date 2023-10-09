import cv2
import numpy as np
img = cv2.imread('C:/Users/ishit/Desktop/Screenshot_2021-11-13-18-04-25-26_6012fa4d4ddec268fc5c7112cbb265e7.jpg',1)
screen = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
cv2.imwrite('f2.png',screen)