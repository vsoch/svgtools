'''
imutils.py
part of svgtools package

'''

from PIL import Image
import pandas


def get_coordinates(png_image,transparent_filter=True,white_filter=True,sample_rate=2):
    """get_coordinates: reads in a png image, and returns xy coordinates of non transparent pixels 
    :param png_image: the image to read
    :param transparent_filter: don't include transparent pixels (default True)
    :param white_filter: don't include white pixels (default True)
    :param sample_rate: the sampling rate to include in range (eg, every N pixel)
    """

    img = Image.open(png_image)
    width, height = img.size

    # make a list of all pixels in the image
    pixels = img.load()
    coords = []
    data = []
    for x in range(0,width,sample_rate):
        for y in range(0,height,sample_rate):
            cpixel = pixels[x, y]
            coords.append([x,y])
            data.append(cpixel)

    print "Parsing %s pixels for image of size %sx%s with sample rate %s" %(len(data),width,height,sample_rate)
    print "To decrease time, you can increase the sample rate."

    df = pandas.DataFrame(columns=["x","y"])
    count = 0
    for x in range(len(data)):
        include_point = True

        # Include transparent filter?
        if transparent_filter==True:
            if (data[x][3] == 0):
                include_point = False

        # Include white filter?
        if white_filter == True:
            if (data[x][0] == 255 and data[x][1] == 255 and data[x][2] == 255):
                include_point = False

        if include_point == True:
            df.loc[count] = coords[x]
            count+=1

    print "Finished adding %s pixel coordinates." %(count+1)
    return df

