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
from bibtexparser.library import Entry
from . import AccField


class AccEntry:
    """Accomplishments entry object that wraps immutable bibtex Entry object."""
    _immutable_entry: Entry
    fields: list[AccField]
    _template: str | None
    _row: str | None

    def __init__(self, entry: Entry, template: str):
        assert entry
        assert template

        self._immutable_entry = entry
        self._template = template
        self._row = None
        self.fields = [
            AccField(f)
            for f in self._immutable_entry.fields
        ]

    @property
    def origin(self):
        """
        :returns: immutable entry origin
        """
        return self._immutable_entry

    def update(self, text: str):
        """Update current alias"""
        self._row = text

    def __repr__(self):
        if not self._row:
            _fields: dict[str, str] = {}

            for field in self.fields:
                try:
                    _fields[field.origin.key] = field.alias
                except ValueError:
                    _fields[field.origin.key] = field.origin.value

            self._row = self._template.format(**_fields)
        return self._row
