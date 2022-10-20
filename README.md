# dotfiles

My dotfiles and script. Script can easily manage dotfiles.

## Quick Start

1. Clone this repo.\
   ( Example, `~/.local/share/` )

2. Create/Copy config files or directories you want to manage this repo.

```shell
sudo cp /etc/i3 .
```

3. Run `script.py`

```shell
chmod +x script.py
./script.py link
```

## Command Usage

```shell
./script.py [COMMAND] [FILE]
```

- [COMMAND]
  - link
  - unlink

### Examples

Use `unlink` command to remove symlinks.

```shell
./script.py unlink
```

You can choose targets.

```shell
./script.py link i3 i3status polybar

# unlink is too
# ./script.py unlink i3 i3status polybar
```

## LICENSE

MIT
