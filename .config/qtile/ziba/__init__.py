import os
import subprocess
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
    def __init__(self, size, opacity, color: colors.Color, font="") -> None:
        self._size = size
        self._opacity = opacity
        self._color = color
    
        self._last_color = self._color.next_color()

    @property
    def size(self):
        return self._size
    
    @property
    def opacity(self):
        return self._opacity
    
    @property
    def icon_size(self):
        return self._size - 8

    @property
    def color(self):
        return self._color

    def get_theme(self):
        raise NotImplemented

class MainTheme(Theme):
    def get_theme(self):
        return {
            "background": self._color.background,
            "foreground": self._color.foreground,
        }

class BarTheme(Theme):
    def get_theme(self):
        return {
            "size": self._size,
            "background": self._color.background,
            "foreground": self._color.foreground,
            "opacity": self._opacity,
            "padding": 10,
            "margin": 4,
        }
class WidgetTheme(Theme):
    def get_theme(self, next_bg_color=False, use_last_color=False):
        self._last_color = self._color.next_color() if next_bg_color else self._last_color

        return {
            "size": self._size,
            "background": self._last_color if use_last_color or next_bg_color else self._color.background,
            # "foreground": self._color.foreground,
            "foreground": self._color.background if use_last_color or next_bg_color else self._color.foreground,
            "opacity": self._opacity,
            "padding": 10,
            "margin": 4,
        }
    
cc = colors.get_colors()
c = colors.Color(cc[0], cc[2], cc[3:])
main_theme = MainTheme(24, 1, c)
top_bar_theme = BarTheme(24, .9, c)
bottom_bar_theme = BarTheme(30, .8, c)
widget_them = WidgetTheme(30, .8, c)

# wmname = "qtile"


from . import bind_keys
from . import groups
from . import layouts
from . import widgets
from . import screens