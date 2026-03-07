import subprocess
import json
import os

def scan_dependencies(path):
    """Scan Python dependencies using pip-audit and return structured results"""

    cmd = ["pip-audit", "-r", f"{path}/requirements.txt", "-f", "json"]

    try:
        output = subprocess.check_output(cmd, stderr=subprocess.DEVNULL)
        audit_results = json.loads(output)
    except subprocess.CalledProcessError:
        return {"dependencies": []}

    results = {"dependencies": []}

    for dep in audit_results.get("dependencies", []):
        results["dependencies"].append({
            "name": dep["name"],
            "version": dep["version"],
            "vulns": [
                {
                    "id": v["id"],
                    "fix_versions": v.get("fix_versions", [])
                }
                for v in dep.get("vulns", [])
            ]
        })

    return results
