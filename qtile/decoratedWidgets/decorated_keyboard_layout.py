from qtile_extras.widget import modify
from decorations.decorations import decoration, base, iconFont, powerline
from libqtile.widget.keyboardlayout import KeyboardLayout
from libqtile.widget.textbox import TextBox
from libqtile.command import lazy


def keyboard_layout(bg: str, fg: str) -> list:
  return [
    modify(
      TextBox,
      **base(bg, fg),
      **iconFont(),
      text = '',
      x = 4,
      padding=14
    ),
    modify(
    KeyboardLayout,
    **decoration('right'),
    **iconFont(),
    configured_keyboards = ['us', 'ru', 'am phonetic-alt'],
    display_map = {'us':'US','ru':'RU','am phonetic-alt':'am'},
    background = bg,
),
  ]