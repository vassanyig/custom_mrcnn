import cv2
import os
import numpy as np

def apply_filters(folder):
    for i, filename in enumerate(os.listdir(folder)):
        img = cv2.imread(path+filename)
        kernel5_5 = np.ones((5,5),np.float32)/25
        if img is not None:
            img_filtered_blur_5_5 = cv2.blur(img, (5,5))
            img_filtered_5_5 = cv2.medianBlur(img,5)
            filename = 'img' + str(i) + '.png'
            filename2 = 'img' + str(i) + '_a.png'
            filename3 = 'img' + str(i) + '_b.png'
            cv2.imwrite(path + filename, img)
            cv2.imwrite(path + filename2, img_filtered_blur_5_5)
            cv2.imwrite(path + filename3, img_filtered_5_5)
            print(filename, filename2, filename3)

path = r"/home/valentin/Downloads/jelek/All_datasets/dataset_lakes/dataset_vizek/train/"
apply_filters(path)











