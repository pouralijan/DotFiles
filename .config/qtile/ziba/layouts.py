from libqtile import layout, hook
from libqtile.config import Match

from . import colors
##### LAYOUTS #####


def get_layout_theme():
    colors_list = colors.get_colors()

    return {"border_width": 3,
            "margin": 5,
            "border_focus": colors_list[8][1],
            "border_normal": colors_list[3][1]
            }

##### FLOATING WINDOWS #####


@hook.subscribe.client_new
def floating(window):
    floating_types = ['notification', 'toolbar', 'splash', 'dialog']
    transient = window.window.get_wm_transient_for()
    if window.window.get_wm_type() in floating_types or transient:
        window.floating = True


def get_floating_layout():
    return layout.Floating(
        border_focus="#3B4022",
        float_rules=[
            # Run the utility of `xprop` to see the wm class and name of an X client.
            *layout.Floating.default_float_rules,
            Match(title="branchdialog"),
            Match(title="pinentry"),
            Match(wm_class="Volumeicon"),
            Match(wm_class="confirm"),
            Match(wm_class="confirmreset"),
            Match(wm_class="dialog"),
            Match(wm_class="download"),
            Match(wm_class="error"),
            Match(wm_class="file_progress"),
            Match(wm_class="makebranch"),
            Match(wm_class="maketag"),
            Match(wm_class="notification"),
            Match(wm_class="pavucontrol"),
            # Match(wm_class="rocket.chat"),
            Match(wm_class="splash"),
            Match(wm_class="ssh-askpass"),
            Match(wm_class="toolbar"),
            Match(wm_class='Pavucontrol'),
            Match(wm_class='ulauncher'),
            Match(wm_class='Places|firefox'),
            Match(wm_class='Places'),
            # Match(wname='Android Emulator - Mi9TProEmu:5554'),
            # Match(wname='Android Emulator.*'),
            # Match(wname='branchdialog'),  # gitk
            # Match(wname='pinentry'),  # GPG key password entry
        ]
    )


def get_layouts():
    layout_theme = get_layout_theme()

    layouts = []
    layouts.append(layout.Bsp(**layout_theme, name='bsp'))
    # layouts.append(layout.Columns(**layout_theme, name='columns'))
    # layouts.append(layout.Floating(**layout_theme, name='floating'))
    # layouts.append(layout.Matrix(**layout_theme, name='matrix'))
    layouts.append(layout.Max(name='max'))
    layouts.append(layout.MonadTall(**layout_theme, name='monadtall'))
    # layouts.append(layout.MonadThreeCol(**layout_theme, name='monadthreecol'))
    # layouts.append(layout.MonadWide(**layout_theme, name='monawide'))
    # layouts.append(layout.RatioTile(**layout_theme, name='ratiotail'))
    # layouts.append(layout.Slice(**layout_theme, name='slice'))
    # layouts.append(layout.Spiral(**layout_theme, name='spiral'))
    # layouts.append(layout.Stack(**layout_theme, name='stack'))
    # layouts.append(layout.Tile(**layout_theme, name='tile'))
    # layouts.append(layout.TreeTab(**layout_theme, name='treetab'))
    # layouts.append(layout.VerticalTile(**layout_theme, name='verticaltile'))
    layouts.append(layout.Zoomy(**layout_theme, name='zoomy'))
    # layouts.append(get_floating_layout())

    return layouts