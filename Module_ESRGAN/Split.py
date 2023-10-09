import cv2
from Config import *
import numpy as np


def merge(image_list,row_size,colsize):
    start = 1
    final_img = ''
    for j in range(0,colsize):
        row_img = cv2.imread(image_list[j*row_size])
        for i in range(1,row_size):
            row_img = np.concatenate((row_img, cv2.imread(image_list[(j*row_size)+i])), axis=1)
        if start==1:
            start =0
            final_img = row_img
        else:
            final_img = np.concatenate((final_img, row_img), axis=0)
    cv2.imwrite(r'C:\Users\ishit\Desktop\DBSS\Module_ESRGAN\Split_Images\image.jpg',final_img)
    return final_img

#
# def merge(image_list,row_size,colsize):
#     j = 0
#     final_img = ''
#     for j in range(colsize):
#         # if(j*row_size>len(image_list)):
#         #     break
#         row_img = cv2.imread(image_list[j*row_size])
#         cv2.imshow(row_img)
#         cv2.waitKey(0)
#         for i in range(1,row_size):
#             row_img = cv2.hconcat(row_img,cv2.imread(image_list[(j*row_size)+i]))
#             cv2.imshow(row_img)
#             cv2.waitKey(0)
#         if final_img == '':
#             final_img = row_img
#         else:
#             final_img = cv2.vconcat(final_img,row_img)
#         cv2.imshow(final_img)
#         cv2.waitKey(0)
#         j = j+1
#     cv2.imshow(final_img)
#     cv2.waitKey(0)
#     return final_img


def splitImage_32(Original_image):
    split_img_list = []
    i = 0
    j = 0
    h , w, _ = Original_image.shape
    hmul = 32
    vmul = 32
    temph = 0
    hsplit = (int)(h/32)
    vsplit = (int)(w/32)
    while(i<hsplit):
        j = 0
        tempv =0
        while(j<vsplit):
            split_img = Original_image[temph:temph+hmul,tempv:tempv+vmul,:]
            j += 1
            tempv = tempv + vmul
            save_path = f'{Split_Data_Dir_32}{i}_{j}.jpg'
            cv2.imwrite(save_path,split_img)
            split_img_list.append(save_path)
        i += 1
        temph = temph + hmul
    return (split_img_list,vsplit,hsplit)


def splitImage(Original_image,hsplit,vsplit):
    split_img_list = []
    i = 0
    j = 0
    h , w, _ = Original_image.shape
    hmul = (int)(h/hsplit)
    vmul = (int)(w/vsplit)
    temph = 0
    tempv = 0
    while(i<hsplit):
        j = 0
        tempv =0
        while(j<vsplit):
            split_img = Original_image[temph:temph+hmul,tempv:tempv+vmul,:]
            j += 1
            tempv = tempv + vmul
            save_path = f'{Split_Data_Dir}{i}_{j}.jpg'
            cv2.imwrite(save_path,split_img)
            split_img_list.append(save_path)
        i += 1
        temph = temph + hmul
    return split_img_list

def splitImage_test(Original_image,hsplit,vsplit):
    split_img_list = []
    i = 0
    j = 0
    h , w, _ = Original_image.shape
    hmul = (int)(h/hsplit)
    vmul = (int)(w/vsplit)
    temph = 0
    tempv = 0
    while(i<hsplit):
        j = 0
        tempv = 0
        while(j<vsplit):
            split_img = Original_image[temph:temph+hmul,tempv:tempv+vmul,:]
            j += 1
            tempv = tempv + vmul
            split_img_list.append(split_img)
        i += 1
        temph = temph + hmul
    return split_img_list

if __name__=='__main__':
    img = cv2.imread(r"C:\Users\ishit\Desktop\ishit_picture.jpg")
    splitImage_test(img,3,3)