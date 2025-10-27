#!/usr/bin/env python3
"""
Mini E-Kart Testing Framework Setup and Execution Script
This script handles the complete setup and execution of Selenium + Cucumber tests
"""

import os
import sys
import subprocess
import time
from pathlib import Path


class TestFrameworkSetup:
    """
    Handles setup and execution of the Mini E-Kart testing framework
    """
    
    def __init__(self):
        """Initialize the test framework setup"""
        self.project_root = Path.cwd()
        self.reports_dir = self.project_root / "reports"
        self.features_dir = self.project_root / "features"
        
    def check_python_version(self):
        """Check if Python version is compatible"""
        if sys.version_info < (3, 7):
            print("❌ Python 3.7 or higher is required")
            sys.exit(1)
        print(f"✅ Python {sys.version.split()[0]} detected")
    
    def install_dependencies(self):
        """Install required Python packages"""
        print("📦 Installing dependencies...")
        try:
            subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], 
                          check=True, capture_output=True, text=True)
            print("✅ Dependencies installed successfully")
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to install dependencies: {e}")
            sys.exit(1)
    
    def check_chrome_driver(self):
        """Check if Chrome WebDriver is available"""
        print("🔍 Checking Chrome WebDriver...")
        try:
            from selenium import webdriver
            from selenium.webdriver.chrome.options import Options
            
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            
            driver = webdriver.Chrome(options=chrome_options)
            driver.quit()
            print("✅ Chrome WebDriver is working")
        except Exception as e:
            print(f"❌ Chrome WebDriver issue: {e}")
            print("💡 Please install Chrome and ChromeDriver")
            sys.exit(1)
    
    def create_directories(self):
        """Create necessary directories"""
        print("📁 Creating directories...")
        self.reports_dir.mkdir(exist_ok=True)
        print("✅ Directories created")
    
    def run_tests(self):
        """Execute all Cucumber tests"""
        print("🚀 Starting test execution...")
        print("="*60)
        
        try:
            # Run behave with detailed output
            cmd = [
                sys.executable, "-m", "behave",
                "features/",
                "--format=pretty",
                "--format=json.pretty",
                "--outfile=reports/behave_results.json",
                "--no-capture",
                "--no-capture-stderr"
            ]
            
            print("Executing command:", " ".join(cmd))
            print()
            
            # Run the tests
            result = subprocess.run(cmd, cwd=self.project_root, 
                                  capture_output=True, text=True)
            
            # Save output to file
            with open(self.reports_dir / "behave_output.txt", "w") as f:
                f.write(result.stdout)
                if result.stderr:
                    f.write("\nSTDERR:\n")
                    f.write(result.stderr)
            
            # Print output to console
            print(result.stdout)
            if result.stderr:
                print("STDERR:")
                print(result.stderr)
            
            print("="*60)
            print(f"Test execution completed with exit code: {result.returncode}")
            
            return result.returncode == 0
            
        except Exception as e:
            print(f"❌ Error running tests: {e}")
            return False
    
    def generate_summary(self):
        """Generate test summary report"""
        print("📊 Generating test summary...")
        try:
            summary_script = self.project_root / "reports" / "test_summary.py"
            subprocess.run([sys.executable, str(summary_script)], check=True)
        except Exception as e:
            print(f"❌ Error generating summary: {e}")
    
    def setup_and_run(self):
        """Complete setup and test execution"""
        print("🎯 Mini E-Kart Testing Framework Setup")
        print("="*50)
        
        # Setup steps
        self.check_python_version()
        self.install_dependencies()
        self.check_chrome_driver()
        self.create_directories()
        
        print("\n✅ Setup completed successfully!")
        print("\n🚀 Starting test execution...")
        
        # Run tests
        success = self.run_tests()
        
        # Generate summary
        self.generate_summary()
        
        # Final status
        if success:
            print("\n🎉 All tests completed successfully!")
        else:
            print("\n⚠️ Some tests failed. Check the reports for details.")
        
        print(f"\n📁 Reports saved in: {self.reports_dir}")
        print("📄 Check 'behave_output.txt' for detailed test results")
        print("📊 Check 'test_summary_report.txt' for summary statistics")


def main():
    """Main function"""
    setup = TestFrameworkSetup()
    setup.setup_and_run()


if __name__ == "__main__":
    main()

