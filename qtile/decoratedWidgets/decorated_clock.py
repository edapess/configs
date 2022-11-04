from qtile_extras.widget import modify
from decorations.decorations import decoration, base, iconFont, powerline
from libqtile.widget.clock import Clock
from libqtile.widget.textbox import TextBox
from libqtile.command import lazy


def clock(bg: str, fg: str) -> list:
  return [
    modify(
      TextBox,
      **base(bg, fg),
      # **decoration('left'),
      **iconFont(size=13),
      text = '',
      x = 4,
      padding=14
    ),
    modify(
    Clock,
    **decoration('right'),
    **iconFont(size=13),
    foreground = fg,
    background = bg,
    format="%H:%M %Y-%m-%d"

),
  ]