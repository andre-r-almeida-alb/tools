import subprocess
import sys
import unittest
from pathlib import Path


SCRIPT = Path(__file__).with_name("b64.py")


class Base64EncoderCliTests(unittest.TestCase):
    def run_script(self, *args):
        return subprocess.run(
            [sys.executable, str(SCRIPT), *args],
            capture_output=True,
            text=True,
        )

    def test_encode_and_decode(self):
        for operation, value, expected in (
            ("e", "Hello, World!", "SGVsbG8sIFdvcmxkIQ=="),
            ("d", "SGVsbG8sIFdvcmxkIQ==", "Hello, World!"),
            ("e", "café", "Y2Fmw6k="),
            ("d", "Y2Fmw6k=", "café"),
            ("e", "", ""),
        ):
            with self.subTest(operation=operation, value=value):
                result = self.run_script(operation, value)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(result.stdout, "\n" + expected + "\n")

    def test_invalid_arguments_and_input(self):
        for args in ((), ("e",), ("other", "value"), ("d", "%%%"), ("d", "/w==")):
            with self.subTest(args=args):
                result = self.run_script(*args)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("error:", result.stderr)


if __name__ == "__main__":
    unittest.main()
