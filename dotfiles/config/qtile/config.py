from libqtile.config import Key, Screen, Group, Drag, Click
from libqtile.command import lazy
from libqtile import layout, bar, widget
from libqtile import extension


try:
    from typing import List  # noqa: F401
except ImportError:
    pass

mod = "mod4"
dmenu = 'dmenu_run -y 19 -p ">" -l 5 -sb "#126e00" -nb "#202020" -nf "#eeeeee" -sf "#eeeeee" -fn "droid sans mono-10"'

keys = [
    # Switch between windows in current stack pane
    Key([mod], "k", lazy.layout.previous()),
    Key([mod], "j", lazy.layout.next()),

    # Move windows up or down in current stack
    Key([mod, "control"], "k", lazy.layout.shuffle_down()),
    Key([mod, "control"], "j", lazy.layout.shuffle_up()),

    # Switch window focus to other pane(s) of stack
    Key([mod], "space", lazy.layout.next()),

    # Swap panes of split stack
    Key([mod, "shift"], "space", lazy.layout.rotate()),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split()),
    Key([mod], "Return", lazy.spawn("urxvt")),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout()),
    Key([mod], "w", lazy.window.kill()),

    Key([mod, "control"], "r", lazy.restart()),
    Key([mod, "control"], "q", lazy.shutdown()),
    Key([mod, "mod1"], "l", lazy.spawn("/home/transacid/bin/lock.sh")),
    Key([mod, "control"], "h", lazy.spawn("sudo systemctl poweroff")),
    Key([mod, "control"], "l", lazy.spawn("sudo systemctl reboot")),
    Key([mod, "control"], "s", lazy.spawn("sudo systemctl suspend")),
    Key([mod], "r",            lazy.spawn(dmenu)),
]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen()),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
    ])

layouts = [
    layout.RatioTile(border_focus='#126e00', border_normal='#303030', border_width=1),
    layout.Max()
]

widget_defaults = dict(
    font='droid sans mono',
    fontsize=10,
    padding=2,
    foreground='#adadad',
    background='#202020',
    borderwidth=1,
    border_width=1,
    graph_color='126e00',
    border_color='#606060',
    fill_color='#101010',
    line_width=1,
    margin_x=1,
    margin_y=1,
    interface="wlp3s0"
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(active='#126e00', this_current_screen_border='#126e00',inactive='#adadad'),
                widget.TaskList(icon_size=0, urgent_border='#ff7070', unfocused_border='#303030', border='#126e00'),
                widget.CPUGraph(graph_color='#adadad', fill_color='#adadad', border_color='#126e00', type='linefill'),
                widget.Sep(size_percent=70, foreground='#126e00'),
                widget.MemoryGraph(fill_color='#adadad', graph_color='#adadad', border_color='#126e00'),
                widget.Systray(),
                widget.ThermalSensor(foreground='#adadad', threshold=86),
                widget.Sep(size_percent=70, foreground='#126e00'),
                widget.Wlan(format="{essid} {percent:2.0%}"),
                widget.Sep(size_percent=70, foreground='#126e00'),
                widget.Net(),
                widget.Sep(size_percent=70, foreground='#126e00'),
                widget.Battery(low_percentage=0.1),
                widget.Sep(size_percent=70, foreground='#126e00'),
                widget.Clock(format='%a, %d %b %Y'),
                widget.Clock(format='%H:%M:%S', foreground='#ffffff'),
            ],
            19,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
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
])
auto_fullscreen = True
focus_on_window_activation = "smart"

wmname = "LG3D"
