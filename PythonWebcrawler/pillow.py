'''
    so jere we are going to learn about the "pillow" library of python
    it is used for image manipultion or editing, in short photoshopping
    now we have 2 image files 0.jpg and 3.jpg in current directory
'''

from PIL import Image

image = Image.open("0.jpg")
#image.show()    # this will display the image in some image editor

# crop the image
area = (50, 50, 300, 300)
cropped_image = image.crop(area)
#cropped_image.show()

# paste image over another
sun_image = Image.open("6.jpg")

sun_image.paste(cropped_image,area)
sun_image.show()



