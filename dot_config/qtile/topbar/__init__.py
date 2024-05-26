from libqtile import bar, widget
from constants import colors

small_spacer = widget.Spacer(
    background=colors["background"],
    foreground=colors["foreground"],
    length=8
)

medium_spacer = widget.Spacer(
    background=colors["background"],
    foreground=colors["foreground"],
    length=12
)

large_spacer = widget.Spacer(
    background=colors["background"],
    foreground=colors["foreground"],
    length=16
)

topbar = bar.Bar(
    [
        large_spacer,
        # widget.CurrentLayout(
        #     background=colors["background"],
        #     foreground=colors["foreground"],

        #     font="Fira Code Retina",
        #     fontsize=16
        # ),
        # small_spacer,
        widget.GroupBox(
            active=colors["15"],
            background=colors["background"],
            foreground=colors["foreground"],
            inactive=colors["background-lighter"],
            highlight_color=[colors["background"], colors["background"]],
            this_current_screen_border=colors["foreground"],
            this_screen_border=colors["foreground"],
            urgent_border=colors["9"],
            urgent_text=colors["1"],
            
            fmt="⬤",
            font="Fira Code Bold",
            fontsize=16,
            highlight_method="line",
            disable_drag=True
        ),
        small_spacer,
        widget.Prompt(
            background=colors["background"],
            foreground=colors["foreground"],
        ),
        small_spacer,
        widget.WindowName(
            background=colors["background"],
            foreground=colors["foreground"],
            font="Fira Code Bold",
            fontsize=16
        ),
        small_spacer,
        widget.Chord(
            background=colors["background"],
            foreground=colors["foreground"],
            chords_colors={
                "launch": ("#ff0000", "#ffffff"),
            },
            name_transform=lambda name: name.upper(),
        ),
        small_spacer,
        # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
        # widget.StatusNotifier(),
        widget.Systray(
            background=colors["background"],
            foreground=colors["foreground"],
        ),
        small_spacer,
        widget.Volume(
            background=colors["background"],
            foreground=colors["foreground"],
            font="Fira Code Bold",
            fontsize=16
        ),
        small_spacer,
        widget.Clock(
            format="%A, %d/%m/%Y %H:%M",
            background=colors["background"],
            foreground=colors["foreground"],
            font="Fira Code Bold",
            fontsize=16
        ),
        large_spacer
    ],
    36,
    # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
    # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
)
