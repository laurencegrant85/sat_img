
from PIL import Image,ImageFilter,ImageChops
import os
import numpy as np


files = [f for f in os.listdir("./img") ]
files.sort()


def diff(image1,image2):
    analyze_img1 = np.asarray(image1)
    analyze_img2 = np.asarray(image2)
    substr_img  = analyze_img2 - analyze_img1
    return(Image.fromarray(substr_img))

def convert_range(value):
    if np.isnan(value):
        return 0
    return(int(((value+1)/(2))*(255)))

def VDVI(image):
    array = np.array(image,dtype=np.float64)
    vdvi=np.zeros(shape=(len(array),len(array[0])), dtype=np.uint8)
    for i in range(len(array)):
        for j in range(len(array[i])):
            print(array[i][j])
            value=(((2*array[i][j][1]-array[i][j][0]-array[i][j][2]))/((2*array[i][j][1]+array[i][j][0]+array[i][j][2])))
            vdvi[i][j] = convert_range(value)
            #vdvi ranges from -1 to 1 need to convert to 0-255
    PIL_image = Image.fromarray(np.uint8(vdvi)).convert('L')
    return(PIL_image)

def compare_vdvi_between_years(a,b):

    im1 = Image.open("./img/"+files[a])
    im2 = Image.open("./img/"+files[b])

    vdvi_1=VDVI(im1)
    vdvi_2=VDVI(im2)
    dif1 = diff(vdvi_1,vdvi_2)

    dif1 = dif1.filter(ImageFilter.MinFilter)
    blank = im1.point(lambda _: 0)


    ImageChops.composite(blank,im1,dif1).show()

year_1=3
year_2=4

print("Comparing VDVI between years 202"+str(year_1)+" and 202"+str(year_2))

compare_vdvi_between_years(year_1,year_2)