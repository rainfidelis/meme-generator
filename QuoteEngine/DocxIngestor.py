import docx
from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class DocxIngestor(IngestorInterface):
    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception("Cannot ingest file exception.")

        quotes = []
        doc = docx.Document(path)

        for par in doc.paragraphs:
            if par != "":
                parse = par.text.split('-')
                quote = QuoteModel(parse[0].strip(), parse[1].strip())
                quotes.append(quote)

        return quotes
