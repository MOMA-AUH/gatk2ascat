from contextlib import redirect_stdout
from io import StringIO
import unittest

from gatk2ascat import __version__
from gatk2ascat import client


class TestCLI(unittest.TestCase):

    def test_version(self):
        stdout = StringIO()
        with redirect_stdout(stdout):
            with self.assertRaisesRegex(SystemExit, "0"):
                client.main(["--version"])

        self.assertEqual(stdout.getvalue(), f"gatk2ascat {__version__}\n")

    def test_help(self):
        stdout = StringIO()
        with redirect_stdout(stdout):
            with self.assertRaisesRegex(SystemExit, "0"):
                client.main(["--help"])

        self.assertIn("usage: gatk2ascat", stdout.getvalue())
