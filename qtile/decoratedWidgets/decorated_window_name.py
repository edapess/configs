from libqtile.bar import CALCULATED
from libqtile.widget.windowname import WindowName
from decorations.decorations import base
from utils import get_window_name

def window_name(bg: str, fg: str) -> object:
  return WindowName(
    **base(bg, fg),
    format = '{state}{name}',
    parse_text = get_window_name,
    max_chars = 60,
    width = CALCULATED,
    fontsize = 12,
    font="Noto Sans Bold",


  )