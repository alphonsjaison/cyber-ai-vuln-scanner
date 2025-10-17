import os
import re

def scan_file(filepath):
    findings = []
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        for i, line in enumerate(f, 1):
            # Example rule: Detect hardcoded passwords
            if re.search(r'(password|passwd|pwd)\s*=\s*[\'"].+[\'"]', line, re.IGNORECASE):
                findings.append({
                    'file': filepath,
                    'line': i,
                    'type': 'Hardcoded Password',
                    'snippet': line.strip()
                })
    return findings

def scan_directory(directory):
    all_findings = []
    for root, _, files in os.walk(directory):
        for fname in files:
            if fname.endswith('.py'):
                fpath = os.path.join(root, fname)
                all_findings.extend(scan_file(fpath))
    return all_findings