import cv2
import numpy as np

def read_file(filename):
  img=cv2.imread('girl.jpg')
  cv2.imshow('', img)
  cv2.waitKey(0)
  return img

def color_quantization(img, k):

  data=np.float32(img).reshape((-1, 3))

  criteria=(cv2.TERM_CRITERIA_EPS+cv2.TERM_CRITERIA_MAX_ITER,20,0.001)

  ret, label, center=cv2.kmeans(data, k , None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
  center=np.uint8(center)
  result= center[label.flatten()]
  result=result.reshape(img.shape)

  return result

def edge_mask(img, line_size, blur_value):
  gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  gray_blur=cv2.medianBlur(gray, blur_value)
  edges=cv2.adaptiveThreshold(gray_blur,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY, line_size, blur_value)
  return edges

img=read_file('girl.jpg')

line_size=7
blur_value=7

edges=edge_mask(img, line_size,blur_value)
cv2.imshow('', edges)
cv2.waitKey(0)

total_color=9
img=color_quantization(img, total_color)
cv2.imshow('', img)
cv2.waitKey(0)

blurred=cv2.bilateralFilter(img, d=7, sigmaColor=200, sigmaSpace=200,)
cv2.imshow('', blurred)
cv2.waitKey(0)

cartoon=cv2.bitwise_and(blurred, blurred, mask=edges)
cv2.imshow('', cartoon)
cv2.waitKey(0)