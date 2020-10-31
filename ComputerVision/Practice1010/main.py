import cv2
import numpy as np

img = cv2.imread(r'sample4.jpg', 0)


cv2.imshow("Pam", img)
cv2.waitKey(0)  # waits until a key is pressed
# cv2.destroyAllWindows()  # destroys the window showing image

ret,thresh_img = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

# cv2.imshow("Pam", thresh_img)
# cv2.waitKey(0)  # waits until a key is pressed
# cv2.destroyAllWindows()  # destroys the window showing image

kernel = np.array([[0,1,0],[1,1,1],[0,1,0]])


border = cv2.dilate(thresh_img, None, iterations=7)
# border = border - cv2.erode(border, None)


cv2.imshow("Pam", border)
cv2.waitKey(0)  # waits until a key is pressed
cv2.destroyAllWindows()  # destroys the window showing image
# cv2.dilate(img, )
import random
errose = border
# errose = cv2.erode(border, None, iterations=5)
# cv2.imshow("Pam", errose)
# cv2.waitKey(0)  # waits until a key is pressed
# cv2.destroyAllWindows()  # destroys the window showing image

# errose = cv2.erode(border,None,iterations = 2)

# img2 = cv2.cvtColor(errose, cv2.COLOR_BGR2GRAY)

countours, hier = cv2.findContours(errose, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

# countours, hier = cv2.findContours(img2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# countours, hier = cv2.findContours(errose, cv2.RETR_FLOODFILL, cv2.CHAIN_APPROX_SIMPLE)


for cnt in countours:
    color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    cv2.drawContours(errose, [cnt], 0, color, -1)

errose = cv2.erode(errose, None, iterations=5)

# contours = cv2.drawContours(errose, thickness=cv2.FILLED)
cv2.imshow("Pam", errose)
cv2.waitKey(0)  # waits until a key is pressed
cv2.destroyAllWindows()  # destroys the window showing image