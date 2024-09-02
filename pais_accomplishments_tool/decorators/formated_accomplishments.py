from pais_accomplishments_tool.model import AccEntry
from pais_accomplishments_tool.model.types import Parameters


class FormattedAccomplishments:
    """Decorator that formats accomplishments according to the given parameters."""
    _config: Parameters
    _entries: list[AccEntry]
    _is_formatted: bool

    def __init__(self, entries: list[AccEntry], config: Parameters):
        self._config = config
        self._entries = entries
        self._is_formatted = False

    @property
    def entries(self) -> list[AccEntry]:
        if not self._is_formatted:
            self._formatting()

        return self._entries

    def _formatting(self):
        if self._config.is_capitalize:
            for acc in self._entries:
                acc_text = str(acc)
                acc.update(acc_text[0].capitalize() + acc_text[1:])

        if self._config.is_enumerate:
            i = 0
            for acc in self._entries:
                acc.update(f'{i + 1}. {acc}')
                i += 1

        self._is_formatted = True
