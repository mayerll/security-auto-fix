
import unittest
from scanner.dependency_scanner import scan_requirements

class TestScanner(unittest.TestCase):
    def test_scan_empty_dir(self):
        report = scan_requirements("./nonexistent_dir")
        self.assertEqual(report, {"dependencies": [], "fixes": []})

    def test_scan_sample_requirements(self):
        report = scan_requirements("./sample_project/requirements.txt")
        self.assertIn("dependencies", report)
        self.assertIn("fixes", report)

if __name__ == "__main__":
    unittest.main()
