from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TxtIngestor(IngestorInterface):
    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception("Cannot ingest file exception.")

        quotes = []

        with open(path) as file:
            lines = file.readlines()

            for line in lines:
                if len(line) > 1:
                    parse = line.split("-")
                    quote = QuoteModel(parse[0].strip(), parse[1].strip())
                    quotes.append(quote)

        return quotes
