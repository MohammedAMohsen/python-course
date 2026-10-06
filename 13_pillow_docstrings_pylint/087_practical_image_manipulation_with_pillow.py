# Lesson 087 - Practical Image Manipulation With Pillow
# Video: https://www.youtube.com/watch?v=mwmyhIzfkl4

# -------------------------------------------------
# -- Practical => Image Manipulation With Pillow --
# -------------------------------------------------
# pip install pillow
from PIL import Image

# Open The Image

myImage = Image.open("images/sample_screenshot.png")

# Show The Image

myImage.show() # بتفتح الصورة في برنامج عرض الصور الموجود على جهازك

# My Cropped Image

myBox = (0, 0, 400, 400) # ابعاد الصورة الي قطعها, من المحور س 0 والمحور ص 0 اقطع على طول 400 لطول والعرض

myNewImage = myImage.crop(myBox)

# Show The NewImage

myNewImage.show()

# New Converted Mode Image

myConverted = myImage.convert("L") # غير مود الصورة وحولها الى أبيض و أسود

# myConverted.show()

# Save The New Image

# myNewImage.save("images/new_cropped.png") # حفظ الصورة الجديدة في ملف
