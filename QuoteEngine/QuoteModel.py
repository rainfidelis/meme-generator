"""Create a Quote Object."""


class QuoteModel:
    """
    A Quote object.

    A quote contains a quote `body` (or quote) and the `author` of the quote.
    The QuoteModel object creates an object representation of each quote,
    linking each quote body to its author.
    """

    def __init__(self, body: str, author: str) -> None:
        """
        Create a `QuoteModel`.

        :param body: A quote string
        :param author: The quote author's name
        """
        self.body = body
        self.author = author

    def __str__(self) -> str:
        """Return a human-readable representation of the object."""
        return f'"{self.body}" by {self.author.capitalize()}'

    def __repr__(self) -> str:
        """Return a computer-readable representation of the object."""
        return f'<{self.body}>'
