from typing import TYPE_CHECKING

from .entry import AccEntry


class AccGroup:
    """Accomplishments group that contains an entries list and group title."""
    _entries: list[AccEntry]
    _label: str

    def __init__(self, entries: list[AccEntry], label: str | None = None) -> None:
        self._entries = entries
        self._label = label

    @property
    def entries(self) -> list[AccEntry]:
        return self._entries

    @property
    def label(self) -> str:
        return self._label

    def __repr__(self) -> str:
        _out: str = ''
        if self._label:
            _out += f'# {self._label} : group\n'

        for entry in self._entries:
            _out += f'{entry}\n'

        return _out
