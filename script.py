import os.path
import fire
import subprocess


class Dotfiles:
    def __init__(self):
        self._home_dir = os.environ['HOME']
        self._config_dir = os.path.join(self._home_dir, ".config")
        self._current_dir = os.path.dirname(os.path.abspath(__file__))
        self._source_files = self._load_source_files()

    def _load_ignore_files(self):
        dotignore = os.path.join(self._current_dir, ".dotignore")
        with open(dotignore) as f:
            lines = f.readlines()

        files = set()
        for line in lines:
            if line[0] != "#":
                files.add(line[:-1])

        return files

    def _load_source_files(self):
        files = os.listdir(self._current_dir)
        ignore_files = self._load_ignore_files()
        filtered_files = []
        for file in files:
            if file not in ignore_files:
                filtered_files.append(file)

        return filtered_files

    def _symlink_handler(self, source_files, func):
        for source in source_files:
            source_path = os.path.join(self._current_dir, source)
            if source[:4] == "dot_":
                target_path = os.path.join(self._home_dir, ("." + source[4:]))
                func(source_path, target_path)
            else:
                target_path = os.path.join(self._config_dir, source)
                func(source_path, target_path)

    @staticmethod
    def _link(source_path, target_path):
        subprocess.run(["ln", "-s", source_path, target_path])

    def link(self, *files):
        if len(files) != 0:
            self._source_files = files

        self._symlink_handler(self._source_files, self._link)

    @staticmethod
    def _unlink(_, target_path):
        subprocess.run(["unlink", target_path])

    def unlink(self, *files):
        if len(files) != 0:
            self._source_files = files

        self._symlink_handler(self._source_files, self._unlink)


def main():
    fire.Fire(Dotfiles)


if __name__ == '__main__':
    main()
