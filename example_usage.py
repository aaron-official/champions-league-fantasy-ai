#!/usr/bin/env python3
"""
Champions League Fantasy AI - Example Usage
This script demonstrates how to use the system programmatically
"""

import os
from datetime import datetime
from src.fpl_expert.crew import FplExpert
from src.fpl_expert.tools.custom_tool import get_football_season

def example_basic_usage():
    """Example of basic system usage"""
    print("🏆 Champions League Fantasy AI - Basic Usage Example")
    print("=" * 60)
    
    # Initialize the system
    fpl_expert = FplExpert()
    
    # Get current context
    current_date = datetime.now()
    current_season = get_football_season(current_date)
    
    print(f"📅 Current Date: {current_date.strftime('%Y-%m-%d')}")
    print(f"⚽ Current Season: {current_season}")
    
    # Create inputs for the crew
    inputs = {
        "current_date": current_date.strftime('%Y-%m-%d'),
        "current_season": current_season,
        "estimated_gameweek": 1,  # You can adjust this
        "budget": 100.0,  # 100M euros
        "user_preferences": "Aggressive strategy with high-ceiling differentials"
    }
    
    print(f"💰 Budget: {inputs['budget']}M euros")
    print(f"🎯 Strategy: {inputs['user_preferences']}")
    
    # Run the crew
    print("\n🚀 Starting analysis...")
    try:
        result = fpl_expert.crew().kickoff(inputs=inputs)
        print("\n✅ Analysis complete!")
        print("📁 Check the output/ directory for detailed reports")
        return result
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        return None

def example_custom_analysis():
    """Example of custom analysis with specific parameters"""
    print("\n🎯 Champions League Fantasy AI - Custom Analysis Example")
    print("=" * 60)
    
    # Custom parameters
    custom_inputs = {
        "current_date": "2025-09-16",
        "current_season": "2025/26",
        "estimated_gameweek": 2,
        "budget": 95.5,  # Custom budget
        "user_preferences": "Focus on premium defenders and differential midfielders",
        "specific_requirements": [
            "Must include at least 2 Real Madrid players",
            "Avoid players from teams with difficult fixtures",
            "Prioritize set-piece takers"
        ]
    }
    
    print("📋 Custom Analysis Parameters:")
    for key, value in custom_inputs.items():
        print(f"   {key}: {value}")
    
    # You can modify the crew configuration here
    fpl_expert = FplExpert()
    
    print("\n🚀 Starting custom analysis...")
    try:
        result = fpl_expert.crew().kickoff(inputs=custom_inputs)
        print("\n✅ Custom analysis complete!")
        return result
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        return None

def example_tool_usage():
    """Example of using individual tools"""
    print("\n🔧 Champions League Fantasy AI - Individual Tool Usage")
    print("=" * 60)
    
    from src.fpl_expert.tools.custom_tool import (
        PlayerStatsTool, 
        PlayerTeamVerificationTool,
        FixtureAnalysisTool
    )
    
    # Initialize tools
    player_stats_tool = PlayerStatsTool()
    verification_tool = PlayerTeamVerificationTool()
    fixture_tool = FixtureAnalysisTool()
    
    # Example 1: Get player statistics
    print("📊 Getting player statistics...")
    try:
        stats_result = player_stats_tool._run("Kylian Mbappé", "Real Madrid")
        print(f"Player Stats Result: {stats_result[:200]}...")
    except Exception as e:
        print(f"Error getting player stats: {e}")
    
    # Example 2: Verify player team
    print("\n✅ Verifying player team...")
    try:
        verification_result = verification_tool._run("Kylian Mbappé")
        print(f"Verification Result: {verification_result[:200]}...")
    except Exception as e:
        print(f"Error verifying player: {e}")
    
    # Example 3: Analyze fixtures
    print("\n📅 Analyzing fixtures...")
    try:
        fixture_result = fixture_tool._run("Real Madrid", "Champions League")
        print(f"Fixture Analysis Result: {fixture_result[:200]}...")
    except Exception as e:
        print(f"Error analyzing fixtures: {e}")

def main():
    """Main example function"""
    print("🏆 Champions League Fantasy AI - Usage Examples")
    print("=" * 60)
    
    # Check if API keys are configured
    if not os.getenv('DEEPSEEK_API_KEY') or not os.getenv('SERPER_API_KEY'):
        print("⚠️  API keys not found in environment variables")
        print("Please set DEEPSEEK_API_KEY and SERPER_API_KEY")
        print("Or run: python setup.py")
        return
    
    # Run examples
    print("\n1️⃣ Basic Usage Example")
    example_basic_usage()
    
    print("\n2️⃣ Custom Analysis Example")
    example_custom_analysis()
    
    print("\n3️⃣ Individual Tool Usage Example")
    example_tool_usage()
    
    print("\n🎉 All examples completed!")
    print("📚 Check the README.md for more detailed usage instructions")

if __name__ == "__main__":
    main()
