# Sports Coaching Scenarios and Features

# Sports-specific coaching scenarios and their associated responses for different coaching styles
SPORTS_SCENARIOS = {
    "performance_analysis": {
        "keywords": ["performance", "played", "game", "match", "competition", "tournament", "stats", "statistics"],
        "responses": {
            "supportive": [
                "I noticed some great moments in your performance. What aspects are you most proud of?",
                "Your effort was evident throughout. How did you feel about your energy levels during different phases?",
                "You showed real determination out there. What positive elements can we build on for next time?"
            ],
            "challenging": [
                "Let's analyze your performance critically. Where do you think you left opportunities on the table?",
                "How would you rate your performance against your potential? What percentage of your capability did you reach?",
                "If you could replay three key moments, which would they be and what would you do differently?"
            ],
            "analytical": [
                "Looking at your performance metrics, I notice patterns in your execution. Let's break down the data by phase.",
                "Your statistics show variability in certain areas. What factors might explain these fluctuations?",
                "Comparing this performance to your baseline metrics, we can identify specific areas for technical refinement."
            ]
        }
    },
    "technique_development": {
        "keywords": ["technique", "form", "mechanics", "skill", "movement", "execution", "drill"],
        "responses": {
            "supportive": [
                "Your technique is showing improvement. What aspect feels most natural to you now?",
                "I can see you've been practicing. How does this technique feel compared to when you started?",
                "Your dedication to refining your form is paying off. Which element would you like to focus on next?"
            ],
            "challenging": [
                "Your basic technique is solid, but what would take it to an elite level? What details are you missing?",
                "How consistently can you execute this technique under pressure? What happens when fatigue sets in?",
                "The difference between good and great is in the details. Which technical element needs the most refinement?"
            ],
            "analytical": [
                "Let's break down this technique into its component parts and analyze each phase of the movement.",
                "Research shows that this technique has key biomechanical principles. How does your execution align with these principles?",
                "By measuring the angles and timing of your movement, we can identify specific adjustments to optimize efficiency."
            ]
        }
    },
    "mental_state": {
        "keywords": ["nervous", "confidence", "focus", "concentration", "pressure", "anxiety", "mindset", "mental"],
        "responses": {
            "supportive": [
                "Mental strength is just as important as physical ability. What mental techniques have helped you perform well in the past?",
                "It's normal to experience those feelings before competition. What helps you channel that energy productively?",
                "Your awareness of your mental state is a strength in itself. What small practice could help you feel more centered?"
            ],
            "challenging": [
                "Elite performers develop specific mental routines. What's your pre-performance mental preparation process?",
                "How quickly can you reset after a setback? What specific technique do you use to refocus?",
                "Mental toughness is built through deliberate practice. How are you systematically training your mind?"
            ],
            "analytical": [
                "Research in sports psychology suggests several evidence-based techniques for mental performance. Let's identify which might work best for your specific challenges.",
                "Let's track your perceived mental state before, during, and after performances to identify patterns and triggers.",
                "By analyzing situations where your focus wavers, we can develop targeted interventions for maintaining optimal concentration."
            ]
        }
    },
    "team_dynamics": {
        "keywords": ["team", "teammate", "coach", "captain", "leadership", "communication", "role", "position"],
        "responses": {
            "supportive": [
                "Your role in the team is valuable. How do you feel you contribute to the team's success?",
                "Building strong team relationships takes effort. What connections have you been developing?",
                "Your perspective on team dynamics shows awareness. How might you help foster an even stronger team environment?"
            ],
            "challenging": [
                "How would your teammates describe your contribution to the team? Would their assessment match yours?",
                "What uncomfortable conversations might need to happen to improve team performance?",
                "If you were the captain/coach, what changes would you implement to enhance team cohesion and performance?"
            ],
            "analytical": [
                "Team performance data shows patterns in how different combinations of players work together. Let's analyze these interactions.",
                "Research on high-performing teams identifies key communication patterns. How does your team's communication compare to these models?",
                "By mapping the team's strengths and weaknesses, we can identify strategic adjustments to optimize collective performance."
            ]
        }
    },
    "training_plan": {
        "keywords": ["training", "practice", "workout", "exercise", "routine", "schedule", "plan", "program"],
        "responses": {
            "supportive": [
                "Your commitment to training is evident. How is your current plan supporting your overall goals?",
                "Consistent practice builds excellence. What aspect of your training routine gives you the most satisfaction?",
                "It's important to balance intensity and recovery. How are you ensuring you're getting adequate rest?"
            ],
            "challenging": [
                "Is your training plan truly challenging your limits? Where could you add progressive overload?",
                "How specifically does each element of your training plan address your performance gaps?",
                "What would happen if you completely redesigned your training approach? What sacred cows might need questioning?"
            ],
            "analytical": [
                "Let's analyze your training load metrics over time to ensure optimal periodization and progression.",
                "Research suggests specific training ratios for your sport. How does your current plan align with evidence-based protocols?",
                "By tracking multiple performance indicators throughout your training cycle, we can identify which interventions are producing the best results."
            ]
        }
    },
    "competition_preparation": {
        "keywords": ["competition", "tournament", "match", "game", "prepare", "ready", "opponent", "strategy"],
        "responses": {
            "supportive": [
                "Your preparation process shows dedication. What final elements will help you feel fully ready?",
                "Feeling prepared builds confidence. What aspects of your preparation give you the most confidence?",
                "You've put in the work to be ready. What pre-competition routine helps you get in the optimal mindset?"
            ],
            "challenging": [
                "What does your opponent know about your tendencies? How will you counter their expectations?",
                "What's your contingency plan if your primary strategy isn't working? How quickly can you adapt?",
                "How are you preparing for the specific environmental conditions and pressures of this competition?"
            ],
            "analytical": [
                "Let's analyze your opponent's patterns and statistics to identify strategic advantages you can exploit.",
                "Research on optimal pre-competition protocols suggests specific timing for nutrition, warm-up, and mental preparation. How does your routine align with these findings?",
                "By simulating competition conditions in training, we can gather data on your performance under similar stressors."
            ]
        }
    },
    "recovery_management": {
        "keywords": ["recovery", "rest", "injury", "soreness", "fatigue", "sleep", "nutrition", "rehabilitation"],
        "responses": {
            "supportive": [
                "Recovery is where growth happens. How are you prioritizing this essential aspect of performance?",
                "Listening to your body shows wisdom. What is your body telling you about your current recovery needs?",
                "Managing energy is as important as expending it. What recovery practices have been most effective for you?"
            ],
            "challenging": [
                "How systematically are you approaching recovery? What metrics are you tracking beyond how you feel?",
                "What recovery modalities are you neglecting that could give you a competitive edge?",
                "If sleep is the foundation of recovery, how would you rate your sleep hygiene and quality? What needs to improve?"
            ],
            "analytical": [
                "Let's analyze your recovery markers including HRV, sleep quality, and subjective readiness scores to optimize your training load.",
                "Research indicates specific recovery protocols for your type of training stress. How does your approach align with evidence-based practices?",
                "By tracking multiple recovery indicators, we can identify early warning signs of overtraining and make proactive adjustments."
            ]
        }
    }
}

