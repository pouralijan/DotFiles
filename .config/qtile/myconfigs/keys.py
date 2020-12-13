from libqtile.command import lazy
from libqtile.config import Key, Drag, Click

import logging
import os

if not os.path.exists('logs'):
    os.mkdir("logs")
logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('logs/qtile.log')
logger.addHandler(file_handler)


from . import groups

myTerm = "terminator" # My terminal of choice
myTerm = "xfce4-terminal" # My terminal of choice
myTerm = "alacritty" # My terminal of choice
mod = "mod4" # Sets mod key to SUPER/WINDOWS
mod1 = "mod1" # Sets mod key to SUPER/WINDOWS

def init_mouse():
    return [Drag([mod], "Button1", lazy.window.set_position_floating(),      # Move floating windows
                 start=lazy.window.get_position()),
            Drag([mod], "Button3", lazy.window.set_size_floating(),          # Resize floating windows
                 start=lazy.window.get_size()),
            Click([mod, "shift"], "Button1", lazy.window.bring_to_front())]  # Bring floating window to front


# SETS GROUPS KEYBINDINGS

@lazy.function
def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)

#@lazy.function
def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)

##### LAUNCH APPS IN SPECIFIED GROUPS #####
#def app_or_group(group, app):
#    logger.warning(f'{group}, {app}')
#    def f(qtile):
#        if qtile.groupMap[group].windows:
#            qtile.groupMap[group].cmd_toscreen()
#        else:
#            qtile.groupMap[group].cmd_toscreen()
#            qtile.cmd_spawn(app)
#    return f
def app_or_group(qtile, group, app):
    logger.warning(f'{group}, {app}')
    if qtile.groupMap[group].windows:
        qtile.groupMap[group].cmd_toscreen()
    else:
        qtile.groupMap[group].cmd_toscreen()
        qtile.cmd_spawn(app)

def grow(group):
    def function(qtile):
        logger.warning(group)
        if group == "WWW":
            logger.warning("resize window")
            logger.warning(qtile.current_layout)
            qtile.current_layout.cmd_grow()
    return function

#@lazy.function
def switch_screens(qtile):
    current_screen_index = qtile.screens.index(qtile.current_screen)
    group = qtile.screens[current_screen_index - 1].group
    qtile.current_screen.set_group(group)
##### KEYBINDINGS #####

def go_to_group(qtile, group):
    target_group = qtile.groups_map[group]
    # TODO (Hassan Pouralijan <pouralijan@gmail.com): Relpace hardcode screen number with screen_affinity
    # after fixed Group screen_affinity.
    #if hasattr(target_group, "screen_affinity"):
    #    screen_affinity = target_group.screen_affinity
    #else:
    #    screen_affinity = 1
    #logger.warning(f'Target => {screen_affinity}')

    current_screen_index = qtile.current_screen.index
    if group in ['WWW', 'VBOX', 'GFX']:
        if current_screen_index != 1:
            qtile.cmd_to_screen(1)
    else:
        if current_screen_index != 0:
            qtile.cmd_to_screen(0)

    current_group = qtile.current_group
    if current_group != target_group:
        target_group.cmd_toscreen()

import enum
class DIRECTION(enum.Enum):
    LEFT = 0
    RIGHT = 1
    DOWN = 2
    UP = 3

