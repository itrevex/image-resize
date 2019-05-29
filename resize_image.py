
"""Esai Image Resize

    Call script with the image size required. A folder will be 
    created where is called and images will be put inside folder.

    Run
    '$ptyhon resize_image.py 320' to resize images to base width 320 px

Usage:
    resize_image.py 
    resize_image.py <basewidth>
    resize_image.py <basewidth> <height_ratio>
    resize_image.py [--min <basewidth>]

Example:
    $ptyhon resize_image.py 320

Options:
    -h --help Enter base width to start using app
    --min Use if the value should be minimum height incase the height is bigger
"""

from PIL import Image
import os
from resizeimage import resizeimage
import json
from docopt import docopt

class ResizeImages:
    basewidth = 1080
    height_ratio = None
    data = {}
    data['images'] = []
    images_base_name='images/gallery/'
    thumbnails_base_name='images/gallery/thumbnails/'

    def __init__(self, basewidth=1080, height_ratio=None):
        self.basewidth = int(basewidth)
        #create directory to store images
        self.pathName = 'images'+"_"+str(self.basewidth)
        if (os.path.isdir(self.pathName) != True):
            os.makedirs(self.pathName)

        self.countFiles()
        self.runThroughImages()
        self.writeJsonData()


    def getThumbnailName(self, name, ext, height):
        return name+"_"+str(self.basewidth)+"x"+str(height)+"."+ext

    def outPutPath(self, folder, name):
        return folder+"/"+name

    def resizeImage(self, image_name, folder, base_name, ext):
        with open(image_name, 'r+b') as f:
            with Image.open(f) as image:
                wpercent = (self.basewidth/float(image.size[0]))
                if self.height_ratio:
                    hsize = int(self.base_width * self.height_ratio)
                else:
                    hsize = int((float(image.size[1])*float(wpercent)))
                cover = resizeimage.resize_cover(image, [self.basewidth, hsize])
                thumbnail_name = self.getThumbnailName(base_name, ext, hsize)
                path = self.outPutPath(folder, thumbnail_name)
                cover.save(path, image.format)
                return thumbnail_name

    def runThroughImages(self):
        count = 1
        for filename in os.listdir(os.getcwd()):
            if(os.path.isdir(filename)):
                continue
                
            basename = filename.rpartition(".")[0]
            ext = filename.rpartition(".")[2]
            
            try:
                if (ext != 'py'):
                    thumbnail = self.resizeImage(filename, self.pathName, basename, ext)
                    self.data['images'].append({
                        'src_orig': self.images_base_name+filename,
                        'src': self.images_base_name+thumbnail,
                        'thumbnail': self.thumbnails_base_name+thumbnail,
                    });
                    self.printPercentageDone(count)
                    count += 1
            except:
                raise
                print("Warning : " + basename)

    def writeJsonData(self):
        with open(self.outPutPath(self.pathName, 'data.json'), 'w') as outfile:  
            json.dump(self.data, outfile)

    def countFiles(self):
        self.totalFiles = len([name for name in os.listdir('.') if os.path.isfile(name)])
        self.totalFiles -= 1

    def printPercentageDone(self, count):
        percentage = '%.2f' % (count/self.totalFiles * 100)
        print("Resizing ",str(percentage) + "% done ...", end="", flush=True)
        print('\r', end='')
    
        


if __name__ == '__main__':
    args = docopt(__doc__, version='Esai Image Resize 1.0')
    print (args)
    ResizeImages(args['<basewidth>'], height_ratio = args['<height_ratio>'])