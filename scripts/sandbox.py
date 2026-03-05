import subprocess
import sys
import argparse
import os

def run_command(cmd: str):
    print(f"Executing: {cmd}")
    return subprocess.run(cmd, shell=True)

def run_tests(parallel: int = 4):
    cmd = f"pytest -n {parallel} --alluredir=allure-results tests/"
    run_command(cmd)

def main():
    parser = argparse.ArgumentParser(description="Petstore API Framework Sandbox CLI")
    parser.add_argument("action", choices=["test", "report"])
    parser.add_argument("--workers", type=int, default=4)
    
    args = parser.parse_args()
    
    if args.action == "test":
        run_tests(args.workers)
    elif args.action == "report":
        run_command("allure serve allure-results")

if __name__ == "__main__":
    main()