# Player performance tracking system
class PlayerPerformance:
    """Class for tracking and analyzing player performance metrics"""
    
    def __init__(self, player_id):
        """Initialize player performance tracking
        
        Args:
            player_id (str): Unique identifier for the player
        """
        self.player_id = player_id
        self.performance_history = []
        self.metrics = {}
        self.abnormalities = []
        self.mental_state_log = []
    
    def log_performance(self, event_type, metrics, notes=""):
        """Log a performance event with associated metrics
        
        Args:
            event_type (str): Type of event (e.g., 'game', 'training', 'test')
            metrics (dict): Dictionary of performance metrics
            notes (str): Additional notes about the performance
        """
        import time
        
        performance_entry = {
            "timestamp": time.time(),
            "event_type": event_type,
            "metrics": metrics,
            "notes": notes
        }
        
        self.performance_history.append(performance_entry)
        self._update_metrics(metrics)
        self._check_for_abnormalities(performance_entry)
    
    def log_mental_state(self, state_data):
        """Log player's mental state
        
        Args:
            state_data (dict): Data about player's mental state
                (e.g., confidence, anxiety, focus, motivation)
        """
        import time
        
        state_entry = {
            "timestamp": time.time(),
            "state": state_data
        }
        
        self.mental_state_log.append(state_entry)
    
    def _update_metrics(self, new_metrics):
        """Update the player's overall metrics with new data
        
        Args:
            new_metrics (dict): New metrics to incorporate
        """
        for key, value in new_metrics.items():
            if key in self.metrics:
                # For numeric values, we can calculate averages
                if isinstance(value, (int, float)) and isinstance(self.metrics[key], (int, float)):
                    # Simple running average
                    count = self.metrics.get(f"{key}_count", 1)
                    self.metrics[key] = ((self.metrics[key] * count) + value) / (count + 1)
                    self.metrics[f"{key}_count"] = count + 1
            else:
                self.metrics[key] = value
    
    def _check_for_abnormalities(self, performance_entry):
        """Check for abnormal performance metrics
        
        Args:
            performance_entry (dict): The performance entry to check
        """
        # This is a simplified implementation
        # In a real system, this would use statistical methods to detect outliers
        
        for key, value in performance_entry["metrics"].items():
            if key in self.metrics and isinstance(value, (int, float)):
                # Simple threshold-based abnormality detection
                # If the value is 30% higher or lower than the average, flag it
                avg = self.metrics[key]
                if value < avg * 0.7 or value > avg * 1.3:
                    abnormality = {
                        "timestamp": performance_entry["timestamp"],
                        "metric": key,
                        "value": value,
                        "average": avg,
                        "event_type": performance_entry["event_type"]
                    }
                    self.abnormalities.append(abnormality)
    
    def get_performance_summary(self):
        """Get a summary of the player's performance metrics
        
        Returns:
            dict: Summary of performance metrics and trends
        """
        if not self.performance_history:
            return {"status": "No performance data available"}
        
        return {
            "metrics": self.metrics,
            "recent_performances": self.performance_history[-3:],
            "abnormalities": self.abnormalities[-5:],
            "mental_state": self._get_recent_mental_state()
        }
    
    def _get_recent_mental_state(self):
        """Get the player's recent mental state data
        
        Returns:
            dict: Recent mental state or empty dict if none available
        """
        if not self.mental_state_log:
            return {}
        
        return self.mental_state_log[-1]["state"]

