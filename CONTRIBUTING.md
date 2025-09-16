# Contributing to Champions League Fantasy AI

Thank you for your interest in contributing to the Champions League Fantasy AI project! This document provides guidelines and information for contributors.

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher
- Git
- Basic understanding of fantasy football
- Familiarity with CrewAI framework (helpful but not required)

### Development Setup

1. **Fork and clone the repository**
   ```bash
   git clone https://github.com/aaron-official/champions-league-fantasy-ai.git
   cd champions-league-fantasy-ai
   ```

2. **Set up development environment**
   ```bash
   # Install dependencies
   pip install -e .
   
   # Run setup script
   python setup.py
   
   # Configure your .env file with API keys
   ```

3. **Run tests to ensure everything works**
   ```bash
   crewai test
   ```

## 🎯 Areas for Contribution

### High Priority
- **New Custom Tools** - Add tools for specific fantasy football analysis
- **Agent Improvements** - Enhance agent reasoning and decision-making
- **Data Sources** - Integrate additional data sources for better insights
- **Performance Optimization** - Improve system speed and efficiency

### Medium Priority
- **Documentation** - Improve README, add tutorials, code comments
- **Testing** - Add comprehensive test coverage
- **Error Handling** - Improve robustness and error messages
- **UI/UX** - Create web interface or dashboard

### Low Priority
- **Code Refactoring** - Clean up and optimize existing code
- **Configuration** - Add more customization options
- **Logging** - Improve logging and debugging capabilities

## 🛠️ Development Guidelines

### Code Style

- Follow **PEP 8** style guidelines
- Use **type hints** for function parameters and return values
- Write **docstrings** for all functions and classes
- Keep functions **small and focused**
- Use **meaningful variable names**

### Example Code Structure

```python
from typing import Dict, List, Optional
from crewai_tools import BaseTool
from pydantic import BaseModel

class YourToolInput(BaseModel):
    """Input schema for YourTool"""
    parameter: str
    optional_param: Optional[int] = None

class YourCustomTool(BaseTool):
    """Your custom tool description"""
    
    name: str = "Your Custom Tool"
    description: str = "Detailed description of what this tool does"
    args_schema: type[BaseModel] = YourToolInput
    
    def _run(self, parameter: str, optional_param: Optional[int] = None) -> str:
        """
        Execute the tool logic
        
        Args:
            parameter: Required parameter description
            optional_param: Optional parameter description
            
        Returns:
            String result of the tool execution
        """
        try:
            # Your tool logic here
            result = self._process_data(parameter)
            return f"Tool result: {result}"
        except Exception as e:
            return f"Error in tool execution: {str(e)}"
    
    def _process_data(self, data: str) -> str:
        """Helper method for data processing"""
        # Implementation here
        return processed_data
```

### Testing

- Write tests for all new functionality
- Test both success and error cases
- Use descriptive test names
- Aim for high test coverage

```python
import pytest
from src.fpl_expert.tools.custom_tool import YourCustomTool

def test_your_tool_success():
    """Test successful tool execution"""
    tool = YourCustomTool()
    result = tool._run("test_parameter")
    assert "Tool result" in result
    assert "Error" not in result

def test_your_tool_error_handling():
    """Test tool error handling"""
    tool = YourCustomTool()
    result = tool._run("")  # Invalid input
    assert "Error" in result
```

## 📝 Pull Request Process

### Before Submitting

1. **Test your changes**
   ```bash
   crewai test
   python -m pytest tests/
   ```

2. **Check code style**
   ```bash
   # Install flake8 if not already installed
   pip install flake8
   flake8 src/
   ```

3. **Update documentation** if needed

4. **Add tests** for new functionality

### Pull Request Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
- [ ] Tests pass locally
- [ ] New tests added for new functionality
- [ ] Manual testing completed

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] No breaking changes (or clearly documented)
```

### Review Process

1. **Automated checks** must pass
2. **Code review** by maintainers
3. **Testing** in different environments
4. **Documentation** review
5. **Approval** and merge

## 🐛 Bug Reports

When reporting bugs, please include:

- **Clear description** of the issue
- **Steps to reproduce** the problem
- **Expected vs actual behavior**
- **Environment details** (OS, Python version, etc.)
- **Error messages** and logs
- **Screenshots** if applicable

### Bug Report Template

```markdown
**Bug Description**
Clear description of the bug

**Steps to Reproduce**
1. Step one
2. Step two
3. Step three

**Expected Behavior**
What should happen

**Actual Behavior**
What actually happens

**Environment**
- OS: [e.g., Windows 10, macOS 12, Ubuntu 20.04]
- Python Version: [e.g., 3.11.5]
- CrewAI Version: [e.g., 0.186.1]

**Additional Context**
Any other relevant information
```

## 💡 Feature Requests

When requesting features, please include:

- **Clear description** of the feature
- **Use case** and motivation
- **Proposed implementation** (if you have ideas)
- **Alternatives considered**
- **Additional context**

## 📚 Documentation

### Types of Documentation

- **README.md** - Project overview and setup
- **API Documentation** - Code documentation
- **Tutorials** - Step-by-step guides
- **Examples** - Usage examples
- **Contributing** - This file

### Writing Guidelines

- Use **clear, concise language**
- Include **code examples**
- Add **screenshots** when helpful
- Keep **up-to-date** with code changes
- Use **markdown formatting** properly

## 🤝 Community Guidelines

### Code of Conduct

- Be **respectful** and inclusive
- Provide **constructive feedback**
- Help **new contributors**
- Follow **community standards**
- Report **inappropriate behavior**

### Communication

- Use **GitHub Issues** for bugs and feature requests
- Use **GitHub Discussions** for questions and ideas
- Be **patient** with responses
- Provide **clear information**
- Search **existing issues** before creating new ones

## 🏆 Recognition

Contributors will be recognized in:

- **README.md** contributors section
- **Release notes** for significant contributions
- **GitHub contributors** page
- **Project documentation**

## 📞 Getting Help

- **GitHub Issues** - Bug reports and feature requests
- **GitHub Discussions** - Questions and community chat
- **Email** - aaron@example.com for private matters

## 🎯 Roadmap

Current development priorities:

1. **Enhanced Player Analysis** - More sophisticated player evaluation
2. **Real-time Data Integration** - Live match data and updates
3. **Advanced Statistics** - Machine learning models for predictions
4. **Web Interface** - User-friendly dashboard
5. **Mobile Support** - Mobile app or responsive web interface

---

Thank you for contributing to Champions League Fantasy AI! Together, we can build the ultimate fantasy football management system. 🏆⚽
