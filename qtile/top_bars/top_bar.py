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
#import separators for powerline arrows
from topbar_icons import left_arrow, right_arrow, left_system_logos

def init_widgets_list(primary):
    prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())
    widgets_list = [
                left_system_logos(light_colors['green_sheen'], based_colors['white']),

                GroupBox(font="FiraCode Nerd Font",
                                fontsize = 15,
                                margin_y = 2,
                                margin_x = 0,
                                padding_y = 10,
                                padding_x = 10,
                                borderwidth = 0,
                                disable_drag = True,
                                active = based_colors['background_dark'],
                                inactive = based_colors['background_dark'],
                                rounded = True,
                                highlight_method = "block",
                                this_current_screen_border = based_colors['orange'],
                                foreground = colorfull_colors['purple'],
                                background = colorfull_colors['purple'],
                                other_current_screen_border = based_colors['light_orange'],
                                urgent_border=based_colors['alert']
                        ),
               
                right_arrow(light_colors['cadet'],colorfull_colors['purple']),
               
                CurrentLayout(
                                font = "Noto Sans Bold",
                                background=light_colors['cadet'],
                                foreground=based_colors['white']
                        ),
                right_arrow(light_colors['aero_blue'],light_colors['cadet']),

                Pomodoro(
                                font = "Noto Sans Bold",
                                background=light_colors['aero_blue'],
                                color_active = based_colors['background_dark'],
                                color_break = based_colors['background_dark'],
                                color_inactive = based_colors['background_dark'],
                          ),

                right_arrow(based_colors['risin_black'],light_colors['aero_blue']),

                WindowName(
                                font="Noto Sans Bold",
                                fontsize = 12,
                                background=based_colors['background_dark'],
                                foreground=based_colors['white'],
                                format='{state}{name}',
                                parse_text = get_window_name
                        ),
                left_arrow(based_colors['background_dark'],light_colors['cadet']),

                Cmus(
                                font="Noto Sans Bold",
                                background = light_colors['cadet'],
                                play_color = light_colors['baby_powder'],
                        ),

                left_arrow(light_colors['cadet'],colorfull_colors['blue']),

                Wlan(
                                font="Noto Sans Bold",
                                format='{essid} {percent:2.0%}',
                                foreground=based_colors['background_dark'],
                                background=colorfull_colors['blue'],
                                interface='wlp61s0'
                        ),

                left_arrow(colorfull_colors['blue'],based_colors['light_orange']),

                         # # do not activate in Virtualbox - will break qtile
                ThermalSensor(
                                font="Noto Sans Bold",
                                foreground = based_colors['background_dark'],
                                foreground_alert = based_colors['alert'],
                                background = based_colors['light_orange'],
                                metric = True,
                                padding = 3,
                                threshold = 80
                        ),

                left_arrow(based_colors['light_orange'],based_colors['orange']),

                KeyboardLayout(
                                font="Noto Sans Bold",
                                configured_keyboards = ['us', 'ru', 'am phonetic-alt'],
                                display_map = {'us':'US','ru':'RU','am phonetic-alt':'am'},
                                fontsize = 12,
                                background = based_colors['orange'],
                ),

                left_arrow(based_colors['orange'],based_colors['background_dark']),
                 Volume(
                        font="Noto Sans Bold",
                        foreground = based_colors['white'],
                        background = based_colors['background_dark'],
                        fmt='Vol: {}'
                ),
                left_arrow(based_colors['background_dark'],colorfull_colors['sky_blue']),

                Battery(
                                font="Noto Sans Bold",
                                update_interval = 10,
                                fontsize = 12,
                                foreground = based_colors['background_dark'],
                                background = colorfull_colors['sky_blue'],
                                low_foreground = based_colors['alert'],
	                ),

                left_arrow(colorfull_colors['sky_blue'],based_colors['light_background']),
              
                CPU(
                                font="Noto Sans Bold",
                                fill_color = based_colors['white'],
                                background=based_colors['light_background'],
                                mouse_callbacks={'Button1': lazy.spawn("alacritty -e btop")},

                        ),
                left_arrow(based_colors['light_background'],based_colors['risin_black']),
                
                CheckUpdates(
                                font="Noto Sans Bold",
                                distro='Arch_Sup',
                                colour_have_updates=based_colors['alert'],
                                colour_no_updates = light_colors['green_sheen'],
                                background = based_colors['risin_black'],
                                execute = 'pamac-manager',
                                display_format = 'upd {updates}',
                                initial_text = 'check...',
                                no_update_string = 'yay'
                ),

                left_arrow(based_colors['risin_black'],based_colors['purple_background']),
                
                Clock(   
                                font="Noto Sans Bold",
                                foreground = based_colors['background_dark'],
                                background = based_colors['purple_background'],
                                fontsize = 12,
                                format="%Y-%m-%d %H:%M"
                        ),

                ]
#     if primary:
#         widgets_list.insert(
#                 -1,
#             Systray(
#                 foreground=based_colors['light_orange'],
#                 background=based_colors['purple_background'],
#                 padding=15,
#             ),
#         )
    return widgets_list
