import cv2
import os
import numpy as np

def apply_filters(folder):
    for i, filename in enumerate(os.listdir(folder)):
        img = cv2.imread(path+filename)
        kernel5_5 = np.ones((5,5),np.float32)/25
        img_filtered_blur_5_5 = cv2.blur(img, (5,5))
        img_filtered_5_5 = cv2.filter2D(img,-1,kernel5_5)
        if img is not None:
            filename = 'img'+ str(i) + '.png'
            filename2 = 'img' + str(i) + '_blur_5_5.png'
            filename3 = 'img' + str(i) + '_5_5.png'
            cv2.imwrite(path + filename, img)
            cv2.imwrite(path + filename2, img_filtered_blur_5_5)
            cv2.imwrite(path + filename3, img_filtered_5_5)

path = r"/home/valentin/Downloads/jelek/All_datasets/Waters/"
apply_filters(path)










