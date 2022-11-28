# Meme Generator

## Overview

This app is designed to generate a quote meme (an image with some quote on it). It takes an `image`, a `quote body`, and the `quote author`, and combines all three to form a new image.

The program may either generate a specific meme or a random one. Whenever the program is run with no image or quote provided, it generates a random meme using the dog images and dog quotes in the `_data` directory.

For the randomly generated memes, the program is able to receive quotes from multiple file types, including `.pdf`, `.docx`, `.txt`, and `.csv` files. Data read from these files are converted to a Python `Quote` object with a body and author attribute.

Feel free to customize the random memes by feeding in your own quote and image files in the relevant `_data` subdirectory. 

To generate a specific meme, pass your desired image, quote, and quote author to the meme generator.

### Built With

* [Python](https://www.python.org/)
* [Flask](https://flask.palletsprojects.com/en/2.2.x/)


<!-- GETTING STARTED -->
## Getting Started

To work with this project on your local device, you'll need to clone/fork the repository to your local device and install the required dependencies. The project primarily depends on the Python programming language, so you'll need to have that available locally.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.

* Python 3.10

    Visit the [official python website](https://www.python.org/downloads/) and download the appropriate installation binaries for your system.
* Pipenv (Optional!)
  ```sh
  pip install pipenv
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/rainfidelis/meme-generator.git
   ```
2. Install Python packages
   ```sh
   pipenv install
   ```
   To install without pipenv, run:
   ```sh
   pip install -r requirements.txt
   ```

<!-- Directories -->
## Directories and Modules

- [ ] _data: A directory for storing all relevant data files.
    - [ ] DogQuotes: Dog related quotes for random dog memes
    - [ ] photos: The program's image directory
    - [ ] SimpleLines: Accepted file types and desired content formatting for each file type
- [ ] _fonts: Contains true-type fonts for formating text on memes
- [ ] QuoteEngine: Contains a custom quote object, defines `ingestors` for different file types, and defines a custom error class for use in the ingestors.
- [ ] templates: Host to the html templates for the web app.
- [ ] app.py: Packages the meme generator into a web app.
- [ ] meme.py: Packages the meme generator into a command line utility.


<!-- USAGE EXAMPLES -->
## Usage

You can run this program as either a web app or a command line utility.

The command line utility takes three optional arguments:
- `-p` or `--path` an image path
- `-b` or `--body` a string quote body
- `-a` or `--author` a string quote author

Sample usage patterns include:
- `python meme.py` for generating a random image
- `python meme.py -p IMAGE_PATH` for generating a meme with the given image and a random quote
- `python meme.py -b QUOTE_BODY -a QUOTE_AUTHOR` for generating a random image meme with a specific quote
- `python meme.py -b QUOTE_BODY -a QUOTE_AUTHOR -p IMAGE_PATH` for generating a completely custom meme.


<!-- CONTACT -->
## Contact

Your Name - [@rainfidelis](https://twitter.com/rainfidelis) - rainnyfidelis@gmail.com

Project Link: [https://github.com/rainfidelis/meme-generator](https://github.com/rainfidelis/meme-generator)


<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Udacity](https://udacity.com)

