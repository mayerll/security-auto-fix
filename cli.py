
import sys
from scanner.dependency_scanner import scan_requirements
from reporter.report import print_report

def main():
    if len(sys.argv) != 3 or sys.argv[1] != "scan":
        print("Usage: python3 cli.py scan <project_path>")
        sys.exit(1)

    target_path = sys.argv[2]
    report = scan_requirements(target_path)
    print_report(report)

if __name__ == "__main__":
    main()
