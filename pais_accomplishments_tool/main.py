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
from .model import AccLibrary, AccConfiguration, AccGroup
from .decorators import (
    SortedAccomplishments,
    MorphedAccomplishments,
    FormattedAccomplishments,
    Save,
    CombineAccomplishments,
    GroupedAccomplishments,
)

from .model.types import Parameters, Config


class AccomplishmentTool:
    """
    Main accomplishment tool class.
    """
    _params: Parameters
    _config: Config
    _library: AccLibrary

    def __init__(self, params: Parameters):
        self._params = params
        self._config = AccConfiguration(self._params.config).content
        self._library = AccLibrary(self._params.source)

    def accomplishments(self) -> str:
        """Final accomplishments lists at String format."""

        out: str = ''
        acc = CombineAccomplishments(
            self._library.content,
            self._config.kind
        )
        groups = GroupedAccomplishments(acc.entries, self._config.group).groups
        for group in groups:
            out += str(AccGroup(
                FormattedAccomplishments(
                    MorphedAccomplishments(
                        SortedAccomplishments(
                            group.entries, self._config.sort
                        ).entries, self._config
                    ).entries, self._params
                ).entries, group.label
            )) + '\n\n'

        return str(Save(out, self._params))
