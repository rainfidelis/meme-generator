# System imports
import os
import random
import pathlib
import sys

# PyQt5 imports
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication

# Local imports
from QuoteEngine import QuoteModel, Ingestor
from MemeEngine import MemeEngine

def setup():
    """
    Load all resources.
    
    :return quotes: a list of QuoteModel objects.
    :return imgs: a list of fully constructed image paths.
    """
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


class MemeApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Meme Generator")
        self.setGeometry(100, 100, 502, 528)

        # Display generated meme on main window
        img_path = self.random_meme()
        self.memeImage = QtWidgets.QLabel(self)
        self.memeImage.setGeometry(QtCore.QRect(0, 0, 501, 381))
        self.memeImage.setPixmap(QtGui.QPixmap(img_path))

        # Define button configurations
        self.randomButton = QtWidgets.QPushButton("Random", self)
        self.randomButton.setGeometry(QtCore.QRect(175, 400, 75, 23))
        self.randomButton.setStatusTip("Generate a random meme")
        self.randomButton.clicked.connect(self.click_random)

        self.createButton = QtWidgets.QPushButton("Creator", self)
        self.createButton.setGeometry(QtCore.QRect(255, 400, 75, 23))
        self.createButton.setStatusTip("Create a custom meme")
        self.createButton.clicked.connect(self.form_window)

        # Create status bar
        self.statusBar()

    def random_meme(self):
        """Generate a random meme and return the file path."""
        quotes, imgs = setup()
        quote = random.choice(quotes)
        img = random.choice(imgs)
        meme = MemeEngine('./tmp')
        path = meme.make_meme(img, quote.body, quote.author)
        return path

    def click_random(self):
        """Generate a new image whenever the `random` button is clicked."""
        path = self.random_meme()
        self.memeImage.setPixmap(QtGui.QPixmap(path))

    def form_window(self):
        """Open a new window with an input form."""
        self.form = FormWindow()
        self.form.show()

    def custom_meme(self, data_list):
        # Create custom meme
        quote = QuoteModel(data_list[1], data_list[2])
        meme = MemeEngine('./tmp')
        meme_path = meme.make_meme(data_list[0], quote.body, quote.author)
        self.memeImage.setPixmap(QtGui.QPixmap(meme_path))


class FormWindow(QWidget):
    """Generate new window with an input form for custom meme creation."""

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Create Your Meme')
        self.resize(502, 528)

        # Create image selector
        self.file_label = QtWidgets.QLabel('Select Image:')
        self.file_label.setFont(QtGui.QFont("Helvetica", 14))
        self.file_selector = QtWidgets.QPushButton('Browse')
        self.file_selector.clicked.connect(self.select_image)

        # Create text fields
        self.quote_label = QtWidgets.QLabel('Quote:')
        self.quote_label.setFont(QtGui.QFont("Helvetica", 14))
        self.quote_field = QtWidgets.QLineEdit()
        self.author_label = QtWidgets.QLabel('Author:')
        self.author_label.setFont(QtGui.QFont("Helvetica", 14))
        self.author_field = QtWidgets.QLineEdit()

        # Create submit button
        self.submit_button = QtWidgets.QPushButton('Create Meme!')
        self.submit_button.clicked.connect(self.submit_form)

        # Add all elements to layout
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.file_label)
        layout.addWidget(self.file_selector)
        layout.addWidget(self.quote_label)
        layout.addWidget(self.quote_field)
        layout.addWidget(self.author_label)
        layout.addWidget(self.author_field)
        layout.addWidget(self.submit_button)
        self.setLayout(layout)

    def select_image(self):
        # Open file dialog and set selected file to label
        file_dialog = QtWidgets.QFileDialog()
        file_dialog.setDefaultSuffix('.txt')
        path = str(pathlib.Path.home()) + "\\Downloads"
        filename, _ = file_dialog.getOpenFileName(self, "Choose an image", 
                                    path, "Image Files (*.jpg)")
        self.file_label.setText('Selected file: ' + filename)

    def submit_form(self):
        # Get all form data and print to console
        img = self.file_label.text().split(': ')[1]
        qt_body = self.quote_field.text()
        qt_author = self.author_field.text()
        data = [img, qt_body, qt_author]
        window.custom_meme(data)
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MemeApp()
    window.show()
    sys.exit(app.exec_())
