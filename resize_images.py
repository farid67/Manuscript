#!/usr/bin/python                                                  
from PIL import Image                                              
import os, sys                       

path =  "/home/fouhmich/Documents/Thesis/Redaction/Manuscript/Contributions/images/MisSegmentations"   
dirs = os.listdir(path)                                       

def resize():
    for item in dirs:
        if item.split(".")[-1] == "png":
            print (item)
            im = Image.open(os.path.join(path, item))
            x,y = im.size
            imResize = im.resize((int(x/2),int(y/2)), Image.ANTIALIAS)
            imResize.save(os.path.join(path, "Resize" + item), 'png', quality=80)

resize()
