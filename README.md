# dotfiles

My dotfiles and script. Script can easily manage dotfiles.

## Quick Start

1. Clone this repo.\
   ( Example, `~/.local/share/` )

2. Run `script.py`

```shell
chmod +x script.py
./script.py link
```

## Usage

```shell
./script.py [COMMAND] [FILE]
```

- [COMMAND]
  - link
  - unlink

### Examples

remove symlinks

```shell
./script.py unlink
```

choose target

```shell
./script.py link i3 i3status polybar

# unlink is too
# ./script.py unlink i3 i3status polybar
```

## LICENSE

MIT