# Helper function to identify sports scenario from message
def identify_sports_scenario(message):
    """Identify which sports coaching scenario matches the user's message
    
    Args:
        message (str): The user's message
        
    Returns:
        str: The identified sports scenario key, or None if no match
    """
    message_lower = message.lower()
    
    for scenario, data in SPORTS_SCENARIOS.items():
        for keyword in data["keywords"]:
            if keyword in message_lower:
                return scenario
    
    return None

# Helper function to get appropriate sports response for a scenario and coaching style
def get_sports_scenario_response(scenario, coaching_style):
    """Get an appropriate sports coaching response for the identified scenario and coaching style
    
    Args:
        scenario (str): The identified sports coaching scenario
        coaching_style (str): The coaching style to use
        
    Returns:
        str: A sports coaching response appropriate for the scenario and style
    """
    import random
    
    if scenario not in SPORTS_SCENARIOS:
        return None
    
    # Default to supportive if coaching style not found
    if coaching_style not in SPORTS_SCENARIOS[scenario]["responses"]:
        coaching_style = "supportive"
    
    responses = SPORTS_SCENARIOS[scenario]["responses"][coaching_style]
    return random.choice(responses)

# Function to extract performance metrics from a message
def extract_performance_metrics(message):
    """Extract potential performance metrics mentioned in a message
    
    Args:
        message (str): The user's message
        
    Returns:
        dict: Extracted performance metrics
    """
    import re
    
    metrics = {}
    
    # Look for patterns like "I scored 2 goals" or "ran 5 kilometers"
    # This is a simplified implementation - a real system would use NLP
    
    # Goals/points/score pattern
    score_pattern = r"(?:scored|made|got)\s+(\d+)\s+(?:goals?|points?|runs?|baskets?)"
    score_match = re.search(score_pattern, message.lower())
    if score_match:
        metrics["score"] = int(score_match.group(1))
    
    # Distance pattern
    distance_pattern = r"(?:ran|swam|cycled|covered)\s+(\d+(?:\.\d+)?)\s+(?:km|kilometers|miles|meters|m)"
    distance_match = re.search(distance_pattern, message.lower())
    if distance_match:
        metrics["distance"] = float(distance_match.group(1))
    
    # Time pattern
    time_pattern = r"(?:finished in|time of|took me)\s+(\d+)(?::(\d+))?(?::(\d+))?\s*(?:hours?|hrs?|minutes?|mins?|seconds?|secs?)?"
    time_match = re.search(time_pattern, message.lower())
    if time_match:
        # Convert to seconds for storage
        hours = int(time_match.group(1)) if time_match.group(1) else 0
        minutes = int(time_match.group(2)) if time_match.group(2) else 0
        seconds = int(time_match.group(3)) if time_match.group(3) else 0
        
        if not time_match.group(2) and not time_match.group(3):
            # If only one number is provided, assume it's minutes
            minutes = hours
            hours = 0
        
        total_seconds = (hours * 3600) + (minutes * 60) + seconds
        metrics["time"] = total_seconds
    
    return metrics

