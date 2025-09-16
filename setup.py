#!/usr/bin/env python3
"""
Champions League Fantasy AI - Setup Script
This script helps you set up the environment and API keys
"""

import os
import sys
from pathlib import Path

def create_env_file():
    """Create .env file from template"""
    env_content = """# Champions League Fantasy AI - Environment Variables
# Fill in your actual API keys below

# DeepSeek API Key
# Get your API key from: https://platform.deepseek.com/
DEEPSEEK_API_KEY=your_deepseek_api_key_here

# Serper API Key  
# Get your API key from: https://serper.dev/
# Free tier: 100 searches per month
SERPER_API_KEY=your_serper_api_key_here

# Optional: Custom model configurations
# DEEPSEEK_MODEL_CHAT=deepseek-chat
# DEEPSEEK_MODEL_REASONER=deepseek-reasoner

# Optional: Custom search settings
# SERPER_N_RESULTS=10
# SERPER_COUNTRY=US
# SERPER_LOCALE=en
"""
    
    env_file = Path(".env")
    if env_file.exists():
        print("⚠️  .env file already exists. Skipping creation.")
        return
    
    with open(env_file, "w") as f:
        f.write(env_content)
    
    print("✅ Created .env file. Please edit it with your API keys.")

def check_dependencies():
    """Check if required dependencies are installed"""
    try:
        import crewai
        print("✅ CrewAI is installed")
    except ImportError:
        print("❌ CrewAI not found. Run: pip install -e .")
        return False
    
    try:
        import crewai_tools
        print("✅ CrewAI Tools is installed")
    except ImportError:
        print("❌ CrewAI Tools not found. Run: pip install -e .")
        return False
    
    return True

def check_api_keys():
    """Check if API keys are configured"""
    env_file = Path(".env")
    if not env_file.exists():
        print("❌ .env file not found. Run setup first.")
        return False
    
    with open(env_file, "r") as f:
        content = f.read()
    
    if "your_deepseek_api_key_here" in content:
        print("⚠️  DeepSeek API key not configured in .env file")
        return False
    
    if "your_serper_api_key_here" in content:
        print("⚠️  Serper API key not configured in .env file")
        return False
    
    print("✅ API keys appear to be configured")
    return True

def main():
    """Main setup function"""
    print("🏆 Champions League Fantasy AI - Setup")
    print("=" * 50)
    
    # Create .env file
    create_env_file()
    
    # Check dependencies
    print("\n📦 Checking dependencies...")
    if not check_dependencies():
        print("\n❌ Setup incomplete. Please install dependencies first.")
        sys.exit(1)
    
    # Check API keys
    print("\n🔑 Checking API keys...")
    if not check_api_keys():
        print("\n⚠️  Please configure your API keys in .env file")
        print("   Get DeepSeek API key: https://platform.deepseek.com/")
        print("   Get Serper API key: https://serper.dev/")
        sys.exit(1)
    
    print("\n🎉 Setup complete! You can now run: crewai run")

if __name__ == "__main__":
    main()
