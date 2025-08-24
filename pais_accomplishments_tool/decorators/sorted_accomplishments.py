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
from pais_accomplishments_tool.model import AccEntry
from pais_accomplishments_tool.model.types import SortConf


class SortedAccomplishments:
    """Decorator that sorts accomplishments according to the sort key."""
    _config: SortConf
    _entries: list[AccEntry]
    _is_sort: bool

    def __init__(self, entries: list[AccEntry], config: SortConf):
        assert any(isinstance(entry, AccEntry) for entry in entries)
        self._config = config
        self._entries = entries
        self._is_sort = False

    @property
    def entries(self) -> list[AccEntry]:
        if not self._is_sort:
            self._sort()

        return self._entries

    def _sort(self):
        if self._config:
            def _entry_key(entry: AccEntry):
                for field in entry.origin.fields:
                    if self._config.key in field.key:
                        return field.value
                return entry.origin.key

            self._entries.sort(key=_entry_key, reverse=self._config.reversed)
        self._is_sort = True
