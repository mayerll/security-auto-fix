
import os
import shutil
from fixer.dependency_fixer import fix_dependencies

TEST_PATH = "tests/sample_project_test"

def setup_module(module):
    os.makedirs(TEST_PATH, exist_ok=True)
    with open(f"{TEST_PATH}/requirements.txt", "w") as f:
        f.write("flask==1.0\n")

def teardown_module(module):
    shutil.rmtree(TEST_PATH)

def test_fix_dependencies():
    scan_results = {
        "dependencies": [
            {
                "name": "flask",
                "version": "1.0",
                "vulns": [{"id": "CVE-2023-30861", "fix_versions": ["2.2.5"]}]
            }
        ]
    }
    fix_dependencies(scan_results, TEST_PATH, dry_run=True)
