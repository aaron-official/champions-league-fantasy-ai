from crewai.tools import BaseTool
from crewai_tools import SerperDevTool
from typing import Type, Dict, List
from pydantic import BaseModel, Field
from datetime import datetime, timedelta
import json
import os


def get_football_season(current_date: datetime = None) -> str:
    """
    Calculate the current football season based on the football calendar.
    Season runs from August 1st to June 10th of the following year.
    
    Args:
        current_date: Date to calculate season for (defaults to now)
    
    Returns:
        String in format "YYYY/YY" (e.g., "2025/26")
    """
    if current_date is None:
        current_date = datetime.now()
    
    # If we're between August 1st and June 10th, we're in the season that started in August
    if current_date.month >= 8:  # August to December
        season_start_year = current_date.year
        season_end_year = current_date.year + 1
    elif current_date.month <= 6 and current_date.day <= 10:  # January to June 10th
        season_start_year = current_date.year - 1
        season_end_year = current_date.year
    else:  # June 11th to July 31st (off-season)
        # During off-season, we're still in the previous season until August 1st
        season_start_year = current_date.year - 1
        season_end_year = current_date.year
    
    return f"{season_start_year}/{str(season_end_year)[-2:]}"


class PlayerStatsInput(BaseModel):
    """Input schema for PlayerStatsTool."""
    player_name: str = Field(..., description="Name of the player to get statistics for")
    team_name: str = Field(..., description="Team name the player plays for")

class PlayerStatsTool(BaseTool):
    name: str = "Player Statistics Tool"
    description: str = (
        "Search the web for detailed player statistics including goals, assists, minutes played, "
        "recent form data, and Champions League fantasy points using current date context."
    )
    args_schema: Type[BaseModel] = PlayerStatsInput
    serper_tool: SerperDevTool = None

    def __init__(self):
        super().__init__()
        self.serper_tool = SerperDevTool()

    def _run(self, player_name: str, team_name: str) -> str:
        # Use current date for relevant search context
        current_date = datetime.now()
        current_season = get_football_season(current_date)
        
        # Use Serper to search for player statistics with current season context and team verification
        search_query = f"{player_name} current team {current_season} season Champions League Fantasy stats goals assists form gameweek points recent matches {current_date.strftime('%B %Y')} transfer news"
        
        try:
            search_result = self.serper_tool.run(search_query=search_query)
            return f"Player statistics search results for {player_name} ({team_name}) - {current_season} season:\n{search_result}"
        except Exception as e:
            return f"Error searching for {player_name} stats: {str(e)}"


class FixtureAnalysisInput(BaseModel):
    """Input schema for FixtureAnalysisTool."""
    team_name: str = Field(..., description="Team name to analyze fixtures for")
    num_fixtures: int = Field(default=3, description="Number of upcoming fixtures to analyze")

class FixtureAnalysisTool(BaseTool):
    name: str = "Fixture Analysis Tool"
    description: str = (
        "Search the web for upcoming Champions League fixtures, difficulty ratings, "
        "and team form analysis using current date context."
    )
    args_schema: Type[BaseModel] = FixtureAnalysisInput
    serper_tool: SerperDevTool = None

    def __init__(self):
        super().__init__()
        self.serper_tool = SerperDevTool()

    def _run(self, team_name: str, num_fixtures: int = 3) -> str:
        # Get current date and season context
        current_date = datetime.now()
        current_season = get_football_season(current_date)
        next_week = current_date + timedelta(days=7)
        
        # Search for upcoming fixtures with current date context and team verification
        search_query = f"{team_name} current squad {current_season} season Champions League Fantasy upcoming fixtures gameweek next {num_fixtures} matches {current_date.strftime('%B %Y')} difficulty schedule transfer news"
        
        try:
            search_result = self.serper_tool.run(search_query=search_query)
            return f"Fixture analysis for {team_name} ({current_season} season):\n{search_result}"
        except Exception as e:
            return f"Error searching for {team_name} fixtures: {str(e)}"


