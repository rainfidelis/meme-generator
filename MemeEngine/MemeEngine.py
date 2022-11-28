"""Create a meme object generator."""

import random
from PIL import Image, ImageFont, ImageDraw, ImageFilter


class MemeEngine:
    """
    Create a meme using an image, quote text, and quote author.

    A `meme` in this instance is an image containing a quote and its author.
    The MemeEngine creates a new image and saves it to the directory specified
    during the class instantiation.
    """

    def __init__(self, output_dir) -> None:
        """Initialize the `MemeEngine` with the output file name."""
        self.out_path = f"{output_dir}/{random.randint(0, 1000000)}.jpg"

    def make_meme(self, img_path, text, author, width=500) -> str:
        """
        Create a meme using the provided image and quote details.

        :param img_path: Relative path to the image file
        :param text: Quote body for the meme
        :param author: Author of the provided quote
        :param width: Width to use when resizing image. Defaults to 500

        :return: The string location of the newly created meme.
        """
        fonts = ["./_fonts/LilitaOne-Regular.ttf", "./_fonts/Satisfy-Regular.ttf"]

        with Image.open(img_path) as img:

            # Resize image while maintaining the existing aspect ratio
            ratio = width/float(img.size[0])
            height = int(ratio*float(img.size[1]))
            img = img.resize((width, height), Image.Resampling.NEAREST)

            # Blur image for clearer quotes
            img = img.filter(ImageFilter.BLUR)

            # Add caption to image
            message = f"{text}\n - {author}"
            fnt = ImageFont.truetype(random.choice(fonts), 30)
            d = ImageDraw.Draw(img)
            d.multiline_text((100, 350), message, font=fnt, fill='red', align="center")

            # Save image
            img.save(self.out_path)

            return self.out_path

