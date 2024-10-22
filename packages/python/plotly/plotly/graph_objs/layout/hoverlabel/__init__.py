import sys
from typing import TYPE_CHECKING

if sys.version_info < (3, 7) or TYPE_CHECKING:
    from ._font import Font
    from ._grouptitlefont import Grouptitle_font
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__, __dir__ = relative_import(
        __name__, [], ["._font.Font", "._grouptitlefont.Grouptitle_font"]
    )
