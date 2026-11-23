import subprocess
import sys
import unittest
from pathlib import Path


SCRIPT = Path(__file__).with_name("base64_encoder.py")


class Base64EncoderCliTests(unittest.TestCase):
    def run_script(self, *args):
        return subprocess.run(
            [sys.executable, str(SCRIPT), *args],
            capture_output=True,
            text=True,
        )

    def test_encode_and_decode(self):
        for operation, value, expected in (
            ("encode", "Hello, World!", "SGVsbG8sIFdvcmxkIQ=="),
            ("decode", "SGVsbG8sIFdvcmxkIQ==", "Hello, World!"),
            ("encode", "café", "Y2Fmw6k="),
            ("decode", "Y2Fmw6k=", "café"),
            ("encode", "", ""),
        ):
            with self.subTest(operation=operation, value=value):
                result = self.run_script(operation, value)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(result.stdout, expected + "\n")

    def test_invalid_arguments_and_input(self):
        for args in ((), ("encode",), ("other", "value"), ("decode", "%%%"), ("decode", "/w==")):
            with self.subTest(args=args):
                result = self.run_script(*args)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("error:", result.stderr)


if __name__ == "__main__":
    unittest.main()
