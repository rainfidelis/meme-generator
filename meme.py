"""A script for generating memes directly on the command line."""

import os
import random
import argparse
from PIL import Image, ImageFont, ImageDraw

from QuoteEngine import Ingestor, QuoteModel


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
            ratio = img.size[0] / img.size[1]
            height = int(ratio * img.size[1])
            img = img.resize((width, height), Image.Resampling.NEAREST)

            # Add caption to image
            message = f"{text}\n - {author}"
            fnt = ImageFont.truetype(random.choice(fonts), 30)
            d = ImageDraw.Draw(img)
            d.multiline_text((150, 350), message, font=fnt, fill='black', align="center")

            # Save image
            img.save(self.out_path)

            return self.out_path


def generate_meme(path=None, body=None, author=None):
    """
    Generate a meme given an image path and a quote.
    
    If no path or quote is given, generate a meme with a random quote and image
    from the existing database. All parameters default to `None`, in which case a
    random meme has to be generated.

    :param path: Relative path to the image file
    :param body: Quote body for the meme
    :param author: Author of the provided quote
    """
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path

    if body is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)

    meme = MemeEngine('./tmp')
    path = meme.make_meme(img, quote.body, quote.author)
    return path


if __name__ == "__main__":
    # Create argument parser for use on the command line

    parser = argparse.ArgumentParser()
    parser.add_argument('--path', '-p',
                        help="Optional path to an image file", type=str)
    parser.add_argument('--body', '-b',
                        help="Optional quote body for the image", type=str)
    parser.add_argument('--author', '-a',
                        help="Optional quote author for the image", type=str)
    
    args = parser.parse_args()
    print(generate_meme(args.path, args.body, args.author))
