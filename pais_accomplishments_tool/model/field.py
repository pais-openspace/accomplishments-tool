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
from bibtexparser.model import Field


class AccField:
    """Accomplishments field of the entry object that wraps immutable bibtex Field object."""
    _immutable_field: Field
    _alias: str | None

    def __init__(self, field: Field):
        self._immutable_field = field
        self._alias = None

    @property
    def origin(self):
        """
        :return: immutable field origin
        """
        return self._immutable_field

    @property
    def alias(self):
        """
        :return: alias of the field
        """
        if self._alias is None:
            raise ValueError("AccField has no alias set")
        return self._alias

    def update(self, text: str):
        """
        :param text: new text as an alias of the field
        """
        self._alias = text
