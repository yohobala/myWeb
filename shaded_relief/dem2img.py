"""Convert an ASCII DEM to an image."""
import os

import numpy as np

try:
    import Image
    import ImageOps
except:
    from PIL import Image, ImageOps

class dem2img():
    def dem2img(self,path,file):
        # Source LIDAR DEM file

        source = path + file

        # Output image file
        target = os.path.dirname(os.getcwd()) + '/webGIS/static/shaded_relief/' + file.split('.')[0] + '.jpg'
        print(target)
        imagePath = '/static/shaded_relief/'+file.split('.')[0]+'.jpg'
        print(imagePath)
        # Load the ASCII DEM into a numpy array
        arr = np.loadtxt(source, skiprows=6)
        print(arr)
        # Convert array to numpy image
        im = Image.fromarray(arr).convert('RGB')

        # Enhance the image:
        # equalize and increase contrast
        im = ImageOps.equalize(im)
        im = ImageOps.autocontrast(im)

        # Save the image
        im.save(target)

        return imagePath

