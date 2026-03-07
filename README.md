# Security Dependency Auto Fix Tool

A lightweight security automation tool that scans Python dependencies
for known vulnerabilities and automatically applies safe remediation
when safe versions are available.

Repository:\
https://github.com/mayerll/security-auto-fix

------------------------------------------------------------------------

# Features

-   Dependency vulnerability scanning
-   Automatic remediation of vulnerable dependencies
-   Dry-run mode to preview fixes
-   JSON output for automation or CI/CD
-   Rollback support for patches
-   Basic test coverage
-   Docker support
-   CI/CD integration
-   Readable security reports
-   Simple CLI interface

------------------------------------------------------------------------

# Architecture Overview

The tool workflow:

1.  Scan dependencies in `requirements.txt`
2.  Detect vulnerabilities with pip-audit
3.  Generate readable report or JSON
4.  Automatically upgrade vulnerable packages
5.  Dry-run mode for preview
6.  Rollback support to restore backup

## Workflow Diagram

    +-------------------+
    | User Project      |
    | requirements.txt  |
    +---------+---------+
              |
              v
    +-------------------+
    | Dependency Scanner|
    |  (pip-audit)      |
    +---------+---------+
              |
              v
    +-------------------+
    | Security Findings |
    | (vulnerable deps) |
    +---------+---------+
              |
              v
    +-------------------+
    | Report Generator  |
    | (CLI & JSON)      |
    +---------+---------+
              |
              v
    +-------------------+
    | Auto Remediation  |
    | - update deps     |
    | - dry-run optional|
    | - rollback option |
    +-------------------+

------------------------------------------------------------------------

# Installation

Clone the repository:

``` bash
git clone https://github.com/mayerll/security-auto-fix.git
cd security-auto-fix
pip install pip-audit pytest
```

------------------------------------------------------------------------

# Usage

## Scan for vulnerabilities

``` bash
python3 cli.py scan ./sample_project
```

## JSON output

``` bash
python3 cli.py scan ./sample_project --json
```

## Automatically fix vulnerable dependencies

``` bash
python3 cli.py fix ./sample_project
```

## Dry-run mode

Preview changes without modifying files.

``` bash
python3 cli.py fix ./sample_project --dry-run
```

## Rollback to previous state

Restore previous `requirements.txt` from backup.

``` bash
python3 cli.py fix ./sample_project --rollback
```

------------------------------------------------------------------------

# Docker Support

Build and run container:

``` bash
docker build -t security-auto-fix .
docker run --rm -v $(pwd)/sample_project:/app/sample_project security-auto-fix scan ./sample_project
```

------------------------------------------------------------------------

# Test Coverage

Run basic tests:

``` bash
pytest tests/
```

------------------------------------------------------------------------

# CI/CD Example

GitHub Actions workflow automatically:

-   Scans dependencies on push or pull request
-   Produces JSON security report
-   Runs tests
-   Can fail build if vulnerabilities are detected

Example workflow file: `.github/workflows/security-scan.yml`

``` yaml
name: Dependency Security Scan

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  scan:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: 3.10

      - name: Install dependencies
        run: pip install pip-audit pytest

      - name: Run security scan
        run: python3 cli.py scan ./sample_project --json > security_report.json

      - name: Run tests
        run: pytest tests/

      - name: Upload security report
        uses: actions/upload-artifact@v3
        with:
          name: security-report
          path: security_report.json
```

------------------------------------------------------------------------

# Limitations

-   Only Python dependencies (`requirements.txt`) supported
-   Selects the first available fixed version
-   Dependency compatibility is not validated

------------------------------------------------------------------------

# Future Improvements

-   Support Poetry / Pipenv / npm / yarn
-   Secret scanning
-   Container / Dockerfile scanning
-   Rollback with version history
-   Web dashboard for vulnerability visualization
