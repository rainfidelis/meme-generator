"""Ingest files with the `txt` extension."""

from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from .Errors import FileIngestError


class TxtIngestor(IngestorInterface):
    """Ingest files with the `txt` extension."""

    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Extract quote data from `txt` file.

        Open files using the built-in `open()` function and create
        QuoteModel objects from each line.

        Raise an exception if an unaccepted file extension is passed.
        """
        if not cls.can_ingest(path):
            raise FileIngestError(path, "TxtIngestor")

        quotes = []

        with open(path) as file:
            lines = file.readlines()

            for line in lines:
                if len(line) > 1:
                    parse = line.split("-")
                    quote = QuoteModel(parse[0].strip(), parse[1].strip())
                    quotes.append(quote)

        return quotes
