from typing import List

from .IngestorInterface import IngestorInterface
from .CSVIngestor import CSVIngestor
from .PDFIngestor import PDFIngestor
from .TxtIngestor import TxtIngestor
from .DocxIngestor import DocxIngestor
from .QuoteModel import QuoteModel


class Ingestor(IngestorInterface):
    ingestors = [CSVIngestor, PDFIngestor, TxtIngestor, DocxIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:

        for ingestor in cls.ingestors:

            if ingestor.can_ingest(path):
                quotes = ingestor.parse(path)

        return quotes