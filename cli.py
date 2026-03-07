#!/usr/bin/env python3
import argparse
from scanner.dependency_scanner import scan_dependencies
from fixer.dependency_fixer import fix_dependencies
from reporter.report import print_report, print_json_report

parser = argparse.ArgumentParser(description="Security Dependency Auto Fix Tool")

parser.add_argument("command", choices=["scan", "fix"])
parser.add_argument("path", help="Path to project to scan")
parser.add_argument("--dry-run", action="store_true", help="Show what would be fixed without applying changes")
parser.add_argument("--json", action="store_true", help="Output results in JSON format")

args = parser.parse_args()

results = scan_dependencies(args.path)

if args.command == "scan":
    if args.json:
        print_json_report(results)
    else:
        print_report(results)

elif args.command == "fix":
    if args.json:
        print_json_report(results)
    else:
        print_report(results)

    fix_dependencies(results, args.path, dry_run=args.dry_run)
