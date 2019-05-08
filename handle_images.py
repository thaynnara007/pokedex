import os, PIL
from PIL import Image
from os import listdir

PATH = "dataset/"
ROOT = os.getcwd()

def handle_prictures(directories, path):

  for d in directories:
    
    directory = os.path.join(path,d)   
    d = "{}/{}".format(ROOT, directory)
    print ("[INFO] directory: {}".format(d))
    os.chdir(d)

    for img in listdir(os.getcwd()):
      
      print ("[INFO] image: {}".format(img))
      image = Image.open(img)
      newImage = image.resize((256,256), Image.ANTIALIAS)
      newImage.save(img, optimize=True, quality=95)

      picture = Image.open(img)
      picture.rotate(45, expand=True).save('rotated{}_{}'.format('45',img))
      picture.rotate(90, expand=True).save('rotated{}_{}'.format('90',img), optimize=True, quality=95)
      picture.rotate(135, expand=True).save('rotated{}_{}'.format('135',img))
      picture.rotate(180, expand=True).save('rotated{}_{}'.format('180',img), optimize=True, quality=95)
      picture.rotate(225, expand=True).save('rotated{}_{}'.format('225',img))
      picture.rotate(270, expand=True).save('rotated{}_{}'.format('270',img), optimize=True, quality=95)
      picture.rotate(315, expand=True).save('rotated{}_{}'.format('315',img))

      for angle in [45,135,225,315]:
        name = 'rotated{}_{}'.format(angle, img)
        image = Image.open(name)
        new_image = image.resize((256,256), Image.ANTIALIAS)
        new_image.save(name, optimize=True, quality=95)  
   
def main():

  path = input("Type the directory from the files, if any directory is type it will be set to the default one, which is {}:".format(PATH))
  if (len(path)== 0): path = PATH
  directories = listdir(path)

  handle_prictures(directories, path)

if __name__ == "__main__":
  main()

