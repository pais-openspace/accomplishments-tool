import bibtexparser


class AccLibrary:
    """Library of Accomplishments. Decorator of the bibtexparser"""
    _src: str
    _library: bibtexparser.Library | None
    _entries: list[bibtexparser.library.Entry] | None

    def __init__(self, path: str):
        self._src = path
        self._entries = None
        self._library = None

    @property
    def content(self):
        """
        :returns List of Entry. Lazy load mode.
        """
        if self._entries is None:
            self._load_entries()
        return self._entries

    def _load_library(self):
        """Get a bibtex library object from a file."""
        self._library = bibtexparser.parse_file(self._src)

    def _load_entries(self):
        """Loads all entries from bibtex library. Lazy load mode."""
        if self._library is None:
            self._load_library()
        self._entries = list(self._library.entries)
        # for entry in self._entries:
        #     for field in entry.fields:
        #         if field.key in ('start', 'end'):
        #             field.value = datetime.datetime.strptime(field.value, "%d.%m.%Y")
