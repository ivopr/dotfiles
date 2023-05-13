#                                                               #
#       ______                  __  _ __        _    _____      #
#      / ____/___  ____  __  __/ /_(_) /__     | |  / /__ \     #
#     / /   / __ \/_  / / / / / __/ / / _ \    | | / /__/ /     #
#    / /___/ /_/ / / /_/ /_/ / /_/ / /  __/    | |/ // __/      #
#    \____/\____/ /___/\__, /\__/_/_/\___/     |___//____/      #
#                     /____/                                    #
#                                                               #
#                                                     DARKKAL44 #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


from libqtile import bar, layout, widget, hook, qtile
from libqtile.config import Click, Drag, Group, Key, Match, hook, Screen, Rule
from libqtile.lazy import lazy
from os import path

cwdir = path.dirname(__file__)

mod = "mod4"
terminal = "alacritty"

# █▄▀ █▀▀ █▄█ █▄▄ █ █▄░█ █▀▄ █▀
# █░█ ██▄ ░█░ █▄█ █ █░▀█ █▄▀ ▄█
keys = [

#  D E F A U L T
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    Key([mod, "control"], "Left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "control"], "Right", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "control"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "control"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([mod, "shift"], "Left", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "shift"], "Up", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod], "f", lazy.window.toggle_floating()),
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "c", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawn("rofi -show drun"), desc="Spawn a command using a prompt widget"),
    Key([mod], "p", lazy.spawn("sh -c ~/.config/rofi/scripts/power"), desc='powermenu'),

# C U S T O M
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume 0 +5%"), desc='Volume Up'),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume 0 -5%"), desc='volume down'),
    Key([], "XF86AudioMute", lazy.spawn("pulsemixer --toggle-mute"), desc='Volume Mute'),
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause"), desc='playerctl'),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous"), desc='playerctl'),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next"), desc='playerctl'),
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl s 10%+"), desc='brightness UP'),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl s 10%-"), desc='brightness Down'),
	Key([mod], "h", lazy.spawn("roficlip"), desc='clipboard'),
    Key([mod], "s", lazy.spawn("flameshot gui"), desc='Screenshot'),
]



# █▀▀ █▀█ █▀█ █░█ █▀█ █▀
# █▄█ █▀▄ █▄█ █▄█ █▀▀ ▄█
groups = [Group(f"{i+1}", label="󰏃") for i in range(5)]

for i in groups:
    keys.extend(
            [
                Key(
                    [mod],
                    i.name,
                    lazy.group[i.name].toscreen(),
                    desc="Switch to group {}".format(i.name),
                    ),
                Key(
                    [mod, "shift"],
                    i.name,
                    lazy.window.togroup(i.name, switch_group=True),
                    desc="Switch to & move focused window to group {}".format(i.name),
                    ),
                ]
            )




# L A Y O U T S
layouts = [
    layout.Columns(
        margin=3,
        border_focus='#607767',
	    border_normal='#1F1D2E',
        border_width=2,
    )
]


widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=0,
)

extension_defaults = [
    widget_defaults.copy()
]


def power():
    qtile.cmd_spawn("sh -c ~/.config/rofi/scripts/power")


