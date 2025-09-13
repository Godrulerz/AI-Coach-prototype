import os
from openai import OpenAI
import config
from .scenarios import identify_scenario, get_scenario_response
from .sports import identify_sports_scenario, get_sports_scenario_response, extract_performance_metrics, extract_mental_state, PlayerPerformance

# Initialize OpenAI client
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    print("Warning: OPENAI_API_KEY environment variable not set. Using mock responses.")
    USE_MOCK_RESPONSES = True
else:
    USE_MOCK_RESPONSES = False
    client = OpenAI(api_key=api_key)

def _get_mock_coaching_response(message, user_profile, coaching_style, safety_status=None):
    """Generate a mock coaching response when OpenAI API is not available
    
    Args:
        message (str): The user's message
        user_profile (dict): User profile information
        coaching_style (dict): Coaching style configuration
        safety_status (dict, optional): Safety status information
        
    Returns:
        str: Coaching response
    """
    message_lower = message.lower()
    
    # Check for safety concerns first
    if safety_status and safety_status.get('escalation_required'):
        return "🚨 I'm concerned about your safety and well-being. Please consider speaking with a healthcare professional or mental health specialist. Your safety is my top priority."
    
    # Check for greeting
    if any(greeting in message_lower for greeting in ["hello", "hi", "hey", "greetings"]):
        response = f"Hello! I'm your {coaching_style['description']}. How can I help you today?"
        if safety_status and safety_status.get('recent_alerts', 0) > 0:
            response += f"\n\nNote: I've detected {safety_status['recent_alerts']} recent safety alerts. Let's make sure we're focusing on your well-being."
        return response
    
    # Check for goal setting
    if any(goal_word in message_lower for goal_word in ["goal", "want to", "achieve", "improve"]):
        return "That's a great goal! What's your first step toward achieving it?"
    
    # Check for challenges
    if any(challenge in message_lower for challenge in ["difficult", "hard", "challenge", "struggle", "problem"]):
        if coaching_style['description'].startswith("Supportive"):
            return "I understand this is challenging. Remember that challenges are opportunities for growth. What specific aspect is most difficult for you?"
        elif coaching_style['description'].startswith("Challenging"):
            return "What's stopping you from overcoming this challenge? What would happen if you pushed through this difficulty?"
        else:  # Analytical
            return "Let's break down this challenge. What are the specific components that make it difficult, and what data do we have about each one?"
    
    # Check for progress
    if any(progress in message_lower for progress in ["progress", "better", "improved", "accomplished"]):
        return "That's excellent progress! How does this achievement align with your larger goals?"
    
    # Check for sports-related terms
    sports_terms = ["game", "match", "practice", "training", "player", "team", "coach", "performance", 
                   "technique", "strategy", "competition", "tournament", "athlete", "fitness", "drill"]
    
    if any(term in message_lower for term in sports_terms):
        if coaching_style['description'].startswith("Supportive"):
            return "I believe in your athletic potential. What specific aspect of your performance would you like to work on today?"
        elif coaching_style['description'].startswith("Challenging"):
            return "Champions are made when no one is watching. How are you pushing yourself beyond your comfort zone in training?"
        else:  # Analytical
            return "Let's analyze your recent performance data. What metrics have you been tracking, and what patterns do you notice?"
    
    # Default responses based on coaching style
    if coaching_style['description'].startswith("Supportive"):
        return "I'm here to support you. What would be most helpful for you to focus on right now?"
    elif coaching_style['description'].startswith("Challenging"):
        return "What's one thing you could do today that would push you outside your comfort zone?"
    else:  # Analytical
        return "Let's analyze your current situation. What metrics or indicators would help us measure your progress?"

def get_coaching_response(message, conversation_history, user_profile, coaching_style, safety_status=None):
    """Generate a coaching response based on the user's message and context
    
    Args:
        message (str): The user's message
        conversation_history (list): List of previous conversation messages
        user_profile (dict): User profile information
        coaching_style (dict): Coaching style configuration
        safety_status (dict, optional): Safety status information
        
    Returns:
        str: Coaching response
    """
    # First, check if the message matches any of our sports coaching scenarios
    sports_scenario = identify_sports_scenario(message)
    if sports_scenario:
        # Extract and store performance metrics if present
        performance_metrics = extract_performance_metrics(message)
        mental_state = extract_mental_state(message)
    
    # If using mock responses, return a mock response
    if USE_MOCK_RESPONSES:
        return _get_mock_coaching_response(message, user_profile, coaching_style, safety_status)
    
    # Format conversation history for the API
    formatted_history = []
    for entry in conversation_history[-5:]:  # Use last 5 messages for context
        formatted_history.append({
            "role": "user" if entry["role"] == "user" else "assistant",
            "content": entry["content"]
        })
    
    # Create system message with coaching style and user profile
    system_message = f"{coaching_style['prompt_template']}\n\n"
    
    # Add user profile information to system message
    if user_profile.get('goals'):
        system_message += f"User goals: {', '.join(user_profile['goals'])}\n"
    
    if user_profile.get('insights'):
        system_message += f"User insights: {', '.join([i['content'] for i in user_profile['insights']])}\n"
    
    # Add performance metrics and mental state if available
    if user_profile.get('performance_metrics'):
        system_message += f"Performance metrics: {user_profile['performance_metrics']}\n"
    
    if user_profile.get('mental_state'):
        system_message += f"Mental state: {user_profile['mental_state']}\n"
    
    # Add safety considerations
    if safety_status:
        if safety_status.get('escalation_required'):
            system_message += f"\n🚨 SAFETY ALERT: Immediate attention required! Critical safety concerns detected.\n"
            system_message += f"Recent critical alerts: {safety_status.get('critical_alerts', 0)}\n"
            system_message += "PRIORITY: Focus on athlete safety and well-being. Reduce intensity, provide support, and consider professional referral.\n"
        elif safety_status.get('recent_alerts', 0) > 0:
            system_message += f"\n⚠️ SAFETY NOTICE: {safety_status.get('recent_alerts', 0)} recent safety alerts detected.\n"
            system_message += "Consider adjusting coaching approach to address safety concerns.\n"
        
        if safety_status.get('recommendations'):
            system_message += f"\nSafety recommendations: {'; '.join(safety_status['recommendations'])}\n"
    
    # Add the current message
    formatted_history.append({"role": "user", "content": message})
    
    # Prepend system message
    formatted_history.insert(0, {"role": "system", "content": system_message})
    
    # Call OpenAI API with error handling
    try:
        response = client.chat.completions.create(
            model=config.OPENAI_MODEL,
            messages=formatted_history
        )
        return response.choices[0].message.content
    except Exception as e:
        # If API fails (quota, network, etc.), fall back to mock response
        print(f"OpenAI API error: {e}")
        return _get_mock_coaching_response(message, user_profile, coaching_style, safety_status)

# Function removed as we're now using ChatGPT for all responses