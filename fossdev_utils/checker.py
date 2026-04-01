import ast
import subprocess
import sys
from pathlib import Path

def check_imports(src_dir="src"):
    imports = set()
    src_path = Path(src_dir)
    
    if not src_path.exists():
        return {"status": "error", "message": f"Directory {src_dir} not found"}
    
    for py_file in src_path.glob("*.py"):
        try:
            with open(py_file) as f:
                tree = ast.parse(f.read())
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        imports.add(alias.name.split('.')[0])
                elif isinstance(node, ast.ImportFrom) and node.module:
                    imports.add(node.module.split('.')[0])
        except Exception:
            continue
    
    stdlib = {'os', 'sys', 'json', 're', 'datetime', 'math', 'random', 'pathlib', 'typing'}
    third_party = {imp for imp in imports if imp not in stdlib}
    
    req_path = Path("requirements.txt")
    if not req_path.exists():
        return {"status": "error", "message": "requirements.txt not found"}
    
    requirements = set()
    with open(req_path) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#'):
                requirements.add(line.split('==')[0].split('>=')[0].split('>')[0].strip().lower())
    
    missing = third_party - requirements
    
    if missing:
        return {"status": "fail", "missing": list(missing)}
    
    return {"status": "ok"}

def run_typecheck(src_dir="src"):
    result = subprocess.run(
        [sys.executable, "-m", "mypy", src_dir],
        capture_output=True,
        text=True
    )
    return {
        "status": "ok" if result.returncode == 0 else "fail",
        "output": result.stdout + result.stderr
    }

def run_lint(src_dir="src"):
    result = subprocess.run(
        [sys.executable, "-m", "flake8", src_dir],
        capture_output=True,
        text=True
    )
    return {
        "status": "ok" if result.returncode == 0 else "fail",
        "output": result.stdout + result.stderr
    }

def format_code(src_dir="src"):
    result = subprocess.run(
        [sys.executable, "-m", "black", src_dir],
        capture_output=True,
        text=True
    )
    return {
        "status": "ok" if result.returncode == 0 else "fail",
        "output": result.stdout + result.stderr
    }

class Project:
    def __init__(self, name, version="0.1.0"):
        self.name = name
        self.version = version
    
    def info(self):
        return {
            "name": self.name,
            "version": self.version,
            "status": "ready"
        }
