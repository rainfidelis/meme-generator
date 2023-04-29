# System imports
import os
import random
import pathlib
import sys
import shutil

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
        self.resize(502, 528)

        # Display generated meme on main window
        img_path = self.random_meme()
        self.meme_image = QtWidgets.QLabel(self)
        self.meme_image.setGeometry(QtCore.QRect(0, 0, 501, 381))
        self.meme_image.setPixmap(QtGui.QPixmap(img_path))

        # Button for generating random memes
        self.random_button = QtWidgets.QPushButton("Random", self)
        self.random_button.setGeometry(QtCore.QRect(145, 400, 75, 23))
        self.random_button.setStatusTip("Generate a random meme")
        self.random_button.clicked.connect(self.click_random)

        # Button for creating custom memes
        self.create_button = QtWidgets.QPushButton("Creator", self)
        self.create_button.setGeometry(QtCore.QRect(225, 400, 75, 23))
        self.create_button.setStatusTip("Create a custom meme")
        self.create_button.clicked.connect(self.form_window)

        # Button for saving images
        self.save_button = QtWidgets.QPushButton("Save", self)
        self.save_button.setGeometry(QtCore.QRect(305, 400, 75, 23))
        self.save_button.setStatusTip("Save image to folder")
        self.save_button.clicked.connect(self.save_image)

        # Create status bar
        self.statusBar()

    def random_meme(self):
        """Generate a random meme and return the file path."""
        quotes, imgs = setup()
        quote = random.choice(quotes)
        img = random.choice(imgs)
        meme = MemeEngine('./tmp')
        path = meme.make_meme(img, quote.body, quote.author)
        self.current_path = pathlib.Path(path).absolute()
        return path

    def click_random(self):
        """Generate a new image whenever the `random` button is clicked."""
        path = self.random_meme()
        self.current_path = pathlib.Path(path).absolute()
        self.meme_image.setPixmap(QtGui.QPixmap(path))

    def form_window(self):
        """Open a new window with an input form for custom meme attributes."""
        self.form = FormWindow()
        self.form.show()

    def custom_meme(self, data_list):
        """Create custom meme using parameters passed from the form window"""
        quote = QuoteModel(data_list[1], data_list[2])
        meme = MemeEngine('./tmp')
        path = meme.make_meme(data_list[0], quote.body, quote.author)
        self.current_path = pathlib.Path(path).absolute()
        self.meme_image.setPixmap(QtGui.QPixmap(path))

    def save_image(self):
        """Save current image to user-selected file location"""
        dialog = QtWidgets.QFileDialog()
        dst = str(pathlib.Path.home()) + "\\Downloads"
        filename, _ = dialog.getSaveFileName(self, "Save Image", dst, "(*.jpg)")
        shutil.copyfile(self.current_path, filename)


class FormWindow(QWidget):
    """Generate new window with an input form for custom meme creation."""

    def __init__(self):
        super().__init__()

        self.setup_ui()

    def setup_ui(self):
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
