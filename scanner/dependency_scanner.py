import subprocess
import json

def scan_dependencies(path):

    result = subprocess.run(
        ["pip-audit", "-r", f"{path}/requirements.txt", "-f", "json"],
        capture_output=True,
        text=True
    )

    return json.loads(result.stdout)
