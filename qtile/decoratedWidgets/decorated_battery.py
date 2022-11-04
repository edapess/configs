from qtile_extras.widget import modify
from decorations.decorations import decoration, base, iconFont
from libqtile.widget.battery import Battery
from libqtile.widget.textbox import TextBox
from libqtile.command import lazy


def battery(bg: str, fg: str,low_fg: str):
  return modify(
    Battery,
    **decoration('right'),
    **iconFont(),
    **base(bg, fg),
    update_interval = 10,
    low_foreground = low_fg,
    charge_char='',
    discharge_char='',
    empty_char='',
    full_char='',
    format='{char} {percent:2.0%}',
),
