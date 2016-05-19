'''
components.py
part of svgtools package

'''

def create_circle(uid,x,y,diameter=1,fill_opacity=1,fill="#666666",stroke="none",
                  upper_leftx=10,upper_lefty=10):
    '''create_circle returns a circle path (right now most is hard coded)
    :uid: the identifier to give the circle path
    :x: x coordinate
    :y: y coordinate
    :diameter: diameter of circle, in pixels (default is 4)
    :param fill_opacity: default 1
    :param fill: default gray (#666666)
    :stroke: default is none
    :param upper_leftx: upper left x coordinate
    :param upper_lefty: upper left y coordinate
    '''
    circle = '''<path
       d="m %s,%s a 2.2728431,2.2728431 0 1 1 -4.54569,0 2.2728431,2.2728431 0 1 1 4.54569,0 z"
       transform="matrix(0.87995515,0,0,0.87995515,%s,%s)"
       id="%s"
       style="fill:%s;fill-opacity:%s;stroke:%s" />''' %(upper_leftx,upper_lefty,
                                                         x,y,uid,fill,fill_opacity,stroke)
    return circle

