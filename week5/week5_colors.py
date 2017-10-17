from PIL import Image, ImageDraw

'''
 get_colors analyzes an image for its colors.
 here are what the variables mean.

 infile : the name of the file you wish to analyze
 outfile : the name of the file to save your output
 numcolors : the number of colors to generate for your pallete
 swatch size : size of swatches in your output file.

'''

def get_colors(infile, outfile, numcolors=10, swatchsize=20, resize=150):
    image = Image.open(infile)
    image = image.resize((resize, resize))

    # we need to convert the image for python+PIL to work nicely
    result = image.convert('P', palette=Image.ADAPTIVE, colors=numcolors)
    result.putalpha(0)
    colors = result.getcolors(resize*resize)

    # print the colors for debugging
    print colors

    # Save colors to file
    colorPallete = Image.new('RGB', (swatchsize * numcolors, swatchsize))
    draw = ImageDraw.Draw(colorPallete)

    # create a pallete from our image
    # for each color, draw a square!
    posx = 0
    for count, col in colors:
        draw.rectangle([posx, 0, posx + swatchsize, swatchsize], fill=col)
        posx = posx + swatchsize

    del draw
    colorPallete.save(outfile, "PNG")

# update the following filenames for your project
# the first parameter is the image you wish to load, the second is the output image.
get_colors('seujorge.JPG', 'seujorge.PNG') 
get_colors('birthday.JPG', 'birthday.PNG') 
get_colors('coffee_love.JPG', 'coffee_love.PNG')
get_colors('coffee.JPG', 'coffee.PNG') 
get_colors('depeche_mode.JPG', 'depeche_mode.PNG')
get_colors('door.JPG', 'door.PNG')
get_colors('flowers.JPG', 'flowers.PNG')
get_colors('lincoln_center.JPG', 'lincoln_center.PNG')
get_colors('pumpkins.JPG', 'pumpkins.PNG')
get_colors('sculpture.JPG', 'sculpture.PNG')
get_colors('sunset.JPG', 'sunset.PNG')
get_colors('theelk.JPG', 'theelk.PNG')