# Function to extract mental state from a message
def extract_mental_state(message):
    """Extract information about mental state from a message
    
    Args:
        message (str): The user's message
        
    Returns:
        dict: Extracted mental state information
    """
    message_lower = message.lower()
    mental_state = {}
    
    # Check for confidence levels
    confidence_keywords = {
        "very confident": 5,
        "confident": 4,
        "somewhat confident": 3,
        "not very confident": 2,
        "unconfident": 1,
        "no confidence": 0
    }
    
    for keyword, level in confidence_keywords.items():
        if keyword in message_lower:
            mental_state["confidence"] = level
            break
    
    # Check for anxiety levels
    anxiety_keywords = {
        "extremely anxious": 5,
        "very anxious": 4,
        "anxious": 3,
        "somewhat anxious": 2,
        "a little anxious": 1,
        "not anxious": 0,
        "calm": 0,
        "relaxed": 0
    }
    
    for keyword, level in anxiety_keywords.items():
        if keyword in message_lower:
            mental_state["anxiety"] = level
            break
    
    # Check for focus/concentration
    focus_keywords = {
        "very focused": 5,
        "focused": 4,
        "somewhat focused": 3,
        "distracted": 2,
        "very distracted": 1,
        "cannot concentrate": 0
    }
    
    for keyword, level in focus_keywords.items():
        if keyword in message_lower:
            mental_state["focus"] = level
            break
    
    # Check for motivation
    motivation_keywords = {
        "highly motivated": 5,
        "motivated": 4,
        "somewhat motivated": 3,
        "not very motivated": 2,
        "unmotivated": 1,
        "completely unmotivated": 0
    }
    
    for keyword, level in motivation_keywords.items():
        if keyword in message_lower:
            mental_state["motivation"] = level
            break
    
    return mental_state