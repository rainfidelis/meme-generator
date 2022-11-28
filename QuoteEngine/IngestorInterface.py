"""Abstract base class (ABC) for ingesting data from multiple file types."""

from abc import ABC, abstractmethod
from typing import List

from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """
    Abstract base class (ABC) for ingesting data from multiple file types.

    An `IngestorInterface` represents a file consumption and extraction object.
    When realized, the interface receives a file and confirms the file type is
    a match using `can_ingest(path)`.

    Finally, it extracts the data in the file using `parse(path)` and
    constructs a list of `QuoteModel` objects for use in the main program.

    Realized subclasses provide their own allowed extensions for `can_ingest`
    and provide custom behavior to read and extract data from the file.
    """

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """
        Confirm the file's extension is in the list of allowed extensions.

        :param path: A data file path of type string
        :return: True or False

        """
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Create `QuoteModel` objects using data from the provided data file.

        Realized subclasses must override this method to parse their allowed
        file extensions and extract the data contained within.

        :param path: A data file path of type string
        :return: A list of `QuoteModel` objects, each created with a quote body
                 and an author.
        """
        pass
