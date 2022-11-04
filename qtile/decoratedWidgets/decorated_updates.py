from qtile_extras.widget import modify
from decorations.decorations import decoration, base, iconFont,powerline
from libqtile.widget.check_updates import CheckUpdates
from libqtile.widget.textbox import TextBox
from libqtile.command import lazy


def check_updates(bg: str, fg: str, no_updates_color:str, have_updates_colors: str) -> list:
  return [
    modify(
      TextBox,
      **base(bg, fg),
      **iconFont(),
      **decoration('left'),
      text = '',
    #   x = 4,
      padding=14
    ),
    modify(
    CheckUpdates,
    **iconFont(size=13),
    **powerline('arrow_right'),
    distro='Arch_Sup',
    colour_have_updates=have_updates_colors,
    colour_no_updates = no_updates_color,
    background = bg,
    execute = 'alacritty -e yay',
    display_format = 'upd {updates}',
    initial_text = 'check...',
    no_update_string = 'yay'
),
  ]