#%%
import pathlib
import random

#%%
from libqtile.config import Screen
from libqtile import bar
from more_itertools import raise_

#%%
# from . import utils
from . import widgets
from . import colors
import ziba
from ziba import wallpaper_path

#%%
def select_wallpaper(wallpaper_path):
    # check path exists.
    if isinstance(wallpaper_path, str):
        wallpaper_path = pathlib.Path(wallpaper_path)
    elif not isinstance(wallpaper_path, pathlib.Path):
        raise ValueError()
    wallpaper =  list(wallpaper_path.iterdir())
    wallpaper = random.choice(wallpaper)
    wallpaper = wallpaper_path / wallpaper
    if not wallpaper.is_file():
        return select_wallpaper()
    return wallpaper

#%%
# SCREENS
def get_screens():
    top_widgets = []
    top_widgets.append(widgets.primary_top_widgets())
    # top_widgets.append(widgets.init_top_bar_widgets_list_sc())

    top_bar = []
    top_bar.append(bar.Bar(widgets=top_widgets[0], **ziba.top_bar_theme.get_theme()))
    # top_bar.append(bar.Bar(widgets=top_widgets[1], size=24, opacity=.8, background=colors_list[2][1]))

    bottom_widgets = []
    bottom_widgets.append(widgets.primary_bottom_widgets())
    bottom_widgets.append(widgets.secondary_bottom_widgets())
    bottom_widgets.append(widgets.secondary_bottom_widgets())
    bottom_widgets.append(widgets.secondary_bottom_widgets())

    bottom_bar = []
    bottom_bar.append(bar.Bar(widgets=bottom_widgets[0], **ziba.bottom_bar_theme.get_theme())) 
    bottom_bar.append(bar.Bar(widgets=bottom_widgets[1], **ziba.bottom_bar_theme.get_theme())) 
    bottom_bar.append(bar.Bar(widgets=bottom_widgets[2], **ziba.bottom_bar_theme.get_theme())) 
    bottom_bar.append(bar.Bar(widgets=bottom_widgets[3], **ziba.bottom_bar_theme.get_theme())) 

    screens = []

    # for monitor_numer in range(utils.get_num_monitors()):
    for monitor_number in range(4):
        if monitor_number == 0:
            screens.append(
                Screen(
                    wallpaper=str(select_wallpaper(wallpaper_path)),
                    top=top_bar[monitor_number],
                    bottom=bottom_bar[monitor_number], 
                    )
                )
        else:
            screens.append(
                Screen(
                    wallpaper=str(select_wallpaper(wallpaper_path)),
                    bottom=bottom_bar[monitor_number]
                )
            )

    return screens