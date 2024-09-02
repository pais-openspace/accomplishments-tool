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
import os

from pais_accomplishments_tool import AccomplishmentTool, Parameters


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
    acc = AccomplishmentTool(params).accomplishments()
    print(acc)
