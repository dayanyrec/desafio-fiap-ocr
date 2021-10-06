import cv2
import pytesseract

img_path = 'img/cupom.jpg'

img = cv2.imread(img_path)

img_strings = pytesseract.image_to_string(img)

print(img_strings)