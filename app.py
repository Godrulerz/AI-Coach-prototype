from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv
from coach.agent import CoachingAgent
import config

# Load environment variables (with fallback)
try:
    load_dotenv()
except:
    pass  # Continue without .env file if there are issues

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = config.SECRET_KEY

# Initialize coaching agent
coach_agent = CoachingAgent()

@app.route('/')
def index():
    """Render the main chat interface"""
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    """Process chat messages and return coaching responses"""
    data = request.json
    user_message = data.get('message', '')
    user_id = data.get('user_id', 'default_user')
    coaching_style = data.get('coaching_style', None)
    
    # Set coaching style if provided
    if coaching_style:
        coach_agent.set_coaching_style(coaching_style)
    
    # Get response from coaching agent
    result = coach_agent.process_message(user_message, user_id)
    
    # Return response and user profile for UI updates
    return jsonify({
        'response': result['response'],
        'user_profile': result['user_profile']
    })

if __name__ == '__main__':
    app.run(debug=True)