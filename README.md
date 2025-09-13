# AI Coaching Agent

A comprehensive AI-powered coaching chatbot that provides personalized coaching through a conversational interface. The system supports multiple coaching styles, sports-specific scenarios, safety monitoring, and advanced memory management.

## Features

### Core Features
- **Multi-Style Coaching**: Supportive, Challenging, and Analytical coaching styles
- **Sports Coaching**: Specialized scenarios for athletic performance and training
- **Memory Management**: Context-aware conversations with user profile tracking
- **Safety Monitoring**: Built-in safety checks and escalation protocols
- **Performance Tracking**: Metrics extraction and progress monitoring
- **Mental State Analysis**: Confidence, anxiety, focus, and motivation tracking

### Technical Features
- **Flask Web Interface**: Modern, responsive chat interface
- **OpenAI Integration**: GPT-3.5-turbo powered responses
- **Environment Configuration**: Secure API key management
- **Modular Architecture**: Extensible coaching scenarios and responses
- **Error Handling**: Graceful fallbacks and mock responses

## Quick Start

### Option 1: Automated Setup
```bash
python setup.py
```

### Option 2: Manual Setup

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure Environment**
   ```bash
   # Copy the template
   copy env_template.txt .env
   
   # Edit .env file and add your OpenAI API key
   OPENAI_API_KEY=your_actual_api_key_here
   ```

3. **Run the Application**
   ```bash
   python app.py
   ```

4. **Access the Application**
   Open your browser and go to: `http://127.0.0.1:5000`

## Configuration

### Environment Variables

Create a `.env` file with the following variables:

```env
# Required
OPENAI_API_KEY=your_openai_api_key_here

# Optional
FLASK_ENV=development
FLASK_DEBUG=True
OPENAI_MODEL=gpt-3.5-turbo
SECRET_KEY=your_secret_key_here
MEMORY_MAX_ENTRIES=10
SAFETY_MONITORING_ENABLED=True
```

### Getting an OpenAI API Key

1. Visit [OpenAI Platform](https://platform.openai.com/api-keys)
2. Sign in to your account
3. Create a new API key
4. Copy the key and paste it in your `.env` file

## Usage

### Basic Chat
Simply type messages to start a conversation with the AI coach.

### Special Commands
- `/goals` - View your current goals and progress
- `/insights` - Show coaching insights about you
- `/preferences` - List learned preferences
- `/safety` - Check safety status and recommendations
- `/help` - Show available commands

### Coaching Styles
- **Supportive**: Encouraging and positive approach
- **Challenging**: Pushes you to do better
- **Analytical**: Data-focused and systematic

### Sports Scenarios
The system automatically detects sports-related conversations and provides specialized coaching for:
- Performance analysis
- Technique development
- Mental state management
- Team dynamics
- Training planning
- Competition preparation
- Recovery management

## Project Structure

```
chatbot/
├── app.py                 # Main Flask application
├── config.py             # Configuration management
├── setup.py              # Automated setup script
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables (create from template)
├── env_template.txt      # Environment template
├── coach/                # Core coaching modules
│   ├── __init__.py
│   ├── agent.py          # Main coaching agent
│   ├── memory.py         # User memory and context
│   ├── responses.py      # Response generation
│   ├── safety.py         # Safety monitoring
│   ├── scenarios.py      # General coaching scenarios
│   └── sports.py         # Sports-specific scenarios
├── templates/            # HTML templates
│   └── index.html        # Main chat interface
└── static/              # Static assets
    ├── css/
    │   └── style.css     # Styling
    └── js/
        └── script.js     # Frontend JavaScript
```

## Development

### Running in Development Mode
```bash
export FLASK_ENV=development
python app.py
```

### Testing
The application includes mock responses when the OpenAI API key is not configured, allowing you to test the interface without API costs.

### Adding New Scenarios
1. Add scenario definitions to `coach/scenarios.py` or `coach/sports.py`
2. Update the identification functions
3. Add appropriate responses for each coaching style

## Troubleshooting

### Common Issues

1. **"Warning: OPENAI_API_KEY environment variable not set"**
   - Make sure you've created a `.env` file with your API key
   - Check that the file is in the same directory as `app.py`

2. **Import errors**
   - Run `pip install -r requirements.txt` to install dependencies
   - Make sure you're using Python 3.7 or higher

3. **Port already in use**
   - The application runs on port 5000 by default
   - Stop other applications using this port or modify the port in `app.py`

### Getting Help
- Check the console output for error messages
- Ensure all dependencies are installed
- Verify your `.env` file configuration
- Test with mock responses first (no API key needed)

## License

This project is for educational and demonstration purposes.# AI-Coach-prototype
