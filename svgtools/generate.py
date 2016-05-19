'''
generate.py
part of svgtools package

'''
from svgtools.components import create_circle
from svgtools.imutils import get_coordinates
from svgtools.base import get_svg_base
from svgtools.utils import save_svg

def create_pointilism_svg(png_image,uid_base="uid",transparent_filter=True,white_filter=True,
                          sample_rate=2,width=300,height=900,diameter=4,fill_opacity=1,
                          fill="#666666",stroke="none",output_file=None):
    '''create_svg will return an svg string (or file, if output specified) for some png_image.
    :param png_image: the image to read
    :param transparent_filter: don't include transparent pixels (default True)
    :param white_filter: don't include white pixels (default True)
    :param sample_rate: the sampling rate to include in range (eg, every N pixel)
    :output_file: if specified, will save svg to file, Otherwise returns string
    :diameter: diameter of circle, in pixels (default is 4)
    :param fill_opacity: default 1
    :param fill: default gray (#666666)
    :stroke: default is none
    '''
    coords = get_coordinates(png_image,transparent_filter=transparent_filter,
                                       white_filter=white_filter,
                                       sample_rate=sample_rate)
    base = get_svg_base(uid_base,width,height)
    paths = ""

    print "Generating paths..."
    for uid,xy in coords.iterrows():
        path = create_circle(uid,x=xy["x"],y=xy["y"],
                             diameter=diameter,
                             fill_opacity=fill_opacity,
                             fill=fill,
                             stroke=stroke)
        paths = "%s\n%s" %(paths,path)
        
    svg = base.replace("[SUB_PATHS_SUB]",paths)
    if output_file == None:
        return svg
    save_svg(output_file,svg)
