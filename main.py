import cv2 
import numpy as np 
import cvzone 


img = cv2.imread('paper.jpg')
coordinates = np.float32([[16,86],[487,19],[106,649],[581,567]])

width = 400
height = 500

converted_points = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(coordinates,converted_points)
output_img = cv2.warpPerspective(img,matrix,(width,height))

final_out = cvzone.stackImages([img,output_img],2,0.70)

cv2.imwrite('output_image.jpg', output_img)

cv2.imshow('frame', final_out)
# cv2.imshow('output_frame', output_img)
cv2.waitKey(0)