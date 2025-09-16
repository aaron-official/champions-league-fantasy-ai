#!/usr/bin/env python3
"""
Champions League Fantasy AI - Quick Start Script
This script provides a simple way to get started with the system
"""

import os
import sys
import subprocess
from pathlib import Path

def print_banner():
    """Print welcome banner"""
    print("🏆" + "="*60 + "🏆")
    print("   Champions League Fantasy AI - Quick Start")
    print("🏆" + "="*60 + "🏆")
    print()

def check_python_version():
    """Check if Python version is compatible"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 10):
        print("❌ Python 3.10+ is required. Current version:", f"{version.major}.{version.minor}")
        return False
    print(f"✅ Python {version.major}.{version.minor} detected")
    return True

def check_dependencies():
    """Check if required packages are installed"""
    try:
        import crewai
        print("✅ CrewAI is installed")
        return True
    except ImportError:
        print("❌ CrewAI not found")
        return False

def check_env_file():
    """Check if .env file exists and is configured"""
    env_file = Path(".env")
    if not env_file.exists():
        print("❌ .env file not found")
        return False
    
    with open(env_file, "r") as f:
        content = f.read()
    
    if "your_deepseek_api_key_here" in content or "your_serper_api_key_here" in content:
        print("⚠️  API keys not configured in .env file")
        return False
    
    print("✅ .env file is configured")
    return True

def run_system():
    """Run the Champions League Fantasy AI system"""
    print("\n🚀 Starting Champions League Fantasy AI...")
    print("This may take a few minutes as the agents analyze players and build your team.")
    print()
    
    try:
        # Run the crew
        result = subprocess.run(["crewai", "run"], capture_output=False, text=True)
        if result.returncode == 0:
            print("\n🎉 Analysis complete! Check the output/ directory for your reports.")
        else:
            print("\n❌ An error occurred. Check the output above for details.")
    except FileNotFoundError:
        print("❌ crewai command not found. Make sure CrewAI is properly installed.")
    except KeyboardInterrupt:
        print("\n⏹️  Analysis interrupted by user.")

def main():
    """Main quick start function"""
    print_banner()
    
    # Check prerequisites
    print("🔍 Checking prerequisites...")
    
    if not check_python_version():
        print("\n❌ Please upgrade to Python 3.10 or higher")
        sys.exit(1)
    
    if not check_dependencies():
        print("\n❌ Please install dependencies: pip install -e .")
        sys.exit(1)
    
    if not check_env_file():
        print("\n❌ Please configure your API keys:")
        print("   1. Copy .env.example to .env")
        print("   2. Edit .env with your API keys")
        print("   3. Get DeepSeek API key: https://platform.deepseek.com/")
        print("   4. Get Serper API key: https://serper.dev/")
        sys.exit(1)
    
    print("\n✅ All prerequisites met!")
    
    # Ask user if they want to run the system
    print("\n🎯 Ready to analyze Champions League Fantasy players!")
    response = input("Would you like to run the analysis now? (y/n): ").lower().strip()
    
    if response in ['y', 'yes']:
        run_system()
    else:
        print("\n👋 You can run the analysis anytime with: crewai run")
        print("📚 Check the README.md for more information")

if __name__ == "__main__":
    main()
