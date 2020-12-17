#!/usr/bin/env python
import os
import argparse
from subprocess import run, PIPE

from xdg import BaseDirectory, DesktopEntry


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--categories', action='store_true',
                        help='Show category names')
    parser.add_argument('-e', '--executable', action='store_true',
                        help='Show command line')
    parser.add_argument('-g', '--generic-name', action='store_true',
                        help='Show generic name for apps')
    parser.add_argument('-n', '--dry-run', action='store_true',
                        help='Do not run app, output to stdout')
    parser.add_argument('-x', '--xdg-de', action='store_true',
                        help='Show apps for specific desktop environments')
    parser.add_argument('-d', '--dmenu', metavar='dmenu_cmd',
                        default='dmenu -i -l 10 -p drun',
                        help='Customize dmenu command, default is %(default)s')
    parser.add_argument('-t', '--terminal', metavar='terminal',
                        default='xterm',
                        help='Terminal emulator to run text based programs, '
                        'default is %(default)s')
    return parser.parse_args()


if __name__ == '__main__':
    args = get_args()

    current_desktop = set(os.getenv('XDG_CURRENT_DESKTOP').split(':'))

    lines = []
    cmds = {}
    for data_dir in BaseDirectory.xdg_data_dirs:
        app_dir = os.path.join(data_dir, 'applications')
        if not os.path.exists(app_dir) or not os.path.isdir(app_dir):
            continue

        for app in os.listdir(app_dir):
            if not app.endswith('.desktop'):
                continue

            app_path = os.path.join(app_dir, app)
            entry = DesktopEntry.DesktopEntry(app_path)
            Exec = entry.getExec()
            Icon = entry.getIcon()
            Name = entry.getName()
            Terminal = entry.getTerminal()
            TryExec = entry.getTryExec()
            GenericName = entry.getGenericName()
            Categories = entry.getCategories()
            NoDisplay = entry.getNoDisplay()
            OnlyShowIn = entry.getOnlyShowIn()
            NotShowIn = entry.getNotShowIn()

            if (NoDisplay or
                    Exec is None or
                    (TryExec and entry.findTryExec() is None) or
                    set(NotShowIn).intersection(current_desktop) or
                    (OnlyShowIn and
                        not set(OnlyShowIn).intersection(current_desktop))):
                continue

            line = Name

            if GenericName and args.generic_name:
                line += " ({generic_name})".format(generic_name=GenericName)

            if Categories and args.categories:
                line += " [{category}]".format(category=';'.join(Categories))

            cmd = Exec.replace(' %f', '') \
                      .replace(' %F', '') \
                      .replace(' %u', '') \
                      .replace(' %U', '') \
                      .replace('%c', Name) \
                      .replace('%k', app_path)

            if Icon:
                cmd = cmd .replace('%i', "--icon {icon}".format(icon=Icon))

            if Terminal:
                cmd = "{terminal} -e {cmd}".format(terminal=args.terminal,
                                                   cmd=cmd)
            if args.executable:
                line += " $" + cmd

            cmds[line] = cmd

            if Icon and args.dmenu.startswith("rofi"):
                line += "\0icon\x1f{icon}".format(icon=Icon)

            lines.append(line)

    result = run(args.dmenu,
                 shell=True,
                 stdout=PIPE,
                 input='\n'.join(lines),
                 encoding='ascii')

    if result.stdout != '':
        run(cmds[result.stdout[:-1]], shell=True)
