import dataclasses
from typing import List

@dataclasses.dataclass
class Color:
    background : List[str] = dataclasses.field()
    foreground : List[str] = dataclasses.field()
    colors : List[List[str]] = dataclasses.field()

    def __init__(self, background, foreground, colors) -> None:
        self.background = background
        self.foreground = foreground
        self.colors = colors
        
        self._next_color = self._color_generator()

    
    def next_color(self):
        return next(self._next_color)

    def _color_generator(self):
        while True:
            for color in self.colors:
                yield color

def get_colors():
    colors0 = [
                ["#292D3E", "#292D3E"],
                ["#434758", "#434758"],
                ["#D0D0D0", "#D0D0D0"],
                ["#F07178", "#F07178"],
                ["#000000", "#000000"],
                ["#AD69AF", "#AD69AF"],
                ["#C3E88D", "#C3E88D"],
                ["#C792EA", "#C792EA"],
                ["#9CC4FF", "#9CC4FF"],
                ["#000000", "#000000"],
                ["#434758", "#434758"],
            ]

    colors1 = [
                ["#1d1f21", "#1d1f21"],
                ["#c5c8c6", "#969896"],
                ["#cc342b", "#cc342b"],
                ["#198844", "#198844"],
                ["#fba922", "#fba922"],
                ["#3971ed", "#3971ed"],
                ["#a36ac7", "#a36ac7"],
                ["#3971ed", "#3971ed"],
                ["#c5c8c6", "#ffffff"],
            ]

    # *.cursorColor:  #1abc9c
    colors2 = [
                ["#1abc9c", "#2c2c2c"],
                ["#3f3f3f", "#709080"],
                ["#705050", "#dca3a3"],
                ["#60b48a", "#72d5a3"],
                ["#dfaf8f", "#f0dfaf"],
                ["#3498db", "#7eb2e6"],
                ["#5b2c70", "#9b59b6"],
                ["#8cd0d3", "#93e0e3"],
                ["#dcdccc", "#ffffff"],
            ]

    colors3 = [
            # special
            ['#cfd6e4', '#cfd6e4'],
            ['#cfd6e4', '#232731'],

            # black
            ['#2d3241', '#3b4358'],

            # red
            ['#b14a56', '#b14a56'],

            # green
            ['#92b477', '#92b477'],

            # yellow
            ['#e6c274', '#e6c274'],

            # blue
            ['#6d8eb5', '#6d8eb5'],

            # magenta
            ['#a5789e', '#a5789e'],

            # cyan
            ['#75b3c7', '#7cafad'],

            # white
            ['#dfe3ed', '#e7ebf1'],
        ]
    
    colors4 = [
        ["#2e3440", "#2e3440"],  # background
        ["#242831", "#242831"],  # background alt
        ["#ffffff", "#ffffff"],  # white foreground
        ["#ff5555", "#ff5555"],  # white alt foreground
        ["#797FD4", "#797FD4"],  # violet
        ["#89aaff", "#89aaff"],  # blue
        ["#89ddff", "#89ddff"],  # ice
        ["#E05F27", "#E05F27"],  # orange
        ["#c3e88d", "#c3e88d"],  # green
        ["#ffcb6b", "#ffcb6b"],  # orange
        ["#f07178", "#f07178"],  # red
    ]  


    # colors = colors0
    colors = colors1
    colors = colors2
    colors = colors3
    colors = colors4
    return colors