class OwnershipAnalysisInput(BaseModel):
    """Input schema for OwnershipAnalysisTool."""
    player_name: str = Field(..., description="Player name to check ownership percentage")

class OwnershipAnalysisTool(BaseTool):
    name: str = "Player Ownership Analysis Tool"
    description: str = (
        "Search the web for current Champions League fantasy ownership percentages, popular picks, "
        "and differential opportunities using current date context."
    )
    args_schema: Type[BaseModel] = OwnershipAnalysisInput
    serper_tool: SerperDevTool = None

    def __init__(self):
        super().__init__()
        self.serper_tool = SerperDevTool()

    def _run(self, player_name: str) -> str:
        # Get current date for timely search context
        current_date = datetime.now()
        current_season = get_football_season(current_date)
        
        # Search for ownership data with current context
        search_query = f"{player_name} Champions League Fantasy ownership percentage popular picks differential gameweek {current_season} {current_date.strftime('%B %Y')}"
        
        try:
            search_result = self.serper_tool.run(search_query=search_query)
            return f"Ownership analysis for {player_name} ({current_season} season):\n{search_result}"
        except Exception as e:
            return f"Error searching for {player_name} ownership data: {str(e)}"


class FormAnalysisInput(BaseModel):
    """Input schema for FormAnalysisTool."""
    player_name: str = Field(..., description="Player name to analyze recent form")
    games_back: int = Field(default=5, description="Number of recent games to analyze")

class FormAnalysisTool(BaseTool):
    name: str = "Player Form Analysis Tool"
    description: str = (
        "Search the web for a player's recent form including goals, assists, minutes played, "
        "and fantasy points using current date context for relevancy."
    )
    args_schema: Type[BaseModel] = FormAnalysisInput
    serper_tool: SerperDevTool = None

    def __init__(self):
        super().__init__()
        self.serper_tool = SerperDevTool()

    def _run(self, player_name: str, games_back: int = 5) -> str:
        # Get current date for recent form context
        current_date = datetime.now()
        current_season = get_football_season(current_date)
        last_month = (current_date - timedelta(days=30)).strftime('%B')
        
        # Search for recent form with current date context
        search_query = f"{player_name} recent form last {games_back} games Champions League Fantasy {current_season} goals assists gameweek points {last_month} {current_date.strftime('%B')}"
        
        try:
            search_result = self.serper_tool.run(search_query=search_query)
            return f"Form analysis for {player_name} (last {games_back} games, {current_season} season):\n{search_result}"
        except Exception as e:
            return f"Error searching for {player_name} form data: {str(e)}"


class FantasyNewsInput(BaseModel):
    """Input schema for FantasyNewsTool."""
    topic: str = Field(..., description="Specific fantasy football topic to search for")

class FantasyNewsTool(BaseTool):
    name: str = "Fantasy Football News Tool"
    description: str = (
        "Search for the latest Champions League fantasy football news, expert tips, "
        "injury updates, and community insights using current date context."
    )
    args_schema: Type[BaseModel] = FantasyNewsInput
    serper_tool: SerperDevTool = None

    def __init__(self):
        super().__init__()
        self.serper_tool = SerperDevTool()

    def _run(self, topic: str) -> str:
        # Get current date for latest news context
        current_date = datetime.now()
        current_season = get_football_season(current_date)
        this_week = current_date.strftime('%W')
        
        # Search for latest fantasy football news
        search_query = f"Champions League Fantasy {topic} {current_season} latest news tips experts reddit twitter gameweek this week {current_date.strftime('%B %Y')}"
        
        try:
            search_result = self.serper_tool.run(search_query=search_query)
            return f"Latest fantasy football news about {topic} ({current_season} season):\n{search_result}"
        except Exception as e:
            return f"Error searching for fantasy news about {topic}: {str(e)}"


