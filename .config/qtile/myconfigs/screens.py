from libqtile.config import Screen
from libqtile import bar

from . import helper
from . import widgets
from . import colors


# SCREENS
def get_screens():
    colors_list = colors.get_colors()
    top_widgets = []
    top_widgets.append(widgets.init_top_bar_widgets_list())
    top_widgets.append(widgets.init_top_bar_widgets_list_sc())

    top_bar = []
    top_bar.append(bar.Bar(widgets=top_widgets[0], size=24, opacity=.8, background=colors_list[2][1]))
    top_bar.append(bar.Bar(widgets=top_widgets[1], size=24, opacity=.8, background=colors_list[2][1]))

    bottom_widgets = []
    bottom_widgets.append(widgets.init_bottom_bar_widgets_list())
    bottom_widgets.append(widgets.init_bottom_bar_widgets_list_sc())

    bottom_bar = []
    bottom_bar.append(bar.Bar(widgets=bottom_widgets[0], size=24, opacity=.8, background=colors_list[2][1]))
    bottom_bar.append(bar.Bar(widgets=bottom_widgets[1], size=24, opacity=.8, background=colors_list[2][1]))

    screens = []

    for monitor_numer in range(helper.get_num_monitors()):
        screens.append(Screen(top=top_bar[monitor_numer], bottom=bottom_bar[monitor_numer]))

    return screens
