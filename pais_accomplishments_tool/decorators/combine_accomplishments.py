from bibtexparser.library import Entry
from pais_accomplishments_tool.model import AccEntry
from pais_accomplishments_tool.model.types import KindConf


class CombineAccomplishments:
    """Decorator that """
    _config: dict[str, KindConf]
    _entries: list[Entry]

    def __init__(self, entries: list[Entry], config: dict[str, KindConf]):
        assert any(isinstance(entry, Entry) for entry in entries)
        self._config = config
        self._entries = entries

    @property
    def entries(self) -> list[AccEntry]:
        combined_entries: list[AccEntry] = []

        for entry in self._entries:
            combined_entries.append(AccEntry(entry, self._config.get(entry.entry_type).template))

        return combined_entries

