import pandas as pd
from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class CSVIngestor(IngestorInterface):
    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception("Cannot ingest file exception.")

        quotes = []
        df = pd.read_csv(path, header=0)

        for index, row in df.iterrows():
            quote = QuoteModel(row['body'], row['author'])
            quotes.append(quote)

        return quotes
