from qtile_extras.widget import modify
from decorations.decorations import decoration, base, iconFont, powerline
from libqtile.widget.volume import Volume
from libqtile.widget.textbox import TextBox


def volume(bg: str, fg: str) -> list:
  return [
    modify(
      TextBox,
      **base(bg, fg),
      **iconFont(),
      text = '',
      x = 4,
    ),
    modify(
      Volume,
      **base(bg, fg),
      **iconFont(),
      **powerline('arrow_right'),
      commands = {
        'decrease': 'pamixer --decrease 5',
        'increase': 'pamixer --increase 5',
        'get': 'pamixer --get-volume-human',
        'mute': 'pamixer --toggle-mute',
      },
      update_interval = 0.1,
    ),
  ]