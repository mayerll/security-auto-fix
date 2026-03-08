
import subprocess
import json
import os
import sys


def scan_requirements(target_path):
    """
    Scan a Python project for vulnerabilities using pip-audit.
    Returns a report dictionary with 'dependencies' and 'fixes'.
    """
    report = {"dependencies": [], "fixes": []}

    # Determine requirements.txt path
    req_file = target_path
    if os.path.isdir(target_path):
        req_file = os.path.join(target_path, "requirements.txt")

    if not os.path.isfile(req_file):
        print(f"No requirements.txt found at {req_file}", file=sys.stderr)
        return report

    cmd = ["pip-audit", "-r", req_file, "-f", "json"]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True)

        # Parse JSON output
        data = []
        if result.stdout:
            try:
                parsed = json.loads(result.stdout)

                # Handle new pip-audit structure: {"dependencies": [...]}
                if isinstance(parsed, dict) and "dependencies" in parsed:
                    data = parsed["dependencies"]
                elif isinstance(parsed, list):
                    data = parsed
                else:
                    print(f"Unexpected JSON structure: {parsed}", file=sys.stderr)

            except json.JSONDecodeError as e:
                print(f"Error decoding JSON output: {e}", file=sys.stderr)

        # Populate report
        for dep in data:
            if isinstance(dep, dict):
                dep_entry = {
                    "name": dep.get("name"),
                    "version": dep.get("version"),
                    "vulns": []
                }
                for vuln in dep.get("vulns", []):
                    if isinstance(vuln, dict):
                        dep_entry["vulns"].append({
                            "id": vuln.get("id"),
                            "description": vuln.get("description"),
                            "fix_versions": vuln.get("fix_versions", [])
                        })
                        # Collect fixes
                        if vuln.get("fix_versions"):
                            for fix_version in vuln["fix_versions"]:
                                report["fixes"].append(f"{dep.get('name')} → {fix_version}")
                report["dependencies"].append(dep_entry)

        # Status messages
        if result.returncode == 0:
            print("No vulnerabilities Found", file=sys.stdout)
        elif result.returncode == 1:
            print("Vulnerabilities Found", file=sys.stderr)
        else:
            print(f"pip-audit returned exit code {result.returncode}", file=sys.stderr)
            if result.stderr:
                print(result.stderr, file=sys.stderr)

    except FileNotFoundError:
        print("pip-audit CLI not found. Install it with `pip install pip-audit`.", file=sys.stderr)
    except Exception as e:
        print(f"Error running pip-audit: {e}", file=sys.stderr)

    return report
