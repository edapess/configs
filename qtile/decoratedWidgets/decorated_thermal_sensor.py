from qtile_extras.widget import modify
from decorations.decorations import decoration, base, iconFont,powerline
from libqtile.widget.sensors import ThermalSensor
from libqtile.widget.textbox import TextBox
from libqtile.command import lazy


def thermal_sensor(bg: str, fg: str, fg_alert:str) -> list:
  return [
    modify(
      TextBox,
      **base(bg, fg),
      **decoration('left'),
      **iconFont(),
      text = '',
    #   x = 4,
      padding=14
    ),
    modify(
    ThermalSensor,
    **base(bg, fg),
    # **decoration('right'),
    **powerline('arrow_right'),
    **iconFont(),
    metric = True,
    padding = 3,
    threshold = 80,
    foreground_alert=fg_alert
),
  ]