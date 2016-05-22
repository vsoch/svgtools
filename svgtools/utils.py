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


def save_json(json_obj,output_file):
    '''save_json saves a json object to file
    :param json_obj: json object
    :param output_file: output json file
    '''
    filey = open(output_file,'wb')
    filey.write(json.dumps(json_obj, sort_keys=True,indent=4, separators=(',', ': ')))
    filey.close()
    return output_file

def read_json(json_file):
    '''read_json reads in a json structure, corresponding to different regions to annotate
    :param json_file: path to json_file
    '''
    return json.load(open(json_file,'r'),encoding="utf-8")
