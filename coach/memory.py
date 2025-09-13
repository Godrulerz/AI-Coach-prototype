import time
import config
from .safety import SafetyMonitor, SafetyCategory, SafetyLevel

class UserMemory:
    """Manages memory and context for a specific user"""
    
    def __init__(self, user_id):
        """Initialize user memory
        
        Args:
            user_id (str): Unique identifier for the user
        """
        self.user_id = user_id
        self.conversation_history = []
        self.user_profile = {
            "goals": [],
            "preferences": {},
            "progress": {},
            "insights": [],
            "performance_metrics": {},
            "mental_state": {},
            "safety_alerts": [],
            "safety_recommendations": []
        }
        self.safety_monitor = SafetyMonitor()
    
    def add_message(self, role, content):
        """Add a message to the conversation history
        
        Args:
            role (str): The role of the message sender ("user" or "coach")
            content (str): The message content
        """
        # Add message with timestamp
        self.conversation_history.append({
            "role": role,
            "content": content,
            "timestamp": time.time()
        })
        
        # Limit conversation history size
        if len(self.conversation_history) > config.MEMORY_MAX_ENTRIES:
            self.conversation_history = self.conversation_history[-config.MEMORY_MAX_ENTRIES:]
        
        # If user message, update user profile based on content
        if role == "user":
            self._update_user_profile(content)
            # Monitor for safety concerns
            self._monitor_safety(content)
    
    def get_conversation_history(self):
        """Get the conversation history
        
        Returns:
            list: List of conversation messages
        """
        return self.conversation_history
    
    def get_user_profile(self):
        """Get the user profile
        
        Returns:
            dict: User profile information
        """
        return self.user_profile
    
    def _update_user_profile(self, message):
        """Update user profile based on message content
        
        This implementation looks for keywords related to goals, preferences, emotions,
        and sports performance metrics.
        In a real implementation, this would use more sophisticated NLP techniques.
        
        Args:
            message (str): The user's message
        """
        message_lower = message.lower()
        
        # Update goals
        self._extract_goals(message, message_lower)
        
        # Update preferences
        self._extract_preferences(message, message_lower)
        
        # Extract emotions and generate insights
        self._extract_emotions_and_insights(message, message_lower)
        
        # Check for progress updates
        self._extract_progress_updates(message, message_lower)
        
        # Extract sports performance metrics
        self._extract_performance_metrics(message, message_lower)
        
        # Extract mental state data
        self._extract_mental_state(message, message_lower)
    
    def _extract_goals(self, message, message_lower):
        """Extract goals from the message
        
        Args:
            message (str): The original message
            message_lower (str): Lowercase version of the message
        """
        # Goal-related keywords
        goal_keywords = ["goal", "want to", "achieve", "improve", "learn", "aspire", "aim"]
        
        # Check for goal-related content
        for keyword in goal_keywords:
            if keyword in message_lower:
                # Extract potential goal (simple implementation)
                goal_start = message_lower.find(keyword) + len(keyword)
                goal_end = message_lower.find(".", goal_start)
                
                if goal_end == -1:  # No period found
                    goal_end = len(message_lower)
                
                potential_goal = message[goal_start:goal_end].strip()
                
                # Add goal if it's not empty and not already in goals
                if potential_goal and potential_goal not in self.user_profile["goals"]:
                    self.user_profile["goals"].append(potential_goal)
                    
                    # Initialize progress tracking for this goal
                    self.user_profile["progress"][potential_goal] = 0.0
                    
                    # Add an insight about the new goal
                    self.add_insight(f"New goal identified: {potential_goal}")
                
                break  # Only extract one goal per message for simplicity
    
    def _extract_preferences(self, message, message_lower):
        """Extract user preferences from the message
        
        Args:
            message (str): The original message
            message_lower (str): Lowercase version of the message
        """
        # Preference-related phrases
        preference_phrases = [
            ("i prefer", "preference"),
            ("i like", "like"),
            ("i enjoy", "enjoy"),
            ("i don't like", "dislike"),
            ("i hate", "dislike"),
            ("i love", "like")
        ]
        
        for phrase, category in preference_phrases:
            if phrase in message_lower:
                # Extract the preference
                pref_start = message_lower.find(phrase) + len(phrase)
                pref_end = message_lower.find(".", pref_start)
                
                if pref_end == -1:  # No period found
                    pref_end = len(message_lower)
                
                preference = message[pref_start:pref_end].strip()
                
                if preference:
                    # Store the preference
                    if category not in self.user_profile["preferences"]:
                        self.user_profile["preferences"][category] = []
                    
                    if preference not in self.user_profile["preferences"][category]:
                        self.user_profile["preferences"][category].append(preference)
    
    def _extract_emotions_and_insights(self, message, message_lower):
        """Extract emotions and generate insights
        
        Args:
            message (str): The original message
            message_lower (str): Lowercase version of the message
        """
        # Emotion keywords
        positive_emotions = ["happy", "excited", "proud", "satisfied", "confident", "motivated"]
        negative_emotions = ["frustrated", "disappointed", "anxious", "stressed", "overwhelmed", "stuck"]
        
        # Check for emotions
        found_emotions = []
        
        for emotion in positive_emotions:
            if emotion in message_lower:
                found_emotions.append((emotion, "positive"))
        
        for emotion in negative_emotions:
            if emotion in message_lower:
                found_emotions.append((emotion, "negative"))
        
        # Generate insights based on emotions
        if found_emotions:
            for emotion, sentiment in found_emotions:
                # Find context around the emotion
                emotion_idx = message_lower.find(emotion)
                start_idx = max(0, message_lower.rfind(".", 0, emotion_idx) + 1)
                end_idx = message_lower.find(".", emotion_idx)
                if end_idx == -1:
                    end_idx = len(message_lower)
                
                context = message[start_idx:end_idx].strip()
                
                # Generate an insight
                if sentiment == "positive":
                    insight = f"User feels {emotion} about: {context}"
                else:
                    insight = f"User is experiencing {emotion} regarding: {context}"
                
                self.add_insight(insight)
    
    def _extract_progress_updates(self, message, message_lower):
        """Extract progress updates from the message
        
        Args:
            message (str): The original message
            message_lower (str): Lowercase version of the message
        """
        
    def _extract_performance_metrics(self, message, message_lower):
        """Extract sports performance metrics from the message
        
        Args:
            message (str): The original message
            message_lower (str): Lowercase version of the message
        """
        # Import the extraction function from sports module
        from .sports import extract_performance_metrics
        
        # Extract metrics using the specialized function
        metrics = extract_performance_metrics(message)
        
        # Update the user profile with any found metrics
        if metrics:
            for metric, value in metrics.items():
                self.user_profile["performance_metrics"][metric] = value
    
    def _extract_mental_state(self, message, message_lower):
        """Extract mental state data from the message
        
        Args:
            message (str): The original message
            message_lower (str): Lowercase version of the message
        """
        # Import the extraction function from sports module
        from .sports import extract_mental_state
        
        # Extract mental state using the specialized function
        mental_state = extract_mental_state(message)
        
        # Update the user profile with any found mental state data
        if mental_state:
            for state, value in mental_state.items():
                self.user_profile["mental_state"][state] = value
        # Progress-related keywords
        progress_keywords = ["progress", "completed", "finished", "accomplished", "achieved"]
        
        # Check if message contains progress updates
        contains_progress = any(keyword in message_lower for keyword in progress_keywords)
        
        if contains_progress and self.user_profile["goals"]:
            # Check which goal the progress might be related to
            for goal in self.user_profile["goals"]:
                goal_lower = goal.lower()
                # If the message mentions the goal and progress
                if any(word in goal_lower for word in goal_lower.split()) and contains_progress:
                    # Simple heuristic: if positive progress words, increase by 0.2
                    current_progress = self.user_profile["progress"].get(goal, 0.0)
                    new_progress = min(current_progress + 0.2, 1.0)  # Cap at 1.0
                    self.update_progress(goal, new_progress)
                    
                    # Add an insight about the progress
                    progress_percentage = int(new_progress * 100)
                    self.add_insight(f"Progress update: {goal} is now at {progress_percentage}% completion")
                    break
    
    def add_insight(self, insight):
        """Add a coaching insight about the user
        
        Args:
            insight (str): The insight about the user
        """
        self.user_profile["insights"].append({
            "content": insight,
            "timestamp": time.time()
        })
    
    def update_progress(self, goal, progress_value):
        """Update progress for a specific goal
        
        Args:
            goal (str): The goal to update progress for
            progress_value (float): Progress value between 0 and 1
        """
        self.user_profile["progress"][goal] = min(max(progress_value, 0), 1)  # Ensure between 0 and 1

    def _monitor_safety(self, message):
        """Monitor user message for safety concerns
        
        Args:
            message (str): The user's message
        """
        # Get safety alerts from the safety monitor
        alerts = self.safety_monitor.monitor_message(message, self.user_id, self.user_profile)
        
        # Store alerts in user profile
        for alert in alerts:
            self.user_profile["safety_alerts"].append({
                "category": alert.category.value,
                "level": alert.level.value,
                "message": alert.message,
                "timestamp": alert.timestamp,
                "recommended_action": alert.recommended_action,
                "escalation_required": alert.escalation_required
            })
            
            # Add safety insight
            self.add_insight(f"Safety Alert ({alert.level.value}): {alert.message}")
        
        # Update safety recommendations
        self.user_profile["safety_recommendations"] = self.safety_monitor.get_safety_recommendations(self.user_id)
        
        # Check for escalation alerts
        escalation_alerts = self.safety_monitor.get_escalation_alerts()
        if escalation_alerts:
            self.add_insight("URGENT: Safety escalation required - immediate attention needed")

    def get_safety_status(self):
        """Get current safety status for the user
        
        Returns:
            dict: Safety status information
        """
        recent_alerts = [alert for alert in self.user_profile["safety_alerts"] 
                        if time.time() - alert["timestamp"] < 3600]  # Last hour
        
        critical_alerts = [alert for alert in recent_alerts 
                          if alert["level"] in ["critical", "emergency"]]
        
        return {
            "total_alerts": len(self.user_profile["safety_alerts"]),
            "recent_alerts": len(recent_alerts),
            "critical_alerts": len(critical_alerts),
            "recommendations": self.user_profile["safety_recommendations"],
            "escalation_required": len(critical_alerts) > 0
        }