from qtile_extras.widget import modify
from decorations.decorations import decoration, base, iconFont,powerline
from libqtile.widget.wlan import Wlan
from libqtile.widget.textbox import TextBox
from libqtile.command import lazy


def wlan(bg: str, fg: str) -> list:
  return [
    modify(
      TextBox,
      **base(bg, fg),
      **decoration('left'),
      **iconFont(),
      text = '',
    #   x = 4,
      padding=14
    ),
    modify(
      Wlan,
      **base(bg, fg),
      **powerline('arrow_right'),
    **iconFont(),
    format='{quality}/70',
    interface='wlp61s0',
    mouse_callbacks={'Button1': lazy.spawn('nm-connection-editor')}
),
  ]