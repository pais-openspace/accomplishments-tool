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
from itertools import groupby

from pais_accomplishments_tool.model import AccEntry, AccGroup
from pais_accomplishments_tool.model.types import GroupConf


class GroupedAccomplishments:
    """Decorator that groups accomplishments according to the key"""
    _config: GroupConf
    _entries: list[AccEntry]
    _groups: list[AccGroup] | None
    _is_grouped: bool

    def __init__(self, entries: list[AccEntry], config: GroupConf):
        assert any(isinstance(entry, AccEntry) for entry in entries)
        self._config = config
        self._entries = entries
        self._groups = []
        self._is_grouped = False

    @property
    def groups(self) -> list[AccGroup]:
        """"""
        if not self._is_grouped:
            self._grouping()

        return self._groups

    def _grouping(self):
        if self._config:
            def _entry_key(entry: AccEntry):
                if self._config.is_entry_type:
                    return entry.origin.entry_type
                if self._config.is_field:
                    for field in entry.origin.fields:
                        if self._config.field == field.key:
                            return field.value

            self._entries.sort(key=_entry_key)

            for key, value in groupby(self._entries, key=_entry_key):
                self._groups.append(AccGroup(list(value), key))

        self._is_sort = True
