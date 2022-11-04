from qtile_extras.widget import modify
from decorations.decorations import decoration, base, iconFont, powerline
from libqtile.widget.pomodoro import Pomodoro
from libqtile.widget.textbox import TextBox

#

def pomodoro(bg: str, fg: str) -> list:
  return [
        modify(
      TextBox,
      **base(bg, fg),
      **iconFont(),
      text = '',
      x = 4,
      # padding=14
    ),
    modify(
      Pomodoro,
      **base(bg, fg),
      **decoration('right'),
      **iconFont(size=13),
    color_active = fg,
    color_break = fg,
    color_inactive = fg
    ),
  ]