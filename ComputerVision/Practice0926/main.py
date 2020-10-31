import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread(r'b.jpg', 0)

img_float32 = np.float32(img)
dft = cv2.dft(img_float32, flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)

rows, cols = img.shape
crow, ccol = rows / 2, cols / 2

plt.show()


# create a mask first, center square is 1, remaining all zeros
param_rows = 2
param_cols = param_rows * 0.75
mask = np.ones((rows, cols, 2), np.uint8)


for i in range(rows):
    for j in range(cols):
        if abs(i - j * 3 / 4) <= 7:
            mask[i, j, 0] = 0
            mask[i, j, 1] = 0


mask[int(crow - param_rows):int(crow + param_rows), int(ccol - param_cols):int(ccol + param_cols)] = 1

# apply mask and inverse DFT
fshift = dft_shift * mask
f_ishift = np.fft.ifftshift(fshift)
img_back = cv2.idft(f_ishift)
img_back = cv2.magnitude(img_back[:, :, 0], img_back[:, :, 1])
plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(img_back, cmap='gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])

plt.show()

# cv2.imshow("Pam", img)
# cv2.waitKey(0) # waits until a key is pressed
# cv2.destroyAllWindows() # destroys the window showing image
