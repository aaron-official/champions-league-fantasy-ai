# 🏆 Champions League Fantasy AI

> **A sophisticated multi-agent AI system built with CrewAI to dominate Champions League Fantasy Football**

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://python.org)
[![CrewAI](https://img.shields.io/badge/CrewAI-0.186.1%2B-green.svg)](https://crewai.com)
[![DeepSeek](https://img.shields.io/badge/DeepSeek-LLM-orange.svg)](https://deepseek.com)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 🎯 Overview

This project is an advanced AI-powered fantasy football management system specifically designed for **Champions League Fantasy Football**. It leverages the power of CrewAI's multi-agent framework with DeepSeek language models to provide intelligent player scouting, tactical analysis, and team optimization.

### 🌟 Key Features

- **🤖 7 Specialized AI Agents** - Each with unique expertise and DeepSeek models
- **⚽ Champions League Focus** - Built for the new 36-team, 8-gameweek format
- **📊 Real-time Data** - Dynamic player verification and current team status
- **🎯 Aggressive Strategy** - Optimized for top 1% ranking and championship wins
- **💡 Smart Analytics** - Data-driven decisions with advanced insights
- **📁 Organized Output** - Professional reports saved to structured directories

## 🏗️ System Architecture

### AI Agents

| Agent | Model | Role | Expertise |
|-------|-------|------|-----------|
| **Player Scout** | `deepseek-chat` | Player Research | Current form, injuries, rotation risk |
| **Tactical Analyst** | `deepseek-reasoner` | Strategy | Formation analysis, tactical insights |
| **Fixture Expert** | `deepseek-chat` | Scheduling | Gameweek planning, fixture difficulty |
| **Budget Optimizer** | `deepseek-chat` | Financial | Value analysis, budget management |
| **Community Analyst** | `deepseek-chat` | Market Intelligence | Ownership trends, differential picks |
| **Captain Selector** | `deepseek-reasoner` | Leadership | Captaincy decisions, chip strategy |
| **Team Builder** | `deepseek-reasoner` | Final Assembly | Complete team construction |

### Custom Tools

- **🔍 Player Statistics Tool** - Real-time player performance data
- **📅 Fixture Analysis Tool** - Upcoming match analysis
- **👥 Ownership Analysis Tool** - Community ownership insights
- **📈 Form Analysis Tool** - Recent performance trends
- **📰 Fantasy News Tool** - Latest fantasy football news
- **🏥 Injury Report Tool** - Player injury and fitness status
- **✅ Player Team Verification Tool** - Current team and eligibility verification
- **📝 File Writer Tool** - Professional report generation

## 🚀 Quick Start

### Prerequisites

- **Python 3.10+**
- **API Keys** (see [Setup](#setup) section)
- **Git**

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/aaron-official/champions-league-fantasy-ai.git
   cd champions-league-fantasy-ai
   ```

2. **Install dependencies**
   ```bash
   # Using uv (recommended)
   uv sync
   
   # Or using pip
   pip install -e .
   ```

3. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys
   ```

4. **Run the system**
   ```bash
   crewai run
   ```

## ⚙️ Setup

### Required API Keys

Create a `.env` file in the project root with the following keys:

```env
# DeepSeek API (for AI models)
DEEPSEEK_API_KEY=your_deepseek_api_key_here

# Serper API (for web search)
SERPER_API_KEY=your_serper_api_key_here
```

### API Key Setup Guide

#### 1. DeepSeek API
- Visit [DeepSeek API](https://platform.deepseek.com/)
- Sign up and create an API key
- Add to `.env` file

#### 2. Serper API
- Visit [Serper.dev](https://serper.dev/)
- Sign up for a free account (100 searches/month)
- Get your API key and add to `.env` file

## 🎮 Usage

### Basic Usage

```bash
# Run the complete analysis
crewai run

# The system will:
# 1. Scout current top players
# 2. Analyze fixtures and form
# 3. Optimize budget allocation
# 4. Select captain and vice-captain
# 5. Build the final team
# 6. Generate detailed reports
```

### Output Structure

After running, you'll find organized outputs in the `output/` directory:

```
output/
├── player_analysis_2025-09-16.md
├── fixture_analysis_2025-09-16.md
├── budget_optimization_2025-09-16.md
├── community_insights_2025-09-16.md
├── captain_selection_2025-09-16.md
└── final_team_2025-09-16.md
```

### Customization

#### User Preferences
Edit `knowledge/user_preference.txt` to customize your strategy:

```txt
User name: Your Name
User's goal: WIN the Champions League Fantasy league
User prefers: Aggressive strategies with high-ceiling differential picks
User prioritizes: Attacking players, set-piece takers, penalty takers
```

#### Agent Configuration
Modify `src/fpl_expert/config/agents.yaml` to adjust agent behavior, goals, and backstories.

#### Task Configuration
Update `src/fpl_expert/config/tasks.yaml` to modify task descriptions and expected outputs.

## 🏆 Champions League Fantasy Rules

This system is optimized for the **new Champions League Fantasy format**:

- **36 Teams** in the league phase
- **8 Gameweeks** in the new format
- **Max 3 players** per club
- **100M Euro budget**
- **Unlimited transfers** between gameweeks
- **Captain and Vice-Captain** selection
- **Chip strategies** (Wildcard, Bench Boost, etc.)

## 📊 Features in Detail

### Dynamic Date Management
- Automatically calculates current football season (August 1st - June 10th)
- Real-time gameweek estimation
- No hardcoded dates - always current

### Player Verification
- Verifies current team and Champions League eligibility
- Prevents outdated player recommendations
- Real-time transfer and injury updates

### Advanced Analytics
- Form analysis with recent performance trends
- Fixture difficulty assessment
- Ownership analysis for differential picks
- Budget optimization algorithms

### Professional Reporting
- Detailed markdown reports for each analysis
- Structured output in organized directories
- Comprehensive team selection rationale

## 🛠️ Development

### Project Structure

```
fpl_expert/
├── src/fpl_expert/
│   ├── config/
│   │   ├── agents.yaml          # Agent definitions
│   │   └── tasks.yaml           # Task configurations
│   ├── tools/
│   │   └── custom_tool.py       # Custom tools implementation
│   ├── crew.py                  # Main crew assembly
│   └── main.py                  # Entry point
├── knowledge/
│   ├── champions_league_fantasy_rules.md
│   ├── top_champions_league_teams.md
│   ├── fantasy_strategies.md
│   └── user_preference.txt
├── output/                      # Generated reports
└── tests/                       # Test files
```

### Adding New Tools

1. Create a new tool class in `custom_tool.py`:

```python
class YourCustomTool(BaseTool):
    name: str = "Your Custom Tool"
    description: str = "Tool description"
    args_schema: Type[BaseModel] = YourInputSchema
    
    def _run(self, param: str) -> str:
        # Your tool logic here
        return result
```

2. Add the tool to the crew in `crew.py`
3. Update agent configurations to use the new tool

### Testing

```bash
# Run tests
crewai test

# Run specific test
python -m pytest tests/test_specific.py
```

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Commit your changes**: `git commit -m 'Add amazing feature'`
4. **Push to the branch**: `git push origin feature/amazing-feature`
5. **Open a Pull Request**

### Contribution Guidelines

- Follow PEP 8 style guidelines
- Add tests for new features
- Update documentation as needed
- Ensure all tests pass before submitting

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **CrewAI** - Multi-agent framework
- **DeepSeek** - Advanced language models
- **Serper** - Web search capabilities
- **Champions League Fantasy** - The game that inspired this project

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/aaron-official/champions-league-fantasy-ai/issues)
- **Discussions**: [GitHub Discussions](https://github.com/aaron-official/champions-league-fantasy-ai/discussions)

## 🎯 Roadmap

- [ ] **Real-time price tracking**
- [ ] **Advanced statistical models**
- [ ] **Web dashboard interface**
- [ ] **Mobile app integration**
- [ ] **Historical performance analysis**
- [ ] **Machine learning predictions**

---

**Ready to dominate Champions League Fantasy? Let's go! 🏆⚽**

*Built with ❤️ for fantasy football enthusiasts*
