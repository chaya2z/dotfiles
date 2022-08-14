#!/usr/bin/env python3

import os.path
import fire
import subprocess


class Dotfiles:
    def __init__(self):
        self._home_dir = os.environ['HOME']
        self._config_dir = os.path.join(self._home_dir, ".config")
        self._current_dir = os.path.dirname(os.path.abspath(__file__))
        self._target_files = self._load_target_files()

    def _load_ignore_files(self):
        """
        read .dotignore file
        """
        dotignore = os.path.join(self._current_dir, ".dotignore")
        with open(dotignore) as f:
            lines = f.readlines()

        files = set()
        for line in lines:
            # remove comments
            if line[0] != "#":
                files.add(line[:-1])

        return files

    def _load_target_files(self):
        files = os.listdir(self._current_dir)
        ignore_files = self._load_ignore_files()
        filtered_files = []
        for file in files:
            if file not in ignore_files:
                filtered_files.append(file)

        return filtered_files

    def _symlink_handler(self, target_files, func):
        """
        create links to "target_path" with the name "link_path"
        """
        for target in target_files:
            target_path = os.path.join(self._current_dir, target)
            if target[:4] == "dot_":
                link_path = os.path.join(self._home_dir, ("." + target[4:]))
            else:
                link_path = os.path.join(self._config_dir, target)

            func(target_path, link_path)

    @staticmethod
    def _link(target_path, link_path):
        subprocess.run(["ln", "-s", target_path, link_path])

    def link(self, *files):
        """
        make symbolic links
        :type files list
        """
        if len(files) != 0:
            # specific target files
            self._target_files = files

        self._symlink_handler(self._target_files, self._link)

    @staticmethod
    def _unlink(_, link_path):
        subprocess.run(["unlink", link_path])

    def unlink(self, *files):
        """
        remove symbolic links
        :type files: list
        """
        if len(files) != 0:
            # specific target files
            self._target_files = files

        self._symlink_handler(self._target_files, self._unlink)


def main():
    fire.Fire(Dotfiles)


if __name__ == '__main__':
    main()
