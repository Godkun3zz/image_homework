# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 14:32:55 2021

@author: Godkun3zz
"""

import numpy as np
import cv2 as cv

def Dft(raw,new):
    pic = cv.imread(raw,cv.IMREAD_GRAYSCALE)
    h = pic.shape[0]
    w = pic.shape[1]
    emptyImage=np.zeros((h,w),dtype=complex)
    r_matrix=np.zeros((w,w),dtype=complex)
    l_matrix=np.zeros((h,h),dtype=complex)
    for i in range(w):
        for j in range(w):
            r_matrix[i,j]=np.exp(-2j*np.pi*i*j/w)
    for i in range(h):
        for j in range(h):
            l_matrix[i,j]=np.exp(-2j*np.pi*i*j/h)
    pic=pic.dot(r_matrix)
    emptyImage=l_matrix.dot(pic)
    emptyImage=np.fft.fftshift(emptyImage)
    emptyImage=np.log(1+np.abs(emptyImage))
    cv.imwrite(new,emptyImage)

def main():
    raw1 = "A.png"
    new1 = "A_dft.png"
    raw2 = "B.png"
    new2 = "B_dft.png"
    raw3 = "C.png"
    new3 = "C_dft.png"
    raw4 = "D.png"
    new4 = "D_dft.png"
    Dft(raw1,new1)
    Dft(raw2,new2)
    Dft(raw3,new3)
    Dft(raw4,new4)
if __name__ =='__main__':
    main()