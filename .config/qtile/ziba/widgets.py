from ctypes import alignment
from email.policy import default
import os
import socket
from turtle import width
from libqtile import widget

from . import colors
import ziba

_colors = [["#2e3440", "#2e3440"],  # background
           ["#242831", "#242831"],  # background alt
           ["#ffffff", "#ffffff"],  # white
           ["#ff5555", "#ff5555"],  # white alt
           ["#797FD4", "#797FD4"],  # violet
           ["#89aaff", "#89aaff"],  # blue
           ["#89ddff", "#89ddff"],  # ice
           ["#E05F27", "#E05F27"],  # orange
           ["#c3e88d", "#c3e88d"],  # green
           ["#ffcb6b", "#ffcb6b"],  # orange
           ["#f07178", "#f07178"]]  # red

colors_list = colors.get_colors()
group_box_theme = {
    "padding": 5,
    "active": colors_list[4][1],
    "inactive": colors_list[3][1],
    # "block_highlight_text_color":colors_list[3][1],
    "highlight_method": 'block',
}


def primary_top_widgets():
    colors_list = colors.get_colors()
    """
    Init top bar widgets.
    """
    widgets = []
    widgets.append(widget.WindowName(font="Ubuntu", fontsize=11,))
    # temp
    widgets.append(
        widget.TextBox(
            text=" 🌡",
            padding=2,
            foreground=_colors[2],
            background=_colors[0],
        ),
    )
    widgets.append(
        widget.ThermalSensor(
            foreground=_colors[10],
            background=_colors[0],
            threshold=90,
            padding=5
        ),
    )

    # CPU
    widgets.append(
        widget.TextBox(
            text="⏲ : ",
            foreground=_colors[6],
            background=_colors[0],
            padding=0,
        ),
    )

    widgets.append(
        widget.CPU(
            frequency=1,
            format='{freq_current} GHz {load_percent:>7.2f}%',
            samples=10,
            foreground=_colors[6],
            background=_colors[0],
            padding=10,
        ),
    )

    widgets.append(widget.TextBox(
        font="Ubuntu", text="NET:", padding=5, fontsize=14))

    widgets.append(
        widget.Net(
            margin=100,
            format="↓ {down:>7} ↑ {up:>7}"
        ))
    widgets.append(widget.NetGraph(
        graph_color=colors_list[6][1],
        border_width=1,
        frequency=.1,
        line_width=1,
        type='box',
    ))
    widgets.append(widget.TextBox(
        font="Ubuntu",
        text="CPU:",
        padding=5,
        fontsize=14,
    ))
    widgets.append(widget.CPUGraph(
        graph_color=colors_list[6][1], border_width=1, frequency=.1, line_width=1, type='box'))
    widgets.append(widget.TextBox(
        font="Ubuntu", text="HDD:", padding=5, fontsize=14))
    widgets.append(widget.HDDBusyGraph(
        graph_color=colors_list[6][1], border_width=1, frequency=.1, line_width=1, type='box'))
    widgets.append(widget.TextBox(
        font="Ubuntu", text="MEM:", padding=5, fontsize=14))
    widgets.append(widget.MemoryGraph(
        graph_color=colors_list[6][1], border_width=1, frequency=.1, line_width=1, type='box'))

    widgets.append(widget.Volume(padding=5,
                                 #  volume_app="pactl",
                                 fmt="Vol: {}",
                                 ))
    widgets.append(widget.Systray(padding=5))

    widgets.append(widget.Clock(
        background=colors_list[4][1],
        foreground=colors_list[1][1],
        format="%A, %B %d - %H:%M",
    ))
    return widgets


def primary_bottom_widgets():
    """
    Init bottom bar widgets.
    """
    colors_list = colors.get_colors()
    widgets = []

    prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())
    widgets.append(widget.GroupBox(**group_box_theme))
    widgets.append(widget.TaskList(
        parse_text=lambda x: "",
        highlight_method="block",
        icon_size=ziba.bottom_bar_theme.icon_size,
        border=ziba.bottom_bar_theme.foreground,
        rounded=True,
        padding=5,
        txt_floating="🗗",
        txt_maximized="🗖",
        txt_minimized="🗕"
    ))
    widgets.append(widget.Prompt(
        prompt=prompt, font="Ubuntu Mono", padding=10,))

    widgets.append(widget.Spacer())

    widgets.append(widget.KeyboardLayout(configured_keyboards=["us", "ir"]))

    widgets.append(widget.CurrentLayoutIcon(scale=.7))
    widgets.append(widget.CurrentLayout())
    return widgets


def secondary_top_widgets():
    """
    Init bottom bar widgets.
    """
    widgets = []
    widgets.append(widget.GroupBox(**group_box_theme))
    return widgets


# def parse_text(text:str):
    # return text.split("")[-1]
def secondary_bottom_widgets():
    """
    Init bottom bar widgets.
    """
    widgets = []
    widgets.append(widget.GroupBox(**group_box_theme))
    widgets.append(widget.TaskList(
        # parse_text=parse_text,
        highlight_method="block",
        icon_size=ziba.bottom_bar_theme.icon_size,
        border=ziba.bottom_bar_theme.foreground,
        borderwidth=5,
        rounded=True,
        padding=5,
        txt_floating="🗗",
        txt_maximized="🗖",
        txt_minimized="🗕",
        spacing=2,
        
    ))
    widgets.append(widget.Spacer())
    widgets.append(widget.CurrentLayoutIcon(scale=.7))
    widgets.append(widget.CurrentLayout())

    return widgets
