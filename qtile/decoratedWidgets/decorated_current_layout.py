from qtile_extras.widget import modify
from decorations.decorations import decoration, base, iconFont,powerline
from libqtile.widget.textbox import TextBox
from libqtile.widget.currentlayout import CurrentLayout
#

def current_layout(bg: str, fg: str) -> list:
  return [
      modify(
      TextBox,
      **base(bg, fg),
      **iconFont(),
      **decoration('left'),
      text = '練',
      padding=8
    ),
    modify(
      CurrentLayout,
      **base(bg, fg),
      **powerline('arrow_left'),
      **iconFont(size=14),
    ),
  ]