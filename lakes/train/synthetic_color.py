import cv2
import os
import numpy as np

def apply_filters(folder):
    for i, filename in enumerate(os.listdir(folder)):
        if filename[0] != "i":
            img = cv2.imread(path+filename)
            kernel5_5 = np.ones((5,5),np.float32)/25
            print(filename)
            if img is not None:
                img_filtered_blur_5_5 = cv2.blur(img, (5,5))
                img_filtered_5_5 = cv2.filter2D(img,-1,kernel5_5)
                filename2 = 'img' + str(i) + '_blur_5_5.png'
                filename3 = 'img' + str(i) + '_5_5.png'
                cv2.imwrite(path + filename2, img_filtered_blur_5_5)
                cv2.imwrite(path + filename3, img_filtered_5_5)

path = r"/home/valentin/Downloads/jelek/All_datasets/dataset_lakes/dataset_vizek/val"
apply_filters(path)










