import os
from scanner import scan_directory
from report import generate_report

def main():
    # Directory to scan
    target_dir = os.path.join(os.path.dirname(__file__), '..', 'data', 'sample-code')
    print(f"[+] Scanning directory: {target_dir}")

    # Run the scanner
    findings = scan_directory(target_dir)

    # Generate report
    report_path = generate_report(findings)
    print(f"[+] Scan complete. Report saved to: {report_path}")

if __name__ == "__main__":
    main()