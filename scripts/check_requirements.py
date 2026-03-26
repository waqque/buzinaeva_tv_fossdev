import ast
import sys
from pathlib import Path

def get_imports(filepath):
    imports = set()
    try:
        with open(filepath) as f:
            tree = ast.parse(f.read())
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    imports.add(alias.name.split('.')[0])
            elif isinstance(node, ast.ImportFrom) and node.module:
                imports.add(node.module.split('.')[0])
    except Exception:
        pass
    return imports

def get_requirements():
    reqs = set()
    with open('requirements.txt') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#'):
                reqs.add(line.split('==')[0].split('>=')[0].split('>')[0].strip().lower())
    return reqs

def main():
    src_dir = Path('src')
    all_imports = set()
    
    for py_file in src_dir.glob('*.py'):
        all_imports.update(get_imports(py_file))
    
    stdlib = {'os', 'sys', 'json', 're', 'datetime', 'math', 'random', 'pathlib', 'typing', 'argparse', 'logging'}
    third_party = {imp for imp in all_imports if imp not in stdlib}
    
    requirements = get_requirements()
    missing = third_party - requirements
    
    if missing:
        print("Missing in requirements.txt:", ', '.join(sorted(missing)))
        sys.exit(1)
    
    print("All imports declared in requirements.txt")
    sys.exit(0)

if __name__ == "__main__":
    main()