from libqtile import bar, widget
from libqtile.config import Screen

def get_bar():
    return [
        Screen(
            top=bar.Bar(
                [
                    widget.GroupBox(
                        font="FontAwesome",
                        fontsize=24,
                        borderwidth=3,
                        highlight_method='block',
                        active='#CAA9E0',
                        block_highlight_text_color="#91B1F0",
                        highlight_color='#4B427E',
                        inactive='#282738',
                        foreground='#4B427E',
                        background='#353446',
                        this_current_screen_border='#353446',
                        this_screen_border='#353446',
                        other_current_screen_border='#353446',
                        other_screen_border='#353446',
                        urgent_border='#353446',
                        rounded=True,
                        disable_drag=True,
                    ),
                    widget.CurrentLayout(),
                    widget.WindowName(),
                    widget.Chord(
                        chords_colors={
                            "launch": ("#ff0000", "#ffffff"),
                        },
                        name_transform=lambda name: name.upper(),
                    ),
                    widget.TextBox("default config", name="default"),
                    widget.TextBox("Press <M-r> to spawn", foreground="#d75f5f"),
                    widget.Systray(),
                    widget.Clock(format="%Y-%m-%d %a %I:%M %p"),
                    widget.Battery(),
                    widget.QuickExit(),
                ],
                24,
                # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
                # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
            ),
        ),
    ]
