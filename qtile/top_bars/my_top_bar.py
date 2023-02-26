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
                left_system_logos(based_colors['background_dark'], based_colors['white']),

                GroupBox(
                                font="FontAwesome",
                                fontsize = 15,
                                margin_y = 2,
                                margin_x = 0,
                                padding_y = 10,
                                padding_x = 10,
                                borderwidth = 0,
                                disable_drag = True,
                                active = based_colors['light_orange'],
                                inactive = fractal_red['powder_blue'],
                                rounded = False,
                                highlight_method = "block",
                                this_current_screen_border = based_colors['background_dark'],
                                foreground = based_colors['tokyo_green'],
                                background = based_colors['background_dark'],
                                other_current_screen_border = based_colors['background_dark'],
                                urgent_border=based_colors['alert'],
                                block_highlight_text_color = based_colors["tokyo_green"],
                                other_screen_border = based_colors['background_dark']
                        ),

                icon('', based_colors['background_dark'], based_colors['white'],"FontAwesome"),
                
                CurrentLayout(
                                font = "FontAwesome Bold",
                                background=based_colors['background_dark'],
                                foreground=based_colors['white'],
                        ),
                icon('', based_colors['background_dark'], based_colors['white'],"FontAwesome"),

                Pomodoro(
                                font = "FontAwesome Bold",
                                background=based_colors['background_dark'],
                                color_active = fractal_red['pale_spring_bud'],
                                color_break = fractal_red['pale_spring_bud'],
                                color_inactive = fractal_red['pale_spring_bud'],
                          ),

                icon('', based_colors['background_dark'], based_colors['white']),

                WindowName(
                                font="FontAwesome Bold",
                                fontsize = 12,
                                background=based_colors['background_dark'],
                                foreground=based_colors['white'],
                                format='{state}{name}',
                                parse_text = get_window_name
                        ),

                Cmus(
                                font="FontAwesome Bold",
                                background = based_colors['background_dark'],
                                play_color = fractal_red['light_cyan'],
                        ),
                icon('', based_colors['background_dark'], based_colors['white'],"FontAwesome"),

                Wlan(
                                font="FontAwesome Bold",
                                format='{essid} {percent:2.0%}',
                                background = based_colors['background_dark'],
                                play_color = fractal_red['light_cyan'],
                                interface='wlp61s0'
                        ),

                         # # do not activate in Virtualbox - will break qtile
                icon('', based_colors['background_dark'], based_colors['light_orange'],"FontAwesome"),

                ThermalSensor(
                                font="FontAwesome Bold",
                                background = based_colors['background_dark'],
                                play_color = based_colors['light_orange'],
                                foreground_alert = based_colors['alert'],
                                metric = True,
                                padding = 3,
                                threshold = 80,
                                foreground = based_colors['light_orange']
                        ),
                icon('', based_colors['background_dark'], based_colors['purple_background'],"FontAwesome"),

                KeyboardLayout(
                                font="FontAwesome Bold",
                                configured_keyboards = ['us', 'ru', 'am phonetic-alt'],
                                display_map = {'us':'US','ru':'RU','am phonetic-alt':'am'},
                                fontsize = 12,
                                background=based_colors['background_dark'],
                                foreground=based_colors['purple_background'],
                ),

                icon('', based_colors['background_dark'], colorfull_colors['cornflower_blue'],"FontAwesome"),

                Battery(
                                font="FontAwesome Bold",
                                update_interval = 10,
                                fontsize = 12,
                                background=based_colors['background_dark'],
                                foreground=colorfull_colors['cornflower_blue'],
                                low_foreground = based_colors['alert'],
	                ),

                icon('', based_colors['background_dark'], light_colors['green_sheen'],"FontAwesome"),

                CPU(
                                font="FontAwesome Bold",
                                fill_color = based_colors['white'],
                                background=based_colors['background_dark'],
                                foreground=light_colors['green_sheen'],
                                mouse_callbacks={'Button1': lazy.spawn("alacritty -e btop")},

                        ),

                icon('', based_colors['background_dark'], based_colors['tokyo_green'],"FontAwesome"),

                CheckUpdates(
                                font="FontAwesome Bold",
                                distro='Arch_Sup',
                                colour_have_updates=based_colors['alert'],
                                colour_no_updates = based_colors['tokyo_green'],
                                background=based_colors['background_dark'],
                                execute = 'alacritty -e yay',
                                display_format = 'upd {updates}',
                                initial_text = 'check...',
                                no_update_string = 'yay'
                ),

                icon('', based_colors['background_dark'], based_colors['white'],"FontAwesome"),
                
                Clock(   
                                font="FontAwesome Bold",
                                background=based_colors['background_dark'],
                                foreground=based_colors['white'],
                                fontsize = 12,
                                format="%Y-%m-%d %H:%M"
                        ),

                ]
 
    return widgets_list
