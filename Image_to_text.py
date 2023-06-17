from PIL import Image
from pytesseract import pytesseract

path_to_tesseract = (r"C:\Program Files\Tesseract-OCR\tesseract.exe")
path_to_image = r"images/test_image.jpg"

image = Image.open(path_to_image)
pytesseract.tesseract_cmd = path_to_tesseract

text = pytesseract.image_to_string(image)
test = pytesseract.image_to_boxes(image)
test2 = pytesseract.image_to_data(image)
test3 = pytesseract.image_to_pdf_or_hocr(image)
test4 = pytesseract.get_languages(text)


# create a list for all items\lnes by splitting string at new lines
line_list = text.split("\n")

# clean list by removing ""
while "" in line_list:
    line_list.remove("") 

print(line_list)

# isolate the total from the list
search_word = "TOTAL"
total = [n for n in line_list if search_word in n]
total = total[0]

# clean total until onl numbers remain
for i in range(len(total)):
    if total[i] == "R":
        number_value = total[i+1:]
print(number_value)

while " " in number_value:
    number_value = number_value.replace(" ","") 
    

print(number_value)
number_value = float(number_value)
print(number_value + 5)
