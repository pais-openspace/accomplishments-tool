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
import os

import bibtexparser
import yaml
import pymorphy3
from bibtexparser import Library


@dataclasses.dataclass
class KindConf:
    key: str
    template: str
    morphs: tuple[str]


def library(file) -> Library:
    """
    Get a bibtex library object from a file.
    :param file:
    :return:
    """
    return bibtexparser.parse_file(file)


def config(file) -> dict[str, KindConf]:
    _out = {}
    with open(file, "r") as f:
        yml = yaml.safe_load(f)
        if yml.get('kinds'):
            for kind, value in yml.get('kinds').items():
                _out[kind] = (KindConf(kind, value.get('template'), value.get('morphs')))
        else:
            raise ValueError('No kinds found in config file')
    return _out


def accomplishments(lib: Library, config: dict[str, KindConf]) -> list[str]:
    """
    Generate accomplishments list from a bibtex library.
    :param config:
    :param lib:
    :return:
    """
    output = []
    for entry in lib.entries:
        print(f' [ ]  {entry.entry_type} accomplishment: {entry.key}', end='\t')
        fields = {field.key: field.value for field in entry.fields}
        cfg = config.get(entry.entry_type)
        morph = pymorphy3.MorphAnalyzer()
        for field in fields.items():
            if field[0] in cfg.morphs:
                res = []
                for word in field[1].split():
                    try:
                        _word = morph.parse(word.lower())[0].inflect({'gent'}).word
                        if word[0] == _word.capitalize()[0]:
                            res.append(_word.capitalize())
                        else:
                            res.append(_word)
                    except:
                        res.append(word)
                fields[field[0]] = ' '.join(res)
        output.append(cfg.template.format(**fields))
        print('done')
    return output


def formatting(_accomplishments: list[str], _is_capitalize: bool, _is_enumerate: bool) -> list[str]:
    """
    Format accomplishments according to the formatting rules.
    :param _accomplishments:
    :param _is_capitalize:
    :param _is_enumerate:
    :return:
    """
    if _is_capitalize:
        _accomplishments = [acc[0].capitalize() + acc[1:] for acc in _accomplishments]

    if _is_enumerate:
        _accomplishments = [f'{i + 1}. {acc}' for i, acc in enumerate(_accomplishments)]

    return _accomplishments


def save(_accomplishments: list[str], _path: str) -> None:
    """
    Save accomplishments according to the text file
    :param _accomplishments:
    :param _path:
    """
    with open(_path, 'w') as f:
        for line in _accomplishments:
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
    accs = accomplishments(library(source), config(_config_file))
    accs = formatting(accs, is_capitalize, is_enumerate)
    if destination:
        save(accs, destination)
    else:
        print(*accs, sep='\n\r')
