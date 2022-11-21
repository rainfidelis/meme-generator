"""A script for generating memes directly on the command line."""

import os
import random
import argparse
from PIL import Image, ImageFont, ImageDraw

from QuoteEngine import Ingestor, QuoteModel


class MemeEngine:

    def __init__(self, output_dir) -> None:
        self.output_dir = output_dir
    
    def make_meme(self, img_path, text, author, width=500) -> str:
        fonts = ["./_fonts/LilitaOne-Regular.ttf", "./_fonts/Satisfy-Regular.ttf"]

        with Image.open(img_path) as img:

            # Resize image while maintaining the existing aspect ratio
            ratio = img.size[0] / img.size[1]
            height = int(ratio * img.size[1])
            img = img.resize((width, height), Image.Resampling.NEAREST)

            # Write quote to img
            message = f"{text}\n - {author}"
            fnt = ImageFont.truetype(random.choice(fonts), 20)
            d = ImageDraw.Draw(img)
            d.multiline_text((150, 350), message, font=fnt, fill='black', align="center")

            # Save image
            out_path = f"{self.output_dir}/{random.randint(0, 1000000)}.jpg"
            img.save(out_path)

            return out_path


def generate_meme(path=None, body=None, author=None):
    """Generate a meme given a path and a quote."""
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
    # @TODO Use ArgumentParser to parse the following CLI arguments
    # path - path to an image file
    # body - quote body to add to the image
    # author - quote author to add to the image
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', '-p', help="Optional path to an image file", type=str)
    parser.add_argument('--body', '-b', help="Optional quote body for the image", type=str)
    parser.add_argument('--author', '-a', help="Optional quote author for the image", type=str)
    
    args = parser.parse_args()
    print(generate_meme(args.path, args.body, args.author))
