import argparse
import sys
from fossdev_utils.checker import check_imports, run_typecheck, run_lint, format_code, Project

def main():
    parser = argparse.ArgumentParser(description="FOSSDEV Automation Tools")
    parser.add_argument("command", choices=["check", "typecheck", "lint", "format", "info"],
                       help="Command to execute")
    parser.add_argument("--src", default="src", help="Source directory")
    
    args = parser.parse_args()
    
    if args.command == "check":
        result = check_imports(args.src)
        if result["status"] == "ok":
            print("All imports declared in requirements.txt")
            sys.exit(0)
        else:
            print("Missing dependencies:", result.get("missing", []))
            sys.exit(1)
    
    elif args.command == "typecheck":
        result = run_typecheck(args.src)
        print(result["output"])
        sys.exit(0 if result["status"] == "ok" else 1)
    
    elif args.command == "lint":
        result = run_lint(args.src)
        print(result["output"])
        sys.exit(0 if result["status"] == "ok" else 1)
    
    elif args.command == "format":
        result = format_code(args.src)
        print(result["output"])
        sys.exit(0 if result["status"] == "ok" else 1)
    
    elif args.command == "info":
        proj = Project("fossdev-automation")
        print(proj.info())

if __name__ == "__main__":
    main()
