# AI Coaching Chatbot - Project Structure

## Overview
This is a comprehensive AI-powered coaching chatbot built with Flask and OpenAI integration. The system provides personalized coaching through multiple styles and specialized sports scenarios.

## Project Structure

```
chatbot/
├── .gitignore                 # Git ignore rules
├── .env                      # Environment variables (not in repo)
├── app.py                    # Main Flask application
├── config.py                 # Configuration management
├── setup.py                  # Automated setup script
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
├── PROJECT_STRUCTURE.md      # This file
├── coach/                    # Core coaching modules
│   ├── __init__.py
│   ├── agent.py              # Main coaching agent
│   ├── memory.py             # User memory and context management
│   ├── responses.py          # Response generation with OpenAI
│   ├── safety.py             # Safety monitoring and alerts
│   ├── scenarios.py          # General coaching scenarios
│   └── sports.py             # Sports-specific coaching scenarios
├── templates/                # HTML templates
│   └── index.html            # Main chat interface
└── static/                   # Static assets
    ├── css/
    │   └── style.css         # Application styling
    └── js/
        └── script.js         # Frontend JavaScript
```

## Key Features

### Core Functionality
- **Multi-Style Coaching**: Supportive, Challenging, and Analytical approaches
- **Sports Coaching**: Specialized scenarios for athletic performance
- **Memory Management**: Context-aware conversations with user profiling
- **Safety Monitoring**: Built-in safety checks and escalation protocols
- **Performance Tracking**: Metrics extraction and progress monitoring
- **Mental State Analysis**: Confidence, anxiety, focus, and motivation tracking

### Technical Features
- **Flask Web Interface**: Modern, responsive chat interface
- **OpenAI Integration**: GPT-3.5-turbo powered responses with fallbacks
- **Environment Configuration**: Secure API key management
- **Modular Architecture**: Extensible coaching scenarios and responses
- **Error Handling**: Graceful fallbacks and mock responses

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd chatbot
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment**
   ```bash
   # Create .env file
   cp env_template.txt .env
   # Edit .env and add your OpenAI API key
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Access the application**
   Open browser to `http://127.0.0.1:5000`

## Environment Variables

Required:
- `OPENAI_API_KEY`: Your OpenAI API key

Optional:
- `FLASK_ENV`: development/production
- `FLASK_DEBUG`: True/False
- `OPENAI_MODEL`: gpt-3.5-turbo (default)
- `SECRET_KEY`: Flask secret key
- `MEMORY_MAX_ENTRIES`: 10 (default)
- `SAFETY_MONITORING_ENABLED`: True/False

## Usage

### Basic Chat
Simply type messages to start a conversation with the AI coach.

### Special Commands
- `/goals` - View current goals and progress
- `/insights` - Show coaching insights
- `/preferences` - List learned preferences
- `/safety` - Check safety status
- `/help` - Show available commands

### Coaching Styles
- **Supportive**: Encouraging and positive approach
- **Challenging**: Pushes you to do better
- **Analytical**: Data-focused and systematic

## Development

### Adding New Scenarios
1. Add scenario definitions to `coach/scenarios.py` or `coach/sports.py`
2. Update identification functions
3. Add appropriate responses for each coaching style

### Testing
The application includes mock responses when OpenAI API is not available, allowing testing without API costs.

## License
This project is for educational and demonstration purposes.
