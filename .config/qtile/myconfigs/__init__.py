import os
import subprocess
from libqtile import hook

# STARTUP APPLICATIONS
@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/myconfigs/autostart.sh'])

wmname = "qtile"

from . import keys
from . import colors
from . import groups
from . import layouts
from . import screens
