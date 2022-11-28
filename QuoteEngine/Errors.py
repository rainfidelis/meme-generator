"""Custom error classes for the quote engine."""


class FileIngestError(Exception):
    """
    Raised when a file extension is not compatible with the called ingestor.

    :param path: A data file path of type string
    :param ingestor: The string name of the selected ingestor interface.
    """

    def __init__(self, path: str, ingestor=None) -> None:
        """Initialize the exception class with the provided attributes."""
        self.ext = path.split('.')[-1]
        self.ingestor = ingestor
        super().__init__(self.ext, self.ingestor)

    def __str__(self) -> str:
        """Return a custom message when the error is raised."""
        if self.ingestor:
            return f"{self.ext} not in allowed extensions for {self.ingestor}."
        else:
            return f"{self.ext} is not allowed."
