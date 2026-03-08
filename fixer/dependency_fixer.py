
import subprocess
import sys

def apply_fixes(report, target_path):
    """
    Apply fixes for vulnerable packages found in the report.
    Returns updated report with 'fixes' applied.
    """
    if not report.get("dependencies"):
        return report

    fixes_applied = []

    for dep in report["dependencies"]:
        for vuln in dep.get("vulns", []):
            if vuln.get("fix_versions"):
                latest_fix = vuln["fix_versions"][-1]
                try:
                    cmd = [sys.executable, "-m", "pip", "install", f"{dep['name']}=={latest_fix}"]
                    subprocess.run(cmd, check=True)
                    fixes_applied.append(f"{dep['name']} -> {latest_fix}")
                except subprocess.CalledProcessError as e:
                    print(f"Failed to upgrade {dep['name']} to {latest_fix}: {e}")

    report["fixes"] = fixes_applied
    return report

