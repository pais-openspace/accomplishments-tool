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
