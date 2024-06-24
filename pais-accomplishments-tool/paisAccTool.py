# The PAIS Accomplishments - A Python Package
# Copyright (C) 2024 Roman Lupashko <mossy0.civets@icloud.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the Creative Commons Attribution-NonCommercial-ShareAlike 4.0
# International License (the "License").
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# License for the specific language governing permissions and
# limitations under the License.
#
# You should have received a copy of the License along with this program.
# If not, see <https://creativecommons.org/licenses/by-nc-sa/4.0/>.
#
# GitHub repository <https://github.com/CuberHuber/pais-accomplishments-tool>
import argparse
import dataclasses
import datetime
import os

import bibtexparser
import yaml
import pymorphy3
from bibtexparser import Library
from bibtexparser.library import Entry


@dataclasses.dataclass
class KindConf:
    key: str
    template: str
    morphs: tuple[str]


@dataclasses.dataclass
class SortConf:
    key: str
    reversed: bool


@dataclasses.dataclass
class Parameters:
    source: str
    config: str
    destination: str
    is_capitalize: bool
    is_enumerate: bool


@dataclasses.dataclass
class Config:
    kind: dict[str, KindConf]
    sort: SortConf | None


class AccomplishmentTool:
    _params: Parameters
    _library: Library
    _config: Config
    _entries: list[Entry]
    _out: list[str]

    def __init__(self, params: Parameters):
        self._params = params
        self._library = None
        self._config = None
        self._out = None
        self._entries = None

        self._load_library()
        self._load_config()
        self._sort()
        self._morphs()
        self._accomplishments()
        self._formatting()
        self._save()

    @property
    def accomplishments(self):
        return self._out

    def _load_library(self):
        """
        Get a bibtex library object from a file.
        :return:
        """
        self._library = bibtexparser.parse_file(self._params.source)
        self._entries = list(self._library.entries)
        for entry in self._entries:
            for field in entry.fields:
                if field.key in ('start', 'end'):
                    field.value = datetime.datetime.strptime(field.value, "%d.%m.%Y")

    def _sort(self):
        def _entry_key(entry: Entry):
            for field in entry.fields:
                if self._config.sort.key in field.key:
                    return field.value
            return entry.key

        if self._config.sort:
            self._entries.sort(key=_entry_key, reverse=self._config.sort.reversed)
        ...

    def _load_config(self):
        _out = {}
        _sort = None
        with open(self._params.config, "r") as f:
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
        self._config = Config(
            kind=_out,
            sort=_sort
        )

    def _morphs(self):
        morph = pymorphy3.MorphAnalyzer()
        for entry in self._entries:
            cfg = self._config.kind.get(entry.entry_type)
            if cfg.morphs:
                for field in entry.fields:
                    if field.key in cfg.morphs:
                        res = []
                        for word in field.value.split():
                            try:
                                _word = morph.parse(word.lower())[0].inflect({'gent'}).word
                                if word[0] == _word.capitalize()[0]:
                                    res.append(_word.capitalize())
                                else:
                                    res.append(_word)
                            except:
                                res.append(word)
                        field.value = ' '.join(res)

    def _accomplishments(self):
        """
        Generate accomplishments list from a bibtex library.
        :return:
        """
        self._out = []
        for entry in self._entries:
            print(f' [ ]  {entry.entry_type} accomplishment: {entry.key}', end='\t')
            fields = {field.key: field.value for field in entry.fields}
            cfg = self._config.kind.get(entry.entry_type)
            self._out.append(cfg.template.format(**fields))
            print('done')

    def _formatting(self):
        """
        Format accomplishments according to the formatting rules.
        :return:
        """
        if self._params.is_capitalize:
            self._out = [acc[0].capitalize() + acc[1:] for acc in self._out]

        if self._params.is_enumerate:
            self._out = [f'{i + 1}. {acc}' for i, acc in enumerate(self._out)]

    def _save(self):
        """
        Save accomplishments according to the text file
        """
        if self._params.destination:
            with open(self._params.destination, 'w') as f:
                for line in self._out:
                    f.write(line + '\n')


def parameters() -> tuple:
    """
    Get arguments from command line.
    :return:
    """
    parser = argparse.ArgumentParser(description='The micro tools for contain and formating accomplishments from '
                                                 'BibTex source')
    # Add arguments
    parser.add_argument('source', help='Path to source .bib file')
    parser.add_argument('-d', '--destination', required=False, help='Path to destination .bib file')
    parser.add_argument('--config', required=False, help='Path to config.yml file')
    parser.add_argument('-c', '--capitalize', default=False, help=f'Flag', action='store_true')
    parser.add_argument('-en', '--enumerate', default=False, help=f'Flag', action='store_true')
    # Parse the arguments
    args = parser.parse_args()

    if args.source is None:
        raise FileNotFoundError('Source path is required')

    if args.config is None:
        _config = os.path.dirname(__file__) + '/config.default.yml'
    else:
        _config = str(args.config)

    return _config, args.source, args.destination, bool(args.capitalize), bool(args.enumerate)


def hello():
    print("""Hello everyone!
This is the micro tools for contain and formating accomplishments from BibTex source""")


if __name__ == '__main__':
    _config_file, source, destination, is_capitalize, is_enumerate = parameters()
    hello()
    params = Parameters(source, _config_file, destination, is_capitalize, is_enumerate)
    out = AccomplishmentTool(params).accomplishments
    print(*out, sep='\n')
