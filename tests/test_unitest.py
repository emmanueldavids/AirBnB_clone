#!/usr/bin/python3

from console import Shell
import sys
import unittest


class testUnitest(unittest.TestCase):
    def test_shell(self):
        self.assertTrue(Shell.do_EOF(self, True))

    def test_shellconsole(self):
        self.assertTrue(Shell.do_quit(self, True))


if __name__ == '__main__':
    unittest.main()
