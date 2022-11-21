"""
Initialize the QuoteEngine directory.

Receive data from data files for processing and produce a list of quote objects
returned by the appropriate `Ingestor`.
"""


from .Ingestor import Ingestor
from .QuoteModel import QuoteModel
