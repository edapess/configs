#####################################################################################
####..........####################............########################################
####..######..####################  ########..#########...############...##############
####..........####################  ########..########...############...################
####..############################...........########...############...##################
####..........##..####........####  ################...############...####################
################..############..##  ##..........###............###............ ############
################..############..##  ##..######..###########...#############...##############
########..........###...........######..........##########...#############...################
########..######..###..#######..######..#################...#############...##################
########..######..###..#######..######..........########...#############...####################
########..........###...........################################################################
#################################################################################################

import os
import socket
from libqtile.command import lazy

from libqtile import bar
from libqtile.widget.groupbox import GroupBox
from libqtile.widget.sep import Sep
from libqtile.widget.currentlayout import CurrentLayout
from libqtile.widget.windowname import WindowName
from libqtile.widget.textbox import TextBox
from libqtile.widget.clock import Clock
from libqtile.widget.systray import Systray
from libqtile.widget.net import Net
from libqtile.widget.textbox import TextBox
from libqtile.widget.battery import Battery
from libqtile.widget.keyboardkbdd import KeyboardKbdd
from libqtile.widget.bluetooth import Bluetooth
from libqtile.widget.cpu import CPU
from libqtile.widget.volume import Volume
from libqtile.widget.wlan import Wlan
from libqtile.widget.cmus import Cmus
from libqtile.widget.pomodoro import Pomodoro
from libqtile.widget.check_updates import CheckUpdates
from libqtile.widget.keyboardlayout import KeyboardLayout
#utils imports (etc functions)
from utils import get_window_name

#sensors
from libqtile.widget.sensors import ThermalSensor


from libqtile import widget
from more_itertools import padded 
from colors import based_colors
from colors import colorfull_colors
from colors import light_colors
from colors import fractal_red
#import separators for powerline arrows
from topbar_icons import left_arrow, right_arrow, left_system_logos, icon

