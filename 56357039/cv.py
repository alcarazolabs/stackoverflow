import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread("machupichu.jpg")
#blur = cv2.blur(img,(5,5))
#rows,cols,ch = img.shape

point=[[170,270],[480,220],[240, 710],[540,650]]

pts1 = np.float32([[170,270],[480,220],[240, 710],[540,650]])
pts2 = np.float32([[0,0],[210,0],[0,297],[210,297]])

M = cv2.getPerspectiveTransform(pts1,pts2)

dst = cv2.warpPerspective(img,M,(210,297))

plt.subplot(121)
plt.imshow(img)
plt.title('Input')

plt.plot(*zip(*point), marker='.', color='r', ls='')
plt.subplot(122)
plt.imshow(dst)
plt.title('Output')
plt.show()