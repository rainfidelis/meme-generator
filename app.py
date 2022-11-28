"""Create a web app for rendering and generating random or custom memes."""

import random
import os
import requests
from flask import (
            Flask, render_template,
            abort, request, flash,
            redirect, url_for)

from QuoteEngine import Ingestor, QuoteModel
from MemeEngine import MemeEngine


app = Flask(__name__)
app.secret_key = os.urandom(12)

meme = MemeEngine('./static')


def setup():
    """Load all resources."""
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    # Generate a list of quote objects from all quote files
    quotes = []
    for file in quote_files:
        quotes.extend(Ingestor.parse(file))

    # Find all images within the image directory
    images_path = "./_data/photos/dog/"
    imgs = []
    for root, dirs, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generate a random meme."""
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme."""
    # Receive form data
    img_url = request.form.get('image_url')
    body = request.form.get('body')
    author = request.form.get('author')

    # Generate and save image from img_url
    response = requests.get(img_url)
    if response.status_code == 200:
        img_path = f'./_data/photos/uploads/{random.randint(0, 100000000)}.png'
        with open(img_path, 'wb') as img:
            img.write(response.content)

    else:
        # Display error message and abort
        print(response.status_code)
        flash("Could not generate image from URL")
        return redirect(url_for('meme_form'))

    # Generate and return meme
    quote = QuoteModel(body, author)
    path = meme.make_meme(img_path, quote.body, quote.author)

    # Delete temp image file
    os.remove(img_path)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
