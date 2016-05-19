'''
utils.py
part of svgtools package

'''

import json

def save_svg(output_file,svg):
    '''save_svg saves svg to file
    :param output_file: the output file to save to (*.svg)
    :param svg: the svg string to save
    '''
    print "Saving svg file to %s" %(output_file)
    filey = open(output_file,"w")
    filey.writelines(svg)
    filey.close()



def read_json(json_file):
    '''read_json reads in a json structure, corresponding to different regions to annotate
    :param json_file: path to json_file
    '''
    return json.load(open(json_file,'r'),encoding="utf-8")
