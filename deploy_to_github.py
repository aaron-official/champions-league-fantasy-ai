#!/usr/bin/env python3
"""
Champions League Fantasy AI - GitHub Deployment Script
This script helps you deploy your project to GitHub
"""

import os
import subprocess
import sys
from pathlib import Path

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e}")
        if e.stdout:
            print(f"Output: {e.stdout}")
        if e.stderr:
            print(f"Error: {e.stderr}")
        return False

def check_git_status():
    """Check if git is initialized and what the status is"""
    if not Path(".git").exists():
        print("📁 Git repository not initialized")
        return False
    
    # Check if there are uncommitted changes
    result = subprocess.run("git status --porcelain", shell=True, capture_output=True, text=True)
    if result.stdout.strip():
        print("📝 There are uncommitted changes:")
        print(result.stdout)
        return "uncommitted"
    
    print("✅ Git repository is clean")
    return True

def initialize_git():
    """Initialize git repository and make initial commit"""
    print("🏆 Champions League Fantasy AI - GitHub Deployment")
    print("=" * 60)
    
    # Check if git is installed
    if not run_command("git --version", "Checking Git installation"):
        print("❌ Git is not installed. Please install Git first.")
        return False
    
    # Initialize git if not already done
    if not Path(".git").exists():
        if not run_command("git init", "Initializing Git repository"):
            return False
    
    # Add all files
    if not run_command("git add .", "Adding files to Git"):
        return False
    
    # Check what we're about to commit
    result = subprocess.run("git status --porcelain", shell=True, capture_output=True, text=True)
    if result.stdout.strip():
        print("📝 Files to be committed:")
        print(result.stdout)
    else:
        print("ℹ️  No changes to commit")
        return True
    
    # Make initial commit
    commit_message = "Initial commit: Champions League Fantasy AI with CrewAI and DeepSeek"
    if not run_command(f'git commit -m "{commit_message}"', "Making initial commit"):
        return False
    
    print("✅ Git repository initialized and committed")
    return True

def setup_github_remote():
    """Set up GitHub remote repository"""
    print("\n🌐 Setting up GitHub remote...")
    
    # Check if remote already exists
    result = subprocess.run("git remote -v", shell=True, capture_output=True, text=True)
    if "origin" in result.stdout:
        print("ℹ️  Remote 'origin' already exists")
        print(result.stdout)
        return True
    
    # Get repository name from current directory
    repo_name = Path.cwd().name
    github_url = f"https://github.com/aaron-official/{repo_name}.git"
    
    print(f"🔗 Adding remote: {github_url}")
    if not run_command(f"git remote add origin {github_url}", "Adding GitHub remote"):
        return False
    
    print("✅ GitHub remote added")
    return True

def push_to_github():
    """Push to GitHub"""
    print("\n🚀 Pushing to GitHub...")
    
    # Check if we're on main branch
    result = subprocess.run("git branch --show-current", shell=True, capture_output=True, text=True)
    current_branch = result.stdout.strip()
    
    if current_branch != "main":
        print(f"📝 Current branch: {current_branch}")
        print("🔄 Switching to main branch...")
        if not run_command("git checkout -b main", "Creating main branch"):
            return False
    
    # Push to GitHub
    if not run_command("git push -u origin main", "Pushing to GitHub"):
        print("💡 If this fails, you may need to create the repository on GitHub first:")
        print(f"   1. Go to https://github.com/aaron-official")
        print(f"   2. Click 'New repository'")
        print(f"   3. Name it: {Path.cwd().name}")
        print(f"   4. Don't initialize with README (we already have one)")
        print(f"   5. Click 'Create repository'")
        print(f"   6. Run this script again")
        return False
    
    print("✅ Successfully pushed to GitHub!")
    return True

def main():
    """Main deployment function"""
    print("🏆 Champions League Fantasy AI - GitHub Deployment")
    print("=" * 60)
    
    # Check current directory
    current_dir = Path.cwd()
    print(f"📁 Current directory: {current_dir}")
    
    # Check if we're in the right directory
    if not Path("README.md").exists():
        print("❌ README.md not found. Are you in the project directory?")
        return
    
    # Initialize git and make initial commit
    if not initialize_git():
        print("❌ Failed to initialize Git repository")
        return
    
    # Set up GitHub remote
    if not setup_github_remote():
        print("❌ Failed to set up GitHub remote")
        return
    
    # Push to GitHub
    if not push_to_github():
        print("❌ Failed to push to GitHub")
        return
    
    print("\n🎉 Deployment complete!")
    print(f"🌐 Your repository is now available at:")
    print(f"   https://github.com/aaron-official/{current_dir.name}")
    print("\n📋 Next steps:")
    print("   1. Set up GitHub secrets for CI/CD:")
    print("      - DEEPSEEK_API_KEY")
    print("      - SERPER_API_KEY")
    print("   2. Enable GitHub Actions in repository settings")
    print("   3. Consider adding topics/tags to your repository")
    print("   4. Share your amazing project with the world! 🚀")

if __name__ == "__main__":
    main()
