from qtile_extras.widget.decorations import RectDecoration, PowerLineDecoration
from libqtile.widget.textbox import TextBox

def decoration(side: str = '') -> dict:
  return { 'decorations': [
    RectDecoration(
      filled = True,
      radius = {
        'left': [8, 0, 0, 8],
        'right': [0, 8, 8, 0]
      }.get(side, 8),
      use_widget_background = True,
    )
  ]}
def base(bg: str, fg: str) -> dict:
  return {
    'background': bg,
    'foreground': fg,
  }
  
def iconFont(size = 15) -> dict:
  return {
    'font': 'CaskaydiaCove Nerd Font',
    'fontsize': size
  }

def sep(bg: str,fg: str, offset = 0, padding = 8) -> TextBox:
  return TextBox(
    **base(bg, fg),
    **iconFont(),
    offset = offset,
    padding = padding,
    text = '',
)
def powerline(path: str | list, size = 9) -> dict:
  return { 'decorations': [
    PowerLineDecoration(
      path = path,
      size = size,
    )
  ]}