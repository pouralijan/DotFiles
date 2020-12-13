import os
import socket
from libqtile import widget

from . import colors


# WIDGETS
def init_top_bar_widgets_list_sc():
    """
    Init top bar widgets.
    """
    colors_list = colors.get_colors()

    widgets = []
    widgets.append(widget.WindowName(font="Ubuntu", fontsize=11))
    #widgets.append(widget.CPUGraph(graph_color=colors_list[6][1], border_width=1, frequency=.1, line_width=1, type='box'))
    return widgets

def init_top_bar_widgets_list():
    colors_list = colors.get_colors()
    """
    Init top bar widgets.
    """
    widgets = []
    widgets.append(widget.WindowName(font="Ubuntu", fontsize=11,))
    #widgets.append(widget.Notify(font="Ubuntu", fontsize=11,))
    #widgets.append(widget.PulseVolume())
    #widgets.append(widget.Volume())
    #widgets.append(widget.ThermalSensor())

    #widgets.append(widget.TextBox(font="Ubuntu", text="NET:", padding=5, fontsize=14))
    #widgets.append(widget.NetGraph(graph_color=colors_list[6][1], border_width=1, frequency=.1, line_width=1, type='box'))
    #widgets.append(widget.NetGraph(interface="enp0s20f0u7"))
    #widgets.append(widget.NetGraph(interface="enp0s31f6"))
    #widgets.append(widget.NetGraph(interface="enp0s20f0u4"))
    #widgets.append(widget.TextBox(font="Ubuntu", text="CPU:", padding=5, fontsize=14))
    #widgets.append(widget.CPUGraph(graph_color=colors_list[6][1], border_width=1, frequency=.1, line_width=1, type='box'))
    #widgets.append(widget.TextBox(font="Ubuntu", text="HDD:", padding=5, fontsize=14))
    #widgets.append(widget.HDDBusyGraph(graph_color=colors_list[6][1], border_width=1, frequency=.1, line_width=1, type='box'))
    #widgets.append(widget.HDDGraph(path='/home', graph_color=colors_list[6][1], border_width=1, frequency=.1, line_width=1, type='box'))
    #widgets.append(widget.TextBox(font="Ubuntu", text="MEM:", padding=5, fontsize=14))
    #widgets.append(widget.MemoryGraph(graph_color=colors_list[6][1], border_width=1, frequency=.1, line_width=1, type='box'))
    widgets.append(widget.Systray(padding=5))
    widgets.append(widget.TextBox(font="Ubuntu Bold", text=" ⟳", padding=5, fontsize=14))
    widgets.append(widget.Pacman(execute="urxvtc", update_interval=1800,))
    widgets.append(widget.TextBox(text="Updates", padding=5,))
    widgets.append(widget.TextBox(font="Ubuntu Bold", text=" 🕒", padding=5, fontsize=14))
    widgets.append(widget.Clock(format="%A, %B %d - %H:%M"))
    return widgets

def init_bottom_bar_widgets_list_sc():
    """
    Init bottom bar widgets.
    """
    colors_list = colors.get_colors()
    widgets = []
    widgets.append(widget.GroupBox(padding=3, active=colors_list[7][1], inactive=colors_list[6][1]))
    widgets.append(widget.Chord())
    widgets.append(widget.Spacer())
    widgets.append(widget.CurrentLayoutIcon(scale=.7))
    widgets.append(widget.CurrentLayout())
    return widgets

def init_bottom_bar_widgets_list():
    """
    Init bottom bar widgets.
    """
    colors_list = colors.get_colors()
    widgets = []

    prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())
    widgets.append(widget.GroupBox(padding=3, active=colors_list[7][1], inactive=colors_list[6][1]))
    widgets.append(widget.TaskList())
    #widgets.append(widget.WindowTabs())
    widgets.append(widget.Prompt(prompt=prompt, font="Ubuntu Mono", padding=10,))
    widgets.append(widget.Spacer())
    widgets.append(widget.CapsNumLockIndicator())
    widgets.append(widget.KeyboardLayout(configured_keyboards=["us", "ir"]))
    widgets.append(widget.CurrentLayoutIcon(scale=.7))
    widgets.append(widget.CurrentLayout(fmt="{:<8}"))
    widgets.append(widget.TextBox( font="Ubuntu Bold", text=" ♫", padding=5, fontsize=14))
    widgets.append(widget.Cmus( max_chars=40, update_interval=0.5,))
    return widgets
