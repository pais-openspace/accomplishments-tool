# The PAIS Accomplishments - A Python Package
# Copyright (c) 2024-2025 Roman Lupashko <mossy0.civets@icloud.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the Creative Commons Attribution-NonCommercial-ShareAlike 4.0
# International License (the "License").
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# License for the specific language governing permissions and
# limitations under the License.
#
# You should have received a copy of the License along with this program.
# If not, see <https://creativecommons.org/licenses/by-nc-sa/4.0/>.
#
# GitHub repository <https://github.com/CuberHuber/pais-accomplishments-tool>
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
