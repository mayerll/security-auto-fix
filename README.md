
# Security Dependency Auto Fix Tool

A lightweight security automation tool that scans Python dependencies for known vulnerabilities and automatically applies safe remediation when safe versions are available.

Repository:
https://github.com/mayerll/security-auto-fix

---

# Features

* Dependency vulnerability scanning
* Automatic remediation of vulnerable dependencies
* Dry-run mode to preview fixes
* JSON output for automation or CI/CD
* Readable security reports
* Simple CLI interface
* Local execution with minimal setup

---

# Architecture Overview

The tool performs the following workflow:

1. Scan Python dependencies in a `requirements.txt`
2. Detect vulnerabilities using pip-audit
3. Produce a readable security report (or JSON)
4. Automatically upgrade vulnerable packages when safe
5. Optionally run in dry-run mode to preview changes

## Workflow Diagram

```text
+----------------+
| User Project   |
| requirements.txt|
+--------+-------+
         |
         v
+--------------------+
| Dependency Scanner  |
|  (pip-audit)       |
+--------+-----------+
         |
         v
+--------------------+
| Security Findings   |
| (vulnerable deps)  |
+--------+-----------+
         |
         v
+--------------------+
| Report Generator   |
| (CLI & JSON)       |
+--------+-----------+
         |
         v
+--------------------+
| Auto Remediation   |
| (update requirements.txt)
| Dry-run optional   |
+--------------------+
```

---

# Project Structure

```text
security-auto-fix/
│
├── cli.py
├── scanner/
│   ├── __init__.py
│   └── dependency_scanner.py
├── fixer/
│   ├── __init__.py
│   └── dependency_fixer.py
├── reporter/
│   ├── __init__.py
│   └── report.py
├── sample_project/
│   └── requirements.txt
├── .github/workflows/security-scan.yml
├── README.md
└── design.md
```

---

# Requirements

* Python 3.8 or newer
* pip
* pip-audit

Install pip-audit:

```bash
pip install pip-audit
```

---

# Usage

## Scan for vulnerabilities

```bash
python3 cli.py scan ./sample_project
```

Example output:

```text
SECURITY REPORT
================

Package: flask
Installed Version: 1.0
Vulnerability ID: CVE-2023-30861
Fix Versions: 2.2.5
----------------------------------------
```

## JSON output

```bash
python3 cli.py scan ./sample_project --json
```

Produces structured JSON results, e.g., for CI:

```json
{
  "dependencies": [
    {
      "name": "flask",
      "version": "1.0",
      "vulns": [
        {
          "id": "CVE-2023-30861",
          "fix_versions": ["2.2.5"]
        }
      ]
    }
  ]
}
```

## Automatically fix vulnerable dependencies

```bash
python3 cli.py fix ./sample_project
```

## Dry-run mode

Preview changes without modifying files:

```bash
python3 cli.py fix ./sample_project --dry-run
```

Output example:

```text
Dry-run mode: The following changes would be applied:
flask: flask==1.0 -> flask==2.2.5
```

---

# Example Vulnerable Project

`sample_project/requirements.txt` contains:

```text
flask==1.0
urllib3==1.25
django==2.2
```

---

# CI/CD Example

The project includes a GitHub Actions workflow `.github/workflows/security-scan.yml`:

* Automatically scans dependencies on push or pull request
* Produces JSON security report
* Can be extended to fail build or open PRs with fixes

---

# Limitations

* Only Python dependencies (`requirements.txt`) supported
* Selects first available fixed version
* Dependency compatibility not validated

---

# Future Improvements

* Support Poetry / Pipenv / npm / yarn
* Secret scanning
* Container image scanning
* Rollback support
* Web dashboard for vulnerability visualization
* CI integration with automatic PR for fixes

---

# Purpose

Demonstrates automated security workflows for dependency management:

* Detect vulnerabilities
* Generate clear reports
* Apply safe remediation
* Integrate with CI/CD pipelines

---

# License

Educational and demonstration purposes

