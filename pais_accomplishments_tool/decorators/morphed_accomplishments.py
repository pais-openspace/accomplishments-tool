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
import pymorphy3

from pais_accomplishments_tool.model import AccEntry
from pais_accomplishments_tool.model.types import Config


class MorphedAccomplishments:
    """Decorator that """
    _config: Config
    _entries: list[AccEntry]
    _is_morphed: bool

    def __init__(self, entries: list[AccEntry], config: Config):
        self._config = config
        self._entries = entries
        self._is_morphed = False

    @property
    def entries(self) -> list[AccEntry]:
        if not self._is_morphed:
            self._morphing()

        return self._entries

    def _morphing(self):
        morph = pymorphy3.MorphAnalyzer()
        for entry in self._entries:
            cfg = self._config.kind.get(entry.origin.entry_type)
            if cfg.morphs:
                for field in entry.fields:
                    if field.origin.key in cfg.morphs:
                        res = []
                        for word in field.origin.value.split():
                            try:
                                _word = morph.parse(word.lower())[0].inflect({'gent'}).word
                                if word[0] == _word.capitalize()[0]:
                                    res.append(_word.capitalize())
                                else:
                                    res.append(_word)
                            except:
                                res.append(word)
                        field.update(' '.join(res))
        self._is_morphed = True
