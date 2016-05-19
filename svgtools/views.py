'''
views.py
part of svgtools package

'''

def generate_annotator(svg_file,labels):
    '''generate_annotator will return a static web page to allow for annotation of an svg image with some set of labels.
    :param svg_file: full path to svg file to annotate
    :param labels: list of labels to provide to user
    '''
    template = "\n".join(open("data/annotator.html","r").readlines())
    svg = "\n".join(open(svg_file,"r").readlines())

