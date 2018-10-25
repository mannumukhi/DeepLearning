import cv2
import numpy as np
import time
image = cv2.imread('./input_images/Image2.jpg',0)
F1 = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], dtype = np.float)
F2 = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]], dtype = np.float)
print("Img size:",image.shape)
img_row = image.shape[0]
img_col = image.shape[1]
print(img_row,img_col)
#resized_image = cv2.resize(image, (1024,1024), fx=0.5, fy=0.5)
#newimg_row = resized_image.shape[0]
#newimg_column = resized_image.shape[1]
F1_new = np.zeros((img_row,img_col))
F2_new = np.zeros((img_row,img_col))
New_image = np.zeros((img_row,img_col))

#image = np.pad(image, (1,1), 'edge')

for i in range(1, img_row-1):
    for j in range(1, img_col-1):
        #print("type:",image.shape)
        #Filtering with horizontal filter
        gx = (F1[0][0] * image[i-1][j-1]) + (F1[0][1] * image[i-1][j]) + (F1[0][2] * image[i-1][j+1]) + \
             (F1[1][0] * image[i][j-1]) + (F1[1][1] * image[i][j]) + (F1[1][2] * image[i][j+1]) + \
             (F1[2][0] * image[i+1][j-1]) + (F1[2][1] * image[i+1][j]) + (F1[2][2] * image[i+1][j+1])

        # Filtering with Vertical Filter
        gy = (F2[0][0] * image[i-1][j-1]) + (F2[0][1] * image[i-1][j]) + (F2[0][2] * image[i-1][j+1]) + \
             (F2[1][0] * image[i][j-1]) + (F2[1][1] * image[i][j]) + (F2[1][2] * image[i][j+1]) + \
             (F2[2][0] * image[i+1][j-1]) + (F2[2][1] * image[i+1][j]) + (F2[2][2] * image[i+1][j+1])

        F1_new[i-1][j-1] = gx
        F2_new[i-1][j-1] = gy

        #Calculating the gradient
        gres = np.sqrt(gx * gx + gy * gy)
        New_image[i-1][j-1] = gres

#cv2.imwrite('./GX.png',F1_new)
#cv2.imwrite('./GY.png',F2_new)
cv2.imwrite('./Output_Image.jpg',New_image)
