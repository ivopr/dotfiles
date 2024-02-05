from libqtile.config import Group, Key, Match, Rule
from libqtile.lazy import lazy

from bindings import keys
from constants import mod

groups = [Group(i) for i in "1234567890"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

dgroups_app_rules = [
    Rule(Match(wm_class="code"), group="1"),
    Rule(Match(wm_class="kitty"), group="2"),
    Rule(Match(wm_class="google-chrome"), group="3"),
    Rule(Match(wm_class="discord"), group="4"),
    Rule(Match(wm_class="nemo"), group="5"),
    Rule(Match(wm_class="spotify"), group="7"),
]