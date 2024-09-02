from pais_accomplishments_tool.model.types import Parameters


class Save:
    """Decorator that saving text to file"""
    _config: Parameters
    _text: str

    def __init__(self, text: str, config: Parameters):
        self._config = config
        self._text = text
        self._save()

    def _save(self):
        """
        Save accomplishments according to the text file
        """
        if self._config.destination:
            with open(self._config.destination, 'w') as f:
                f.write(self._text + '\n')

    def __repr__(self):
        return self._text + '\n'
