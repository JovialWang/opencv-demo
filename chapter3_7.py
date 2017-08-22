import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('resource/timg.jpeg')
mask = np.zeros(img.shape[:2], np.uint8)

newmask = cv2.imread('/Users/wangjuewei/Desktop/test.png',0)

mask[newmask > 127] = 0
mask[newmask < 10] = 1

bgdModel = np.zeros((1,65), np.float64)
fgbModel = np.zeros((1,65), np.float64)

rect = (81, 56 , 439, 483)

mask, bgdModel, fgdModel  = cv2.grabCut(img, mask, None, bgdModel, fgbModel, 15, cv2.GC_INIT_WITH_MASK)

mask2 = np.where((mask==2) | (mask==0),0,1).astype("uint8")
img = img*mask2[:,:,np.newaxis]

plt.subplot(121), plt.imshow(img)
plt.title("grabcut"), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(cv2.cvtColor(cv2.imread("resource/timg.jpeg"), cv2.COLOR_BGR2RGB))

plt.title("original"), plt.xticks([]), plt.yticks([])
plt.show()