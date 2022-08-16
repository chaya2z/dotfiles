#!/usr/bin/env python3
import errno
import os.path
import sys
import fire
import subprocess


class Dotfiles:
    def __init__(self):
        # path
        self._home_dir = os.environ['HOME']
        self._config_dir = os.path.join(self._home_dir, ".config")
        self._current_dir = os.path.dirname(os.path.abspath(__file__))
        self._dotignore_path = os.path.join(self._current_dir, ".dotignore")
        # file
        self._ignore_files = self._load_ignore_files()
        self._all_targets = self._load_all_targets()
        self._target_files = set()

    def _gen_target_files(self, files):
        """
        Check command line arguments is valid

        :param files: command line arguments
        :type files: tuple
        :return: link/unlink valid target files
        :rtype: set
        :raise: OSError ENOENT: if not found file/directory given command line arguments
        """
        if len(files) == 0:
            # no command arguments
            return self._all_targets
        else:
            # files is targets specified by user
            for item in files:
                try:
                    if item not in self._all_targets:
                        raise OSError(errno.ENOENT, os.strerror(errno.ENOENT), item)
                except OSError as err:
                    print(err)
                    print("If '" + item + "' is specified in '.dotignore, remove it")
                    sys.exit(errno.ENOENT)

            return set(files)

    def _load_all_targets(self):
        """
        load non ignored targets (files/directories)

        :return: non ignored targets
        :rtype: set
        """
        files = os.listdir(self._current_dir)
        filtered_files = set()
        for item in files:
            if item in self._ignore_files:
                continue

            filtered_files.add(item)

        return filtered_files

    def _load_ignore_files(self):
        """
        read .dotignore file

        :return: ignore targets
        :rtype: set
        """
        try:
            with open(self._dotignore_path) as f:
                lines = f.readlines()
        except FileNotFoundError as err:
            print(err)
            print("You have to create", self._dotignore_path)
            sys.exit(errno.ENOENT)

        files = set()
        for line in lines:
            # remove comments
            if line[0] != "#":
                files.add(line[:-1])

        return files

    def _confirm(self, target, link, func):
        """
        confirm link/unlink symbolic link
        """
        try:
            user_reply = ""
            if func == self._link:
                user_reply = input("Create symbolic link '" + link + "' to '" + target + "' [Y/n]: ")

            if func == self._unlink:
                user_reply = input("Remove symbolic link '" + link + "' [Y/n]: ")

            if user_reply == "" or user_reply == "Y" or user_reply == "y" or user_reply == "yes":
                return True
            else:
                return False
        except KeyboardInterrupt:
            print("\nexit")
            sys.exit(0)

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

            if self._confirm(target_path, link_path, func):
                func(target_path, link_path)
            else:
                print("Skipped")
                continue

    # link

    @staticmethod
    def _link(target_path, link_path):
        subprocess.run(["ln", "-s", target_path, link_path])

    def link(self, *files):
        """
        make symbolic links
        This function will be called by Fire

        :param files: command line arguments
        :type files: tuple
        """
        self._target_files = self._gen_target_files(files)
        self._symlink_handler(self._target_files, self._link)

    # unlink

    @staticmethod
    def _unlink(_, link_path):
        subprocess.run(["unlink", link_path])

    def unlink(self, *files):
        """
        remove symbolic links
        This function will be called by Fire

        :param files: command line arguments
        :type files: tuple
        """
        self._target_files = self._gen_target_files(files)
        self._symlink_handler(self._target_files, self._unlink)


def main():
    fire.Fire(Dotfiles)
    print("Done")


if __name__ == '__main__':
    main()
