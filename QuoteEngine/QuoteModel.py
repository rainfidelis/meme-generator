class QuoteModel:
    def __init__(self, body, author) -> None:
        self.body = body
        self.author = author

    def __str__(self) -> str:
        return f"{self.body} - {self.author}"

    def __repr__(self) -> str:
        return f"<{self.quote}>"
