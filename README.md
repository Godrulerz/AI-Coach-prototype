# 🤖 AI Coaching Agent

<div align="center">

![Python](https://img.shields.io/badge/Python-3.7+-blue?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.0.1-green?style=for-the-badge&logo=flask&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--3.5--turbo-orange?style=for-the-badge&logo=openai&logoColor=white)
![License](https://img.shields.io/badge/License-Educational-purple?style=for-the-badge)

*A comprehensive AI-powered coaching chatbot that provides personalized coaching through a conversational interface*

[![Live Demo](https://img.shields.io/badge/Live%20Demo-🚀%20Try%20Now-brightgreen?style=for-the-badge)](http://127.0.0.1:5000)
[![GitHub](https://img.shields.io/badge/GitHub-View%20Source-black?style=for-the-badge&logo=github)](https://github.com/Godrulerz/AI-Coach-prototype)

</div>

---

## ✨ Overview

An AI-powered conversational coaching platform designed to deliver personalized guidance across multiple coaching styles and scenarios. The system supports athletic performance, mental readiness, safety monitoring, and advanced memory management for context-aware interactions.

---

## 🚀 Features

### 🎯 Core Capabilities

* 🎭 **Multi-Style Coaching**: Supportive, Challenging, and Analytical approaches
* ⚽ **Sports-Specific Coaching**: Tailored guidance for training, performance, and recovery
* 🧠 **Memory Management**: Persistent user profiles with context tracking
* 🛡️ **Safety Monitoring**: Built-in checks with escalation protocols
* 📊 **Performance Tracking**: Extracts metrics and monitors progress
* 🧘 **Mental State Analysis**: Evaluates confidence, anxiety, focus, and motivation

### ⚙️ Technical Features

* 🌐 **Flask Web Interface**: Modern, responsive chat UI
* 🤖 **OpenAI Integration**: Powered by `gpt-3.5-turbo`
* 🔐 **Secure Configuration**: Environment-based API key management
* 🏗️ **Modular Architecture**: Easily extendable coaching modules
* 🛠️ **Error Handling**: Graceful fallbacks and mock response support

---

## 🚀 Quick Start

### ⚡ Option 1: Automated Setup

```bash
python setup.py
```

### 🔧 Option 2: Manual Setup

1. **📦 Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

2. **⚙️ Configure environment**

   ```bash
   # Copy the template
   copy env_template.txt .env

   # Edit .env and add your OpenAI API key
   OPENAI_API_KEY=your_actual_api_key_here
   ```

3. **▶️ Run the application**

   ```bash
   python app.py
   ```

4. **🌐 Access in browser**
   Open: `http://127.0.0.1:5000`

---

## Configuration

### Environment Variables

Create a `.env` file with:

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
2. Sign in and create a new API key
3. Add the key to your `.env` file

---

## Usage

### Basic Chat

Start typing to interact with the AI coach.

### Commands

* `/goals` – View current goals and progress
* `/insights` – Display personal coaching insights
* `/preferences` – List learned preferences
* `/safety` – Show safety status and recommendations
* `/help` – List available commands

### Coaching Styles

* **Supportive**: Encouraging and positive
* **Challenging**: Pushes for higher performance
* **Analytical**: Data-driven and systematic

### Sports Coaching Scenarios

Automatically adapts to:

* Performance analysis
* Technique development
* Mental readiness
* Team dynamics
* Training plans
* Competition preparation
* Recovery strategies

---

## Project Structure

```
chatbot/
├── app.py              # Flask application entry point
├── config.py           # Configuration management
├── setup.py            # Automated setup script
├── requirements.txt    # Python dependencies
├── .env                # Local environment variables
├── env_template.txt    # Environment template
├── coach/              # Core coaching logic
│   ├── agent.py        # Main coaching agent
│   ├── memory.py       # Memory and context
│   ├── responses.py    # Response generation
│   ├── safety.py       # Safety monitoring
│   ├── scenarios.py    # General coaching scenarios
│   └── sports.py       # Sports-specific modules
├── templates/          # HTML templates
│   └── index.html      # Chat UI
└── static/             # Static assets
    ├── css/style.css
    └── js/script.js
```

---

## Development

### Run in Development Mode

```bash
export FLASK_ENV=development
python app.py
```

### Testing Without API Key

If no OpenAI key is set, the app generates mock responses—allowing testing without incurring API costs.

### Adding New Scenarios

1. Define scenarios in `coach/scenarios.py` or `coach/sports.py`
2. Update scenario identification logic
3. Add responses for each coaching style

---

## Troubleshooting

### Common Issues

1. **Missing API key**

   * Ensure `.env` exists and contains `OPENAI_API_KEY`
   * File must be in the project root

2. **Import errors**

   * Run `pip install -r requirements.txt`
   * Confirm Python 3.7+

3. **Port already in use**

   * Default port: `5000`
   * Stop conflicting processes or change port in `app.py`

### Getting Help

* Review console logs for errors
* Check `.env` configuration
* Verify dependencies installed
* Test with mock responses first

---

---

## 👨‍💻 Developer

<div align="center">

**Developed with ❤️ by [ASHISH KUMAR](https://godz.rf.gd)**

[![Portfolio](https://img.shields.io/badge/Portfolio-🌐%20Visit%20Now-blue?style=for-the-badge)](https://godz.rf.gd)
[![GitHub](https://img.shields.io/badge/GitHub-@Godrulerz-black?style=for-the-badge&logo=github)](https://github.com/Godrulerz)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=for-the-badge&logo=linkedin)](https://linkedin.com/in/ashish-kumar-godrulerz)

*Full-Stack Developer | AI Enthusiast | Open Source Contributor*

</div>

---

## 📄 License

This project is provided for educational and demonstration purposes only.

---

<div align="center">

**⭐ Star this repository if you found it helpful!**

[![GitHub stars](https://img.shields.io/github/stars/Godrulerz/AI-Coach-prototype?style=social)](https://github.com/Godrulerz/AI-Coach-prototype/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/Godrulerz/AI-Coach-prototype?style=social)](https://github.com/Godrulerz/AI-Coach-prototype/network)

</div>
