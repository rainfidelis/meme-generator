"""Leverage other realized ingestor classes to ingest `pdf`, `csv`, `txt`, and `docx` files."""

from typing import List

from .IngestorInterface import IngestorInterface
from .CSVIngestor import CSVIngestor
from .PDFIngestor import PDFIngestor
from .TxtIngestor import TxtIngestor
from .DocxIngestor import DocxIngestor
from .QuoteModel import QuoteModel


class Ingestor(IngestorInterface):
    """Leverage other realized ingestor classes to ingest `pdf`, `csv`, `txt`, and `docx` files."""

    ingestors = [CSVIngestor, PDFIngestor, TxtIngestor, DocxIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Find the appropriate ingestor for the provided file type and return a list of QuoteModel objects.

        Raise `cannot ingest exception` if file type is not supported by any ingestor.
        """
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                quotes = ingestor.parse(path)
                return quotes

        raise Exception("Cannot ingest file exception.")
