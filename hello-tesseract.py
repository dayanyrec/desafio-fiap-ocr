import sys
import cv2
import pytesseract

try:
    img_path = sys.argv[1]
except:
    sys.exit('Por favor, passe o caminho para a imagem a ser lida')

img = cv2.imread(img_path)

img_strings = pytesseract.image_to_string(img, lang='por')

print(img_strings)
