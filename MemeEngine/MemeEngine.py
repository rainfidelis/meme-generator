"""Create a meme object generator."""

import random
import textwrap
from PIL import Image, ImageFont, ImageDraw, ImageFilter
from string import ascii_letters


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
        fonts = ["./_fonts/LilitaOne-Regular.ttf",
                 "./_fonts/Lobster-Regular.ttf"]

        with Image.open(img_path) as img:

            # Resize image while maintaining the existing aspect ratio
            ratio = width/float(img.size[0])
            height = int(ratio*float(img.size[1]))
            img = img.resize((width, height), Image.Resampling.NEAREST)

            # Blur image for clearer quotes
            img = img.filter(ImageFilter.BLUR)

            # Define text and font
            txt = f"{text} - {author}"
            fnt = ImageFont.truetype(random.choice(fonts), 30)

            # Calculate the average length of a character and scale char count
            avg_char_width = (sum(fnt.getsize(char)[0]
                              for char in ascii_letters) / len(ascii_letters))
            max_char_count = int(img.size[0] * .90 / avg_char_width)

            # Create wrapped text object using the scaled character count
            txt = textwrap.fill(text=txt, width=max_char_count)
            draw = ImageDraw.Draw(img)
            draw.text((img.size[0]/2, img.size[1]/2), text=txt, font=fnt,
                      fill='red', anchor="mm")

            # Save image
            img.save(self.out_path)

            return self.out_path
