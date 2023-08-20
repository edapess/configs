from libqtile import layout
from colors import base, alert, accent, alert, secondary, text

def init_layout_theme():
    return {"margin":5,
            "border_width":2,
            "border_focus": text,
            "border_normal": secondary
            }

layout_theme = init_layout_theme()

def init_layouts():
    return [
    layout.Max(**layout_theme),
    layout.Columns(**layout_theme),
    layout.Stack(**layout_theme),
    layout.Bsp(**layout_theme),
    layout.Matrix(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.MonadWide(**layout_theme),
    layout.RatioTile(**layout_theme),
    layout.Tile(**layout_theme),
    layout.TreeTab(**layout_theme),
    layout.VerticalTile(**layout_theme),
    layout.Zoomy(**layout_theme),
]