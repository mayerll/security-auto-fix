
import json

def print_report(results):
    print("\nSECURITY REPORT")
    print("================\n")
    for dep in results.get("dependencies", []):
        vulns = dep.get("vulns", [])
        if vulns:
            for v in vulns:
                print(f"Package: {dep['name']}")
                print(f"Installed Version: {dep['version']}")
                print(f"Vulnerability ID: {v['id']}")
                print(f"Fix Versions: {', '.join(v['fix_versions'])}")
                print("-" * 40)

def print_json_report(results):
    print(json.dumps(results, indent=2))
