# dmenu_drun

As you can guess from the name, this script is `dmenu_run` counter-part for desktop applications, the `drun` is borrowed from `rofi`'s modi name.

## Requirements

- `dmenu` or alternatives like `rofi`
- `pyxdg` module

## Usage

```
usage: dmenu_drun [-hcCegkNxX] [-d dmenu_cmd] [-t terminal]

options:
  -h, --help            show this help message and exit
  -c, --categories      Show main category names
  -C, --all-categories  Show all category names
  -d dmenu_cmd, --dmenu dmenu_cmd
                        Customize dmenu command, default is dmenu -i -l 10 -p drun
  -e, --xdg-de          Show apps despite only for specific desktop environments
  -g, --generic-name    Show generic name for apps
  -k, --keywords        Show keywords
  -N, --dry-run         Do not run app, output to stdout
  -t terminal, --terminal terminal
                        Terminal emulator to use, default is xterm
  -x, --executable      Show executable name
  -X, --fullcmd         Show command line

```

Note: all unknown arguments (not listed above) are passed to `dmenu`, so instead of specify `-d "dmenu -p prompt"`, you can use `-p prompt` directly.

## Features

- Fast enough loading (less than 0.1s should be negligible for most)
- Options to show categories, generic name and command. This can let you match more info.
- You can customize `dmenu` command as you like
  - If using `rofi -dmenu` as `dmenu` replacement, it will show icons! However, that seems just like `rofi -show drun`. Why not reinvent some wheels, right?
- Considers lots of freedesktop standards (to decide whether to show an app)

TODO:
- Parse .menu and .directory files
- tabulate output for dmenu
