from libqtile.widget.cmus import Cmus
from libqtile.widget.textbox import TextBox

from qtile_extras.widget import modify
from decorations.decorations import decoration, base, iconFont

def cmus(bg: str,fg:str, pc: str) -> list:
      return [
    modify(
      TextBox,
      **base(bg, fg),
      **decoration('left'),
      **iconFont(),
      text = '',
      x = 4,
    ),
    modify(
      Cmus,
      **base(bg, None),
        font="Noto Sans Bold",
      **decoration('right'),
      play_color=pc

    ),
  ]