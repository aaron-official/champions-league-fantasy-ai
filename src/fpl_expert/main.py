#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from fpl_expert.crew import FplExpert
from fpl_expert.tools.custom_tool import get_football_season

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the Champions League Fantasy crew.
    """
    # Dynamic date and season calculation
    current_date = datetime.now()
    current_season = get_football_season(current_date)
    
    # Auto-detect approximate gameweek based on date (Champions League typically starts in September)
    # New format: 36 teams, 8 gameweeks in league phase (not 6 like old groups)
    if current_date.month >= 9:  # September onwards
        weeks_since_start = (current_date - datetime(current_date.year, 9, 1)).days // 14  # Rough 2-week intervals
        estimated_matchweek = min(max(weeks_since_start + 1, 1), 8)  # New league phase has 8 gameweeks
    else:
        estimated_matchweek = 1
    
    inputs = {
        'current_year': str(current_date.year),
        'current_date': current_date.strftime('%Y-%m-%d'),
        'current_season': current_season,
        'budget': '100',  # Typical Champions League Fantasy budget
        'matchweek': str(estimated_matchweek),
        'competition': 'UEFA Champions League',
        'month_year': current_date.strftime('%B %Y')
    }
    
    try:
        result = FplExpert().crew().kickoff(inputs=inputs)
        print("\n" + "="*50)
        print("CHAMPIONS LEAGUE FANTASY TEAM SELECTION COMPLETE!")
        print(f"Season: {current_season}")
        print(f"Estimated Gameweek: {estimated_matchweek}")
        print(f"Analysis Date: {current_date.strftime('%B %d, %Y')}")
        print("="*50)
        print("Check the 'champions_league_team.md' file for your optimal team selection.")
        return result
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'current_year': str(datetime.now().year),
        'budget': '100',
        'matchweek': '1',
        'competition': 'UEFA Champions League'
    }
    try:
        FplExpert().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        FplExpert().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        'current_year': str(datetime.now().year),
        'budget': '100',
        'matchweek': '1',
        'competition': 'UEFA Champions League'
    }
    
    try:
        FplExpert().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

def run_for_matchweek(matchweek: str, budget: str = '100'):
    """
    Run the crew for a specific gameweek with custom budget.
    """
    inputs = {
        'current_year': str(datetime.now().year),
        'budget': budget,
        'matchweek': matchweek,
        'competition': 'UEFA Champions League'
    }
    
    try:
        result = FplExpert().crew().kickoff(inputs=inputs)
        print(f"\nTeam selection for Gameweek {matchweek} complete!")
        return result
    except Exception as e:
        raise Exception(f"An error occurred while running the crew for matchweek {matchweek}: {e}")

if __name__ == "__main__":
    # Default run if no arguments provided
    if len(sys.argv) == 1:
        run()
    elif sys.argv[1] == "train" and len(sys.argv) >= 4:
        train()
    elif sys.argv[1] == "replay" and len(sys.argv) >= 3:
        replay()
    elif sys.argv[1] == "test" and len(sys.argv) >= 4:
        test()
    elif sys.argv[1] == "matchweek" and len(sys.argv) >= 3:
        matchweek = sys.argv[2]
        budget = sys.argv[3] if len(sys.argv) > 3 else '100'
        run_for_matchweek(matchweek, budget)
    else:
        print("Usage:")
        print("python main.py                           - Run with default settings")
        print("python main.py train <iterations> <filename>")
        print("python main.py replay <task_id>")
        print("python main.py test <iterations> <eval_llm>")
        print("python main.py matchweek <gameweek> [budget]")
        run()