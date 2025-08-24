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
import dataclasses


@dataclasses.dataclass
class MorphConf:
    """Configuration of accomplishments morphing."""
    fields: tuple[str]


@dataclasses.dataclass
class KindConf:
    """Configuration of a kind of accomplishments."""
    key: str
    template: str
    morphs: MorphConf


@dataclasses.dataclass
class SortConf:
    """Configuration of a sort order."""
    key: str
    reversed: bool


@dataclasses.dataclass
class GroupConf:
    """Configuration of a group of the final list"""
    is_entry_type: bool
    is_field: bool
    field: str


@dataclasses.dataclass
class Parameters:
    """Configuration of an entry parameters."""
    source: str
    config: str
    destination: str
    is_capitalize: bool
    is_enumerate: bool


@dataclasses.dataclass
class Config:
    """An entry configuration."""
    kind: dict[str, KindConf]
    sort: SortConf | None
    group: GroupConf | None


__all__ = [
    "KindConf",
    "MorphConf",
    "Parameters",
    "SortConf",
    "Parameters",
    "Config",
    "GroupConf",
]
