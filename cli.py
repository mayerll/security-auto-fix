
import argparse
import json
from scanner.dependency_scanner import scan_requirements
from reporter.report import print_report

def apply_fixes(report, dry_run=True):
    applied = []
    for dep in report.get("dependencies", []):
        for vuln in dep.get("vulns", []):
            for fix_version in vuln.get("fix_versions", []):
                action = "{} -> {}".format(dep['name'], fix_version)
                if dry_run:
                    print("[DRY-RUN] Would apply: {}".format(action))
                else:
                    print("Applying: {}".format(action))
                    applied.append(action)
    return applied

def rollback_fixes(applied):
    for action in reversed(applied):
        print("Rolling back: {}".format(action))

def main():
    parser = argparse.ArgumentParser(description="Python Dependency Security Scanner")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Scan subcommand
    scan_parser = subparsers.add_parser("scan", help="Scan a project for vulnerabilities")
    scan_parser.add_argument("scan_path", help="Path to project or requirements.txt")
    scan_parser.add_argument("--json", action="store_true", help="Output results as JSON")
    scan_parser.add_argument("--dry-run", action="store_true", help="Simulate fixes without applying")
    scan_parser.add_argument("--rollback", action="store_true", help="Rollback applied fixes")

    args = parser.parse_args()

    if args.command == "scan":
        report = scan_requirements(args.scan_path)

        if args.json:
            print(json.dumps(report, indent=2))
        else:
            print_report(report)

        applied = []
        if report.get("fixes") and not args.rollback:
            applied = apply_fixes(report, dry_run=args.dry_run)

        if args.rollback and applied:
            rollback_fixes(applied)

if __name__ == "__main__":
    main()
