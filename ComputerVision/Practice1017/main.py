import cv2
import numpy as np
from matplotlib import pyplot as plt

name = "domik-dlya-risunka-quotkak-ya-provel-letoquot-640x540.jpg"
img = cv2.imread(r'domik-dlya-risunka-quotkak-ya-provel-letoquot-640x540.jpg', 0)

# cv2.imshow("Pam", img)
# cv2.waitKey(0)  # waits until a key is pressed

img = np.float32(img)
corners = cv2.cornerHarris(img, 2, 3, 0.04)

corners = cv2.cornerHarris(img, 2, 3, 0.04)

# plt.subplot(2, 1, 1), plt.imshow(corners, cmap='jet')
plt.title('Harris Corner Detection'), plt.xticks([]), plt.yticks([])

img2 = cv2.imread(r'domik-dlya-risunka-quotkak-ya-provel-letoquot-640x540.jpg')
corners2 = cv2.dilate(corners, None, iterations=1)
img2[corners2 > 0.01 * corners2.max()] = [255, 0, 0]

plt.subplot(1, 1, 1), plt.imshow(img2, cmap='gray')
plt.title('Canny Edge Detection'), plt.xticks([]), plt.yticks([])

plt.show()

# img = cv2.imread(r'domik-dlya-risunka-quotkak-ya-provel-letoquot-640x540.jpg' )
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# edges = cv2.Canny(gray,50,150,apertureSize = 3)
#
# lines = cv2.HoughLines(edges,1,np.pi/180,200)
# for rho,theta in lines[0]:
#     a = np.cos(theta)
#     b = np.sin(theta)
#     x0 = a*rho
#     y0 = b*rho
#     x1 = int(x0 + 1000*(-b))
#     y1 = int(y0 + 1000*(a))
#     x2 = int(x0 - 1000*(-b))
#     y2 = int(y0 - 1000*(a))
#
#     cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)
#
# # cv2.imwrite('houghlines3.jpg',img)
# cv2.imshow("Pam", img)
# cv2.waitKey(0)  # waits until a key is pressed

img = cv2.imread(name)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 200, None, 3)
minLineLength = 1
maxLineGap = 1
lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 150)
# for x1,y1,x2,y2 in lines[0]:
#     cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
# import math
#
# for i in range(0, len(lines)):
#     rho = lines[i][0][0]
#     theta = lines[i][0][1]
#     a = math.cos(theta)
#     b = math.sin(theta)
#     x0 = a * rho
#     y0 = b * rho
#     pt1 = (int(x0 + 1000 * (-b)), int(y0 + 1000 * (a)))
#     pt2 = (int(x0 - 1000 * (-b)), int(y0 - 1000 * (a)))
#     cv2.line(gray, pt1, pt2, (0, 0, 130), 1, cv2.LINE_AA)
# cv2.imwrite('houghlines5.jpg', gray)
# cv2.imshow("Pam", gray)
# cv2.waitKey(0)  # waits until a key is pressed

linesP = cv2.HoughLinesP(edges, 1, np.pi / 180, 50, None, 50, 10)
if linesP is not None:
    for i in range(0, len(linesP)):
        l = linesP[i][0]
        cv2.line(gray2, (l[0], l[1]), (l[2], l[3]), (0, 0, 130), 1, cv2.LINE_AA)
cv2.imwrite('houghlines5.jpg', gray)
cv2.imshow("Pam", gray2)
cv2.waitKey(0)  # waits until a key is pressed
