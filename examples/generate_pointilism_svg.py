# Transform a standard png image into a pointilism (of paths)

from svgtools.generate import create_pointilism_svg

# Select your png image!
png_image = "data/body.png"

# uid_base will be the id of the svg
# sample rate determines the space between points (larger --> more space)

create_pointilism_svg(png_image,uid_base="bodymap",
                                sample_rate=8,width=330,height=800,
                                output_file="data/bodymappp.svg")
