from PIL import Image, ImageDraw
from base64 import b64encode
from hashlib import sha256
from io import BytesIO


"""
Based off of: https://github.com/evuez/identicons
Subsequently modified
"""


GRID_SIZE = 12
BORDER_SIZE = 12
SQUARE_SIZE = 12


class Identicon(object):
    def __init__(self, str_, background="#fff"):
        """
        `str_` is the string used to generate the identicon.
        `background` is the background of the identicon.
        """
        w = h = BORDER_SIZE * 2 + SQUARE_SIZE * GRID_SIZE
        self.image = Image.new("RGB", (w, h), background)
        self.draw = ImageDraw.Draw(self.image)
        self.hash = self.digest(str_)

    def digest(self, str_):
        """
        Returns a sha256 numeric hash
        """
        return int(sha256(str_.encode("utf-8")).hexdigest(), 16)

    def calculate(self):
        """
        Creates the identicon.
        First three bytes are used to generate the color,
        remaining bytes are used to create the drawing
        """
        color = (self.hash & 0xFF, self.hash >> 8 & 0xFF, self.hash >> 16 & 0xFF)
        self.hash >>= 24  # skip first three bytes
        square_x = square_y = 0  # init square position
        for x in range(GRID_SIZE * (GRID_SIZE + 1) // 2):
            if self.hash & 1:
                x = BORDER_SIZE + square_x * SQUARE_SIZE
                y = BORDER_SIZE + square_y * SQUARE_SIZE
                self.draw.rectangle(
                    (x, y, x + SQUARE_SIZE, y + SQUARE_SIZE), fill=color, outline=color
                )
                # following is just for mirroring
                x = BORDER_SIZE + (GRID_SIZE - 1 - square_x) * SQUARE_SIZE
                self.draw.rectangle(
                    (x, y, x + SQUARE_SIZE, y + SQUARE_SIZE), fill=color, outline=color
                )
            self.hash >>= 1  # shift to right
            square_y += 1
            if square_y == GRID_SIZE:  # done with first column
                square_y = 0
                square_x += 1

    def base64(self, format="PNG"):
        """
        Return the identicon's base64
        """
        self.calculate()

        self.image.encoderinfo = {}
        self.image.encoderconfig = ()

        buff = BytesIO()
        self.image.save(buff, format=format.upper())

        return b64encode(buff.getvalue())


def getIdenticon(parameters, name):
    if parameters == "b64":
        identicon = Identicon(name)
        identicon_b64 = identicon.base64("PNG")
        formatted_identicon_b64 = (
            str(identicon_b64).replace("b", "", 1).replace("'", "")
        )
        return formatted_identicon_b64