class InjuryReportInput(BaseModel):
    """Input schema for InjuryReportTool."""
    team_name: str = Field(..., description="Team name to check for injury reports")

class InjuryReportTool(BaseTool):
    name: str = "Injury Report Tool"
    description: str = (
        "Search for the latest injury reports, team news, and player availability "
        "for Champions League matches using current date context."
    )
    args_schema: Type[BaseModel] = InjuryReportInput
    serper_tool: SerperDevTool = None

    def __init__(self):
        super().__init__()
        self.serper_tool = SerperDevTool()

    def _run(self, team_name: str) -> str:
        # Get current date for latest injury news
        current_date = datetime.now()
        current_season = get_football_season(current_date)
        today = current_date.strftime('%Y-%m-%d')
        
        # Search for latest injury reports with date context
        search_query = f"{team_name} injury report team news Champions League Fantasy {current_season} latest today {current_date.strftime('%B %Y')} doubtful suspended available gameweek"
        
        try:
            search_result = self.serper_tool.run(search_query=search_query)
            return f"Latest injury report for {team_name} ({current_season} season, as of {today}):\n{search_result}"
        except Exception as e:
            return f"Error searching for {team_name} injury report: {str(e)}"


class PlayerTeamVerificationInput(BaseModel):
    """Input schema for PlayerTeamVerificationTool."""
    player_name: str = Field(..., description="Name of the player to verify current team and status")

class PlayerTeamVerificationTool(BaseTool):
    name: str = "Player Team Verification Tool"
    description: str = (
        "Verify a player's current team, playing status, and Champions League eligibility for the current season. "
        "This tool ensures all player recommendations are based on current team information and not outdated data."
    )
    args_schema: Type[BaseModel] = PlayerTeamVerificationInput
    serper_tool: SerperDevTool = None

    def __init__(self):
        super().__init__()
        self.serper_tool = SerperDevTool()

    def _run(self, player_name: str) -> str:
        # Get current date and season context
        current_date = datetime.now()
        current_season = get_football_season(current_date)
        
        # Search for current team and status with specific date context
        search_query = f"{player_name} current team {current_season} season Champions League transfer news today {current_date.strftime('%B %Y')} playing status starting XI"
        
        try:
            search_result = self.serper_tool.run(search_query=search_query)
            return f"Current team verification for {player_name} ({current_season} season, as of {current_date.strftime('%Y-%m-%d')}):\n{search_result}"
        except Exception as e:
            return f"Error verifying {player_name}'s current team: {str(e)}"


class FileWriterInput(BaseModel):
    """Input schema for FileWriterTool."""
    filename: str = Field(..., description="Name of the file to write (including extension)")
    content: str = Field(..., description="Content to write to the file")
    directory: str = Field(default="output", description="Directory to save the file in")

class FileWriterTool(BaseTool):
    name: str = "File Writer Tool"
    description: str = (
        "Write content to a file in the specified directory. "
        "Useful for saving analysis reports, team selections, and other outputs."
    )
    args_schema: Type[BaseModel] = FileWriterInput

    def _run(self, filename: str, content: str, directory: str = "output") -> str:
        try:
            # Get the project root directory (where the crew is running from)
            # This should be the fpl_expert directory
            current_dir = os.getcwd()
            
            # If we're in a subdirectory, navigate to the project root
            if "fpl_expert" in current_dir:
                # Find the fpl_expert directory
                parts = current_dir.split(os.sep)
                fpl_expert_index = parts.index("fpl_expert")
                project_root = os.sep.join(parts[:fpl_expert_index + 1])
            else:
                project_root = current_dir
            
            # Create the output directory path
            output_dir = os.path.join(project_root, directory)
            
            # Create directory if it doesn't exist
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
            
            # Create full file path
            file_path = os.path.join(output_dir, filename)
            
            # Write content to file
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            return f"Successfully wrote content to {file_path}"
        except Exception as e:
            return f"Error writing to file {filename}: {str(e)}"