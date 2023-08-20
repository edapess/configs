from libqtile import bar, widget
from libqtile.config import Screen
from colors import accent, base, secondary, secondary2, text, alert, darkBase
from utils import search_dmenu

def get_bar():
    return [
        Screen(
            top=bar.Bar(
                [
                    widget.Spacer(
                        length=10,
                        background=darkBase
                    ),
                    widget.Image(
                        filename='~/.config/qtile/assets/top-bar-icons/launch.svg',
                        background=darkBase
                    ),
                    widget.Image(
                        filename='~/.config/qtile/assets/top-bar-icons/rightWave.svg',
                        margin_y=-10,
                        margin_x=-10,
                        scale=True,
                    ),
                    widget.GroupBox(
                        font="FiraCode Nerd Font",
                        fontsize=16,
                        padding_y=10,
                        padding_x=4,
                        border=0,
                        highlight_method='text',
                        active=secondary,
                        block_highlight_text_color=text,
                        inactive=secondary2,
                        background=base,
                        this_current_screen_border=text,
                        urgent_text=alert,
                        rounded=False,
                        disable_drag=True,
                    ),
                    widget.Image(
                        filename='~/.config/qtile/assets/top-bar-icons/toRightAngle.svg',
                        margin_y=-10,
                        margin_x=-10
                    ),
                    widget.Image(
                        filename='~/.config/qtile/assets/top-bar-icons/layout.svg',
                        background=base,
                    ),
                    widget.Spacer(
                        length=8,
                        background=base
                    ),
                    widget.CurrentLayout(
                        font="FontAwesome Bold",
                        fontsize=14,
                        background=base,
                    ),
                    widget.Image(
                        filename='~/.config/qtile/assets/top-bar-icons/leftWave.svg',
                        margin_y=-10,
                        margin_x=-10
                    ),
                    widget.Image(
                        filename='~/.config/qtile/assets/top-bar-icons/search.svg',
                        background=darkBase,
                        mouse_callbacks={"Button1": search_dmenu},
                        margin=-2
                    ),
                    widget.TextBox(
                        fmt='Search',
                        background=darkBase,
                        font="FontAwesome Bold",
                        fontsize=14,
                        foreground=text,
                        mouse_callbacks={"Button1": search_dmenu},
                    ),
                    widget.Image(
                        filename='~/.config/qtile/assets/top-bar-icons/rightCircle.svg',
                        background=darkBase,
                        mouse_callbacks={"Button1": search_dmenu},
                        margin_y=-10
                    ),
                    widget.WindowName(
                        font="FontAwesome Bold",
                        fontsize=14,
                        background=base,
                    ),
                    widget.Image(
                        filename='~/.config/qtile/assets/top-bar-icons/toLeftAngle.svg',
                        margin_y=-10,
                        margin_x=-10
                    ),
                    widget.Image(
                        filename='~/.config/qtile/assets/top-bar-icons/leftWave.svg',
                        background=darkBase,
                        mouse_callbacks={"Button1": search_dmenu},
                        margin_y=-10,
                        margin_x=-10
                    ),
                    widget.Clock(
                        format="%I:%M %p %m-%d %a",
                        font="FontAwesome Bold",
                        fontsize=14,
                        background=darkBase,
                    ),
                    widget.Image(
                        filename='~/.config/qtile/assets/top-bar-icons/rightCircle.svg',
                        margin_y=-6,
                    ),
                    widget.Image(
                        filename='~/.config/qtile/assets/top-bar-icons/leftCircle.svg',
                        margin_y=-6,
                    ),
                    widget.BatteryIcon(
                        theme_path='~/.config/qtile/assets/battery-icons/',
                        background=darkBase,
                    ),
                    widget.Battery(
                        font="FontAwesome Bold",
                        fontsize=14,
                        background=darkBase,
                        padding=8,
                    ),
                    widget.Image(
                        filename='~/.config/qtile/assets/top-bar-icons/rightWave.svg',
                        margin_y=-6,
                    ),
                    widget.Systray(
                        icon_size=20,
                        background=base,
                        padding=8
                    ),
                    widget.QuickExit(
                        font="FiraCode Nerd Font",
                        default_text=" ",
                        fontsize=18,
                        background=base,
                        padding=8
                    ),
                ],
                32,
                border_width=[0, 0, 0, 0],
                margin=[19, 16, 6, 16],
            ),
        ),
    ]
