"""Ingest files with the `pdf` extension."""

import os
import subprocess
from typing import List
from random import randint

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from .Errors import FileIngestError


class PDFIngestor(IngestorInterface):
    """Ingest files with the `pdf` extension."""

    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Extract quote data from `pdf` file.

        Use the `pdftotext` CMD tool and create QuoteModel objects from each
        line. The `PDFIngestor` first converts pdf to text files before
        extracting its content. Upon completion, the text file is deleted.

        Raise an exception if an unaccepted file extension is passed.
        """
        if not cls.can_ingest(path):
            raise FileIngestError(path, "PDFIngestor")

        quotes = []
        tmp = f"./tmp/{randint(0, 1000000)}.txt"
        call = subprocess.call(['pdftotext', '-layout', path, tmp])

        with open(tmp) as file:
            lines = file.readlines()

            for line in lines:
                if len(line) > 1:
                    parse = line.split("-")
                    quote = QuoteModel(parse[0].strip(), parse[1].strip())
                    quotes.append(quote)

        os.remove(tmp)
        return quotes