def get_keys():
    keys = []

    ########################################################################
    index = 1
    for current_group in groups.get_groups():
        keys.append(Key([mod], str(index), lazy.function(go_to_group, current_group.name))) # Switch to another group
        keys.append(Key([mod, "shift"], str(index), lazy.window.togroup(current_group.name))) # Send current window to another group
        index += 1
    ########################################################################

    ########################################################################
    keys.append(Key([mod], "h", lazy.layout.left()))
    keys.append(Key([mod], "l", lazy.layout.right()))
    keys.append(Key([mod], "j", lazy.layout.down()))
    keys.append(Key([mod], "k", lazy.layout.up()))

    keys.append(Key([mod, "shift"], "h", lazy.layout.swap_left()))
    keys.append(Key([mod, "shift"], "l", lazy.layout.swap_right()))
    keys.append(Key([mod, "shift"], "j", lazy.layout.shuffle_down()))
    keys.append(Key([mod, "shift"], "k", lazy.layout.shuffle_up()))

    keys.append(Key([mod], "i", lazy.layout.grow()))
    keys.append(Key([mod], "m", lazy.layout.shrink()))
    #keys.append(Key([mod], "m", lazy.layout.maximize())) # Toggle a window between minimum and maximum sizes
    keys.append(Key([mod], "n", lazy.layout.normalize()))
    keys.append(Key([mod], "o", lazy.layout.maximize()))
    #keys.append(Key([mod, "shift"], "space", lazy.layout.flip()))
    keys.append(Key([mod, "shift"], "space", lazy.layout.flip()))
    keys.append(Key([mod1], "Tab", lazy.layout.next(), desc="Move window focus to other window"))

    #keys.append(Key([mod, "shift"], "space", lazy.function(switch_screens)))

   # # Switch between windows
   # keys.append(Key([mod], "h", lazy.layout.left(), desc="Move focus to left"))
   # keys.append(Key([mod], "l", lazy.layout.right(), desc="Move focus to right"))
   # keys.append(Key([mod], "j", lazy.layout.down(), desc="Move focus down"))
   # keys.append(Key([mod], "k", lazy.layout.up(), desc="Move focus up"))
   # keys.append(Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"))

   # # Move windows between left/right columns or move up/down in current stack.
   # # Moving out of range in Columns layout will create new column.
   # keys.append(Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"))
   # keys.append(Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"))
   # keys.append(Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"))
   # keys.append(Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"))

   # # Grow windows. If current window is on the edge of screen and direction
   # # will be to screen edge - window would shrink.

   # keys.append(Key([mod, "control"], "h", lazy.function(grow("WWW")), desc="Grow window to the left"))
   # #keys.append(Key([mod, "control"], "h", lazy.layout.grow(), desc="Grow window to the left"))
   # #keys.append(Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"))
   # #keys.append(Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"))
   # #keys.append(Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"))
   # #keys.append(Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"))

   # keys.append(Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"))
    # keys.append(Key([mod], "n", lazy.layout.normalize())) # Restore all windows to default size ratios 

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    keys.append(Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack"))
    keys.append(Key([mod], "Return", lazy.spawn(myTerm), desc="Launch terminal"))

    # Toggle between different layouts as defined below
    keys.append(Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"))
    keys.append(Key([mod], "w", lazy.window.kill(), desc="Kill focused window"))

    keys.append(Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"))
    keys.append(Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"))
    keys.append(Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"))
    ########################################################################


    keys.append(Key(["control", "mod1"], "l", lazy.spawn("light-locker-command -l")))
    ########################################################################

    # Increase number in master pane (Tile)), # Grow size of current window (XmonadTall)
    # keys.append(Key([mod, "shift"], "l", lazy.layout.grow(), lazy.layout.increase_nmaster()))

    # Shrink size of current window (XmonadTall), # Decrease number in master pane (Tile)
    #keys.append(Key([mod, "shift"], "h", lazy.layout.shrink(), lazy.layout.decrease_nmaster()))

    #keys.append(Key([mod, "shift"], "Left", window_to_prev_group)) # Move window to workspace to the left
    #keys.append(Key([mod, "shift"], "Right", window_to_next_group)) # Move window to workspace to the right
    #keys.append(Key([mod, "shift"], "KP_Enter", lazy.window.toggle_floating())) # Toggle floating

    # Swap panes of split stack (Stack), # Switch which side main pane occupies (XmonadTall)
    #keys.append(Key([mod, "shift"], "space", lazy.layout.rotate(), lazy.layout.flip()))
    ########################################################################
    # Stack controls
    #keys.append(Key([mod], "space", lazy.layout.next())) # Switch window focus to other pane(s) of stack
    #keys.append(Key([mod, "control"], "Return", lazy.layout.toggle_split())) # Toggle between split and unsplit sides of stack
    #keys.append(Key([mod], "Tab", lazy.next_layout())) # Toggle through layouts
    #keys.append(Key([mod, "shift"], "c", lazy.window.kill())) # Kill active window
    # keys.append(Key([mod], "w", lazy.to_screen(2))) # Keyboard focus screen(0)
    # keys.append(Key([mod], "e", lazy.to_screen(0))) # Keyboard focus screen(1)
    # keys.append(Key([mod], "r", lazy.to_screen(1))) # Keyboard focus screen(2)
    #keys.append(Key([mod, "control"], "k", lazy.layout.section_up())) # Move up a section in treetab
    #keys.append(Key([mod, "control"], "j", lazy.layout.section_down())) # Move down a section in treetab
    ########################################################################
    # GUI Apps
    #keys.append(Key([mod], "b", lazy.function(app_or_group, "WWW", "firefox")))
    keys.append(Key([mod], "b", lazy.function(app_or_group, "SYS", "firefox")))
    #keys.append(Key([mod], "b", lazy.function(app_or_group("WWW", "firefox"))))
    #keys.append(Key([mod], "f", lazy.spawn("pcmanfm")))
    #keys.append(Key([mod], "g", lazy.spawn("geany")))
    ################################################################################
    return keys
#def init_keys0():
#    keys = [
#            # Apps Launched with <SUPER> + <KEYPAD 0-9>
#            Key(
#                [mod], "KP_Insert",                                  # Keypad 0
#                # lazy.spawncmd()                                    # Qtile Run Dialog
#                lazy.spawn("dmenu_run -fn 'UbuntuMono Nerd Font:size=10' -nb '#292d3e' -nf '#bbc5ff' -sb '#82AAFF' -sf '#292d3e' -p 'dmenu:'")
#                ),
#            Key(
#                [mod], "KP_End",                                     # Keypad 1
#                lazy.spawn(myTerm+" -e lynx -cfg=~/.lynx/lynx.cfg -lss=~/.lynx/lynx.lss gopher://distro.tube")
#                # lazy.spawn(myTerm+" -e lynx -cfg=~/.lynx.cfg -lss=~/.lynx.lss http://www.distrowatch.com")
#                ),
#            Key(
#                [mod], "KP_Down",                                    # Keypad 2
#                lazy.spawn(myTerm+" -e sh ./scripts/googler-script.sh")
#                ),
#            Key(
#                [mod], "KP_Page_Down",                               # Keypad 3
#                lazy.spawn(myTerm+" -e newsboat")
#                ),
#            Key(
#                [mod], "KP_Left",                                    # Keypad 4
#                lazy.spawn(myTerm+" -e rtv")
#                ),
#            Key(
#                [mod], "KP_Begin",                                   # Keypad 5
#                lazy.spawn(myTerm+" -e neomutt")
#                ),
#            Key(
#                [mod], "KP_Right",                                   # Keypad 6
#                lazy.spawn(myTerm+" -e twitch-curses")
#                ),
#            Key(
#                [mod], "KP_Home",                                    # Keypad 7
#                lazy.spawn(myTerm+" -e sh ./scripts/haxor-news.sh")
#                ),
#            Key(
#                [mod], "KP_Up",                                      # Keypad 8
#                lazy.spawn(myTerm+" -e sh ./scripts/toot.sh")
#                ),
#            Key(
#                [mod], "KP_Page_Up",                                 # Keypad 9
#                lazy.spawn(myTerm+" -e sh ./scripts/tig-script.sh")
#                ),
#            # Apps Launched with <SUPER> + <SHIFT> + <KEYPAD 0-9>
#            Key(
#                [mod, "shift"], "KP_End",                            # Keypad 1
#                lazy.spawn(myTerm+" -e sh ./.config/vifm/scripts/vifmrun")
#                ),
#            Key(
#                [mod, "shift"], "KP_Down",                           # Keypad 2
#                lazy.spawn(myTerm+" -e joplin")
#                ),
#            Key(
#                [mod, "shift"], "KP_Page_Down",                      # Keypad 3
#                lazy.spawn(myTerm+" -e cmus")
#                ),
#            Key(
#                [mod, "shift"], "KP_Left",                           # Keypad 4
#                lazy.spawn(myTerm+" -e irssi")
#                ),
#            Key(
#                [mod, "shift"], "KP_Begin",                          # Keypad 5
#                lazy.spawn(myTerm+" -e rtorrent")
#                ),
#            Key(
#                [mod, "shift"], "KP_Right",                          # Keypad 6
#                lazy.spawn(myTerm+" -e youtube-viewer")
#                ),
#            Key(
#                [mod, "shift"], "KP_Home",                           # Keypad 7
#                lazy.spawn(myTerm+" -e ncpamixer")
#                ),
#            Key(
#                [mod, "shift"], "KP_Up",                             # Keypad 8
#                lazy.spawn(myTerm+" -e calcurse")
#                ),
#            Key(
#                [mod, "shift"], "KP_Page_Up",                        # Keypad 9
#                lazy.spawn(myTerm+" -e vim /home/dt/.config/qtile/config.py")
#                ),
#            # Apps Launched with <SUPER> + <CONTROL> + <KEYPAD 0-9>
#            Key(
#                [mod, "control"], "KP_End",                            # Keypad 1
#                lazy.spawn(myTerm+" -e htop")
#                ),
#            Key(
#                [mod, "control"], "KP_Down",                           # Keypad 2
#                lazy.spawn(myTerm+" -e gtop")
#                ),
#            Key(
#                [mod, "control"], "KP_Page_Down",                      # Keypad 3
#                lazy.spawn(myTerm+" -e nmon")
#                ),
#            Key(
#                [mod, "control"], "KP_Left",                           # Keypad 4
#                lazy.spawn(myTerm+" -e glances")
#                ),
#            Key(
#                [mod, "control"], "KP_Begin",                          # Keypad 5
#                lazy.spawn(myTerm+" -e s-tui")
#                ),
#            Key(
#                [mod, "control"], "KP_Right",                          # Keypad 6
#                lazy.spawn(myTerm+" -e httping -KY --draw-phase localhost")
#                ),
#            Key(
#                [mod, "control"], "KP_Home",                           # Keypad 7
#                lazy.spawn(myTerm+" -e cmatrix -C cyan")
#                ),
#            Key(
#                [mod, "control"], "KP_Up",                             # Keypad 8
#                lazy.spawn(myTerm+" -e pianobar")
#                ),
#            Key(
#                [mod, "control"], "KP_Page_Up",                        # Keypad 9
#                lazy.spawn(myTerm+" -e wopr report.xml")
#                ),
#        ]
#    return keys
#
