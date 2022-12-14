"""Ingest files with the `docx` extension."""

import docx
from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from .Errors import FileIngestError


class DocxIngestor(IngestorInterface):
    """Ingest files with the `docx` extension."""

    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Extract quote data from `docx` file.

        Read files using the `docx` library and create QuoteModel objects from
        each paragraph.

        Raise an exception if an unaccepted file extension is passed.
        """
        if not cls.can_ingest(path):
            raise FileIngestError(path, "DocxIngestor")

        quotes = []
        doc = docx.Document(path)

        for par in doc.paragraphs:
            if par.text != "":
                parse = par.text.split('-')
                quote = QuoteModel(parse[0].strip(), parse[1].strip())
                quotes.append(quote)

        return quotes
