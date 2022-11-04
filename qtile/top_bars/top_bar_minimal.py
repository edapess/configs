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

from libqtile import bar
from libqtile.bar import CALCULATED

from libqtile.widget.clock import Clock
from libqtile.widget.textbox import TextBox
from libqtile.widget.battery import Battery
from libqtile.widget.bluetooth import Bluetooth
from libqtile.widget.cpu import CPU
from libqtile.widget.check_updates import CheckUpdates
from libqtile.widget.keyboardlayout import KeyboardLayout

from extras import widget
#utils imports (etc functions)
from utils import get_window_name

#colors
from colors import based_colors
from colors import colorfull_colors
from colors import light_colors
#import separators for powerline arrows
from topbar_icons import left_system_logos_modified, spacer
#decorations for extra
from decorations.decorations import decoration, base, iconFont, sep
#decorated widgets
from decoratedWidgets.decorated_volume import volume
from decoratedWidgets.decorated_groups import groups
from decoratedWidgets.decorated_current_layout import current_layout
from decoratedWidgets.decorated_pomodoro import pomodoro
from decoratedWidgets.decorated_window_name import window_name
from decoratedWidgets.decorated_wlan import wlan
from decoratedWidgets.decorated_thermal_sensor import thermal_sensor
from decoratedWidgets.decorated_keyboard_layout import keyboard_layout
from decoratedWidgets.decorated_battery import battery
from decoratedWidgets.decorated_cpu import cpu
from decoratedWidgets.decorated_updates import check_updates
from decoratedWidgets.decorated_clock import clock
from decoratedWidgets.decorated_cmus import cmus

def init_widgets_list(primary):
    prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())
    widgets_list = [
        widget.Spacer(
                length=12,
                        background=based_colors['background_dark'] 
                ),
                *left_system_logos_modified(light_colors['green_sheen'], based_colors['white']),
                
                sep(based_colors['background_dark'],based_colors['white'], offset=-10),
                groups(based_colors['background_dark']),

                sep(based_colors['background_dark'],based_colors['white'], offset=-10),
               *current_layout(light_colors['cadet'],based_colors['white']),
               *pomodoro(light_colors['aero_blue'],based_colors['background_dark']),
                
                spacer(),
                window_name(based_colors['background_dark'],based_colors['white']),
                spacer(),
                
                
                *check_updates(based_colors['light_background'],based_colors['white'],light_colors['green_sheen'],based_colors['alert']),               
                *clock(based_colors['purple_background'],based_colors['background_dark']),
                sep(based_colors['background_dark'],based_colors['white'], offset=-10),

                *wlan(colorfull_colors['sky_blue'],based_colors['background_dark']), 
                *volume(colorfull_colors['blue'],based_colors['background_dark']),
                *keyboard_layout(based_colors['orange'],based_colors['white']),
                sep(based_colors['background_dark'],based_colors['white'], offset=-10),

                 # # do not activate ThermalSensor in Virtualbox - will break qtile
                *thermal_sensor(based_colors['light_orange'],based_colors['background_dark'], based_colors['alert']),
                *cpu(based_colors['light_background'],based_colors['white'],based_colors['white']),
                *battery(colorfull_colors['sky_blue'],based_colors['white'],based_colors['alert']),

                widget.Spacer(
                length=12,
                        background=based_colors['background_dark'] 
                ),
                ]
    return widgets_list
