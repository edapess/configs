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

from libqtile.widget.textbox import TextBox
from libqtile.widget.spacer import Spacer
from libqtile.bar import CALCULATED
from colors import based_colors
from qtile_extras.widget import modify
from decorations.decorations import decoration, base, iconFont
from libqtile.command import lazy

def left_system_logos_modified(bg_color, fg_color) -> list:
    return [ 
        modify(
      TextBox,
      **base(bg_color, fg_color),
      **decoration('left'),
      **iconFont(),
      padding = 10,
      text='',
       ),
        modify(
      TextBox,
      **base(bg_color, fg_color),
      **decoration('right'),
      **iconFont(),
      mouse_callbacks = { 'Button1': lazy.restart() },
      offset = 4,
      padding = 10,
      text='',
       )]

def left_system_logos(bg_color, fg_color):
    return  TextBox(
        font="Hack Nerd Font",
        text=' ',
        fontsize = 23,
        padding = 15,
        background = bg_color,
        foreground=fg_color)
        
def left_arrow(bg_color, fg_color):
    return TextBox(
        text='\uE0B2',
        padding=0,
        fontsize=22,
        background=bg_color,
        foreground=fg_color)


def right_arrow(bg_color, fg_color):
    return TextBox(
        text='\uE0B0',
        padding=0,
        fontsize=22,
        background=bg_color,
        foreground=fg_color)

def right_circle(bg_color, fg_color):
    return TextBox(
        text='\uE0B4',
        padding=0,
        fontsize=32,
        background=bg_color,
        foreground=fg_color)

def left_circle(bg_color, fg_color):
    return TextBox(
        text='\uE0B6',
        padding=0,
        fontsize=22,
        background=bg_color,
        foreground=fg_color)

def spacer():
    return Spacer(
         background=based_colors['background_dark']
    )




    