
def fix_dependencies(scan_results, path, dry_run=False):
    requirements_file = f"{path}/requirements.txt"

    # 读取当前 requirements.txt
    with open(requirements_file, "r") as f:
        lines = f.readlines()

    updated_lines = lines.copy()
    changes = []

    for dep in scan_results.get("dependencies", []):
        vulns = dep.get("vulns", [])
        if vulns:
            pkg = dep["name"]
            fixed_version = vulns[0]["fix_versions"][0] if vulns[0]["fix_versions"] else None
            if fixed_version:
                for i, line in enumerate(updated_lines):
                    if line.startswith(f"{pkg}==") or line.startswith(f"{pkg}>="):
                        updated_lines[i] = f"{pkg}=={fixed_version}\n"
                        changes.append(f"{pkg}: {line.strip()} -> {pkg}=={fixed_version}")

    if dry_run:
        print("Dry-run mode: The following changes would be applied:")
        for change in changes:
            print(change)
    else:
        with open(requirements_file, "w") as f:
            f.writelines(updated_lines)
        for change in changes:
            print(f"Applied fix: {change}")

    if not changes:
        print("No vulnerable dependencies found or nothing to fix.")