def init_widgets_list(primary):
    prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())
    widgets_list = [
                left_system_logos(fractal_red['dark_byzantium'], based_colors['white']),

                GroupBox(
                                font="FiraCode Nerd Font",
                                fontsize = 15,
                                margin_y = 2,
                                margin_x = 0,
                                padding_y = 10,
                                padding_x = 10,
                                borderwidth = 0,
                                disable_drag = True,
                                active = fractal_red['light_cyan'],
                                inactive = fractal_red['powder_blue'],
                                rounded = False,
                                highlight_method = "block",
                                this_current_screen_border = based_colors['orange'],
                                foreground = fractal_red['light_cyan'],
                                background = fractal_red['eggplant'],
                                other_current_screen_border = based_colors['light_orange'],
                                urgent_border=fractal_red['indian_red'],
                                block_highlight_text_color = based_colors["white"],
                                other_screen_border = fractal_red["dark_electric_blue"]
                        ),

                icon('', fractal_red['dark_byzantium'], based_colors['white']),
                
                CurrentLayout(
                                font = "FiraCode Nerd Font Bold",
                                background=fractal_red['dark_byzantium'],
                                foreground=based_colors['white'],
                        ),
                Sep(
                                background=fractal_red['dark_byzantium'],
                                foreground=based_colors['white'],
                ),
                icon('', fractal_red['eggplant'], based_colors['white']),

                Pomodoro(
                                font = "FiraCode Nerd Font Bold",
                                background=fractal_red['eggplant'],
                                color_active = fractal_red['pale_spring_bud'],
                                color_break = fractal_red['pale_spring_bud'],
                                color_inactive = fractal_red['pale_spring_bud'],
                          ),

                Sep(
                                background=fractal_red['dark_byzantium'],
                                foreground=based_colors['white'],
                ),
                icon('', fractal_red['dark_byzantium'], based_colors['white']),

                WindowName(
                                font="FiraCode Nerd Font Bold",
                                fontsize = 12,
                                background=fractal_red['dark_byzantium'],
                                foreground=based_colors['white'],
                                format='{state}{name}',
                                parse_text = get_window_name
                        ),

                Cmus(
                                font="FiraCode Nerd Font Bold",
                                background = fractal_red['dark_byzantium'],
                                play_color = fractal_red['light_cyan'],
                        ),
                Sep(
                                background=fractal_red['dark_byzantium'],
                                foreground=based_colors['white'],
                ),
                icon('', fractal_red['eggplant'], based_colors['white']),

                Wlan(
                                font="FiraCode Nerd Font Bold",
                                format='{essid} {percent:2.0%}',
                                background = fractal_red['eggplant'],
                                play_color = fractal_red['light_cyan'],
                                interface='wlp61s0'
                        ),

                Sep(
                                background=fractal_red['dark_byzantium'],
                                foreground=based_colors['white'],
                ),
                         # # do not activate in Virtualbox - will break qtile
                icon('󱤋', fractal_red['dark_byzantium'], based_colors['white']),

                ThermalSensor(
                                font="FiraCode Nerd Font Bold",
                                background = fractal_red['dark_byzantium'],
                                play_color = fractal_red['light_cyan'],
                                foreground_alert = based_colors['alert'],
                                metric = True,
                                padding = 3,
                                threshold = 80
                        ),
                Sep(
                                background=fractal_red['dark_byzantium'],
                                foreground=based_colors['white'],
                ),
                icon('', fractal_red['eggplant'], based_colors['white']),

                KeyboardLayout(
                                font="FiraCode Nerd Font Bold",
                                configured_keyboards = ['us', 'ru', 'am phonetic-alt'],
                                display_map = {'us':'US','ru':'RU','am phonetic-alt':'am'},
                                fontsize = 12,
                                background=fractal_red['eggplant'],
                                foreground=based_colors['white'],
                ),

                Sep(
                                background=fractal_red['dark_byzantium'],
                                foreground=based_colors['white'],
                ),
                icon('󰁼', fractal_red['dark_byzantium'], based_colors['white']),

                Battery(
                                font="FiraCode Nerd Font Bold",
                                update_interval = 10,
                                fontsize = 12,
                                background=fractal_red['dark_byzantium'],
                                foreground=based_colors['white'],
                                low_foreground = based_colors['alert'],
	                ),

                Sep(
                                background=fractal_red['dark_byzantium'],
                                foreground=based_colors['white'],
                ),
                icon('󰻠', fractal_red['eggplant'], based_colors['white']),

                CPU(
                                font="FiraCode Nerd Font Bold",
                                fill_color = based_colors['white'],
                                background=fractal_red['eggplant'],
                                foreground=based_colors['white'],
                                mouse_callbacks={'Button1': lazy.spawn("alacritty -e btop")},

                        ),
                Sep(
                                background=fractal_red['dark_byzantium'],
                                foreground=based_colors['white'],
                ),
                icon('󱑤', fractal_red['dark_byzantium'], based_colors['white']),

                CheckUpdates(
                                font="FiraCode Nerd Font Bold",
                                distro='Arch_Sup',
                                colour_have_updates=based_colors['alert'],
                                colour_no_updates = light_colors['green_sheen'],
                                background=fractal_red['dark_byzantium'],
                                execute = 'alacritty -e yay',
                                display_format = 'upd {updates}',
                                initial_text = 'check...',
                                no_update_string = 'yay'
                ),
                Sep(
                                background=fractal_red['dark_byzantium'],
                                foreground=based_colors['white'],
                ),
                icon('', fractal_red['eggplant'], based_colors['white']),
                
                Clock(   
                                font="FiraCode Nerd Font Bold",
                                background=fractal_red['eggplant'],
                                foreground=based_colors['white'],
                                fontsize = 12,
                                format="%Y-%m-%d %H:%M"
                        ),

                ]
 
    return widgets_list
