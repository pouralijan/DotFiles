import os
import subprocess
from turtle import color
from libqtile import hook
from libqtile.utils import guess_terminal
import pathlib

wallpaper_path = pathlib.Path("/mnt/MultimediaAndGames/pic/Wallpapers/")

from . import colors

# STARTUP APPLICATIONS
@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/ziba/autostart.sh'])

# mod = "mod4"
# terminal = guess_terminal()

class Theme:
    def __init__(self, size, opacity, background, foreground, font="") -> None:
        self._size = size
        self._opacity = opacity
        self._background = background
        self._foreground = foreground
    
    @property
    def size(self):
        return self._size
    
    @property
    def opacity(self):
        return self._opacity
    
    @property
    def background(self):
        return self._background

    @property
    def icon_size(self):
        return self._size - 8

    @property
    def foreground(self):
        return self._foreground
    
    def get_theme(self):
        raise NotImplemented

class BarTheme(Theme):
    def get_theme(self):
        return {
            "size": self._size,
            "background": self._background,
            "opacity": self._opacity,
        }

top_bar_theme = BarTheme(24, .9, colors.get_colors()[2][1], colors.get_colors()[4][1])
bottom_bar_theme = BarTheme(30, .8, colors.get_colors()[2][1], colors.get_colors()[4][1])

# wmname = "qtile"


from . import bind_keys
from . import groups
from . import layouts
from . import widgets
from . import screens