# █▄▄ ▄▀█ █▀█
# █▄█ █▀█ █▀▄
screens = [
    Screen(
        wallpaper=f"{cwdir}/Assets/wallpaper.jpg",
        wallpaper_mode="fill",
        top=bar.Bar(
            [
				widget.Spacer(length=15,
                    background='#0F1212',
                ),

                widget.Image(
                    filename=f'{cwdir}/Assets/launch_Icon.png',
                    margin=2,
                    background='#0F1212',
                    mouse_callbacks={"Button1": power},
                ),

                widget.Image(
                    filename=f'{cwdir}/Assets/6.png',
                ),

                widget.GroupBox(
                    fontsize=10,
                    borderwidth=3,
                    highlight_method='block',
                    active='#607767',
                    block_highlight_text_color="#B2BEBC",
                    highlight_color='#D0DAF0',
                    inactive='#0F1212',
                    foreground='#4B427E',
                    background='#202222',
                    this_current_screen_border='#202222',
                    this_screen_border='#202222',
                    other_current_screen_border='#202222',
                    other_screen_border='#202222',
                    urgent_border='#202222',
                    rounded=True,
                    disable_drag=True,
                ),

                widget.Spacer(
                    length=8,
                    background='#202222',
                ),

                widget.Image(
                    filename=f'{cwdir}/Assets/5.png',
                ),


                widget.Image(
                    filename=f'{cwdir}/Assets/layout.png',
                    background="#0F1212"
                ),

                widget.CurrentLayout(
                    background='#0F1212',
                    foreground='#607767',
                    fmt='{}',
                    font="Fira Code Bold",
                ),


                widget.Image(
                    filename=f'{cwdir}/Assets/4.png',
                ),


                widget.WindowName(
                    background = '#202222',
                    format = "{name}",
                    font='Fira Code Bold',
                    foreground='#607767',
                    empty_group_string = 'Desktop',

                ),


                widget.Image(
                    filename=f'{cwdir}/Assets/3.png',
                ),


                widget.Systray(
                    background='#0F1212',
                    fontsize=2,
                    padding=10
                ),


                widget.TextBox(
                    text=' ',
                    background='#0F1212',
                ),


                widget.Image(
                    filename=f'{cwdir}/Assets/6.png',
                    background='#202222',
                ),

                widget.Image(
                    filename=f'{cwdir}/Assets/Misc/ram.png',
                    background='#202222',
                ),


                widget.Spacer(
                    length=-7,
                    background='#202222',
                ),


                widget.Memory(
                    background='#202222',
                    format='{MemUsed: .0f}{mm}',
                    foreground='#607767',
                    font="Fira Code Bold",
                    fontsize=13,
                    update_interval=5,
                ),

                widget.Image(
                    filename=f'{cwdir}/Assets/2.png',
                ),


                widget.Spacer(
                    length=8,
                    background='#202222',
                ),


                widget.BatteryIcon(
                    theme_path=f'{cwdir}/Assets/Battery/',
                    background='#202222',
                    scale=1,
                ),


                widget.Battery(
                    font='Fira Code Bold',
                    background='#202222',
                    foreground='#607767',
                    format='{percent:2.0%}',
                ),


                widget.Image(
                    filename=f'{cwdir}/Assets/2.png',
                ),


                widget.Spacer(
                    length=8,
                    background='#202222',
                ),

                widget.Volume(
                    font='Fira Code Nerd',
                    theme_path=f'{cwdir}/Assets/Volume/',
                    emoji=True,
                    fontsize=13,
                    background='#202222',
                    padding=2
                ),


                widget.Spacer(
                    length=-5,
                    background='#202222',
                    ),


                widget.Volume(
                    font='Fira Code Bold',
                    background='#202222',
                    foreground='#607767',
                ),


                widget.Image(
                    filename=f'{cwdir}/Assets/5.png',
                    background='#202222',
                ),


                widget.Image(
                    filename=f'{cwdir}/Assets/Misc/clock.png',
                    background='#0F1212',
                    margin_y=6,
                    margin_x=5,
                ),


                widget.Clock(
                    format='%I:%M %p',
                    background='#0F1212',
                    foreground='#607767',
                    font="Fira Code Bold",
                    fontsize=13,
                ),


                widget.Spacer(
                    length=18,
                    background='#0F1212',
                ),
            ],
            30,
            border_color='#282738',
            border_width=[0, 0, 0, 0],
            margin=[15, 60, 6, 60],
        ),
        left=bar.Gap(35),
        right=bar.Gap(7),
        bottom=bar.Gap(7)
    ),
]



# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = [
    Rule(Match(wm_class=["code"]), group="1"),
    Rule(Match(wm_class=["Alacritty"]), group="2"),
    Rule(Match(wm_class=["google-chrome", "Google-chrome"]), group="3"),
    Rule(Match(wm_class=["discord", "Spotify"]), group="4")
]  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    border_focus='#607767',
    border_normal='#1F1D2E',
	border_width=2,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)




from libqtile import hook
# some other imports
import os
import subprocess
# stuff
@hook.subscribe.startup_once
def autostart_once():
    home = os.path.expanduser(f'{cwdir}/autostart_once.sh')
    subprocess.Popen([home])

@hook.subscribe.client_new
def floating_size_hints(window):
    floating_window_names = ["Save File"]

    window_wm_name = window.name

    should_float = window_wm_name in floating_window_names

    if should_float:
        window.floating = True
        window.cmd_set_size_floating(800, 600)
        window.cmd_center()


auto_fullscreen = False
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"



# E O F
