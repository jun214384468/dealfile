from PIL import Image, ImageDraw

im = Image.open("IMG_0063.jpg")
draw = ImageDraw.Draw(im)
fname = 'IMG_0063.txt'
f = open(fname, 'r')
savestr = ''
for line in f:
    line = line.strip()
    line = line.split(',')
    line = list(map(float, line[0:-1]))
    print(line)
    draw.polygon(line, outline='red')
im.show('t')