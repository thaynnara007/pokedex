import os, PIL
from PIL import Image
from os import listdir

path = "data/dataset/"
directories = listdir(path)

for d in directories:
  
  directorie = "{}/{}".format(path, d)
  absolutePath = os.path.dirname(os.path.abspath(d))
  d = "{}/{}".format(absolutePath, directorie)
  os.chdir(d)

  for img in listdir(os.getcwd()):
    
    picture = Image.open(img)
    img_type = img.split('.')[-1]

    picture.rotate(45, expand=True).save('rotated{}_{}.{}'.format(45,img ,img_type))
    picture.rotate(90, expand=True).save('rotated{}_{}.{}'.format(90,img ,img_type))
    picture.rotate(135, expand=True).save('rotated{}_{}.{}'.format(135,img ,img_type))
    picture.rotate(180, expand=True).save('rotated{}_{}.{}'.format(180,img ,img_type))
    picture.rotate(225, expand=True).save('rotated{}_{}.{}'.format(225,img ,img_type))
    picture.rotate(270, expand=True).save('rotated{}_{}.{}'.format(270,img ,img_type))
   
   