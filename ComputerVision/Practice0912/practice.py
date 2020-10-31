import cv2

img = cv2.imread(r'D:/1491667901141674282.png')
print(img)
cv2.imshow("Pam", img)
cv2.waitKey(0) # waits until a key is pressed
cv2.destroyAllWindows() # destroys the window showing image

import matplotlib.pyplot
img2 = matplotlib.pyplot.imread(r"D:\Всякое\Картинки\трейсер.png")
plot = matplotlib.pyplot.imshow(img2)
matplotlib.pyplot.show()