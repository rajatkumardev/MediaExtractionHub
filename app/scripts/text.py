import easyocr

image = "C:\\Users\\RajatKumar\\Downloads\\we.png"
reader = easyocr.Reader(['en'])
result = reader.readtext(image, detail = 0)
print(result)