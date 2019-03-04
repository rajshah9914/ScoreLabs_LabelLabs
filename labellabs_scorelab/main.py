from PIL import Image
import requests
import numpy as np
import urllib.request
import cv2
import matplotlib.pyplot as plt

def url_to_image(url):
    with urllib.request.urlopen(url) as url1:
        resp = url1.read()
        image = np.asarray(bytearray(resp), dtype="uint8")
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)
        return image

def convertToRGB(imag):
    return cv2.cvtColor(imag, cv2.COLOR_BGR2RGB)

test_image=url_to_image("https://b-i.forbesimg.com/parmyolson/files/2013/06/Faces-of-the-Future-1.jpg") 
plt.imshow(test_image) 
cv2.imshow('image',test_image)
cv2.waitKey(0)  
test_image_gray = cv2.cvtColor(test_image, cv2.COLOR_BGR2GRAY)
haar_cascade_face = cv2.CascadeClassifier('/home/rajshah9914/.local/lib/python3.5/site-packages/cv2/data/haarcascade_frontalface_default.xml')
faces_rects = haar_cascade_face.detectMultiScale(test_image_gray, scaleFactor = 1.2, minNeighbors = 5)
print('Faces found: ', len(faces_rects))
for (x,y,w,h) in faces_rects:
    cv2.rectangle(test_image, (x, y), (x+w, y+h), (0, 255, 0), 2)
im=convertToRGB(test_image)    
plt.imshow(im)    
cv2.imshow('image',test_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
# data/haarcascade/haarcascade_frontalface_default.xml