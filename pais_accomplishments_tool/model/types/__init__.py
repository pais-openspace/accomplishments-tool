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
