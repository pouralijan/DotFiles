# -*- coding: utf-8 -*-


from libqtile import layout

import myconfigs

# DEFINING A FEW THINGS
if __name__ in ["config", "__main__"]:

    keys = myconfigs.keys.get_keys()
    layouts = myconfigs.layouts.get_layouts()
    groups = myconfigs.groups.get_groups()
    screens = myconfigs.screens.get_screens()

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
    {'wmclass': 'Steam'},
    {'wname': 'Steam Login'},

])
