import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Open the image
img = np.array(Image.open('C:/Users/adith/AuE8930_HW02_Adithya_Suresh/Lenna.jpg')).astype(np.uint8)
plt.figure(1)
plt.title('Lenna image.jpg')
fit = plt.imshow(img)
plt.axis("off")
fit.axes.get_xaxis().set_visible(False)
fit.axes.get_yaxis().set_visible(False)
# Apply gray scale
gray_img = np.round(0.299 * img[:, :, 0] +
                    0.587 * img[:, :, 1] +
                    0.114 * img[:, :, 2]).astype(np.uint8)

plt.figure(2)
plt.imshow(gray_img)
fig= plt.imshow(gray_img, cmap = plt.get_cmap('gray'))
plt.axis("off")
fig.axes.get_xaxis().set_visible(False)
fig.axes.get_yaxis().set_visible(False)
plt.title('Lenna grey scale image.jpg')
plt.show()

# Sobel Operator
w, h = gray_img.shape[:2]
print('The height value is:', h)
print('The width value is:', w)

print('The gray scale w is:', w)
print('The gray scale h is:', h)

downscale = np.zeros(shape=(64,64))
for i in range(64):
    for j in range(64):
        downscale[i,j] = gray_img[i*4, j*4]
plt.figure(3)
plt.imshow(downscale, cmap = plt.get_cmap('gray'))
plt.savefig('downscaled_gray_scale.jpg')
plt.title('Lenna grey scale downscaled image.jpg')

# define filters
horizontal = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])  # s2
vertical = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])  # s1

# define images with 0s
newhorizontalImage = np.zeros((h, w))
newverticalImage = np.zeros((h, w))
newgradientImage = np.zeros((h, w))

# offset by 1
for i in range(1, h - 1):
    for j in range(1, w - 1):
        horizontalGrad = (horizontal[0, 0] * gray_img[i - 1, j - 1]) + \
                         (horizontal[0, 1] * gray_img[i - 1, j]) + \
                         (horizontal[0, 2] * gray_img[i - 1, j + 1]) + \
                         (horizontal[1, 0] * gray_img[i, j - 1]) + \
                         (horizontal[1, 1] * gray_img[i, j]) + \
                         (horizontal[1, 2] * gray_img[i, j + 1]) + \
                         (horizontal[2, 0] * gray_img[i + 1, j - 1]) + \
                         (horizontal[2, 1] * gray_img[i + 1, j]) + \
                         (horizontal[2, 2] * gray_img[i + 1, j + 1])

        newhorizontalImage[i - 1, j - 1] = abs(horizontalGrad)

        verticalGrad = (vertical[0, 0] * gray_img[i - 1, j - 1]) + \
                       (vertical[0, 1] * gray_img[i - 1, j]) + \
                       (vertical[0, 2] * gray_img[i - 1, j + 1]) + \
                       (vertical[1, 0] * gray_img[i, j - 1]) + \
                       (vertical[1, 1] * gray_img[i, j]) + \
                       (vertical[1, 2] * gray_img[i, j + 1]) + \
                       (vertical[2, 0] * gray_img[i + 1, j - 1]) + \
                       (vertical[2, 1] * gray_img[i + 1, j]) + \
                       (vertical[2, 2] * gray_img[i + 1, j + 1])

        newverticalImage[i - 1, j - 1] = abs(verticalGrad)

        # Edge Magnitude
        mag = np.sqrt(pow(horizontalGrad, 2.0) + pow(verticalGrad, 2.0))
        newgradientImage[i - 1, j - 1] = mag

plt.figure(4)
plt.title('Sobel Operator on Lennagrey.jpg')
figure1 = plt.imshow(newgradientImage, cmap='gray')
plt.savefig('sobel_lenna.jpg', cmap = 'gray')
plt.axis("off")
figure1.axes.get_xaxis().set_visible(False)
figure1.axes.get_yaxis().set_visible(False)
plt.show()
