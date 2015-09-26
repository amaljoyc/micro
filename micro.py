import curses


class MicroEditor:

    def __init__(self):
        self.window = curses.initscr()
        curses.noecho()
        self.window.addstr("Welcome to micro text editor!!\n\n")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        curses.endwin()

    def edit(self):
        while True:
            key = self.window.getch()
            if key == ord("q"):
                break
            elif key == 127:
                y, x = self.window.getyx()
                self.window.delch(y, x-1)
            else:
                self.window.addch(chr(key))


if __name__ == '__main__':
    with MicroEditor() as micro:
        micro.edit()
