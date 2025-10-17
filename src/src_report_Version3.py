import os
import datetime

def generate_report(findings):
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    report_path = os.path.join(os.path.dirname(__file__), f'../scan_report_{timestamp}.md')
    with open(report_path, 'w') as f:
        f.write(f"# Vulnerability Scan Report\nGenerated: {timestamp}\n\n")
        if not findings:
            f.write("No vulnerabilities found.\n")
            return report_path
        for item in findings:
            f.write(f"## {item['type']}\n")
            f.write(f"- **File:** {item['file']}\n")
            f.write(f"- **Line:** {item['line']}\n")
            f.write(f"- **Snippet:** `{item['snippet']}`\n\n")
    return report_path