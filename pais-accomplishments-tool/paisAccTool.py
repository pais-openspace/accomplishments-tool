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

import bibtexparser
import pymorphy3
from bibtexparser import Library

DEF_TEMPLATE = '{prefix} {type} {title}, {author}, {organization}, {month}.{year}'
DEF_MORPHS = ('type', 'organization')


def library(file) -> Library:
    """
    Get a bibtex library object from a file.
    :param file:
    :return:
    """
    return bibtexparser.parse_file(file)


def accomplishments(lib: Library, template: str, for_morphs: tuple[str]) -> list[str]:
    """
    Generate accomplishments list from a bibtex library.
    :param lib:
    :param template:
    :param for_morphs:
    :return:
    """
    output = []
    for entry in lib.entries:
        print(f' [ ]  {entry.entry_type} accomplishment: {entry.key}', end='\t')
        fields = {field.key: field.value for field in entry.fields}
        morph = pymorphy3.MorphAnalyzer()
        for field in fields.items():
            if field[0] in for_morphs:
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
        output.append(template.format(**fields))
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
        _accomplishments = [acc[0].capitalize()+acc[1:] for acc in _accomplishments]

    if _is_enumerate:
        _accomplishments = [f'{i+1}. {acc}' for i, acc in enumerate(_accomplishments)]

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
    parser.add_argument('-t', '--template', required=False,
                        help='A template string for generating accomplishment string. '
                             'Default: ' + DEF_TEMPLATE)
    parser.add_argument('-m', '--morphs', required=False, nargs='+',
                        help=f'A list of fields for morphological transformations. '
                             f'Default: {DEF_MORPHS}')
    parser.add_argument('-c', '--capitalize', default=False, help=f'Flag', action='store_true')
    parser.add_argument('-en', '--enumerate', default=False, help=f'Flag', action='store_true')
    # Parse the arguments
    args = parser.parse_args()

    template = args.template if args.template else DEF_TEMPLATE
    morphs = tuple(args.morphs) if args.morphs else DEF_MORPHS
    if args.source is None:
        raise FileNotFoundError('Source path is required')

    return template, morphs, args.source, args.destination, bool(args.capitalize), bool(args.enumerate)


def hello():
    print("""Hello everyone!
This is the micro tools for contain and formating accomplishments from BibTex source""")


if __name__ == '__main__':
    template, morphs, source, destination, is_capitalize, is_enumerate = parameters()
    hello()
    accs = accomplishments(library(source), template, morphs)
    accs = formatting(accs, is_capitalize, is_enumerate)
    if destination:
        save(accs, destination)
    else:
        print(*accs, sep='\n\r')

