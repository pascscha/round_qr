#!/usr/bin/python3

from PIL import Image

qr_code = []

corner_NW = Image.open("tiles/corner.png")
corner_SW = corner_NW.transpose(Image.ROTATE_90)
corner_SE = corner_SW.transpose(Image.ROTATE_90)
corner_NE = corner_SE.transpose(Image.ROTATE_90)

corner_inverse_NW = Image.open("tiles/corner_inv.png")
corner_inverse_SW = corner_inverse_NW.transpose(Image.ROTATE_90)
corner_inverse_SE = corner_inverse_SW.transpose(Image.ROTATE_90)
corner_inverse_NE = corner_inverse_SE.transpose(Image.ROTATE_90)

full = Image.open("tiles/full.png")
empty = Image.open("tiles/empty.png")
diag1 = Image.open("tiles/diag.png")
diag2 = diag1.transpose(Image.ROTATE_90)

left = Image.open("tiles/left.png")
bottom = left.transpose(Image.ROTATE_90)
right = bottom.transpose(Image.ROTATE_90)
top = right.transpose(Image.ROTATE_90)

images = [empty, corner_NW, corner_NE, bottom,
          corner_SW, right, diag2, corner_inverse_SE,
          corner_SE, diag1, left, corner_inverse_SW,
          top, corner_inverse_NE, corner_inverse_NW, full]

qr_code = [[True, True, True, True, True, True, True, False, False, True, True, False, False, False, True, True, True, False, True, True, True, True, True, True, True], [True, False, False, False, False, False, True, False, False, False, False, True, True, False, False, True, True, False, True, False, False, False, False, False, True], [True, False, True, True, True, False, True, False, False, True, False, True, False, True, False, False, True, False, True, False, True, True, True, False, True], [True, False, True, True, True, False, True, False, True, False, False, True, True, True, False, True, False, False, True, False, True, True, True, False, True], [True, False, True, True, True, False, True, False, False, True, False, True, True, True, True, True, True, False, True, False, True, True, True, False, True], [True, False, False, False, False, False, True, False, True, False, False, False, True, True, False, True, False, False, True, False, False, False, False, False, True], [True, True, True, True, True, True, True, False, True, False, True, False, True, False, True, False, True, False, True, True, True, True, True, True, True], [False, False, False, False, False, False, False, False, True, True, True, True, False, False, False, False, True, False, False, False, False, False, False, False, False], [False, True, True, False, False, False, True, False, False, True, False, False, True, True, False, False, False, False, True, True, False, True, False, False, False], [False, False, True, False, False, True, False, False, True, False, False, False, False, True, False, False, False, False, True, True, True, True, False, False, True], [False, True, False, False, True, False, True, False, False, True, True, False, False, False, True, True, True, True, True, False, True, False, True, False, True], [True, False, False, False, True, True, False, True, True, False, False, False, True, False, False, False, True, True, False, True, True, True, False, False, True], [False, True, False, True, True, False, True, True, True, False, False, False, True, True, True, False, False, False, True, False, True, True, True, True, False], [False, False, False, False, True, False, False, False, False, False, False, False, True, True, False, True, False, True, False, False, False, True, False, False, True], [True, True, True, True, False, True, True, True, False, False, True, True, True, True, True, True, True, True, True, True, False, True, False, True, False], [False, False, False, True, False, True, False, True, False, False, False, False, True, False, True, True, True, False, False, False, False, False, False, True, False], [True, True, False, False, True, True, True, True, True, True, False, False, False, True, False, True, True, True, True, True, True, False, False, True, True], [False, False, False, False, False, False, False, False, True, False, True, True, False, True, True, False, True, False, False, False, True, True, True, True, True], [True, True, True, True, True, True, True, False, False, False, False, True, False, False, False, False, True, False, True, False, True, False, True, True, False], [True, False, False, False, False, False, True, False, False, False, True, True, False, False, False, False, True, False, False, False, True, True, True, False, True], [True, False, True, True, True, False, True, False, False, True, True, True, False, True, True, True, True, True, True, True, True, False, True, False, False], [True, False, True, True, True, False, True, False, False, False, False, False, False, False, False, True, True, False, True, True, False, False, False, False, False], [True, False, True, True, True, False, True, False, True, True, False, False, True, False, True, False, True, True, False, False, True, True, False, True, True], [True, False, False, False, False, False, True, False, True, False, True, True, False, True, False, False, False, True, False, True, True, True, False, False, True], [True, True, True, True, True, True, True, False, False, False, False, True, False, False, True, False, True, False, False, False, True, False, True, True, True]]
width = len(qr_code[0])
height = len(qr_code)

sqr_width = corner_NW.width
sqr_height = corner_NW.height


canvas = Image.new("RGBA", ((width - 1) * sqr_width, (height - 1) * sqr_height), color=(255, 255, 255, 255))

for r in range(0, len(qr_code) - 1):
  for c in range(0, len(qr_code[r]) - 1):
    tl = qr_code[r][c]
    bl = qr_code[r + 1][c]
    tr = qr_code[r][c + 1]
    br = qr_code[r + 1][c + 1]
    n = 8 * tl + 4 * tr + 2 * bl + br
    image = images[n]
    canvas.paste(image, (sqr_height * c, sqr_width * r))

canvas.save("out.png")
canvas.show()
