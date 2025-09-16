from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
try:
    from crewai.knowledge.source.file_knowledge_source import FileKnowledgeSource
except ImportError:
    try:
        from crewai.knowledge import FileKnowledgeSource
    except ImportError:
        # Fallback: knowledge sources not available in this version
        FileKnowledgeSource = None
from crewai_tools import SerperDevTool
from .tools.custom_tool import (
    PlayerStatsTool, 
    FixtureAnalysisTool, 
    OwnershipAnalysisTool, 
    FormAnalysisTool,
    FantasyNewsTool,
    InjuryReportTool,
    FileWriterTool,
    PlayerTeamVerificationTool
)
from typing import List

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class FplExpert():
    """Champions League Fantasy Expert crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    def __init__(self):
        # Initialize all tools
        self.serper_tool = SerperDevTool()
        self.player_stats_tool = PlayerStatsTool()
        self.fixture_analysis_tool = FixtureAnalysisTool()
        self.ownership_analysis_tool = OwnershipAnalysisTool()
        self.form_analysis_tool = FormAnalysisTool()
        self.fantasy_news_tool = FantasyNewsTool()
        self.injury_report_tool = InjuryReportTool()
        self.file_writer_tool = FileWriterTool()
        self.player_team_verification_tool = PlayerTeamVerificationTool()
        
        # Initialize knowledge sources (if available)
        if FileKnowledgeSource is not None:
            self.fantasy_rules_knowledge = FileKnowledgeSource(
                file_path="knowledge/champions_league_fantasy_rules.md",
                chunk_size=1000,
                chunk_overlap=200
            )
            
            self.teams_knowledge = FileKnowledgeSource(
                file_path="knowledge/top_champions_league_teams.md",
                chunk_size=1000,
                chunk_overlap=200
            )
            
            self.strategies_knowledge = FileKnowledgeSource(
                file_path="knowledge/fantasy_strategies.md",
                chunk_size=1000,
                chunk_overlap=200
            )
            
            self.user_preference_knowledge = FileKnowledgeSource(
                file_path="knowledge/user_preference.txt",
                chunk_size=500,
                chunk_overlap=100
            )
        else:
            # Fallback: knowledge sources not available
            self.fantasy_rules_knowledge = None
            self.teams_knowledge = None
            self.strategies_knowledge = None
            self.user_preference_knowledge = None
        
        # Create tool sets for different agent types
        self.research_tools = [
            self.serper_tool,
            self.player_stats_tool,
            self.form_analysis_tool,
            self.player_team_verification_tool,
            self.file_writer_tool
        ]
        
        self.analysis_tools = [
            self.serper_tool,
            self.fixture_analysis_tool,
            self.injury_report_tool,
            self.player_team_verification_tool,
            self.file_writer_tool
        ]
        
        self.community_tools = [
            self.serper_tool,
            self.ownership_analysis_tool,
            self.fantasy_news_tool,
            self.player_team_verification_tool,
            self.file_writer_tool
        ]

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools

    @agent
    def player_scout(self) -> Agent:
        return Agent(
            config=self.agents_config['player_scout'], # type: ignore[index]
            tools=self.research_tools,
            verbose=True
        )

    @agent
    def tactical_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['tactical_analyst'], # type: ignore[index]
            tools=self.analysis_tools,
            verbose=True
        )

    @agent
    def fixture_expert(self) -> Agent:
        return Agent(
            config=self.agents_config['fixture_expert'], # type: ignore[index]
            tools=self.analysis_tools,
            verbose=True
        )

    @agent
    def captain_selector(self) -> Agent:
        return Agent(
            config=self.agents_config['captain_selector'], # type: ignore[index]
            tools=self.research_tools + self.analysis_tools,
            verbose=True
        )

    @agent
    def budget_optimizer(self) -> Agent:
        return Agent(
            config=self.agents_config['budget_optimizer'], # type: ignore[index]
            tools=[self.serper_tool, self.player_stats_tool],
            verbose=True
        )

    @agent
    def community_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['community_analyst'], # type: ignore[index]
            tools=self.community_tools,
            verbose=True
        )

    @agent
    def team_builder(self) -> Agent:
        return Agent(
            config=self.agents_config['team_builder'], # type: ignore[index]
            tools=[self.serper_tool],
            verbose=True
        )

    # Task definitions with proper dependencies
    @task
    def scout_players_task(self) -> Task:
        return Task(
            config=self.tasks_config['scout_players_task'], # type: ignore[index]
        )

    @task
    def analyze_tactics_task(self) -> Task:
        return Task(
            config=self.tasks_config['analyze_tactics_task'], # type: ignore[index]
        )

    @task
    def analyze_fixtures_task(self) -> Task:
        return Task(
            config=self.tasks_config['analyze_fixtures_task'], # type: ignore[index]
        )

    @task
    def select_captain_task(self) -> Task:
        return Task(
            config=self.tasks_config['select_captain_task'], # type: ignore[index]
        )

    @task
    def optimize_budget_task(self) -> Task:
        return Task(
            config=self.tasks_config['optimize_budget_task'], # type: ignore[index]
        )

    @task
    def gather_community_insights_task(self) -> Task:
        return Task(
            config=self.tasks_config['gather_community_insights_task'], # type: ignore[index]
        )

    @task
    def build_optimal_team_task(self) -> Task:
        return Task(
            config=self.tasks_config['build_optimal_team_task'], # type: ignore[index]
            output_file='champions_league_team.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Champions League Fantasy Expert crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        # Prepare knowledge sources (filter out None values)
        knowledge_sources = []
        if self.fantasy_rules_knowledge is not None:
            knowledge_sources.append(self.fantasy_rules_knowledge)
        if self.teams_knowledge is not None:
            knowledge_sources.append(self.teams_knowledge)
        if self.strategies_knowledge is not None:
            knowledge_sources.append(self.strategies_knowledge)
        if self.user_preference_knowledge is not None:
            knowledge_sources.append(self.user_preference_knowledge)
        
        # Create crew with or without knowledge sources
        crew_kwargs = {
            'agents': self.agents, # Automatically created by the @agent decorator
            'tasks': self.tasks, # Automatically created by the @task decorator
            'process': Process.sequential,
            'verbose': True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        }
        
        # Add knowledge sources if available
        if knowledge_sources:
            crew_kwargs['knowledge_sources'] = knowledge_sources
        
        return Crew(**crew_kwargs)