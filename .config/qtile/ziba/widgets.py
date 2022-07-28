import copy
from ctypes import alignment
from email.policy import default
import os
import socket
from tkinter.tix import Tree
from turtle import width
from typing import Tuple
from libqtile import widget
from more_itertools import padded

from . import colors
import ziba


colors_list = colors.get_colors()
group_box_theme = {
    "active": colors_list[4],
    "inactive": colors_list[3],
    "highlight_method": "line",
    "margin_y":3,
    "margin_x":0,
    "padding_y":5,
    "padding_x":3,
    "borderwidth":3,
    "rounded": True,
    "foreground": colors_list[2],
    "background": colors_list[0],
    # "this_current_screen_border": colors_list[4],
    # "this_screen_border": colors_list[3],
    # "other_current_screen_border": colors_list[4],
    # "other_screen_border": colors_list[3],
}

def primary_top_widgets():
    """
    Init top bar widgets.
    """
    separator = widget.Sep(
        # padding=0,
        linewidth=2,
        background=ziba.main_theme.color.background,
        foreground=ziba.main_theme.color.background,
    )
    widgets = []

    widgets.append(
        widget.WindowName(
            font="Ubuntu",
            fontsize=11,
            **ziba.widget_them.get_theme(),
        ))

    # temp
    widgets.append(separator)
    widgets.append(
        widget.TextBox(
            text=" 🌡",
            **ziba.widget_them.get_theme(next_bg_color=True),
        ),
    )
    widgets.append(
        widget.ThermalSensor(
            threshold=90,
            # padding=5,
            **ziba.widget_them.get_theme(use_last_color=True),
        ),
    )

    widgets.append(separator)
    # CPU
    widgets.append(
        widget.TextBox(
            text="⏲ : ",
            # padding=0,
            **ziba.widget_them.get_theme(next_bg_color=True),
        ),
    )

    widgets.append(
        widget.CPU(
            frequency=1,
            format='{freq_current} GHz {load_percent:>7.2f}%',
            samples=10,
            **ziba.widget_them.get_theme(use_last_color=True),
        ),
    )

    widgets.append(separator)

    widgets.append(
        widget.TextBox(
            font="Ubuntu",
            text="NET:",
            fontsize=14,
            **ziba.widget_them.get_theme(next_bg_color=True),
        )
    )

    widgets.append(
        widget.NetGraph(
            border_width=1,
            frequency=.1,
            line_width=1,
            type='box',
            **ziba.widget_them.get_theme(use_last_color=True),
        )
    )

    widgets.append(separator)

    widgets.append(
        widget.TextBox(
            font="Ubuntu",
            text="CPU:",
            fontsize=14,
            **ziba.widget_them.get_theme(next_bg_color=True),
        ))
    widgets.append(
        widget.CPUGraph(
            border_width=1,
            frequency=.1,
            line_width=1,
            type='box',
            **ziba.widget_them.get_theme(use_last_color=True),
        )
    )

    widgets.append(separator)
    widgets.append(
        widget.TextBox(
            font="Ubuntu",
            text="HDD:",
            fontsize=14,
            **ziba.widget_them.get_theme(next_bg_color=True),
        )
    )
    widgets.append(
        widget.HDDBusyGraph(
            border_width=1,
            frequency=.1,
            line_width=1,
            type='box',
            **ziba.widget_them.get_theme(use_last_color=True),
        )
    )
    widgets.append(separator)

    widgets.append(
        widget.TextBox(
            font="Ubuntu",
            text="MEM:",
            fontsize=14,
            **ziba.widget_them.get_theme(next_bg_color=True),
        )
    )
    widgets.append(
        widget.MemoryGraph(
            border_width=1,
            frequency=.1,
            line_width=1,
            type='box',
            **ziba.widget_them.get_theme(use_last_color=True),
        )
    )

    widgets.append(separator)
    widgets.append(
        widget.Volume(
            #  volume_app="pactl",
            fmt="Vol: {}",
            **ziba.widget_them.get_theme(next_bg_color=True),
        )
    )

    widgets.append(separator)
    widgets.append(
        widget.Systray(
            **ziba.widget_them.get_theme(next_bg_color=True),
        )
    )

    widgets.append(separator)
    widgets.append(
        widget.Clock(
            format="%A, %B %d - %H:%M",
            **ziba.widget_them.get_theme(next_bg_color=True),
        ))
    return widgets


def primary_bottom_widgets():
    """
    Init bottom bar widgets.
    """
    widgets = []

    prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())
    widgets.append(
        widget.GroupBox(
            **group_box_theme,
        )
    )
    widgets.append(
        widget.TaskList(
            parse_text=lambda x: "",
            highlight_method="block",
            icon_size=ziba.bottom_bar_theme.icon_size,
            border=ziba.bottom_bar_theme.color.foreground,
            rounded=True,
            padding=5,
            txt_floating="🗗",
            txt_maximized="🗖",
            txt_minimized="🗕"
        )
    )
    widgets.append(
        widget.Prompt(
            prompt=prompt,
            font="Ubuntu Mono",
            padding=10,
        )
    )

    widgets.append(widget.Spacer())

    widgets.append(
        widget.KeyboardLayout(
            configured_keyboards=["us", "ir"],
        )
    )

    widgets.append(
        widget.CurrentLayoutIcon(
            scale=.7,
        )
    )
    widgets.append(
        widget.CurrentLayout()
    )
    return widgets


def secondary_top_widgets():
    """
    Init bottom bar widgets.
    """
    widgets = []
    widgets.append(widget.GroupBox(**group_box_theme))
    return widgets


def parse_text(text: str):
    if len(text) > 20:
        return text[:20]
    return text


def secondary_bottom_widgets():
    """
    Init bottom bar widgets.
    """
    widgets = []
    widgets.append(widget.GroupBox(**group_box_theme))
    widgets.append(widget.TaskList(
        parse_text=parse_text,
        highlight_method="block",
        icon_size=ziba.bottom_bar_theme.icon_size,
        border=ziba.bottom_bar_theme.color.foreground,
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
