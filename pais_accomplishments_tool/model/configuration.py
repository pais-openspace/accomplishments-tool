import yaml

from pais_accomplishments_tool.model.types import KindConf, SortConf, GroupConf, Config


class AccConfiguration:
    """Configuration of the Accomplishments tool. Decorator of the yaml"""
    _path: str
    _config: Config | None

    def __init__(self, path: str):
        self._path = path
        self._config = None

    @property
    def content(self) -> Config:
        """
        :returns Config object. Lazy load mode.
        """
        if self._config is None:
            self._load_config()

        return self._config

    def _load_config(self):
        _out = {}
        _sort = None
        _group = None
        with open(self._path, "r") as f:
            yml = yaml.safe_load(f)
            if yml.get('kinds'):
                for kind, value in yml.get('kinds').items():
                    _out[kind] = (KindConf(kind, value.get('template'), value.get('morphs')))
            else:
                raise ValueError('No kinds found in config file')
            if yml.get('sort'):
                _sort = SortConf(
                    key=yml.get('sort').get('field'),
                    reversed=bool(yml.get('sort').get('reversed'))
                )
            if yml.get('group'):
                _group = GroupConf(
                    is_entry_type=yml.get('group').get('is_entry_type'),
                    is_field=yml.get('group').get('is_field'),
                    field=yml.get('group').get('field'),
                )

        self._config = Config(
            kind=_out,
            sort=_sort,
            group=_group,
        )
