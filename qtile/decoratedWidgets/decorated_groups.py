from decorations.decorations import iconFont
from extras.group_box import GroupBox

from colors import based_colors, light_colors, colorfull_colors


def groups(bg: str) -> GroupBox:
  return GroupBox(
    **iconFont(size=17),
    background = bg,
    borderwidth = 1,
    colors = [
      based_colors['orange'],based_colors['light_orange'],based_colors['spanish_viridian'],
      based_colors['white'],based_colors['light_background'],based_colors['purple_background'],
      colorfull_colors['purple'],colorfull_colors['sky_blue'],light_colors['baby_powder'],
    ],
    highlight_color = based_colors['risin_black'],
    highlight_method = 'line',
    inactive = colorfull_colors['purple'],
    invert = True,
    padding = 7,
    rainbow = True,
  )