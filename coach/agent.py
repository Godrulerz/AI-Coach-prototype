import os
from .memory import UserMemory
from .responses import get_coaching_response
from .safety import SafetyCategory, SafetyLevel
import config

class CoachingAgent:
    """AI Coaching Agent that provides personalized coaching responses"""
    
    def __init__(self, coaching_style=None):
        """Initialize the coaching agent
        
        Args:
            coaching_style (str, optional): The coaching style to use. Defaults to None (uses DEFAULT_COACHING_STYLE).
        """
        # Set coaching style
        self.coaching_style = coaching_style or config.DEFAULT_COACHING_STYLE
        
        # Initialize user memory storage
        self.user_memories = {}
    
    def set_coaching_style(self, coaching_style):
        """Set the coaching style
        
        Args:
            coaching_style (str): The coaching style to use
        """
        self.coaching_style = coaching_style
    
    def get_user_memory(self, user_id):
        """Get or create memory for a specific user
        
        Args:
            user_id (str): Unique identifier for the user
            
        Returns:
            UserMemory: Memory object for the user
        """
        if user_id not in self.user_memories:
            self.user_memories[user_id] = UserMemory(user_id)
        return self.user_memories[user_id]
    
    def process_message(self, message, user_id):
        """Process a user message and return a coaching response
        
        Args:
            message (str): The user's message
            user_id (str): Unique identifier for the user
            
        Returns:
            dict: Response containing coaching message and user profile updates
        """
        # Get user memory
        memory = self.get_user_memory(user_id)
        
        # Add user message to memory
        memory.add_message("user", message)
        
        # Get coaching style configuration
        style_config = config.COACHING_STYLES.get(
            self.coaching_style, 
            config.COACHING_STYLES[config.DEFAULT_COACHING_STYLE]
        )
        
        # Process special commands
        if message.lower().startswith("/"):
            return self._handle_command(message.lower(), memory, style_config)
        
        # Check safety status before generating response
        safety_status = memory.get_safety_status()
        
        # Generate coaching response with safety considerations
        response = get_coaching_response(
            message=message,
            conversation_history=memory.get_conversation_history(),
            user_profile=memory.get_user_profile(),
            coaching_style=style_config,
            safety_status=safety_status
        )
        
        # Add response to memory
        memory.add_message("coach", response)
        
        # Return response with user profile and safety status for UI updates
        user_profile = memory.get_user_profile()
        user_profile["safety_status"] = safety_status
        
        return {
            "response": response,
            "user_profile": user_profile
        }
        
    def _handle_command(self, command, memory, style_config):
        """Handle special commands
        
        Args:
            command (str): The command message
            memory (UserMemory): The user's memory object
            style_config (dict): The coaching style configuration
            
        Returns:
            dict: Response containing coaching message and user profile updates
        """
        if command.startswith("/performance") or command.startswith("/stats"):
            # Show performance metrics if available
            profile = memory.get_user_profile()
            if "performance_metrics" not in profile or not profile["performance_metrics"]:
                response = "No performance metrics have been recorded yet. You can share your stats during our conversations."
            else:
                response = "Here are your tracked performance metrics:\n"
                for metric, value in profile["performance_metrics"].items():
                    response += f"- {metric}: {value}\n"
                
                if "mental_state" in profile and profile["mental_state"]:
                    response += "\nMental state metrics:\n"
                    for state, value in profile["mental_state"].items():
                        response += f"- {state}: {value}/5\n"
            
            return {
                "response": response,
                "user_profile": profile
            }
        
        elif command.startswith("/goals"):
            # List all goals
            goals = memory.get_user_profile()["goals"]
            if not goals:
                response = "You haven't set any goals yet. Would you like to set one now?"
            else:
                response = "Here are your current goals:\n"
                for i, goal in enumerate(goals, 1):
                    progress = memory.get_user_profile()["progress"].get(goal, 0.0)
                    progress_percent = int(progress * 100)
                    response += f"{i}. {goal} - {progress_percent}% complete\n"
        
        elif command.startswith("/insights"):
            # List all insights
            insights = memory.get_user_profile()["insights"]
            if not insights:
                response = "I don't have any insights about your progress yet. Let's continue our coaching conversations to develop some."
            else:
                response = "Here are my coaching insights so far:\n"
                # Show last 5 insights (most recent first)
                for i, insight in enumerate(insights[-5:], 1):
                    response += f"{i}. {insight['content']}\n"
        
        elif command.startswith("/preferences"):
            # List all preferences
            preferences = memory.get_user_profile()["preferences"]
            if not preferences:
                response = "I haven't learned about your preferences yet. Feel free to share what you like or dislike during our conversations."
            else:
                response = "Here are the preferences I've learned about you:\n"
                for category, items in preferences.items():
                    response += f"{category.capitalize()}: {', '.join(items)}\n"
        
        elif command.startswith("/safety"):
            # Show safety status
            safety_status = memory.get_safety_status()
            if safety_status["total_alerts"] == 0:
                response = "No safety concerns detected. You're doing great! 🟢"
            else:
                response = f"Safety Status:\n"
                response += f"Total Alerts: {safety_status['total_alerts']}\n"
                response += f"Recent Alerts: {safety_status['recent_alerts']}\n"
                response += f"Critical Alerts: {safety_status['critical_alerts']}\n"
                
                if safety_status["escalation_required"]:
                    response += "\n🚨 URGENT: Immediate attention required!\n"
                
                if safety_status["recommendations"]:
                    response += "\nRecommendations:\n"
                    for i, rec in enumerate(safety_status["recommendations"], 1):
                        response += f"{i}. {rec}\n"
        
        elif command.startswith("/help"):
            # Show help
            response = "Available commands:\n"
            response += "/goals - List your current goals and progress\n"
            response += "/insights - Show coaching insights about you\n"
            response += "/preferences - List your preferences I've learned\n"
            response += "/safety - Show safety status and recommendations\n"
            response += "/help - Show this help message\n"
        
        else:
            # Unknown command
            response = "I don't recognize that command. Type /help to see available commands."
        
        # Add response to memory
        memory.add_message("coach", response)
        
        # Return response with user profile for UI updates
        return {
            "response": response,
            "user_profile": memory.get_user_profile()
        }
    
    def set_coaching_style(self, style):
        """Set the coaching style
        
        Args:
            style (str): The coaching style to use
            
        Returns:
            bool: True if style was set successfully, False otherwise
        """
        if style in config.COACHING_STYLES:
            self.coaching_style = style
            return True
        return False