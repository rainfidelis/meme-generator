"""A script for generating memes directly on the command line."""

import os
import random
import argparse

from QuoteEngine import Ingestor, QuoteModel
from MemeEngine import MemeEngine


def generate_meme(path=None, body=None, author=None):
    """
    Generate a meme given an image path and a quote.

    If no path or quote is given, generate a meme with a random quote and image
    from the existing database. All parameters default to `None`, in which case
    a random meme has to be generated.

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
            raise Exception('Author required if quote body is provided')
        quote = QuoteModel(body, author)

    if author:
        if body:
            quote = QuoteModel(body, author)
        else:
            raise Exception('You must provide a quote body with an author.')

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
