import cv2
import numpy as np
import copy

img = cv2.imread(r'D:/1491667901141674282.png', 0)
# print(img)
cv2.imshow("Pam", img)
cv2.waitKey(0)  # waits until a key is pressed
cv2.destroyAllWindows()  # destroys the window showing image
# img = np.ndarray(img)
# kernel = np.array([[-1, 2, 1], [-2, 0, 2], [-1, -2, 1]])
# kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
kernel = np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]]) / 16.0


# new_img = copy.deepcopy(img)
new_img = np.zeros((img.shape[0], img.shape[1]), dtype=np.uint8)



# print(img)
# print(new_img)
for i in range(1, len(img) - 1):
    for j in range(1, len(img[i]) - 1):
        buf = img[i-1: i+2, j-1: j+2]
        res = 0
        # for k in range(len(kernel)):
        #     for l in range(len(kernel[k])):
        #         res += buf[k][l] * kernel[k][l]
        res = np.sum(np.dot(buf, kernel))
        # res /= np.sum(kernel)
        new_img[i][j] = res

np.uint8(new_img)
cv2.imshow("Pam", new_img)
cv2.waitKey(0)  # waits until a key is pressed
cv2.destroyAllWindows()  # destroys the window showing image
