import cv2

img_location = 'cat.png'
img = cv2.imread(img_location)
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
inverted_gray_image = 255 - gray_image
blur_image = cv2.GaussianBlur(inverted_gray_image, (21, 21), 0)
inverted_blur_image = 255 - blur_image
pencil_image = cv2.divide(gray_image, inverted_blur_image, scale=256.0)

cv2.imwrite('cat3.png', pencil_image)
