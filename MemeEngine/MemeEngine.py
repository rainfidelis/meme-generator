"""Create a meme object generator."""

import random
import textwrap
import os
from pathlib import Path
from string import ascii_letters

from PIL import Image, ImageFont, ImageDraw

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
        :param text_color: Define your desired text color. Defaults to black.
        :param width: Width to use when resizing image. Defaults to 500.

        :return: The string location of the newly created meme.
        """
        self.empty_dir()
        font = "./_fonts/LilitaOne-Regular.ttf"

        with Image.open(img_path) as img:

            # Resize image while maintaining the existing aspect ratio
            ratio = width/float(img.size[0])
            height = int(ratio*float(img.size[1]))
            img = img.resize((width, height), Image.Resampling.NEAREST)

            # Create text on background for text
            bg = Image.new('RGBA', (600, 130), color=(0, 0, 0))

            # Define text and font
            txt = f"{text} - {author}"
            fnt = ImageFont.truetype(font, 30)

            # Calculate the average length of a character and scale char count
            avg_char_width = (sum(fnt.getsize(char)[0]
                              for char in ascii_letters) / len(ascii_letters))
            max_char_count = int(bg.size[0] * .90 / avg_char_width)

            # Wrapped the text object using the scaled character count
            txt = textwrap.fill(text=txt, width=max_char_count)

            # Write text to the created background
            draw = ImageDraw.Draw(bg)
            draw.text((bg.size[0]/2, bg.size[1]/2), text=txt, font=fnt,
                      fill=(255, 255, 255), anchor="mm")
            
            # Append background to the bottom of the original image
            img.paste(bg, (-40, 370))

            # Save image
            img.save(self.out_path)

            return self.out_path
        
    def empty_dir(self):
        """
        A function to keep the project lightweight by emptying the tmp
        directory each time the make_meme function is called.
        """
        existing_files = os.listdir(Path('./tmp'))
        for file in existing_files:
            path = Path('./tmp/' + file)
            os.remove(path)
