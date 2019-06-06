#!/usr/bin/python3
from PIL import Image


class BitmapRounder():
    """Can convert a bitmap into the image representation of that bitmap
    with rounded corners.
    """

    def __init__(self):
        """Initialize all tiles we need to put together our image
        """
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

        # The position of the images is encoded in binary by its surrounded corners
        self.tiles = [empty, corner_NW, corner_NE, bottom,
                      corner_SW, right, diag2, corner_inverse_SE,
                      corner_SE, diag1, left, corner_inverse_SW,
                      top, corner_inverse_NE, corner_inverse_NW, full]

    def get_image(self, bitmap):
        """Converts a bitmap into the image representation of that bitmap
           with rounded corners.
        """
        width = len(bitmap[0])
        height = len(bitmap)

        sqr_width = self.tiles[0].width
        sqr_height = self.tiles[0].height

        output = Image.new("RGBA", ((width - 1) * sqr_width, (height - 1) * sqr_height), color=(255, 255, 255, 255))

        for r in range(0, len(bitmap) - 1):
            for c in range(0, len(bitmap[r]) - 1):
                tl = bitmap[r][c]
                bl = bitmap[r + 1][c]
                tr = bitmap[r][c + 1]
                br = bitmap[r + 1][c + 1]
                # The position n of the images is encoded in binary by its surrounded corners
                n = 8 * tl + 4 * tr + 2 * bl + br
                output.paste(self.tiles[n], (sqr_height * c, sqr_width * r))
        return output


if __name__ == "__main__":
    # The QR code
    qr_code_bitmap = [[True, True, True, True, True, True, True, False, False, True, True, False, False, False, True, True, True, False, True, True, True, True, True, True, True], [True, False, False, False, False, False, True, False, False, False, False, True, True, False, False, True, True, False, True, False, False, False, False, False, True], [True, False, True, True, True, False, True, False, False, True, False, True, False, True, False, False, True, False, True, False, True, True, True, False, True], [True, False, True, True, True, False, True, False, True, False, False, True, True, True, False, True, False, False, True, False, True, True, True, False, True], [True, False, True, True, True, False, True, False, False, True, False, True, True, True, True, True, True, False, True, False, True, True, True, False, True], [True, False, False, False, False, False, True, False, True, False, False, False, True, True, False, True, False, False, True, False, False, False, False, False, True], [True, True, True, True, True, True, True, False, True, False, True, False, True, False, True, False, True, False, True, True, True, True, True, True, True], [False, False, False, False, False, False, False, False, True, True, True, True, False, False, False, False, True, False, False, False, False, False, False, False, False], [False, True, True, False, False, False, True, False, False, True, False, False, True, True, False, False, False, False, True, True, False, True, False, False, False], [False, False, True, False, False, True, False, False, True, False, False, False, False, True, False, False, False, False, True, True, True, True, False, False, True], [False, True, False, False, True, False, True, False, False, True, True, False, False, False, True, True, True, True, True, False, True, False, True, False, True], [True, False, False, False, True, True, False, True, True, False, False, False, True, False, False, False, True, True, False, True, True, True, False, False, True], [False, True, False, True, True, False, True, True, True, False, False, False, True, True, True, False, False, False, True, False, True, True, True, True, False], [False, False, False, False, True, False, False, False, False, False, False, False, True, True, False, True, False, True, False, False, False, True, False, False, True], [True, True, True, True, False, True, True, True, False, False, True, True, True, True, True, True, True, True, True, True, False, True, False, True, False], [False, False, False, True, False, True, False, True, False, False, False, False, True, False, True, True, True, False, False, False, False, False, False, True, False], [True, True, False, False, True, True, True, True, True, True, False, False, False, True, False, True, True, True, True, True, True, False, False, True, True], [False, False, False, False, False, False, False, False, True, False, True, True, False, True, True, False, True, False, False, False, True, True, True, True, True], [True, True, True, True, True, True, True, False, False, False, False, True, False, False, False, False, True, False, True, False, True, False, True, True, False], [True, False, False, False, False, False, True, False, False, False, True, True, False, False, False, False, True, False, False, False, True, True, True, False, True], [True, False, True, True, True, False, True, False, False, True, True, True, False, True, True, True, True, True, True, True, True, False, True, False, False], [True, False, True, True, True, False, True, False, False, False, False, False, False, False, False, True, True, False, True, True, False, False, False, False, False], [True, False, True, True, True, False, True, False, True, True, False, False, True, False, True, False, True, True, False, False, True, True, False, True, True], [True, False, False, False, False, False, True, False, True, False, True, True, False, True, False, False, False, True, False, True, True, True, False, False, True], [True, True, True, True, True, True, True, False, False, False, False, True, False, False, True, False, True, False, False, False, True, False, True, True, True]]

    # our rounder class
    rounder = BitmapRounder()

    # generate round image, save and show it
    qr_code = rounder.get_image(qr_code_bitmap)
    qr_code.save("out.png")
    qr_code.show()
