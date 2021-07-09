import cv2
import pytesseract
import os

imgname=''
imgextensions=['png','PNG','JPEG','jpeg','jpg','JPG']
for file in os.listdir('./image/'):
    if file[-3:] in imgextensions:
        imgname=f'./image/{file}'

img = cv2.imread(imgname)

img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
text=pytesseract.image_to_string(img)
text=text.replace('”','"')
text=text.replace('“','"')
text=text.replace("’","'")
text=text.replace("‘","'")
print(f'\n\n{text}\n\n')

with open('solve.c','w') as f:
    f.write(text)

os.remove(imgname)