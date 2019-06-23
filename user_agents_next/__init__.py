from .parsers import parse


__version__ = '1.1.3'
VERSION = tuple(int(x) for x in __version__.split('.'))

__all__ = ['__version__', 'VERSION', 'parse']
