# dotfiles

私の dotfiles とスクリプトです. スクリプトを利用することで dotfiles を簡単に管理することができます.

## Quick Start

1. このリポジトリを clone します.\
   ( 例えば, `~/.local/share/` へ )

2. Git で管理したいファイルやディレクトリをこのリポジトリに作成, またはコピーします.

```shell
sudo cp /etc/i3 .
```

3. `script.py` を実行します.

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

シンボリックリンクを解除するときは `unlink` コマンドを使用します.

```shell
./script.py unlink
```

コマンドの対象を指定することができます.

```shell
./script.py link i3 i3status polybar

# unlink の場合も同様です.
# ./script.py unlink i3 i3status polybar
```

## LICENSE

MIT
