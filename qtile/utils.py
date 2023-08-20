from libqtile import qtile

def search_dmenu():
    qtile.cmd_spawn("dmenu_run")