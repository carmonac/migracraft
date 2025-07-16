#!/usr/bin/env python3
"""
Test runner script for the PostgreSQL Schema Migration Tool.
"""

import subprocess
import sys
import os
from pathlib import Path


def run_tests():
    """Run all tests with coverage reporting"""
    print("🧪 Running PostgreSQL Schema Migration Tool Tests...")
    print("=" * 60)
    
    # Get project root directory
    project_root = Path(__file__).parent.absolute()
    os.chdir(project_root)
    
    # Add project root to Python path
    sys.path.insert(0, str(project_root))
    
    try:
        # Run pytest with coverage
        cmd = [
            sys.executable, "-m", "pytest",
            "tests/",
            "-v",
            "--tb=short",
            "--cov=migracraft",
            "--cov-report=html",
            "--cov-report=term-missing",
            "--cov-fail-under=70"
        ]
        
        print(f"Running command: {' '.join(cmd)}")
        print("=" * 60)
        
        result = subprocess.run(cmd, cwd=project_root)
        
        print("\n" + "=" * 60)
        if result.returncode == 0:
            print("✅ All tests passed!")
            print("📊 Coverage report generated in htmlcov/index.html")
        else:
            print("❌ Some tests failed or coverage is below threshold!")
            return False
            
    except FileNotFoundError:
        print("❌ pytest not found! Please install it with:")
        print("   pip install pytest pytest-cov")
        return False
    except Exception as e:
        print(f"❌ Error running tests: {e}")
        return False
    
    return True


def run_specific_test(test_file):
    """Run a specific test file"""
    project_root = Path(__file__).parent.absolute()
    
    cmd = [
        sys.executable, "-m", "pytest",
        f"tests/{test_file}",
        "-v", "-s"
    ]
    
    print(f"Running specific test: {test_file}")
    result = subprocess.run(cmd, cwd=project_root)
    return result.returncode == 0


def main():
    """Main function to handle command line arguments"""
    if len(sys.argv) == 1:
        # Run all tests
        success = run_tests()
        sys.exit(0 if success else 1)
    elif len(sys.argv) == 2:
        # Run specific test file
        test_file = sys.argv[1]
        if not test_file.startswith("test_"):
            test_file = f"test_{test_file}"
        if not test_file.endswith(".py"):
            test_file = f"{test_file}.py"
        
        success = run_specific_test(test_file)
        sys.exit(0 if success else 1)
    else:
        print("Usage:")
        print("  python run_tests.py                    # Run all tests")
        print("  python run_tests.py test_validation    # Run specific test")
        print("  python run_tests.py differential       # Run differential migration tests")
        sys.exit(1)


if __name__ == "__main__":
    main()
