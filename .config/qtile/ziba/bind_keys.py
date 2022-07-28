from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod4 = "mod4"
mod1 = "mod1"
terminal = guess_terminal()

def get_keys():
    keys = [
        # A list of available commands that can be bound to keys can be found
        # at https://docs.qtile.org/en/latest/manual/config/lazy.html
        # Switch between windows
        Key([mod4], "h", lazy.layout.left(), desc="Move focus to left"),
        Key([mod4], "l", lazy.layout.right(), desc="Move focus to right"),
        Key([mod4], "j", lazy.layout.down(), desc="Move focus down"),
        Key([mod4], "k", lazy.layout.up(), desc="Move focus up"),
        Key([mod1], "Tab", lazy.layout.next(), desc="Move window focus to other window"),
        # Move windows between left/right columns or move up/down in current stack.
        # Moving out of range in Columns layout will create new column.
        Key([mod4, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
        Key([mod4, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
        Key([mod4, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
        Key([mod4, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
        # Grow windows. If current window is on the edge of screen and direction
        # will be to screen edge - window would shrink.
        Key([mod4, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
        Key([mod4, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
        Key([mod4, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
        Key([mod4, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),

        Key([mod4, "control"], "s", lazy.layout.swap_main()),
        Key([mod4, "control"], "r", lazy.layout.rotate()),

        Key([mod4, "control"], "m", lazy.layout.maximize()),
        Key([mod4, "control"], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

        Key([mod4, "control"], "f", lazy.window.toggle_floating(), desc="Reset all window sizes"),
        Key([mod4, "control"], "space", lazy.layout.flip(), desc="Reset all window sizes"),

        Key([mod4, "control"], "Return", lazy.layout.toggle_split()),
        # Toggle between split and unsplit sides of stack.
        # Split = all windows displayed
        # Unsplit = 1 window displayed, like Max layout, but still with
        # multiple stack panes
        Key(
            [mod4, "shift"],
            "Return",
            lazy.layout.toggle_split(),
            desc="Toggle between split and unsplit sides of stack",
        ),


        # Application Keys
        Key([mod4], "Return", lazy.spawn(terminal), desc="Launch terminal"),


        # Qtile Key
        # Toggle between different layouts as defined below
        Key([mod4], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
        Key([mod4], "w", lazy.window.kill(), desc="Kill focused window"),
        Key([mod4, "control", "shift"], "r", lazy.reload_config(), desc="Reload the config"),
        Key([mod4, "control", "shift"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
        Key([mod4], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
        Key([mod4], "d", lazy.spawn("rofi -show drun"), desc="Spawn a command using a prompt widget"),
        Key([mod4], "space", lazy.spawn("rofi -show drun"), desc="Spawn a command using a prompt widget"),
        Key([mod1], "Shift_L", lazy.widget["keyboardlayout"].next_keyboard(), desc="Next keyboard layout"),

        
        Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),
        Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -10%")),
        # Key([], "XF86AudioLowerVolume", lazy.spawn("/usr/bin/volshow")),
        Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +10%")),
        # Key([], "XF86AudioRaiseVolume", lazy.spawn("/usr/bin/volshow")),

    ]
    return keys
