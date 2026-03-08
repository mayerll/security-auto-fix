
def print_report(report):
    print("\nSECURITY REPORT")
    print("=" * 20)

    if not report.get("dependencies"):
        print("No vulnerabilities found or scan failed.")
        return

    for dep in report["dependencies"]:
        print(f"- {dep['name']}=={dep['version']}")
        for vuln in dep.get("vulns", []):
            print(f"  * {vuln.get('id')}: {vuln.get('description')}")
            if vuln.get("fix_versions"):
                fixes = ", ".join(vuln["fix_versions"])
                print(f"    → Fix available in: {fixes}")

    if report.get("fixes"):
        print("\nApplied Fixes:")
        for fix in report["fixes"]:
            print(f"- {fix}")
