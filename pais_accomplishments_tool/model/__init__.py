"""
The PAIS Accomplishments - A Python Package
Copyright (C) 2024 Roman Lupashko <mossy0.civets@icloud.com>

This program is free software: you can redistribute it and/or modify
it under the terms of the Creative Commons Attribution-NonCommercial-ShareAlike 4.0
International License (the "License").

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
License for the specific language governing permissions and
limitations under the License.

You should have received a copy of the License along with this program.
If not, see <https://creativecommons.org/licenses/by-nc-sa/4.0/>.

GitHub repository <https://github.com/CuberHuber/pais-accomplishments-tool>
"""
from .library import AccLibrary
from .configuration import AccConfiguration
from .field import AccField
from .entry import AccEntry
from .group import AccGroup


__all__ = [
    "types",
    "AccEntry",
    "AccField",
    "AccGroup",
    "AccLibrary",
    "AccConfiguration",
]

