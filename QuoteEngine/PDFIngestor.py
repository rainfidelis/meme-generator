import os
import subprocess
from typing import List
from random import randint

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class PDFIngestor(IngestorInterface):
    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception("Cannot ingest file exception.")

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
