from libqtile import layout, hook

from . import colors

##### LAYOUTS #####
def init_floating_layout():
    return layout.Floating(border_focus="#3B4022")

def get_layout_theme():
    colors_list = colors.get_colors()

    return {"border_width": 2,
            "margin": 8,
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
    floating_layout = layout.Floating(float_rules=[
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
    {'wmclass': 'rocket.chat'},
    {'wname': 'Android Emulator.*'},
    {'wname': 'Android Emulator - Mi9TProEmu:5554'},
    {'wmclass': 'pavucontrol'},
    {'wmclass': 'Pavucontrol'},
    {'wmclass': 'volumeicon'},
    {'wmclass': 'Volumeicon'},
])

    return floating_layout


def get_layouts():
    layout_theme = get_layout_theme()

    layouts = []
    layouts.append(layout.MonadTall(**layout_theme, name='monadtall'))
    #layouts.append(layout.MonadWide(**layout_theme, name='monawide'))
    #layouts.append(layout.Stack(stacks=4, **layout_theme, name='stak'))
    #layouts.append(layout.Floating(**layout_theme, name='floating'))
    layouts.append(layout.Floating(**layout_theme, name='floating',))
    #layouts.append(get_floating_layout())
    layouts.append(layout.Max(**layout_theme, name='max'))
    #layouts.append(layout.Bsp(**layout_theme, name='bsp'))
    return layouts

