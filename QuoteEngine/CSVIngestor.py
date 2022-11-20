"""Ingest files with the `csv` extension."""

import pandas as pd
from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from .Errors import FileIngestError


class CSVIngestor(IngestorInterface):
    """Ingest files with the `csv` extension."""

    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Extract quote data from `csv` file using `pandas` and create QuoteModel objects from each row.

        Raise an exception if an unaccepted file extension is passed.
        """
        if not cls.can_ingest(path):
            raise FileIngestError(path, "CSVIngestor")

        quotes = []
        df = pd.read_csv(path, header=0)

        for index, row in df.iterrows():
            quote = QuoteModel(row['body'], row['author'])
            quotes.append(quote)

        return quotes
