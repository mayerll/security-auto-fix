
# Security Dependency Auto Fix Tool

A lightweight security automation tool that scans Python dependencies for known vulnerabilities and automatically applies safe remediation when safe versions are available.

Repository:  
https://github.com/mayerll/security-auto-fix

---

# Features

- Dependency vulnerability scanning
- Automatic remediation of vulnerable dependencies
- Dry-run mode to preview fixes
- JSON output for automation or CI/CD
- Rollback support for patches
- Basic test coverage
- Docker support
- CI/CD integration
- Readable security reports
- Simple CLI interface

---

# Architecture Overview

The tool workflow:

1. Scan dependencies in `requirements.txt`
2. Detect vulnerabilities with pip-audit
3. Generate readable report or JSON
4. Automatically upgrade vulnerable packages
5. Dry-run mode for preview
6. Rollback support to restore backup

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

---

# Installation

Clone the repository:

```bash
git clone https://github.com/mayerll/security-auto-fix.git
cd security-auto-fix
pip install pip-audit pytest
