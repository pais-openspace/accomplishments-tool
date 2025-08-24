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
from pais_accomplishments_tool.model.types import Parameters


class Save:
    """Decorator that saving text to file"""
    _config: Parameters
    _text: str

    def __init__(self, text: str, config: Parameters):
        self._config = config
        self._text = text
        self._save()

    def _save(self):
        """
        Save accomplishments according to the text file
        """
        if self._config.destination:
            with open(self._config.destination, 'w') as f:
                f.write(self._text + '\n')

    def __repr__(self):
        return self._text + '\n'
