# svgtools

Components from images and data for interactive visualizations (under development)

The basic pieces that go into most interactive (e.g., D3) visualizations are circles and bars. While this is ideal for the simple communication of ideas, some of these views would be enhanced by visualization components that are both relatable and meaningful to the viewer. For example, overlaying data on a geographic map is immediately more understandable than showing bars with labels for geographic location. Why don't we have these kind of views for other things, such as the human body? Or a body? Further, we can embed in these custom components data such as ontological relationships. For example, a human body "map" in svg form would carry classes to tag different components, and we know that the "eye" is part of the "head" because it literally is. In the long run, we would want programmatic methods to transform standard images and data into representations that are immediately interactive and customizable for different visualizations. Toward this vision, I see the following needs: 

 - To start, methods to convert images into tagged svg. On the simplest level this could mean finding outline images (e.g., icons) and tagging them when their names, and then making it easy to search and easily add to a visualization. On a more complicated level, this means using computer vision to automatically find parts of images, derive labels, and then add to the same database.
 - Views for the annotation of images. For example, a body map might be represented as a field of points, and then a user is able to annotate sets of points with some vocabulary, and save the svg for later user.

I will start with simple svgtools to generate different components, and then move into more automated approaches that could do this at scale.

**under development**

## Installation

#### manual Installation

     git clone https://github.com/vsoch/svgtools
     cd svgtools
     sudo python setup.py install


#### pip Installation

     pip install svgtools


Submit bugs and feature requests as [issues](https://github.com/vsoch/svgtools/issues).

