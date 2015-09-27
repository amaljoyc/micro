import curses
import sys


class MicroEditor:

    def __init__(self):
        self.window = curses.initscr()
        curses.noecho()
        self.window.keypad(1)
        self.window.addstr('Welcome to micro text editor!!\n\n')

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        curses.endwin()

    def edit(self):
        while True:
            key = self.window.getch()
            if key == 27:
                cmd = self.window.getch()
                if cmd == ord('q'):  # To quit: (ESC and q) OR (ALT + q)
                    break
                elif cmd == ord('s'):  # To save: (ESC and s) OR (ALT + s)
                    self.save()

            elif key == curses.KEY_BACKSPACE:
                y, x = self.window.getyx()
                self.window.delch(y, x-1)

            elif key < 127:
                self.window.addch(chr(key))

    def save(self):
        y, x = self.window.getmaxyx()
        f = open(self.get_filename(), 'w')
        for y in range(y):
            f.write(self.window.instr(y, 0).rstrip())
            f.write('\n')
        f.close()

    def get_filename(self):
        if(len(sys.argv)) > 1:
            return sys.argv[1]
        else:
            return 'untitled.txt'


if __name__ == '__main__':
    with MicroEditor() as micro:
        micro.edit()
