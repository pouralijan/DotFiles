from libqtile.config import Group, Match

##### GROUPS #####
def get_group_names():
    groups = []
    groups.append(( "DEV", { 'layout': 'monadtall',})) # 'layouts': ['monadtall'] }))
    groups.append(( "WWW", { 'layout': 'max', 'matches': [Match(wm_class=["firefox"])], }))
    groups.append(( "SYS", {'layout': 'monadtall'}))
    groups.append(("DOC", {'layout': 'monadtall'}))
    groups.append(("VBOX", {'layout': 'floating'}))
    groups.append(("CHAT", {'layout': 'bsp'}))
    groups.append(("MEDIA", {'layout': 'monadtall'}))
    groups.append(("GFX", {'layout': 'floating'}))
    return groups

def get_groups():
    group_names = get_group_names()
    return [Group(name, **kwargs) for name, kwargs in group_names]

