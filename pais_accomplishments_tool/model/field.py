from bibtexparser.model import Field


class AccField:
    """Accomplishments field of the entry object that wraps immutable bibtex Field object."""
    _immutable_field: Field
    _alias: str | None

    def __init__(self, field: Field):
        self._immutable_field = field
        self._alias = None

    @property
    def origin(self):
        """
        :return: immutable field origin
        """
        return self._immutable_field

    @property
    def alias(self):
        """
        :return: alias of the field
        """
        if self._alias is None:
            raise ValueError("AccField has no alias set")
        return self._alias

    def update(self, text: str):
        """
        :param text: new text as an alias of the field
        """
        self._alias = text
