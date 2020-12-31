# dmenu_drun

As you can guess from the name, this script is `dmenu_run` counter-part for desktop applications, the `drun` is borrowed from `rofi`'s modi name.

## Requirements

- `dmenu`
- `pyxdg` module

## Usage

```
dmenu_drun.py [-h] [-c] [-x] [-g] [-N] [-e] [-d dmenu_cmd] [-t terminal]

optional arguments:
  -h, --help            show this help message and exit
  -c, --categories      Show category names
  -x, --executable      Show command line
  -g, --generic-name    Show generic name for apps
  -N, --dry-run         Do not run app, output to stdout
  -e, --xdg-de          Show apps for specific desktop environments
  -d dmenu_cmd, --dmenu dmenu_cmd
                        Customize dmenu command, default is dmenu -i -l 10 -p drun
  -t terminal, --terminal terminal
                        Terminal emulator to run text based programs, default is xterm
```

Note: all unknown arguments (not listed above) are passed to `dmenu`, so instead of specify `-d "dmenu -p prompt"`, you can use `-p prompt` directly.

## Features

- Rather fast loading (less than 0.1s should be negligible for majorities)
- Options to show categories, generic name and command. This can let you match more info.
- You can customize `dmenu` command as you like
  - If using `rofi -dmenu` as `dmenu` replacement, it will show icons! However, that seems just like `rofi -show drun`, why not reinvent some wheels, right?
- Considers lots of freedesktop standards (to decide whether to show an app)

TODO:
- Parse .menu and .directory files
