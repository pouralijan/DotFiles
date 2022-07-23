from libqtile.config import Group, Match, Key
from libqtile.lazy import lazy

 ##### GROUPS #####
mod = "mod4"

def get_groups():
    groups = []
    com_group_app = [
        Match(wm_class="rocket.chat"),
        Match(wm_class="jitsi meet"),
        Match(wm_class="Jitsi Meet", ),
    ]

    groups.append(Group("DEV", layout='monadtall')) # 'layouts': ['monadtall'] }))
    groups.append(Group("WWW", layout='max', matches=[Match(wm_class=["firefox"])] ))

    groups.append(Group("COM", layout='monadtall', matches=com_group_app))

    groups.append(Group("DOC", layout='monadtall'))
    groups.append(Group("STM", layout='max',matches=[Match(wm_class=["steam"])]))

    keys = []
    for i, group in enumerate(groups):
        keys.extend(
            [
                # mod1 + letter of group = switch to group
                Key(
                    [mod],
                    str(i+1),
                    lazy.group[group.name].toscreen(),
                    desc="Switch to group {}".format(group.name),
                ),
                # mod1 + shift + letter of group = switch to & move focused window to group
                Key(
                    [mod, "shift"],
                    str(i+1),
                    lazy.window.togroup(group.name, switch_group=True),
                    desc="Switch to & move focused window to group {}".format(group.name),
                ),
                # Or, use below if you prefer not to switch to that group.
                # # mod1 + shift + letter of group = move focused window to group
                # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
                #     desc="move focused window to group {}".format(i.name)),
            ]
        )
    return groups, keys

