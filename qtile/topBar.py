from libqtile import bar, widget
from libqtile.config import Screen
from colors import accent, base, secondary, secondary2, text, alert
def get_bar():
    return [
        Screen(
            top=bar.Bar(
                [
                widget.Image(
                    filename='~/.config/qtile/assets/1.png',
                ),
                    widget.GroupBox(
                        font="CaskaydiaCove Nerd Font",
                        fontsize=18,
                        margin_y = 2,
                        margin_x = 0,
                        padding_y = 10,
                        padding_x = 10,
                        border=0,
                        # borderwidth = 6,
                        highlight_method='block',
                        active=text,
                        block_highlight_text_color=text,
                        highlight_color='#4B427E',
                        inactive=secondary2,
                        foreground='#4B427E',
                        background=accent,
                        this_current_screen_border='#353446',
                        this_screen_border='#353446',
                        other_current_screen_border='#353446',
                        other_screen_border='#353446',
                        urgent_border=alert,
                        rounded=False,
                        disable_drag=True,
                    ),
                    widget.CurrentLayout(
                        font="FiraCode Nerd Font Mono Med",
                        background=base,
                        
                    ),
                    widget.WindowName(

                        background=accent,

                    ),
                    widget.Chord(
                        chords_colors={
                            "launch": ("#ff0000", "#ffffff"),
                        },
                        name_transform=lambda name: name.upper(),
                    ),
                    widget.Systray(),
                    widget.Clock(format="%Y-%m-%d %a %I:%M %p"),
                    widget.Battery(),
                    widget.QuickExit(),
                ],
                32,
                border_color = '#282738',
                border_width = [0,0,0,0],
                margin = [12,32,6,32],
            ),
        ),
    ]
