from qtile_extras.widget import modify
from decorations.decorations import decoration, base, iconFont,powerline
from libqtile.widget.cpu import CPU
from libqtile.widget.textbox import TextBox
from libqtile.command import lazy


def cpu(bg: str, fg: str, fg_fill:str) -> list:
  return [
    modify(
      TextBox,
      **base(bg, fg),
      **iconFont(),
      text = '',
    #   x = 4,
      padding=14
    ),
    modify(
    CPU,
    background=bg,
    **iconFont(),
    **powerline('arrow_right'),
    fill_color=fg_fill,
    mouse_callbacks={'Button1': lazy.spawn("alacritty -e btop")},
    format='{load_percent}%',
),
  ]