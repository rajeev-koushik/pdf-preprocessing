import cv2
from matplotlib import pyplot as plt
from PIL import Image 
import pytesseract 
from pdf2image import convert_from_path 
from pathlib import Path

PDF_file = r"path/to/file.pdf"
out = Path(PDF_file).stem

pages = convert_from_path(PDF_file, 300, poppler_path = r"path/to/poppler/bin/") 

image_counter = 1
for page in pages: 
	filename = out+"_PDFtoJPG.jpg"
	page.save(filename, 'JPEG')
	image_counter = image_counter + 1

img = cv2.imread(out+"_PDFtoJPG.jpg",0)
img = cv2.medianBlur(img,5)

th = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,51,10)
plt.xticks([])
plt.yticks([])

plt.imshow(th, 'gray')

plt.savefig(out+"_final.jpg", bbox_inches = 'tight', dpi = 300)

outfile = out+".txt"
f = open(outfile, "a")

pytesseract.pytesseract.tesseract_cmd = r"path/to/tesseract.exe"

filename = out+"_final.jpg"
text = str(((pytesseract.image_to_string(Image.open(filename))))) 
text = text.replace('-\n', '')	 
f.write(text) 

f.close()
